import sys
import time
import datetime
import threading
import queue
from os import environ
rosdistro=environ["ROS_DISTRO"]
rosversion=environ["ROS_VERSION"]

if rosdistro == "noetic":
    from math import dist

from meili_sdk.websockets.models.message import Message
from meili_sdk.websockets import constants

from geometry_msgs.msg import PoseWithCovarianceStamped, Pose, Twist
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry

if rosversion=="2":
    import rclpy
else:
    import rospy

from meili_ros_lib.config_agent import ConfigAgent
from meili_ros_lib.maths import quaternion_to_euler
from meili_ros_lib.parse_data import parse_battery_data
from meili_ros_lib.sentry import initialize_sentry, agent_sentry

from sentry_sdk import capture_exception, capture_message

initialize_sentry()


def update_capacity_lipo(voltage, number_of_cells):
    # Calculate pocentage of battery given the voltage and number of cells
    min_voltage_per_cell = 3.0
    max_voltage_per_cell = 4.0
    min_voltage = min_voltage_per_cell * number_of_cells
    max_voltage = max_voltage_per_cell * number_of_cells
    capacity = (voltage - min_voltage) / (max_voltage - min_voltage) * 100
    capacity = max(0, min(100, capacity))
    return capacity

class Agent:
    def __init__(self, node, file_name_vehicles, file_name_topics):
        # Logging functions

        # Threads
        self.thread1 = None
        self.thread2 = None

        self.publish_frequency_updated = False

        self.log_info = node.log_info
        self.log_error = node.log_error
        self.file_name_vehicles = file_name_vehicles
        self.file_name_topics = file_name_topics

        # Initial instances
        self.node = node
        self.token = None
        self.fleet = None

        self.vehicle_list = []
        self.vehicle_tokens = []
        self.vehicles = {}
        self.number_of_vehicles = None

        # Other classes
        self.connection = None
        self.client = None

        # Messages
        self.msg_pose = []
        self.msg_battery = []
        self.msg_gps = []
        self.msg_speed = []

        self.msg_plan = []
        self.arr_plan = []
        self.buffer = []
        # Internet
        self.ws_open = False

        # Task
        self.task_started = []
        self.number_of_tasks = 0
        self.start_time = None

        # Waypoints
        self.waypoints = []
        self.waypoints_goal_id = []

        # Traffic control
        self.goal_id = []
        self.goal_id_rerouted = []
        self.max_vel_x = []
        self.max_vel_theta = []
        self.path_length = 5  # in Meters
        self.pause_paths = {}

        # Miscellaneous
        self.total_topics = 0
        self.vehicles = self.__agent_setup()


    def __agent_setup(self):
        config = ConfigAgent(self.log_info, self.log_error, self.file_name_vehicles, self.file_name_topics)
        self.log_info("[ROSAgent] The configuration is started...")

        try:
            config.open_files()

            (
                setup_token,
                self.server_instance,
                self.token,
                self.fleet,
            ) = config.config_var()

            self.log_info(f"[ROSAgent] Server instance:{self.server_instance}")
            (
                self.vehicle_list,
                vehicles,
                self.vehicle_tokens,
                self.vehicle_names
            ) = config.config_vehicles()

            self.number_of_vehicles = len(self.vehicle_list)
            self.initialisation()

        except Exception as error:
            self.log_error(
                "[ROSAgent] Agent Setup Error: %s %s" % (type(error).__name__, error)
            )
            agent_sentry(error, "[ROSAgent] Agent Setup Error")
            sys.exit()

        for vehicle in vehicles:
            uuid = vehicle["uuid"]
            self.log_info(f"[ROSAgent] Vehicle {uuid} is on the fleet")
        self.log_info("[ROSAgent] Agent has been configured")

        return vehicles

    def initialisation(self):
        for i in range(0, self.number_of_vehicles):
            self.msg_pose.append(i)
            self.msg_battery.append(i)
            self.msg_gps.append(i)
            self.msg_speed.append(i)

            self.msg_plan.append(i)
            self.arr_plan.append([])
            self.buffer.append(i)

            self.task_started.append(0)
            self.waypoints.append(False)
            self.waypoints_goal_id.append(None)
            self.goal_id_rerouted.append(None)
            self.pause_paths[i] = False

            self.max_vel_x.append(0)
            self.max_vel_theta.append(0)
            self.goal_id.append(0)

    ################################################
    def check_internet(self):
        """Check if there is internet if not connect the offline agent"""
        try:
            self.ws_open = self.connection.check_internet_connection(self.ws_open)
        except Exception as error:
            self.node.log_info(f"[ROSAgent] Error Checking internet:{error}")

    ################################################

    # PING FUNCTIONS
    def send_message_client(self, event, value, vehicle):
        """Sends message via Websocket"""
        try:
            message = Message(event=event, value=value, vehicle=vehicle)
            message.validate()
            self.client.send(message)
        except Exception as e:
            self.log_info(f"SEND MESSAGE ERROR{e} {event} {vehicle}")

    def ping_filtering_mode(self):

        self.ping_status()
        if self.node.traffic_control and not self.node.v2 and rosdistro=="noetic":
            self.ping_trajectory()

    def get_battery(self, msg, index):
        message = msg["msg"]
        if self.node.lipo_battery:
            message.capacity = float(update_capacity_lipo(message.voltage, self.node.number_of_cells))
        battery_data = parse_battery_data(message)
        return battery_data

    def get_location(self, msg, index):
        if isinstance(msg, PoseWithCovarianceStamped):
            x = round(msg.pose.pose.position.x, 3)
            y = round(msg.pose.pose.position.y, 3)
            orientation = msg.pose.pose.orientation
        elif isinstance(msg, Pose):
            x = round(msg.position.x, 3)
            y = round(msg.position.y, 3)
            orientation = msg.orientation
        else:
            self.log_error(
                f"[ROSAgent] Robot {index}-{self.vehicle_names[index]} pose is not available. Message >> {msg}"
            )
            capture_message("[ROSAgent] Robot pose is not available")
            return 0

        yaw = round(quaternion_to_euler(
            orientation.x, orientation.y, orientation.z, orientation.w
        ),
            3)
        return { "xm": x, "ym": y, "rotation": yaw}

    def get_speed(self, msg, index):
        if isinstance(msg, Odometry):
            speed = msg.twist.twist.linear.x
            speed = round(speed, 3)
        else:
            self.log_error(
                f"[ROSAgent] Robot {index}-{self.vehicle_names[index]} speed is not available. Message >> {msg}"
            )
            capture_message("[ROSAgent] Robot speed is not available")
            speed = 0
        return {"speed":speed}

    def ping_status(self):
        value = {}
        for index in range(len(self.vehicle_list)):
            value["timestamp"] = time.time()

            location_msg = self.msg_pose[index]
            try:
                value["location"] = self.get_location(location_msg, index)
                #self.msg_pose[index]=None
            except Exception as error:
                self.log_info("[ROSAgent] No location data is being published")

            if self.node.battery_present:
                battery_msg = self.msg_battery[index]
                try:
                    value["battery"] = self.get_battery(battery_msg, index)
                    #self.msg_battery[index]=None
                except Exception as error:
                    self.log_info("[ROSAgent] No battery data is being published")


            speed_msg = self.msg_speed[index]
            try:
                value["speed"] = self.get_speed(speed_msg,index)
                #self.msg_speed[index]=None
            except Exception as error:
                self.log_info("[ROSAgent] No speed data is being published")
            self.send_message_client(
                constants.EVENT_STATUS,
                value,
                self.vehicle_list[index],
            )

    def ping_location(self):
        """Ping Location """
        try:
            for index, msg in enumerate(self.msg_pose):
                value = self.get_location(msg, index)
                value["timestamp"] = time.time()

                if value != 0:
                    self.send_message_client(
                        constants.EVENT_LOCATION,
                        value,
                        self.vehicle_list[index],
                    )

        except Exception as error:
            self.log_info(f"[ROSAgent] Ping location error: {error}")
            capture_exception(error)

    def ping_battery(self):
        """Sending Battery message via websocket"""
        try:
            for index, msg in enumerate(self.msg_battery):
                value = self.get_battery(msg, index)
                if value is not None:
                    value["timestamp"] = time.time()
                    self.log_info(f"{value}")
                    self.send_message_client(
                        constants.EVENT_BATTERY,
                        {**value},
                        self.vehicle_list[index],
                    )
        except Exception as error:
            capture_exception(error)
            self.log_info(f"[ROSAgent] Ping Battery Error: {error}")

    def ping_trajectory(self):
        """Send the trajectory as an array of poses"""
        try:
            for index, msg in enumerate(self.arr_plan):
                if self.task_started[index] and not self.pause_paths[index]:
                    self.send_message_client(
                        constants.EVENT_PATH_DATA,
                        {"timestamp": time.time(), "path": msg},
                        self.vehicle_list[index],
                    )
        except Exception as error:
            self.log_info(
                f"[ROSAgent] Ping Trajectory Error: {error} "
            )
            self.log_info(f"{index} {self.arr_plan}")
            sys.exit()
            capture_exception(error)

    def ping_gps(self):
        try:
            for index, msg in enumerate(self.msg_gps):
                if isinstance(msg, NavSatFix):
                    lat = msg.latitude
                    lon = msg.longitude
                    rotation = 0
                    self.send_message_client(
                        constants.EVENT_LOCATION,
                        {"timestamp": time.time(), "lat": lat, "lon": lon, "rotation": rotation},
                        self.vehicle_list[index],
                    )
        except Exception as e:
            self.log_info(
                "[ROSAgent] Ping GPS Error: %s ", e)
            capture_exception(e)

    def ping_docking_routine(self, vehicle, path, rotation_angles):
        # send the trajectory as an array of poses
        try:
            self.send_message_client(
                constants.EVENT_DOCKING_ROUTINE,
                {"timestamp": time.time(), "path": path, "rotation_angles": rotation_angles},
                vehicle,
            )
            self.log_info("[ROSAgent] Docking Routine Sent")
        except Exception as e:
            self.log_info(f"[ROSAgent] Ping Docking Routine Error: {e} ")
            capture_exception(e)

    def ping_speed(self):
        """Ping Speed"""
        try:
            for index, msg in enumerate(self.msg_speed):
                try:
                    value = self.get_speed(msg, index)
                    value["timestamp"] = time.time()
                    self.send_message_client(
                        constants.EVENT_SPEED,
                        value,
                        self.vehicle_list[index]
                    )
                except:
                    # self.log_info(f"[ROSAgent] Robot {self.vehicle_names[index]} speed is not available")
                    # capture_message("[ROSAgent] Robot speed is not available")
                    break

        except Exception as e:
            self.log_info(f"[ROSAgent] Ping speed Error: {e} ")
            capture_exception(e)

    ################################################
    def return_vehicle_position(self, vehicle_token):
        """Returns: Vehicle Position"""
        return self.vehicle_list.index(vehicle_token)

    ################################################
    # CALLBACKS
    def callback_pose(self, msg, vehicle_uuid):
        """Parse current robot pose and sent to FMS task_msg_server"""
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        self.msg_pose[vehicle_position] = msg

    def callback_battery(self, msg, vehicle_uuid):
        """When battery topic is available, is parsed and sent to FMS agent"""
        if not self.node.battery_present:
            self.node.battery_present = True
        message = {}
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        message["msg"] = msg
        message["timestamp"] = time.time()
        self.msg_battery[vehicle_position] = message

    def callback_rosoutagg(self, msg, type_msg):
        rosout_message = msg.msg

        count = 0
        # Find the vehicle uuid that corresponds to the message.
        if rosout_message.find('vehicle') != -1:
            for vehicle_uuid in self.vehicle_list:
                if (rosout_message.find(vehicle_uuid)) != -1:
                    vehicle = vehicle_uuid
        elif msg.name.find('robot') != -1:
            name = '/robot' + msg.name[msg.name.find('robot') + 5]
            for vehicle in self.vehicles:
                if (vehicle['prefix']) == name:
                    vehicle = self.vehicle_list[count]
                count += 1
        else:
            vehicle = self.vehicle_list[0]

        if self.ws_open and self.node.logging==type_msg:
            type_msg="warning"

            try:
                self.send_message_client(
                    constants.EVENT_NOTIFICATION,
                            {"vehicle": vehicle,
                             "message": rosout_message, "level": type_msg,
                             "meta": {"file": msg.file, "function": msg.function, "line": msg.line}},
                            vehicle,
                        )
            except Exception as e:
                self.log_error(f"[ROSAgent] Sending notification error {e}")

    def task_in_progress(self, goal_id, status_id, vehicle_uuid):
        if self.ws_open:
            vehicle_position = self.return_vehicle_position(vehicle_uuid)
            if self.waypoints_goal_id[vehicle_position] is not None:
                goal_id = self.waypoints_goal_id[vehicle_position]

                if self.goal_id_rerouted[vehicle_position] is not None:
                    goal_id = self.goal_id_rerouted[vehicle_position]

            self.goal_id[vehicle_position] = goal_id
            self.send_message_client(
                constants.EVENT_GOAL_STATUS,
                {"goal_id": goal_id, "status_id": status_id},
                vehicle_uuid,
            )
            # self.log_info(
            #    f"[ROSAgent] Sending {goal_id} in progress<<{status_id}>> of vehicle {vehicle_position} ")

        else:
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            self.start_time = dt_string
        return 1

    def action_in_progress(self, goal_id, status_id, vehicle_uuid):
        if self.ws_open:
            vehicle_position = self.return_vehicle_position(vehicle_uuid)
            self.goal_id[vehicle_position] = goal_id
            self.send_message_client(
                constants.EVENT_GOAL_STATUS,
                {"goal_id": goal_id, "status_id": status_id},
                vehicle_uuid,
            )
            self.log_info(
                f"[ROSAgent] Sending action {goal_id} in progress<<{status_id}>> of vehicle {vehicle_position} ")
        return 1

    def callback_status(self, msg, goal_id, status_id, vehicle_uuid):
        # Status of navigation task is parsed and send to FMS task_msg_server
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        if (
                self.waypoints_goal_id[vehicle_position] is None
                and self.waypoints[vehicle_position]
        ):
            self.waypoints_goal_id[vehicle_position] = goal_id
        # IN PROGRESS
        if status_id == 1 and self.task_started[vehicle_position] == 0:
            try:
                self.task_started[vehicle_position] = self.task_in_progress(
                    goal_id, status_id, vehicle_uuid
                )
            except Exception as e:
                self.log_error(
                    "[ROSAgent] Task in progress Callback Status error : %s", e
                )
                agent_sentry(e, "[ROSAgent] Task in progress Callback Status error")

        # PREEMPTED NEEDED
        if status_id == 2 and self.task_started[vehicle_position] == 1:
            self.task_started[vehicle_position] = self.task_preempted(goal_id, status_id, vehicle_uuid)

        # IF SUCCEEDED; ABORTED or REJECTED
        if (status_id in (3, 4, 5)) and self.task_started[vehicle_position] == 1:

            try:
                self.task_started[vehicle_position] = self.task_finished(
                    goal_id, status_id, vehicle_uuid
                )

            except Exception as e:
                self.log_error(
                    f"[ROSAgent] Task finished Callback Status error: {e}"
                )
                agent_sentry(e, "[ROSAgent] Task finished Callback Status error")

    def task_preempted(self, goal_id, status_id, vehicle_uuid):
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        if self.waypoints_goal_id[vehicle_position] is not None:
            goal_id = self.waypoints_goal_id[vehicle_position]
            self.waypoints_goal_id[vehicle_position] = None

        self.log_info(
            f"[ROSAgent] Task {goal_id} preempted <<{status_id}>> of vehicle {vehicle_position} ")

        return 0

    def task_finished(self, goal_id, status_id, vehicle_uuid):
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        # TASK ONLINE
        if self.ws_open:
            # self.log_info(
            #     f"[ROSAgent] Task {goal_id} finished<<{status_id}>> of vehicle {vehicle_position} ")
            if not self.waypoints[vehicle_position]:

                if self.waypoints_goal_id[vehicle_position] is not None:
                    goal_id = self.waypoints_goal_id[vehicle_position]
                    self.waypoints_goal_id[vehicle_position] = None
                    if self.goal_id_rerouted[vehicle_position] is not None:
                        goal_id = self.goal_id_rerouted[vehicle_position]
                        self.goal_id_rerouted[vehicle_position] = None

                self.goal_id[vehicle_position] = goal_id
                self.send_message_client(
                    constants.EVENT_GOAL_STATUS,
                    {"goal_id": goal_id, "status_id": status_id},
                    vehicle_uuid,
                )

            #  self.log_info(
            #      f"[ROSAgent] Sending {goal_id} finished<<{status_id}>> of vehicle {vehicle_position} ")

        # OFFLINE TASK
        if self.connection.offline_agent.offline:
            success = True

            for task in self.connection.offline_agent.offline_tasks:
                if self.connection.offline_agent.current_task_uuid == task[0]:

                    if not self.waypoints[vehicle_position]:
                        self.connection.offline_agent.logging_offlinetasks(
                            task,
                            self.number_of_tasks,
                            self.vehicle_list,
                            self.start_time,
                            success=success,
                        )
                        self.start_time = None
                        self.connection.offline_agent.task_offline_started = False
        return 0

    def action_finished(self, goal_id, status_id, vehicle_uuid):
        # TASK ONLINE
        if self.ws_open:
            vehicle_position = self.return_vehicle_position(vehicle_uuid)
            self.log_info(
                f"[ROSAgent] Task {goal_id} finished<<{status_id}>> of vehicle {vehicle_position} ")
            self.goal_id[vehicle_position] = goal_id
            self.send_message_client(
                constants.EVENT_GOAL_STATUS,
                {"goal_id": goal_id, "status_id": status_id},
                vehicle_uuid,
            )

            self.log_info(
                f"[ROSAgent] Sending action {goal_id} finished<<{status_id}>> of vehicle {vehicle_position} ")

    def check_distance_of_array(self, msg):
        path = []
        first = None
        for pose in msg.poses:
            if first is None:
                first = [pose.pose.position.x, pose.pose.position.y]
            point = [pose.pose.position.x, pose.pose.position.y]
            distance = dist(first, point)
            path.append(point)
            if distance > self.path_length:
                yield path
        yield path
    
    def parse_plan(self, msg):
        path = []
        for pose in msg.poses:
            point = [pose.pose.position.x, pose.pose.position.y]
            path.append(point)
        return path

    def callback_plan(self, msg, vehicle_uuid):
        """Callback Plan"""
        # Parse trajectory and send to the fms
        if (rosdistro=="noetic"):
            arr = next(self.check_distance_of_array(msg))
        else:
            arr=self.parse_plan(msg)
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        self.arr_plan[vehicle_position] = arr

    def callback_gps(self, msg, vehicle_uuid):
        """Callback GPS"""
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        self.msg_gps[vehicle_position] = msg

    def callback_speed(self, msg, vehicle_uuid):
        """ Callback Speed"""
        vehicle_position = self.return_vehicle_position(vehicle_uuid)
        self.msg_speed[vehicle_position] = msg

    ################################################
    def run(self, conn_rate, pub_rate, check_threads_rate):
        """Running the agent"""
        # When Mode is filtering, all data is sent to the FMS task_msg_server at specific frequency
        pub_rate_queue = queue.Queue()

        while True:
            try:

                # Update publish frequency if received it
                if self.publish_frequency_updated == True: 
                    pub_rate_queue.put(self.publish_frequency)
                    self.publish_frequency_updated = False

                # Check internet connection
                if not (self.thread1 and self.thread1.is_alive()):
                    self.thread1 = threading.Thread(target=self.connecting, args=(conn_rate,))
                    self.thread1.start()

                if not (self.thread2 and self.thread2.is_alive()):
                    self.thread2 = threading.Thread(target=self.pinging, args=(pub_rate,pub_rate_queue))
                    self.thread2.start()

            except Exception as error:
                capture_exception(error)
                self.log_error(
                    f"[ROSAgent] Run Error: {type(error).__name__}, {error}"
                )
            check_threads_rate.sleep()

    def connecting(self, conn_rate):
        while True:
            if not self.connection.offline_agent.task_offline_started:
                self.check_internet()
                conn_rate.sleep()

    def pinging(self, pub_rate, pub_rate_queue):
        while True:
            try:
                pub_rate_value = pub_rate_queue.get(block=False)

                if rosversion=="2":
                    pub_rate = rclpy.create_rate(pub_rate_value)
                else:
                    pub_rate = rospy.Rate(pub_rate_value)

                if self.ws_open:
                    self.ping_filtering_mode()

            except queue.Empty:
                if self.ws_open:
                    self.ping_filtering_mode()

            pub_rate.sleep()
