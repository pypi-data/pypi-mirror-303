[![Official](https://img.shields.io/badge/Official%20-Auromix-blue?style=flat&logo=world&logoColor=white)](https://github.com/Auromix) &nbsp;
[![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-green)](https://ubuntu.com/) &nbsp;
[![LICENSE](https://img.shields.io/badge/license-Apache--2.0-informational)](https://github.com/Auromix/auro_joystick/blob/main/LICENSE) &nbsp;
[![GitHub Repo stars](https://img.shields.io/github/stars/Auromix/auro_joystick?style=social)](https://github.com/Auromix/auro_joystick/stargazers) &nbsp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Hermanye233?style=social)](https://twitter.com/Hermanye233) &nbsp;

# 🎮 Auro Joystick

Auro Joystick is a Python library designed for interfacing with joystick devices in robotics applications, offering robust support for ROS to facilitate easy integration.

![Joystick ROS Control](docs/images/ros_control.gif)

## 🚀 Features

- **Joystick Detection:** Automatically identifies supported joystick devices.
- **Event Handling:** Efficiently processes input events for joystick buttons and axes.
- **ROS Compatibility:** Seamlessly integrates with both ROS1 and ROS2 for robotic systems.
- **Configurable Logging:** Delivers comprehensive logging for straightforward debugging.
- **Custom Event Handlers:** Supports the registration of custom event handlers for specific joystick actions.

## 🧪 Testing Conditions

Auro Joystick has been tested on the `Beitong` gamepad.

It is also compatible with other controllers that follow the `Xbox` layout.

## ⚙️ Installation

To install Auro Joystick, you can use one of the following methods:

```bash
# Install from PyPI
pip install auro_joystick
```

```bash
# Install from the current directory (local development)
pip install .
```

## 🔥 Quickstart

You can find detailed examples for the project in the `examples` directory of the repository.

### Print Input

This example will display the current inputs and corresponding values from your gamepad:

```bash
python examples/print_input.py
```

### ROS Example

Use the `left joystick` to control the movement of a turtle in Turtlesim, while the `right joystick` will manage its rotation.

Press the `B` key to reset the turtle.

```bash
# [Terminal 1]
# Run roscore
roscore
```

```bash
# [Terminal 2]
# Run Turtlesim
rosrun turtlesim turtlesim_node
```

```bash
# [Terminal 3]
# Run the example
python examples/control_ros_turtlesim.py
```

### Minimal Code Example

This example will call a function when the `A` button is pressed.

```python
import time
from auro_joystick import AuroJoystick


# Your callback function
def on_button_a_pressed():
    print("Button A pressed!")


# Init the joystick
joystick = AuroJoystick()
# Register the function for button A
joystick.register_event_handler(on_button_a_pressed, "button_a_pressed")

# Start the joystick
joystick.start()

# Your loop
while True:
    time.sleep(0.05)
```

```bash
python examples/minimal.py
```

## 🧑‍💻 Documentation

For comprehensive documentation, please refer to the comments within the source code and examples.

## 🙋 Troubleshooting

### Joystick Device Not Found

```python
ValueError: Joystick device not found
```

<details> <summary> Click here to see the solution </summary>
It means that the system couldn't find your joystick.

- Step 1: How AuroJoystick Finds Devices

    AuroJoystick automatically searches for devices matching certain keywords, like `["pad", "X-Box", "360"]`.

- Step 2: Manual Device Path Setup

    If the joystick isn’t found automatically, you can manually specify the device path.

    ```bash
    # Install input-utils
    sudo apt-get install input-utils
    # List input devices
    sudo lsinput
    ```

- Step 3: Find the Joystick Device

   Look for a device that looks like this:

   ```bash
   /dev/input/event17
      bustype : BUS_USB
      vendor  : 0x45e
      product : 0x28e
      version : 256
      name    : "Microsoft X-Box 360 pad"
      phys    : "usb-0000:00:14.0-6.4/input0"
   ```

- Step 4: Use the Device Path

    In your code, specify the path:

    ```python
    joystick = AuroJoystick(device_path="/dev/input/event17")
    ```

</details>

### Permission Denied for Input Device

```bash
PermissionError: [Errno 13] Permission denied: '/dev/input/event18'
```

<details> <summary> Click here to see the solution </summary>
This error means the program does not have the necessary permissions to access the device.

- Step 1: Grant Temporary Permissions

    To give your program temporary access, you can change the permissions of the device using the `chmod` command:

    ```bash
    sudo chmod 777 /dev/input/event18
    ```

    This grants read, write, and execute permissions for all users. Note that this is temporary and will be reset after a reboot.

    This ensures your joystick device is accessible every time it's plugged in.

</details>

If you encounter any issues or have questions regarding this package, please contact the maintainers:

- Herman Ye @ Auromix (Email: <hermanye233@icloud.com>)

## 📜 License

```text
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
```

## 🏆 Contributing

Contributions are welcome! Please follow the guidelines provided in the repository for contributing.
