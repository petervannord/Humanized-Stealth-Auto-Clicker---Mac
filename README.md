# GhostClickV4 - Enhanced Mouse Clicker

GhostClickV4 is an advanced mouse click automation tool designed for precise and efficient clicking, perfect for repetitive tasks or gaming scenarios. Its primary features include customizable CPM (clicks per minute), fail-safe emergency stops, and seamless integration with macOS environments. This project was developed using Python libraries such as Tkinter for the graphical user interface and Quartz.CoreGraphics to interact directly with the operating system's mouse events.

## Features

- Adjustable Click Speed: Control the rate at which clicks are generated using the "Target CPM" input field.
- Fail-Safe Mechanism: To prevent unintended continuous clicking, a failsafe mechanism is implemented that stops the program when the mouse cursor reaches the top-left corner of the screen (coordinates 0, 0). This ensures that if the script malfunctions or becomes unresponsive, manual intervention will be possible by moving the cursor to that location.
- macOS Compatibility: Built specifically for macOS systems, GhostClickV4 leverages Apple's Quartz.CoreGraphics library to simulate mouse clicks using events injected directly into the operating system.

## Usage Instructions

1. Clone this repository to your local machine using Git: [https://github.com/your_username/GhostClickV4](https://github.com/your_username/GhostClickV4)
2. Replace "your_username" in the URL above with your actual GitHub username.


3. Open the downloaded folder and run the main Python file (main.py).

## Dependencies

- Tkinter: For creating the graphical user interface.
- numpy: For numerical operations used in calculating click delays.
- scipy.interpolate: For interpolation functions that create smooth mouse movements when moving between clicking locations.

