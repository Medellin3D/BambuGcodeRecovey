# G-code Recovery Script for Bambu Printers

This is a work-in-progress script written in Python designed to modify G-code for Bambu 3D printers. The primary function of the script is to adjust the Z-axis values by subtracting a specific amount from them.

⚠️ **Warning:** This script is currently in development. Using it on your 3D printer could result in damage to the printer or failed prints. Use it at your own risk and always double-check the modified G-code before using it on your printer.

## Features

- Reads a G-code file and adjusts the Z-axis values starting from a specified line.
- Subtracts a set value from each Z coordinate to compensate for height adjustments.

## Usage

1. Save your G-code file as `plate.gcode`.
2. Run the Python script to generate a new G-code file with the adjusted Z-axis values.
3. Review the new G-code file carefully to ensure it will not cause issues with your printer.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Run the script using the command: `python main.py`

## Disclaimer

This script is a work-in-progress and may contain bugs. It is provided as-is without any guarantees. The author is not responsible for any damage or failed prints that may result from using this script. Always back up your original G-code files and proceed with caution.
