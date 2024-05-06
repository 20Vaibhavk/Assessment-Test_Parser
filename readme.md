# Parser

This script is designed to parse a text file containing questions and answers formatted in LaTeX syntax and convert them into a structured JSON format. Below are instructions on how to run the script, install required packages, and obtain the desired output.

## Running the Script

1. **Clone the Repository**: Clone or download this repository to your local machine.

2. **Install Dependencies**: Ensure you have Python installed on your system. You will also need to install the `re` and `json` libraries, which are usually included with Python.

3. **Prepare Input File**: Place the text file containing the questions and answers in the desired location. Update the `file_path` variable in the script (`main.py`) with the correct file path.

4. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the script (`main.py`), and execute the following command:

    ```bash
    python main.py
    ```

5. **Check Output**: After running the script, an `output.json` file will be generated in the same directory. This file contains the parsed questions and answers in JSON format.

## Example Input File

An example input file (`Task.txt`) is provided in the repository for reference. You can use this file to test the script initially.