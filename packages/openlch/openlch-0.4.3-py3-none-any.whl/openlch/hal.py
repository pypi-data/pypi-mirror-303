import grpc
from typing import List, Tuple, Dict, Union
from . import hal_pb_pb2
from . import hal_pb_pb2_grpc

__all__ = ['HAL']

__pdoc__ = {}
__pdoc__["hal_pb_pb2"] = None
__pdoc__["hal_pb_pb2_grpc"] = None

class HAL:
    """
    Hardware Abstraction Layer for interacting with the MilkV board.

    Args:
        host (str): The IP address of the MilkV board. Defaults to '192.168.42.1'.
        port (int): The port number for gRPC communication. Defaults to 50051.
    """

    def __init__(self, host: str = '192.168.42.1', port: int = 50051) -> None:
        self.__channel = grpc.insecure_channel(f'{host}:{port}')
        self.__stub = hal_pb_pb2_grpc.ServoControlStub(self.__channel)
        self.servo = self.Servo(self.__stub)
        self.system = self.System(self.__stub)

    def close(self) -> None:
        """Close the gRPC channel."""
        self.__channel.close()

    class Servo:
        """Class for servo-related operations."""

        def __init__(self, stub):
            self.__stub = stub

        def get_positions(self) -> List[Tuple[int, float]]:
            """
            Get current positions of all servos.

            Returns:
                List[Tuple[int, float]]: A list of tuples containing servo IDs and their positions.
            """
            response = self.__stub.GetPositions(hal_pb_pb2.Empty())
            return [(pos.id, pos.position) for pos in response.positions]

        def set_positions(self, positions: List[Tuple[int, float]]) -> None:
            """
            Set positions for multiple servos.

            Args:
                positions (List[Tuple[int, float]]): A list of tuples, each containing a servo ID and its target position.
            """
            joint_positions = [
                hal_pb_pb2.JointPosition(id=id, position=position)
                for id, position in positions
            ]
            request = hal_pb_pb2.JointPositions(positions=joint_positions)
            self.__stub.SetPositions(request)

        def get_servo_info(self, servo_id: int) -> Dict[str, Union[int, float]]:
            """
            Get detailed information about a specific servo.

            Args:
                servo_id (int): The ID of the servo to query.

            Returns:
                Dict[str, Union[int, float]]: A dictionary containing servo information.

            Raises:
                Exception: If there's an error retrieving the servo information.
            """
            request = hal_pb_pb2.ServoId(id=servo_id)
            response = self.__stub.GetServoInfo(request)
            if response.HasField('info'):
                info = response.info
                return {
                    'id': info.id,
                    'temperature': info.temperature,
                    'current': info.current,
                    'voltage': round(info.voltage, 2),
                    'speed': info.speed,
                    'current_position': info.current_position,
                    'min_position': info.min_position,
                    'max_position': info.max_position
                }
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

        def scan(self) -> List[int]:
            """
            Scan for connected servos.

            Returns:
                List[int]: A list of IDs of the connected servos.
            """
            response = self.__stub.Scan(hal_pb_pb2.Empty())
            return list(response.ids)

        def change_id(self, old_id: int, new_id: int) -> bool:
            """
            Change the ID of a servo.

            Args:
                old_id (int): The current ID of the servo.
                new_id (int): The new ID to assign to the servo.

            Returns:
                bool: True if the ID change was successful, False otherwise.

            Raises:
                Exception: If there's an error changing the servo ID.
            """
            request = hal_pb_pb2.IdChange(old_id=old_id, new_id=new_id)
            response = self.__stub.ChangeId(request)
            if response.HasField('success'):
                return response.success
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

    class System:
        """Class for system-related operations."""

        def __init__(self, stub):
            self.__stub = stub

        def set_wifi_info(self, ssid: str, password: str) -> None:
            """
            Set WiFi credentials for the MilkV board.

            Args:
                ssid (str): The SSID of the WiFi network.
                password (str): The password for the WiFi network.
            """
            request = hal_pb_pb2.WifiCredentials(ssid=ssid, password=password)
            self.__stub.SetWifiInfo(request)
