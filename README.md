# QR Code Decoder
## Overview
This Python application allows users to scan QR codes using their webcam. The application is built with PyQt5 for the user interface and utilizes the OpenCV library to capture the video feed from the camera. The QR code is decoded using the pyzbar library and displayed in a text field.

## Table of Contents

- [Features](#Features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Real-time webcam feed.
- QR code decoding and displaying the result in a text field.
- Simple and user-friendly interface using PyQt5.
- Modular design with separate pages for the welcome screen and QR code scanner.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required libraries with the command above.
3. Run the wellcome_page.py file to start the application:

```bash
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate to the project directory
cd QR_Code_Coder_Decoder
# Install requirments
# Run wellcome_page.py
python wellcome_page.py

```
## Example Workflow
1. Start the application.
2. On the welcome page, click the "Start" button.
3. The application switches to the QR code scanner page.
4. Hold up a QR code in front of your camera.
5. The QR code's data will be decoded and displayed in the text field.
