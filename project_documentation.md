# Project Documentation

This project uses the web application [TeachableMachine](https://teachablemachine.withgoogle.com/train) to train a deep learning model to recognise whether the user is displaying to the webcam rock, paper, or scissors, and executes the logic for a best-of-three game between user and computer.

## Milestone 1: Creation of the Computer Vision System
Technologies / Skills:
- Teachable Machine

Web application Teachable Machine is used for creating machine learning models based on image or audio files. A model to recognise the three classes of the game (Rock, Paper, and Scissors), as well as a 'Nothing' class, was trained and imported.

## Milestone 2: Install the Dependencies
Technologies / Skills:
- Pip
- Conda virtual environments

Requisite packages installed into a new conda virtual environment, see [requirements.txt](https://github.com/tuttonluke/Computer_Vision_Rock_Paper_Scissors/blob/main/requirements.txt) for
detailed list of dependencies.

## Milestone 3: Create a Rock-Paper-Scissors Game
 
 Manual version of the rock-paper-scissors game created in the python file manual_rps.py. The get_computer_input function randomly chooses "rock", "paper", or "scissors", the get_user_input function asks the user for a choice from the same options, and the get_winner functions returns the winner according to the rules of the game. The play function runs the game as expected by calling the previous three functions sequentially.

 ## Milestone 4: Use the Camera to Play Rock-Paper-Scissors
 Technologies / Skills:
 - opencv-python
 - keras

 The get_user_input function from the manual game is replaced by a get_prediction function which uses keras as an interface for the TensorFlow library to predict whether the user is displaying rock, paper, or scissors in the camera.

 The [main.py](https://github.com/tuttonluke/Computer_Vision_Rock_Paper_Scissors/blob/main/main.py) file consolidates the code in a RockPaperScissors class and runs the game with the function play_rps.

