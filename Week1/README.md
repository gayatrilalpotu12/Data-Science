# Week 1: Python Basics — Personal Introduction Program

## Project Overview
The Personal Introduction Program is a beginner-friendly Python project. It asks the user for basic information and prints a friendly, personalized welcome message.

## Goals and Objectives
- Understand what a Python program does.
- Use variables to store input.
- Use `input()` to ask questions.
- Use `print()` to display text.
- Use f-strings to insert variables into messages.
- Practice strings and basic program flow.

## Requirements
- Python 3.8 or newer
- A text editor such as VS Code, IDLE, or Notepad
- No external Python packages are required.

## Project Structure
```text
Week1-Personal-Introduction/
├── README.md
├── personal_intro.py
├── requirements.txt
└── screenshot.png
```

## Setup Instructions

### 1. Install Python
1. Visit https://www.python.org/downloads/
2. Download the installer for your operating system.
3. Run the installer. On Windows, tick **Add Python to PATH** if that option appears.
4. Finish the installation.

### 2. Check Python
Open Command Prompt/Terminal and run:
- Windows: `py --version` (or `python --version`)
- macOS/Linux: `python3 --version`

### 3. Run the project
1. Open this project folder in your editor or terminal.
2. Run:
   - Windows: `py personal_intro.py` (or `python personal_intro.py`)
   - macOS/Linux: `python3 personal_intro.py`
3. Answer the five questions in the terminal.

## How the Program Works
1. Prints a title.
2. Collects the user's name, age, city, hobby, and favorite food using `input()`.
3. Stores the answers in variables.
4. Uses f-strings to personalize the output.
5. Prints a friendly message and the entered information.

## Algorithm
1. Start.
2. Display the program title.
3. Read name, age, city, hobby, and favorite food.
4. Display a welcome message using the entered name.
5. Display the remaining information.
6. Display a thank-you message.
7. Stop.

## Concepts Learned
- **Variables:** named places to store values.
- **Strings:** text values such as a name or hobby.
- **`input()`:** reads information typed by the user.
- **`print()`:** displays text in the terminal.
- **f-strings:** combine text and variable values, for example `f"Welcome, {name}!"`.
- **Comments:** lines beginning with `#` explain the code.
- **`.strip()`:** removes extra spaces from the beginning and end of input.

## Testing Evidence

| Test | Example input | Expected result |
|---|---|---|
| 1 | Name: Alex | Output welcomes Alex |
| 2 | Age: 21 | Output shows 21 years |
| 3 | City: Pune | Output shows Pune |
| 4 | Hobby: Coding | Output says the user enjoys Coding |
| 5 | Food: Pizza | Output shows Pizza as favorite food |

### Sample Output
```text
========================================
   WELCOME TO MY INTRODUCTION PROGRAM
========================================
What is your name? Alex
How old are you? 21
Which city do you live in? Pune
What is your favorite hobby? Coding
What is your favorite food? Pizza

========================================
Welcome, Alex!
========================================
Your age is 21 years.
You live in Pune.
You enjoy Coding.
Your favorite food is Pizza.

Thank you for introducing yourself!
Have a wonderful day!
========================================
```

## Technical Details
- **Input:** five text answers from the user.
- **Processing:** store each answer in a variable and format it into messages.
- **Output:** personalized text in the terminal.
- **Data structures:** individual string variables; no complex data structure is needed for this small project.
- **Architecture:** simple sequential, console-based Python program.
- **External dependencies:** none.

## Troubleshooting
- If `python` is not recognized on Windows, try `py personal_intro.py`.
- On macOS/Linux, try `python3 personal_intro.py`.
- Make sure the file is named `personal_intro.py`, not `personal_intro.py.txt`.
- If you edit the code, save the file before running it again.

## GitHub Submission
1. Create a GitHub account at https://github.com/ if you do not have one.
2. Create a new repository named `Week1-Personal-Introduction`.
3. Upload `README.md`, `personal_intro.py`, `requirements.txt`, and `screenshot.png`.
4. Open the repository and check that all four files are visible.
5. Submit the repository URL according to your college's instructions.

## Learning Resources
- Python downloads: https://www.python.org/downloads/
- Python tutorial: https://docs.python.org/3/tutorial/
- Beginner video search: https://www.youtube.com/results?search_query=Python+absolute+beginner+tutorial+no+experience
