"""
Copyright 2023-2024 Herman Ye@Auromix

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""

import evdev
import signal
import os
import threading
from auro_utils import Logger


DEVICE_KEYWORDS = ["pad", "X-Box", "360"]


class AuroJoystick:
    """A class to interface with a joystick device.

    This class handles joystick input events and allows for event
    handling through registered functions.
    """

    def __init__(self, device_path=None, log_level="info"):
        """Initializes the AuroJoystick instance.

        Args:
            device_path (str): Optional path to the joystick device.
            log_level (str): The logging level (default is "info").
        """
        self._init_exit_signal()
        self._init_logger(log_level=log_level)
        self._init_device(device_path)
        self._init_event_handlers()

    def signal_handler(self, signum, frame):
        """Handles the exit signal for the joystick.

        Args:
            signum (int): The signal number.
            frame (signal.Frame): The current stack frame.
        """
        print("Received exit signal...")
        os._exit(0)

    def _init_exit_signal(self):
        signal.signal(signal.SIGINT, self.signal_handler)

    def _init_logger(self, log_level):
        """Initializes the logger for the joystick.

        Args:
            log_level (str): The logging level to use.
        """
        self.logger = Logger(log_level=log_level)

    def _init_device(self, device_path=None):
        """Initializes the joystick device.

        If device_path is not provided, searches for a device matching
        DEVICE_KEYWORDS.

        Args:
            device_path (str): Optional path to the joystick device.

        Raises:
            ValueError: If no joystick device is found.
        """
        self._device = None
        self._device_path = device_path
        # Get device
        if self._device_path is None:
            current_devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
            for device in current_devices:
                if any(keyword in device.name.lower() for keyword in DEVICE_KEYWORDS):
                    self._device = device
                    break
        else:
            self._device = evdev.InputDevice(device_path)
        # Check if device is found
        if self._device is None:
            raise ValueError("Joystick device not found")
        else:
            self.logger.log_info(
                f"Device found: {self._device.name} at {self._device.path}"
            )
            self.logger.log_success("Device connected, listening for events...")

    def _init_event_handlers(self):
        """Initializes event handlers and state tracking for joystick input."""
        self._event_handlers = {}
        self._pressed_keys = set()
        self.right_trigger_value = 0
        self.left_trigger_value = 0
        self.right_stick_value = [0, 0]
        self.left_stick_value = [0, 0]

    def _handle_event(self, event):
        """Handles input events from the joystick.

        This method processes key and absolute axis events, invoking the
        appropriate event handlers for the joystick buttons and axes.

        Args:
            event (evdev.Event): The event to handle.
        """
        # Key events
        if event.type == evdev.ecodes.EV_KEY:
            # Start
            if event.code == 315:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_start")
                    self._execute_event_handler("button_start_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_start" in self._pressed_keys:
                        self._pressed_keys.remove("button_start")
                        self._execute_event_handler("button_start_released")
            # Back
            if event.code == 314:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_back")
                    self._execute_event_handler("button_back_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_back" in self._pressed_keys:
                        self._pressed_keys.remove("button_back")
                        self._execute_event_handler("button_back_released")

            # Left bumper
            elif event.code == 310:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_left_bumper")
                    self._execute_event_handler("button_left_bumper_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_left_bumper" in self._pressed_keys:
                        self._pressed_keys.remove("button_left_bumper")
                        self._execute_event_handler("button_left_bumper_released")

            # Right bumper
            elif event.code == 311:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_right_bumper")
                    self._execute_event_handler("button_right_bumper_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_right_bumper" in self._pressed_keys:
                        self._pressed_keys.remove("button_right_bumper")
                        self._execute_event_handler("button_right_bumper_released")

            # Left stick
            if event.code == 317:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_left_stick")
                    self._execute_event_handler("button_left_stick_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_left_stick" in self._pressed_keys:

                        self._pressed_keys.remove("button_left_stick")
                        self._execute_event_handler("button_left_stick_released")

            # Right stick
            if event.code == 318:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_right_stick")
                    self._execute_event_handler("button_right_stick_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_right_stick" in self._pressed_keys:
                        self._pressed_keys.remove("button_right_stick")
                        self._execute_event_handler("button_right_stick_released")

            # A
            if event.code == 304:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_a")
                    self._execute_event_handler("button_a_pressed")

                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_a" in self._pressed_keys:
                        self._pressed_keys.remove("button_a")
                        self._execute_event_handler("button_a_released")

            # B
            if event.code == 305:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_b")
                    self._execute_event_handler("button_b_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_b" in self._pressed_keys:
                        self._pressed_keys.remove("button_b")
                        self._execute_event_handler("button_b_released")

            # X
            if event.code == 307:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_x")
                    self._execute_event_handler("button_x_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_x" in self._pressed_keys:
                        self._pressed_keys.remove("button_x")
                        self._execute_event_handler("button_x_released")

            # Y
            if event.code == 308:
                if event.value == evdev.events.KeyEvent.key_down:
                    self._pressed_keys.add("button_y")
                    self._execute_event_handler("button_y_pressed")
                elif event.value == evdev.events.KeyEvent.key_up:
                    if "button_y" in self._pressed_keys:
                        self._pressed_keys.remove("button_y")
                        self._execute_event_handler("button_y_released")

        # Absolute axis events
        elif event.type == evdev.ecodes.EV_ABS:
            # Dpad up and down
            if event.code == 17:
                if event.value == -1:
                    self._pressed_keys.add("dpad_up")
                    self._execute_event_handler("dpad_up_pressed")
                elif event.value == 1:
                    self._pressed_keys.add("dpad_down")
                    self._execute_event_handler("dpad_down_pressed")
                elif event.value == 0:
                    if "dpad_up" in self._pressed_keys:
                        self._pressed_keys.remove("dpad_up")
                        self._execute_event_handler("dpad_up_released")
                    elif "dpad_down" in self._pressed_keys:
                        self._pressed_keys.remove("dpad_down")
                        self._execute_event_handler("dpad_down_released")
                    else:
                        raise ValueError("Invalid dpad value")
                else:
                    raise ValueError("Invalid dpad value")
            # Dpad left and right
            elif event.code == 16:
                if event.value == -1:
                    self._pressed_keys.add("dpad_left")
                    self._execute_event_handler("dpad_left_pressed")
                elif event.value == 1:
                    self._pressed_keys.add("dpad_right")
                    self._execute_event_handler("dpad_right_pressed")
                elif event.value == 0:
                    if "dpad_left" in self._pressed_keys:
                        self._pressed_keys.remove("dpad_left")
                        self._execute_event_handler("dpad_left_released")
                    elif "dpad_right" in self._pressed_keys:
                        self._pressed_keys.remove("dpad_right")
                        self._execute_event_handler("dpad_right_released")
                    else:
                        raise ValueError("Invalid dpad value")
                else:
                    raise ValueError("Invalid dpad value")
            # Left trigger
            elif event.code == 2:
                if event.value == 0:
                    if "left_trigger" in self._pressed_keys:
                        self._pressed_keys.remove("left_trigger")
                        self.left_trigger_value = event.value
                        self._execute_event_handler(
                            "left_trigger_released", self.left_trigger_value
                        )
                elif event.value > 0:
                    self._pressed_keys.add("left_trigger")
                    self.left_trigger_value = event.value
                    self._execute_event_handler(
                        "left_trigger_pressed", self.left_trigger_value
                    )
                else:
                    raise ValueError("Invalid left trigger value")

            # Right trigger
            elif event.code == 5:
                if event.value == 0:
                    if "right_trigger" in self._pressed_keys:

                        self._pressed_keys.remove("right_trigger")
                        self.right_trigger_value = event.value
                        self._execute_event_handler(
                            "right_trigger_released", self.right_trigger_value
                        )
                elif event.value > 0:
                    self._pressed_keys.add("right_trigger")
                    self.right_trigger_value = event.value
                    self._execute_event_handler(
                        "right_trigger_pressed", self.right_trigger_value
                    )
                else:
                    raise ValueError("Invalid right trigger value")

            # Right stick
            elif event.code == 4:
                self.right_stick_value[0] = -event.value
                self._execute_event_handler(
                    "right_stick_moved",
                    self.right_stick_value[0],
                    self.right_stick_value[1],
                )
            elif event.code == 3:
                self.right_stick_value[1] = -event.value
                self._execute_event_handler(
                    "right_stick_moved",
                    self.right_stick_value[0],
                    self.right_stick_value[1],
                )

            # Left stick
            elif event.code == 1:
                self.left_stick_value[0] = -event.value
                self._execute_event_handler(
                    "left_stick_moved",
                    self.left_stick_value[0],
                    self.left_stick_value[1],
                )
            elif event.code == 0:
                self.left_stick_value[1] = -event.value
                self._execute_event_handler(
                    "left_stick_moved",
                    self.left_stick_value[0],
                    self.left_stick_value[1],
                )

            else:
                self.logger.log_warning(f"Unknown event code: {event.code}")

        # Ignore other event types
        else:
            pass

    def _execute_event_handler(self, handler_name, *args):
        """Executes registered event handlers for the specified event.

        Args:
            handler_name (str): The name of the event handler to execute.
            *args: Additional arguments to pass to the event handler.
        """
        if handler_name in self._event_handlers:
            for handler in self._event_handlers[handler_name]:
                # Pass event data to the handler function
                handler(*args)

    def register_event_handler(self, handler_function, joystick_event):
        """Registers an event handler for a specific joystick event.

        Args:
            handler_function (callable): The function to call when the event occurs.
            joystick_event (str): The joystick event to register the handler for.
        """
        if joystick_event not in self._event_handlers:
            self._event_handlers[joystick_event] = []
        self._event_handlers[joystick_event].append(handler_function)
        self.logger.log_debug(f"Handler registered for event: {joystick_event}")

    def loop(self):
        """Continuously reads events from the joystick device."""
        for event in self._device.read_loop():
            self._handle_event(event)

    def start(self):
        """Starts the event loop in a separate thread."""
        self._thread = threading.Thread(target=self.loop)
        self._thread.start()
