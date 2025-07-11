Python to EXE Compiler

Introduction
Python to EXE Compiler is a simple and user-friendly tool that allows users to compile Python scripts into standalone executable files (EXE). This tool provides an intuitive Graphical User Interface (GUI) to facilitate users in selecting Python files, output directories, icon files, and setting compilation options. Additionally, a key verification mechanism is implemented to ensure the security and authorized use of the tool.

Features
- Key Verification: A valid key is required for verification before using the tool, ensuring that only authorized users can access it.
- Graphical User Interface: An intuitive GUI is provided to simplify file selection and compilation option settings.
- Compilation Option Settings: Supports multiple compilation options such as single-file mode, windowed mode, debug mode, etc.
- Setting Saving and Loading: Users can save and load compilation settings for convenience in future use.
- Real-time Log Output: During the compilation process, logs are output in real-time to help users monitor the progress.

Installation and Dependencies
Dependencies:
- Python 3.x
- PyInstaller: Used to compile Python scripts into EXE files.

Installation Steps:
1. Ensure Python 3.x is installed. It can be downloaded and installed from the official Python website.
2. Install PyInstaller: Open the command line terminal and run the following command:
   pip install pyinstaller
3. Clone or download the project code to your local machine.

Usage (Launching the Program)
1. Open the command line terminal and navigate to the project root directory.
2. Run the following command to start the program:
   python main.py

Key Verification:
- When launching the program for the first time, a key verification window will pop up.
- Enter a valid key and click the "Verify" button.
- If the verification is successful, the program will start automatically; if it fails, prompts will be given based on the remaining number of attempts. Exceeding the maximum number of attempts will lock the key file.

Compilation Settings:
- Python File: Click the "Browse..." button to select the Python file to be compiled.
- Output Directory: Click the "Browse..." button to choose the output directory for the compiled EXE file.
- Icon File (Optional): Click the "Browse..." button to select an icon file (with .ico extension) for the EXE file.
- Compilation Options:
  - Single-file Mode: Package all dependencies into a single EXE file.
  - Windowed Mode (No Console): The compiled EXE runs without displaying a console window.
  - Debug Mode: Enable debug mode to facilitate debugging during compilation.
  - Clean Temporary Files: Clean up temporary files after compilation is completed.
  - Console Encoding: Select the encoding format for console output.

Saving and Loading Settings:
- Save Settings: Click the "Save Settings" button to save the current compilation settings to the py_to_exe_config.json file.
- Load Settings: Click the "Load Settings" button to load previously saved compilation settings from the py_to_exe_config.json file.

Starting Compilation:
- After completing the compilation settings, click the "Start Compilation" button to begin the process.
- During compilation, the log area will display real-time logs, and the progress bar will show the compilation progress.
- Upon completion, a prompt box will pop up to inform the user of the compilation result.

File Structure
exe/
├── main.py               # Program entry point
├── key_verification.py   # Key verification module
├── compiler_gui.py       # Main compilation interface module
├── compilation_engine.py # Compilation engine module
├── config_manager.py     # Configuration management module
├── resources/
│   └── keys.json         # Key configuration file
├── py_to_exe_config.json # Compilation settings save file

Notes
- Ensure the entered key is valid; otherwise, the tool may not function properly.
- The compilation process may take some time, depending on the complexity of the Python script and system performance.
- If issues arise during compilation, check the log output and troubleshoot based on the error messages.

Contribution and Feedback
If you encounter bugs or have suggestions for improvement, feel free to add QQ:1312914463. You are also welcome to share your user experience and propose new feature requirements.