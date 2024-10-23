"""
VICI valve controller class

This file contains a class for controlling various VICI valve. They are connected to the PC through either RS232 or USB
as virtual COM port. Communication is achieved through sending ASCII strings.

Authors: Sebastian Steiner

(c) Hein Group, UBC 2019
"""

from typing import Union
from vicivalve.device_codes import Cmds
import logging
from ftdi_serial import Serial, SerialReadTimeoutException
from time import sleep

logger = logging.getLogger(__name__)

# dictionary to map integers to letter positions
TWO_POSITION_VALVE = {
    1: "A",
    2: "B"
}


class VICI(object):
    """
    This is a basic driver class for the VICI Valco Universal Electric Actuator. At the moment it only implements a
    subset of all available commands based on the most common needs. It works with both the USB and the RS232/485
    variety, as long as an FTDI converter is used.

    To use a VICI valve, creat an instance of the VICI class and pass it a Serial object fo the connection:
    >>> serial = Serial(baudrate=9600)
    >>> valve = VICI(serial)

    If RS485 is used AND all valves on one line have individual addresses, multiple VICI instances can use the same
    Serial object. In that case, an address must be passed:
    >>> valve1 = VICI(serial=serial, address=1)
    >>> valve2 = VICI(serial=serial, address=2)

    After installing a new valve head, the actuator needs to "learn" the end stops in order to properly switch the
    valve:
    >>> valve.learn()

    The valve can be homed (sent to position A or 1), switched to a position (A or B, or 0-n where n is the number of
    positions), or toggled:
    >>> valve.home()  # sends the valve to position A or 1
    >>> valve.switch_valve("B")  # sends the valve to position B
    >>> valve.switch_valve(1)  # sends the valve back to position A, using an integer as argument
    >>> valve.toggle()  # sends the valve to position B, since it was in A before
    >>> valve.toggle()  # sends the valve back to position A
    """

    def __init__(self, serial: Serial, positions: int=2, address: Union[int, str]=None):
        """
        Initializer of the VICI class.

        :param Serial serial: An ftdi_serial object for communication with the valve.
        :param int positions: Number of positions (NOT ports!). A classical HPLC valve is a six port two position valve.
        :param int address: If multiple valves are used with RS485, this is the address of the valve (0-9 or A-Z)
        """
        self.logger = logger.getChild(self.__class__.__name__)

        self._serial = serial
        self._positions = positions
        if address is not None:
            self._address = f"/{address}"
        else:
            self._address = ""

        if positions == 2:
            self._position_dict = TWO_POSITION_VALVE
        elif positions > 2:
            # creates a dictionary {'1': 1, '2': 2, ..., 'n': n}
            self._position_dict = dict(zip([i + 1 for i in range(positions)], [str(i + 1) for i in range(positions)]))
        else:
            raise ValueError(f"Number of positions \"{positions}\" is outside the valid range of 2 or more!")

        self._send_and_receive(f"{Cmds.InterfaceMode}1")

    def _send_and_receive(self, command: str, parameter: Union[str, int]=None, retry: bool=False, retries: int=5,
                          timeout: float = 5) -> str:
        """
        Sends a string to the device and waits for a reply.

        :param command: String to be sent to the valve. For a full list of available commands see VICI user manual.
        :param parameter: Optional parameter for such commands that require one.
        :param retry: If the request times out, should the routine keep trying or throw an error immediately?
        :param retries: If reties are active, how many times should it try before raising an error?
        :param timeout: Maximum wait time for a reply.
        :return:
        """
        if parameter is not None:
            command_string = f"{self._address}{command}{parameter}\r"
        else:
            command_string = f"{self._address}{command}\r"

        while True:
            try:
                self.logger.debug(f"Sending command \"{command_string.strip()}\"")
                reply = self._serial.request(data=command_string.encode(), timeout=timeout, line_ending=b'\r')
                self.logger.debug(f"Received reply \"{reply.strip()}\"")
                return reply.strip().decode()
            except SerialReadTimeoutException:
                retries -= 1
                if retry and retries >= 0:
                    self.logger.debug(f"Connection timed out. Retrying {retries + 1} more times...")
                    continue
                else:
                    logger.exception("Number of retries exceeded!")
                    raise

    def learn(self):
        """
        Prompts the actuator to "learn" the locations of the physical stops. This must be executed after installing
        a new valve head! After learning, the valve ends in Position A.

        :return: True if successful, False in case of error
        """
        reply = self._send_and_receive(Cmds.Learn, timeout=15)
        if reply == f"CPA":
            return True
        else:
            return False

    def home(self):
        """
        Sends the valve to position A or 1.

        :return: True if successful, False in case of error
        """
        reply = self._send_and_receive("HM")

        return reply[-1] == "A" or reply[-1] == "0"

    def _lookup_position(self, position: Union[int, str]):
        """
        Validate that a position is valid for the valve's specified configuration.
        :param int or str position: 0 for position A, 1 for position B
        :return: device-acceptable string representation of the specified position.
        :raises ValueError: if the specified position is invalid.
        """
        if position in self._position_dict.values():
            pos_str = position
        elif position in self._position_dict.keys():
            pos_str = self._position_dict[position]
        else:
            raise ValueError(
                f"Valid position arguments are integers {self._position_dict.keys()}"
                f"or strings {self._position_dict.values()}!"
            )
        return pos_str

    def switch_valve(self, position: Union[int, str]):
        """
        Switches the valve either to the A or B position.

        :param int or str position: 0 for position A, 1 for position B
        :return: True if successful, False in case of error
        """
        pos_str = self._lookup_position(position)
        cmd_str = f"{Cmds.MoveToPosition}{pos_str}"
        reply = self._send_and_receive(cmd_str)
        return True if reply == cmd_str else False

    def move_to_position(self, position: Union[int, str]):
        """
        Alias for :meth:`switch_valve`.
        """
        return self.switch_valve(position)

    def move_clockwise_to_position(self, position: Union[int, str]):
        pos_str = self._lookup_position(position)
        cmd_str = f"{Cmds.MoveClockwiseToPosition}{pos_str}"
        reply = self._send_and_receive(cmd_str)
        return True if reply == cmd_str else False

    def move_counterclockwise_to_position(self, position: Union[int, str]):
        pos_str = self._lookup_position(position)
        cmd_str = f"{Cmds.MoveCounterClockwiseToPosition}{pos_str}"
        reply = self._send_and_receive(cmd_str)
        return True if reply == cmd_str else False

    def toggle(self):
        """
        Toggles the valve (i.e. switches it to the opposite position regardless of the previous position).

        :return: str New position
        """
        reply = self._send_and_receive(Cmds.Toggle)

        if reply.startswith(Cmds.CurrentPosition):
            try: # Multi-position mode
                return int(reply.lstrip(Cmds.CurrentPosition))
            except ValueError: # Two-position mode (returns 'A' or 'B')
                return reply.lstrip(Cmds.CurrentPosition)

    def current_position(self):
        """
        Returns the current valve position.

        :return: str Current position
        """
        reply = self._send_and_receive(Cmds.CurrentPosition)

        if reply.startswith(Cmds.CurrentPosition):
            try: # Multi-position mode
                return int(reply.lstrip(Cmds.CurrentPosition))
            except ValueError: # Two-position mode (returns 'A' or 'B')
                return reply.lstrip(Cmds.CurrentPosition)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # valve_serial = Serial(device_port="COM34", baudrate=9600)
    valve_serial = Serial(device_serial="AJ02ZBW3", baudrate=9600)
    v = VICI(valve_serial)

    v.learn()

    while True:
        v.switch_valve(1)
        sleep(1)
        v.switch_valve(2)
        sleep(1)
        v.switch_valve("A")
        sleep(1)
        v.switch_valve("B")
        sleep(1)
