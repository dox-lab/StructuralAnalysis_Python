# Structural Analysis in Python

Welcome to the Structural Analysis in Python project! This project was created as part of a hackathon focused on developing a tool for structural analysis using Python. It implements the stiffness method for analyzing structures, which is essential for civil engineering applications.

## What is This Project About?

This project helps engineers and students analyze the behavior of structures (like buildings or bridges) using Python, a popular programming language. The project uses an Excel file as input to simplify the process, meaning you don't need to be a programmer to use it.

## Key Features

- **Easy Input**: You can use Excel files to input your data.
- **Python-Powered**: The project uses Python to perform calculations, making it flexible and powerful.
- **Examples Provided**: We provide example files to help you understand how to use the project.
- **Modular Design**: The code is designed in modules, so you can easily extend it if needed.

## How to Use This Project

### 1. Getting Started

Before you can use this project, you need to set it up on your computer. Don’t worry if you’ve never done this before—just follow these steps:

### 2. Prerequisites

- **A Computer**: You need access to a computer running Windows, macOS, or Linux.
- **Python Installed**: Python is the programming language used for this project. Follow the steps below to install it.

#### Installing Python

1. **Go to the Python Website**: Visit [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. **Download Python**: Click the download button for your operating system (Windows, macOS, or Linux).
3. **Run the Installer**: After downloading, open the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH" before clicking "Install Now".

### 3. Setting Up the Project

#### Step 1: Download the Project

You need to get a copy of this project onto your computer. Here’s how:

1. **Go to the GitHub Repository**: Visit the project page on GitHub: [GitHub Project Link](https://github.com/dox-lan/StructuralAnalysis_Python).
2. **Download as ZIP**: Click the green "Code" button, then select "Download ZIP". This will download the project files to your computer.
3. **Extract the Files**: Find the downloaded ZIP file on your computer, right-click it, and select "Extract All" or "Unzip".

#### Step 2: Install Required Software

The project requires a few additional tools (called "libraries") to work. Here's how to install them:

1. **Open the Terminal/Command Prompt**:
   - On Windows: Press `Win + R`, type `cmd`, and hit Enter.
   - On macOS: Press `Cmd + Space`, type `Terminal`, and hit Enter.
   - On Linux: Open the terminal from your applications menu.

2. **Navigate to the Project Folder**:
   - In the terminal, type `cd ` followed by the path to the extracted project folder. For example:
   
   ```bash
   cd C:\Users\YourName\Downloads\StructuralAnalysis_Python-main

3. **Install the Required Libraries**:
- Type the following command and press Enter:

    ```bash
    pip install -r requirements.txt
    
- This command installs the necessary Python libraries.

### 4. Running the Analysis
Now that everything is set up, you can run the analysis. Here’s how:

1. **Prepare Your Input Data**:
    - The project uses an Excel file to input the structural data. You can find an example input file in the data/ folder. If you have your own data, make sure it’s formatted similarly.

2. **Run the Program**:
    - In the terminal, type the following command:  

    ```bash
    python src/Rigidez_sistematizada.py --input data/ANÁLISIS_DE_ESTRUCTURAS_INPUT.xlsx

3. **View Results**:
    - The program will output the results directly in the terminal. Depending on how the program is set up, it might also save the results to a file in the project directory.

### 5. Example Usage
We’ve included an example to help you see how it works. Follow these steps:

1. **Use the Provided Example**:
    - In the examples/ folder, there’s a sample Excel file you can use to run a test analysis.

2. **Run the Example**:
    - Use the same command as above, but point to the example file:

    ```bash
    python src/Rigidez_sistematizada.py --input examples/simple_structure.xlsx

### 6. Need Help?
If you run into any problems or have questions, feel free to ask for help on the project’s GitHub page by opening an "Issue". You can find the "Issues" tab on the main page of the project’s GitHub repository.

### 7. License
This project is licensed under the MIT License. You can do almost anything with it, like using it in your projects, modifying it, or sharing it with others. Just be sure to give credit to the original creators.

### 8. Contributing
If you’d like to contribute to this project, that’s awesome! Check out the CONTRIBUTING.md file in the project for more information on how to get involved.