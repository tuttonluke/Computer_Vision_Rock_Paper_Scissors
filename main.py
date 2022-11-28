#%%
import time
import random
import numpy as np
import cv2
from keras.models import load_model
import traceback
#%%
class RockPaperScissors:
    """Implementation of the game Rock-Paper-Scissors using computer vision and
    a keras neural network model to predict the user input via webcam.

    Args:
        computer_wins: number of times the computer has won
        user_wins: number of times the user has won
        choices_dict: dictionary where keys are integers representing the 
            values rock, paper, and scissors.
    """
    def __init__(self) -> None:
        self.computer_wins = 0
        self.user_wins = 0
        self.choices_dict = {0: "rock", 1 : "paper", 2 : "scissors"}
        self.model_path = r"C:\Users\tutto\OneDrive\Documents\Documents\AiCore\Projects\Computer_Vision_Rock_Paper_Scissors\keras_model.h5"
    
    def get_computer_choice(self) -> int:
        """Randomly chooses one of three options:
        0: Rock
        1: Paper
        2: Scissors

        Returns:
            int: Random choice of 0, 1, or 2, corresponding to roc, paper, and
            scissors, respectively.
        """
        return random.randint(0,2)
    
    def get_prediction(self) -> int:
        """Predicts the user's choice of rock, paper, or scissors via webcam
        using tensorflow model prediction.

        Returns:
            int: 0 Rock
                1 Paper
                2 Scissors
                3 Nothing
        """
        model = load_model(self.model_path, compile=False)
        cap = cv2.VideoCapture(0) # webcam referenced by integer 0 argument
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        time_1 = time.time()
        
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            flipped = flipped = cv2.flip(frame, 1)
            cv2.imshow("Frame", flipped)
            # Press q to close the window
            # print(prediction)
            time_2 = time.time()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif time_2 - time_1 > 3:
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        return prediction[0].argmax()
    
    def get_winner(self, computer_choice, user_choice) -> int:
        """Compares output of get_computer_choice and get_user_choice functions
        and returns an integer corresponding to the three outcomes of tie (0),
        computer win (1), or user win(2).

        Args:
            computer_choice (int): computer's choice of rock, paper, or scissors.
            user_choice (int): user's choice of rock, paper, or scissors.

        Returns:
            int: 0 (Tie)
                1 (Computer win)
                2 (User win)
        """
        if computer_choice == user_choice:
            return 0
        elif (
            (computer_choice == 0 and user_choice == 2) or
            (computer_choice == 1 and user_choice == 0) or
            computer_choice == 2 and user_choice == 1
            ):
            return 1
        else:
            return 2
#%%
def play_rps():
    """This function creates an instance of the RockPaperScissors class and
    plays the game.
    """
    game = RockPaperScissors()
    while True:
        computer_choice = game.get_computer_choice()
        print(game.choices_dict.get(computer_choice))
        user_choice = game.get_prediction()
        # close window by pressing q key or X button
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
            break
        if user_choice < 3:
            print(f'You chose {game.choices_dict.get(user_choice)}')
            result = game.get_winner(computer_choice, user_choice)
            if result == 1:
                game.computer_wins += 1
            elif result == 2:
                game.user_wins += 1
        else:
            print('Input not recognised.')
        if game.computer_wins == 3:
            print(f"Computer wins {game.computer_wins} to {game.user_wins}.")
            break
        elif game.user_wins == 3:
            print(f"User wins {game.user_wins} to {game.computer_wins}.")
            break
#%%
if __name__ == "__main__":
    try:
        play_rps()
    except Exception:
        traceback.print_exc()
# %%
