# Quizzler - A Quiz Game with tkinter

Quizzler is a quiz game built with Python and tkinter that challenges your knowledge with a series of true/false questions. It features a colorful and user-friendly graphical user interface (GUI) for an interactive quiz experience.

## Files

- `main.py`: The main entry point of the application.
- `QuizzlerBrain.py`: Contains the logic for managing the quiz questions and scoring.
- `GameData.py`: Retrieves quiz questions from an external API.
- `QuestionModel.py`: Defines the `Question` class to represent quiz questions.
- `UISetup.py`: Sets up the GUI for the quiz game.

## How to Play

1. Run `main.py` using Python to start the game.
2. The game retrieves a set of true/false questions from an external API.
3. Read each question and decide whether it's true or false.
4. Click the "True" or "False" button to submit your answer.
5. Your score is displayed on the screen, and the next question is presented.
6. Continue answering questions to increase your score.

## Features

- Interactive quiz game with true/false questions.
- Score tracking to measure your knowledge.
- Randomized questions for a dynamic experience.
- Categories displayed for each question.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)
- requests library (for making API requests)

## Customize the Questions

You can customize the quiz questions by modifying the `GameData.py` file. The game fetches questions from an external API, so you can adjust the number of questions and question types by updating the `PARAMETERS` dictionary.

## Contributions

Feel free to contribute to this project by adding new features, improving the user interface, or enhancing the quiz experience.
