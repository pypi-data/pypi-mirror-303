# FlightMatrix Bridge : API for Flight Matrix Simulation Software

**FlightMatrix Bridge** is a Python-based API designed for controlling and fetching information, frames, and other data from Flight Matrix. This library enables efficient and real-time communication between various processes in a system, primarily designed for interfacing flight simulators, UAV systems, or other robotics platforms. It utilizes the `multiprocessing.shared_memory` module to share data such as frames, sensor data, and movement commands across multiple processes.

Download the software from [Flight Matrix](https://gamejolt.com/games/flightmatrix/933049).

The project is structured around two primary files:

- **`bridge.py`**: Implements the core functionalities of shared memory management, handling frames, sensor data, movement commands, and logging.
- **`utilities.py`**: Provides utility functions to handle timestamps and convert them into human-readable formats.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    1. [Initializing the FlightMatrixBridge](#initializing-the-flightmatrixbridge)
    2. [Units](#units)
    3. [Logging Functions](#logging-functions)
    4. [Flight Matrix API](#flight-matrix-api)
        - [Getting Frame Data](#getting-frame-data)
        - [Fetching Sensor Data](#fetching-sensor-data)
        - [Sending Movement Commands](#sending-movement-commands)
    5. [Resolution & Noise Configuration](#resolution--noise-configuration)
    6. [Timestamp Utilities](#timestamp-utilities)
5. [Detailed Functionality](#detailed-functionality)
    - [Initialization](#initialization)
    - [Shared Memory Management](#shared-memory-management)
    - [Frame Handling](#frame-handling)
    - [Sensor Data Handling](#sensor-data-handling)
    - [Movement Command Management](#movement-command-management)
    - [Logging](#logging)
    - [Noise Application](#noise-application)
6. [Examples](#examples)
    1. [Example 1: Fetching Frames](#example-1-fetching-frames)
    2. [Example 2: Sending Movement Commands](#example-2-sending-movement-commands)
    3. [Example 3: Fetching Sensor Data](#example-3-fetching-sensor-data)
7. [Documentation](#documentation)
    1. [Class: `FlightMatrixBridge`](#class-flightmatrixbridge)
        - [Attributes](#attributes)
        - [Methods](#methods) 
        - [utility.py](#utility.py)

## Introduction

The **FlightMatrixBridge** system is designed to bridge multiple processes that need to access shared memory for real-time communication. The typical use cases include flight simulators, robotics platforms, autonomous vehicles, and any application where sharing large datasets like frames or sensor readings between processes is essential.

This package provides:
- An interface to retrieve frames and sensor data from shared memory.
- The ability to send movement commands to be processed by another service.
- Real-time noise application to sensor data.
- Utilities to handle timestamps.

## Features

- **Frame Management**: Retrieve left/right frames, z-depth maps, and segmentation frames in real-time.
- **Sensor Data Access**: Retrieve real-time sensor data such as location, orientation, velocity, acceleration, magnetometer readings, and more.
- **Movement Command Handling**: Send movement commands (position and orientation) for external systems to process.
- **Noise Simulation**: Add configurable levels of noise to sensor data for testing robustness.
- **Flexible Resolution Handling**: Easily set and adjust resolution for frames.
- **Timestamp Management**: Convert timestamps into human-readable formats and handle system-wide timing data.

## Installation

Download the software from [Flight Matrix](https://gamejolt.com/games/flightmatrix/933049).

To install the **FlightMatrixBridge (API)**, simply use pip:

```bash
pip install flightmatrixbridge
```

Make sure your system has Python 3.8+ and supports the `multiprocessing.shared_memory` module.

## Usage

### Initializing the FlightMatrixBridge

To initialize and start using the **FlightMatrixBridge**, create an instance of the `FlightMatrixBridge` class and specify the resolution of the frames you want to handle:

```python
from flightmatrix.bridge import FlightMatrixBridge

bridge = FlightMatrixBridge(resolution=(1226, 370))  # Set frame resolution (width, height)
```

### Units

The system uses the following units for sensor data:
- Length: centimeters (cm)
- Angular values: degrees (°)
- Angular velocity: degrees per second (°/s)
- Acceleration: centimeters per second squared (cm/s²)
- Magnetometer readings: unit vector
- LiDAR data: centimeters (cm)
- Collision detection: centimeters (cm)
- Timestamp: milliseconds (ms)

### Logging Functions

You can configure logging based on your needs. The logging system provides flexibility to output logs either to the console or a file, and supports different log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `SUCCESS`).

```python
# Set log level to 'DEBUG'
bridge.set_log_level('DEBUG')

# Enable logging to file
bridge.set_write_to_file(True)
```

### Flight Matrix API

The core functionalities include retrieving frames, fetching sensor data, and sending movement commands.

#### Getting Frame Data

You can retrieve frames from both the left and right cameras. You also have access to depth and segmentation data.

```python
# Retrieve right camera frame
right_frame = bridge.get_right_frame()

# Retrieve left camera frame
left_frame = bridge.get_left_frame()

# Retrieve z-depth for the right camera
right_zdepth = bridge.get_right_zdepth()

# Retrieve segmentation frame for the left camera
left_seg = bridge.get_left_seg()
```

#### Fetching Sensor Data

The bridge allows real-time access to sensor data from the shared memory block. This data includes location, orientation, velocity, acceleration, and more.

```python
sensor_data = bridge.get_sensor_data()
print(sensor_data)
```

#### Sending Movement Commands

To send movement commands (position and orientation) to a system, use the `send_movement_command` method.

```python
# Send movement command (x, y, z, roll, pitch, yaw)
bridge.send_movement_command(1.0, 2.0, 3.0, 0.1, 0.2, 0.3)
```

### Resolution & Noise Configuration

You can adjust the frame resolution dynamically and control noise levels applied to sensor data.

```python
# Set a new resolution for frames
bridge.set_resolution(1280, 720)

# Set noise level for sensor data
bridge.set_noise_level(0.05)

# Enable or disable noise application
bridge.set_apply_noise(True)
```

### Timestamp Utilities

The `utilities.py` file provides functions to convert timestamps from milliseconds into human-readable formats and to `datetime` objects.

```python
from flightmatrix.utilities import timestamp2string, timestamp2datetime

# Convert timestamp to string
timestamp_string = timestamp2string(1633029600000)
print(timestamp_string)  # Output: '2021-10-01 00:00:00:000'

# Convert timestamp to datetime object
timestamp_dt = timestamp2datetime(1633029600000)
print(timestamp_dt)  # Output: datetime object in UTC
```

## Detailed Functionality

### Initialization

Upon initialization, the `FlightMatrixBridge` class sets up shared memory blocks for frames, sensor data, and movement commands. It also configures the resolution and frame shapes.

### Shared Memory Management

The shared memory blocks are initialized using `multiprocessing.shared_memory.SharedMemory`, providing fast, low-latency access to the data. Each memory block corresponds to specific data types like frames, sensor readings, or movement commands.

The memory block names and their associated data are defined in the `memory_names` dictionary within the `FlightMatrixBridge` class:

- `right_frame`: Stores the right camera frame.
- `left_frame`: Stores the left camera frame.
- `right_zdepth`: Z-depth map for the right camera.
- `left_zdepth`: Z-depth map for the left camera.
- `right_seg`: Segmentation data for the right camera.
- `left_seg`: Segmentation data for the left camera.
- `sensor_data`: Sensor data shared memory.
- `movement_command`: Memory block for sending movement commands.

### Frame Handling

Frames can be retrieved from the shared memory using the `_get_frame` method. The frames are stored as NumPy arrays and can be either 1-channel (grayscale) or 3-channel (RGB).

### Sensor Data Handling

The `get_sensor_data` method retrieves sensor readings from the shared memory. The sensor data includes:

- Location `(x, y, z)` in *centimeters*
- Orientation `(roll, pitch, yaw)` in *degrees*
- Angular velocity `(x, y, z)` in *degrees per second*
- Acceleration `(x, y, z)` in *cm/s^2*
- Magnetometer readings `(x, y, z)` in *unit vector*
- LiDAR data `(LiDARForward, LiDARBackward, LiDARLeft, LiDARRight, LiDARBottom) or (Y, -Y, -X, X, -Z)` in *centimeters*
- Collision detection status `(True/False, LocationX, LocationY, LocationZ)` in *centimeters*
- Timestamp in *milliseconds*

### Movement Command Management

Movement commands are written to shared memory using `send_movement_command`. These commands include the position and orientation of the system and are stored as six floating-point values.

### Logging

The logging system is highly configurable and provides essential feedback about the system's operations. You can adjust the verbosity of the logs and decide whether to write them to a file.

### Noise Application

To simulate real-world noise in sensor data, noise can be added using Gaussian distribution. This feature is optional and can be enabled/disabled dynamically.

## Examples

### Example 1: Fetching Frames

```python
import cv2
from flightmatrix.bridge import FlightMatrixBridge
from flightmatrix.utilities import timestamp2string

# Initialize the FlightMatrixBridge
bridge = FlightMatrixBridge()

# Start a loop to continuously fetch and display frames
while True:
    # Fetch the left and right frames
    left_frame_data = bridge.get_left_frame()
    right_frame_data = bridge.get_right_frame()

    # Fetch the z-depth frames for both left and right
    left_zdepth_data = bridge.get_left_zdepth()
    right_zdepth_data = bridge.get_right_zdepth()

    # Retrieve the actual frame arrays and timestamps
    left_frame = left_frame_data['frame']
    right_frame = right_frame_data['frame']

    left_zdepth = left_zdepth_data['frame']
    right_zdepth = right_zdepth_data['frame']
    
    left_timestamp = left_frame_data['timestamp']
    right_timestamp = right_frame_data['timestamp']

    # Convert timestamps to human-readable format
    left_timestamp = timestamp2string(left_timestamp)
    right_timestamp = timestamp2string(right_timestamp)

    # Display the frames in OpenCV windows
    cv2.imshow("Left Frame", left_frame)
    cv2.imshow("Right Frame", right_frame)

    cv2.imshow("Left Z-Depth", left_zdepth_data)
    cv2.imshow("Right Z-Depth", right_zdepth_data)

    # Print timestamps for each frame (optional)
    print(f"Left Frame Timestamp: {left_timestamp}")
    print(f"Right Frame Timestamp: {right_timestamp}")

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release OpenCV windows
cv2.destroyAllWindows()
```

### Example 2: Sending Movement Commands

```python
from flightmatrix.bridge import FlightMatrixBridge

# Initialize the bridge
bridge = FlightMatrixBridge()

# Send a movement command (x, y, z, roll, pitch, yaw)
bridge.send_movement_command(0.5, 1.0, 0.8, 0.0, 0.1, 0.2)
```

In order to reset/stop the movement, you can send a command with all zeros:

```python
bridge.send_movement_command(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
```

### Example 3: Fetching Sensor Data

```python
from flightmatrix.bridge import FlightMatrixBridge

# Initialize the bridge
bridge = FlightMatrixBridge()

# Fetch sensor data
sensor_data = bridge.get_sensor_data()

# Check for errors
if sensor_data.get('error'):
    print("Error fetching sensor data:", sensor_data['error'])
else:
    # Extract sensor readings
    location = sensor_data['location']
    orientation = sensor_data['orientation']
    angular_velocity = sensor_data['angular_velocity']
    acceleration = sensor_data['acceleration']
    magnetometer = sensor_data['magnetometer']
    lidar = sensor_data['lidar']
    collision = sensor_data['collision']
    timestamp = sensor_data['timestamp']

    # Display sensor data in a readable format
    print("Sensor Data:")
    print("-----------------------")
    print(f"Timestamp: {timestamp} ms")
    print(f"Location (cm): X={location[0]:.2f}, Y={location[1]:.2f}, Z={location[2]:.2f}")
    print(f"Orientation (degrees): Roll={orientation[0]:.2f}, Pitch={orientation[1]:.2f}, Yaw={orientation[2]:.2f}")
    print(f"Angular Velocity (deg/s): X={angular_velocity[0]:.2f}, Y={angular_velocity[1]:.2f}, Z={angular_velocity[2]:.2f}")
    print(f"Acceleration (cm/s²): X={acceleration[0]:.2f}, Y={acceleration[1]:.2f}, Z={acceleration[2]:.2f}")
    print(f"Magnetometer (unit vector): X={magnetometer[0]:.2f}, Y={magnetometer[1]:.2f}, Z={magnetometer[2]:.2f}")
    print(f"LiDAR Data (cm): Forward={lidar[0]:.2f}, Backward={lidar[1]:.2f}, Left={lidar[2]:.2f}, Right={lidar[3]:.2f}, Bottom={lidar[4]:.2f}")
    print(f"Collision Detection: Status={collision[0]}, Location (cm): X={collision[1]:.2f}, Y={collision[2]:.2f}, Z={collision[3]:.2f}")

```

## Documentation

#### Class: `FlightMatrixBridge`
This class interfaces with the Flight Matrix system using shared memory for inter-process communication. It manages frames, timestamps, and movement commands, enabling seamless data sharing between processes.

---

##### **Attributes:**

- `width (int)`: The width of the frame, initialized by the resolution provided.
  
- `height (int)`: The height of the frame, initialized by the resolution provided.

- `frame_shape (tuple)`: Tuple representing the shape of the frame as `(height, width)`.

- `frame_shape_3ch (tuple)`: Tuple representing the shape of the frame with 3 channels as `(height, width, 3)`.

- `noise_level (float)`: Specifies the level of noise to be applied. Defaults to `0.01`.

- `apply_noise (bool)`: Boolean flag that determines whether noise should be applied. Defaults to `False`.

- `memory_names (dict)`: Dictionary mapping keys to shared memory block names. Used for storing frame, depth, segmentation, and movement command data.

- `log (Logger)`: A logger instance used for logging events and debugging messages.

- `shm (dict)`: Dictionary storing the shared memory objects for frame data.

- `shm_timestamps (dict)`: Dictionary storing the shared memory objects for timestamps.

- `num_floats (int)`: Number of float values stored in shared memory for movement commands. Defaults to `6`.

---

##### **Methods:**

---

###### **`__init__(self, resolution=(1226, 370))`**

**Description:**  
Initializes the `FlightMatrixBridge` class by setting up shared memory and logging.

**Args:**  
- `resolution (tuple, optional)`: A tuple specifying the frame's width and height. Defaults to `(1226, 370)`.

**Example:**
```python
bridge = FlightMatrixBridge(resolution=(800, 600))
```

---

###### **`set_log_level(self, log_level='INFO')`**

**Description:**  
Sets the logging level for the logger instance to control the verbosity of log output.

**Args:**  
- `log_level (str)`: Desired log level (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`). Default is `'INFO'`.

**Returns:**  
None.

**Example:**
```python
bridge.set_log_level('DEBUG')
```

---

###### **`set_write_to_file(self, write_to_file)`**

**Description:**  
Sets whether the logging should be written to a file or not.

**Args:**  
- `write_to_file (bool)`: If `True`, log messages will be written to a file; otherwise, they won't.

**Returns:**  
None.

**Example:**
```python
bridge.set_write_to_file(True)
```

---

###### **`_initialize_shared_memory(self)`**

**Description:**  
Initializes shared memory blocks for frames and timestamps based on the keys stored in `memory_names`. If the shared memory block for a specific key is not available, a warning will be logged.

**Raises:**  
- `FileNotFoundError`: If the shared memory block for a key does not exist.

**Returns:**  
None.

**Example:**
```python
bridge._initialize_shared_memory()
```

---

###### **`_initialize_movement_command_memory(self)`**

**Description:**  
Sets up shared memory for movement commands (`x, y, z, roll, pitch, yaw`) and an availability flag. If the shared memory block exists, it will attach to it; otherwise, it will create a new block.

**Raises:**  
- `FileExistsError`: If the shared memory block already exists when trying to create it.

**Returns:**  
None.

**Example:**
```python
bridge._initialize_movement_command_memory()
```

---

###### **`_get_frame(self, key, channels=3)`**

**Description:**  
Retrieves a frame from shared memory. Handles both 3-channel and single-channel frame retrieval.

**Args:**  
- `key (str)`: Key identifying the shared memory segment.
- `channels (int, optional)`: Number of channels in the frame, default is `3`.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved frame or `None` if an error occurred.
  - `'timestamp' (any or None)`: The timestamp associated with the frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Raises:**  
- `Warning`: If shared memory is not available or if there is a resolution mismatch.

**Example:**
```python
frame_data = bridge._get_frame('right_frame', channels=3)
```

---

###### **`_get_timestamp(self, key)`**

**Description:**  
Retrieves the timestamp associated with the frame stored in shared memory.

**Args:**  
- `key (str)`: Key identifying the shared memory segment for the timestamp.

**Returns:**  
- `int or None`: The timestamp as an integer, or `None` if not available.

**Example:**
```python
timestamp = bridge._get_timestamp('right_frame')
```

---

###### **`add_noise(self, data)`**

**Description:**  
Adds Gaussian noise to the given data based on the configured noise level.

**Args:**  
- `data (np.ndarray)`: The data (typically a frame) to which noise will be added.

**Returns:**  
- `np.ndarray`: The noisy data.

**Example:**
```python
noisy_frame = bridge.add_noise(frame_data)
```

---

###### **`get_sensor_data(self)`**

**Description:**  
Retrieves sensor data from shared memory.

**Returns:**  
- `np.ndarray or None`: The sensor data array, or `None` if the shared memory is not available.

**Example:**
```python
sensor_data = bridge.get_sensor_data()
```

---

###### **`send_movement_command(self, x, y, z, roll, pitch, yaw)`**

**Description:**  
Sends movement command values (`x, y, z, roll, pitch, yaw`) to the shared memory block.

**Args:**  
- `x (float)`: Movement in the X-axis.
- `y (float)`: Movement in the Y-axis.
- `z (float)`: Movement in the Z-axis.
- `roll (float)`: Roll rotation.
- `pitch (float)`: Pitch rotation.
- `yaw (float)`: Yaw rotation.

**Returns:**  
None.

**Example:**
```python
bridge.send_movement_command(1.0, 0.5, -1.0, 0.2, 0.1, -0.3)
```

---

###### **`_write_movement_command(self, commands)`**

**Description:**  
Writes the movement commands to shared memory.

**Args:**  
- `commands (list of float)`: List of movement command values (`[x, y, z, roll, pitch, yaw]`).

**Returns:**  
None.

**Example:**
```python
bridge._write_movement_command([1.0, 0.5, -1.0, 0.2, 0.1, -0.3])
```

---

###### **`set_resolution(self, width, height)`**

**Description:**  
Sets the resolution of the frames by updating the `width` and `height` attributes and recalculating the frame shapes.

**Args:**  
- `width (int)`: Width of the frames.
- `height (int)`: Height of the frames.

**Returns:**  
None.

**Example:**
```python
bridge.set_resolution(800, 600)
```

---

###### **`set_noise_level(self, noise_level)`**

**Description:**  
Sets the noise level for the frames.

**Args:**  
- `noise_level (float)`: The level of noise to apply.

**Returns:**  
None.

**Example:**
```python
bridge.set_noise_level(0.05)
```

---

###### **`set_apply_noise(self, apply_noise)`**

**Description:**  
Sets whether noise should be applied to frames.

**Args:**  
- `apply_noise (bool)`: Whether to apply noise (`True` or `False`).

**Returns:**  
None.

**Example:**
```python
bridge.set_apply_noise(True)
```

---

###### **`get_right_frame(self)`**

**Description:**  
Retrieves the right frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved right frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the right frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
right_frame_data = bridge.get_right_frame()
```

---

###### **`get_left_frame(self)`**

**Description:**  
Retrieves the left frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved left frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the left frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
left_frame_data = bridge.get_left_frame()
```

---

###### **`get_right_zdepth(self)`**

**Description:**  
Retrieves the right depth frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved right depth frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the right depth frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
right_zdepth_data = bridge.get_right_zdepth()
```

---

###### **`get_left_zdepth(self)`**

**Description:**  
Retrieves the left depth frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved left depth frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the left depth frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
left_zdepth_data = bridge.get_left_zdepth()
```

---

###### **`get_right_seg(self)`**

**Description:**  
Retrieves the right segmentation frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved right segmentation frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the right segmentation frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
right_segmentation_data = bridge.get_right_seg()
```

---

###### **`get_left_seg(self)`**

**Description:**  
Retrieves the left segmentation frame from shared memory.

**Returns:**  
- `dict`: A dictionary with:
  - `'frame' (np.ndarray or None)`: The retrieved left segmentation frame or `None` if an error occurred.
  - `'timestamp' (int or None)`: The timestamp associated with the left segmentation frame or `None` if an error occurred.
  - `'error' (str or None)`: Error message, if any.

**Example:**
```python
left_segmentation_data = bridge.get_left_seg()
```

---

#### utility.py
This file contains utility functions to handle timestamps and convert them into human-readable formats and more.

---

###### **`timestamp2string(timestamp)`**

**Description:**  
Converts a timestamp in milliseconds (integer) to a human-readable string format.

**Args:**  
- `timestamp (int)`: The timestamp in milliseconds to be converted.

**Returns:**  
- `str`: The formatted timestamp as a string in the format `YYYY-MM-DD HH:MM:SS.sss`.

**Example:**
```python
formatted_time = timestamp2string(1633036800000)
# Output: '2021-10-01 00:00:00.000'
```

---

###### **`timestamp2datetime(timestamp)`**

**Description:**  
Converts a timestamp in milliseconds (integer) to a `datetime` object.

**Args:**  
- `timestamp (int)`: The timestamp in milliseconds to be converted.

**Returns:**  
- `datetime`: The corresponding `datetime` object in UTC timezone.

**Example:**
```python
dt_object = timestamp2datetime(1633036800000)
# Output: datetime.datetime(2021, 10, 1, 0, 0, tzinfo=datetime.timezone.utc)
```