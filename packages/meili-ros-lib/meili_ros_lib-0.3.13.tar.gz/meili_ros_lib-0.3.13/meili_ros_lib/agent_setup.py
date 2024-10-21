from os import environ
from meili_ros_lib.sentry import agent_sentry

rosversion=environ["ROS_VERSION"]

class Setup:
    def __init__(self):
        # Variables initialization
        self.aws_access_key_id = None
        self.aws_secret_access_key = None
        self.path_planning = None
        self.traffic_control = None
        self.battery_present = False
        self.lipo_battery = None
        self.number_of_cells = None
        self.outdoor = False
        self.publish_frequency = None
        self.offline_flag = None

        # Logging
        self.log_info = None
        self.log_error = None

    def init_parameters_setup(self):
        try:

            if (
                    environ.get("AWS_ACCESS_KEY_ID") is not None
                    and environ.get("AWS_SECRET_ACCESS_KEY") is not None
            ):
                self.aws_access_key_id = environ.get("AWS_ACCESS_KEY_ID")
                self.aws_secret_access_key = environ.get("AWS_SECRET_ACCESS_KEY")
            else:
                self.aws_access_key_id = None
                self.aws_secret_access_key = None

            # get ROS distro
            ros_distro = environ["ROS_DISTRO"]
            ros_version = environ["ROS_VERSION"]

            self.log_info("[SetUp] Reading initialization parameters")
            self.log_info(f"[SetUp] Ros distro is : {ros_distro}")
            self.log_info(f"[SetUp] Ros version is :{ros_version}")

        except KeyError:
            self.log_error(f"[SetUp] Parameter {KeyError} does not exist. ")
            agent_sentry(KeyError)
            self.log_error("[SetUp] Roscore is not running, check your ros config")
            raise

        self.log_info(
            "[SetUp] COMPLETED Initial ROS Parameter configuration"
        )

        # get initial ros parameters
    def battery_parameter(self, battery, lipo_cells):
        """
        Sets the battery parameters. 

        Args:
            battery (bool):   If True the battery is present, False otherwise.
            lipo_cells (int): Indicates whether the battery is a LiPo battery or not. If >0 the
                              battery is a LiPo battery and "battery" is automatically set to True.

        Returns:
            None
        """
        if int(lipo_cells) > 0:
            self.battery_present = True
            self.lipo_battery = True
            self.number_of_cells = int(lipo_cells)
            self.log_info(f"[SetUp] The {self.number_of_cells}S Lipo battery is present")

        elif battery is True:
            self.battery_present = True
            self.log_info("[SetUp] The Battery is present")
