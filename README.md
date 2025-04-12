# Steganography Tool

A simple Python-based GUI tool for encoding and decoding hidden messages in images using Least Significant Bit (LSB) Steganography. This tool uses tkinter for the graphical user interface and PIL for image manipulation. It also uses the stegano library to implement the LSB encoding and decoding functionality.

## Features
- *Encode a Message*: Hide a text message inside an image.
- *Decode a Message*: Extract the hidden message from a stego image.
- *Image Preview*: View the image selected for encoding.
- *Save Encoded Image*: Save the image after encoding the message.
- *Cross-platform Support*: Works on Windows, macOS, and Linux (as long as Tkinter is supported).

## Requirements

- Python 3.x
- Tkinter (pip install tk)
- Pillow (pip install pillow)
- Stegano (pip install stegano)

## Installation

1. Clone the repository or download the code files.
2. Install the required libraries by running the following commands in your terminal or command prompt:
   
   ```bash
   pip install pillow stegano
Run the script:

bash
Copy
Edit
python steganography_tool.py
How to Use
Encode a Message:

Click on "Choose Image" to select an image.

Enter the message you want to encode in the text box.

Click "Encode Text" to hide the message in the selected image.

Save the encoded image to your desired location.

Decode a Message:

Click on "Choose Encoded Image" to select an image that contains a hidden message.

Click "Decode Text" to extract and display the hidden message.

License
This project is open-source and available under the MIT License.

Acknowledgements
Tkinter: Python's standard GUI library.

Pillow: Python Imaging Library (PIL) fork for image manipulation.

Stegano: Python library for performing LSB-based Steganography.

For any issues or contributions, feel free to open an issue or submit a pull request.

csharp
Copy
Edit

### Usage Instructions:

1. Save this as README.md in the same directory as your Python script.
2. Update the filename in the How to Use section if your script has a different name.

This README provides clear instructions for setting up, using the tool, and contributing to it!
