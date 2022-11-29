#%%
from keras.models import load_model
import cv2
import mediapipe as mp
import numpy as np
import random
import time
import traceback
#%%
class RockPaperScissors:
    """Implementation of the game Rock-Paper-Scissors using computer vision and
    a keras neural network model to predict the user input via webcam.

    Attributes
    ----------
    computer_wins : int
                    number of times the computer has won
    user_wins : int
                number of times the user has won
    choices_dict : dict
                   dictionary where keys are integers representing the 
                   values rock (0), paper (1), and scissors (2). 
    """
    def __init__(self) -> None:
        self.__mp_hands = mp.solutions.hands
        self.__hands = self.__mp_hands.Hands()
        self.__mp_draw = mp.solutions.drawing_utils
        self.__previous_time = 0
        self.__current_time = 0
        self.computer_wins = 0
        self.user_wins = 0
        self.choices_dict = {0: "rock", 1 : "paper", 2 : "scissors"}
        self.model_path = r"C:\Users\tutto\OneDrive\Documents\Documents\AiCore\Projects\Computer_Vision_Rock_Paper_Scissors\keras_model.h5"

    def __display_frame_rate(self, img):
        """Displays frame rate.

        Parameters
        ----------
        img : img
            Image frame of the video.

        Returns
        -------
        Img
            Img frame with framerate displayed.
        """
        self.__current_time = time.time()
        fps = 1/(self.__current_time - self.__previous_time)
        self.__previous_time = self.__current_time
        cv2.putText(img, str(int(fps)), (10 , 30), cv2.FONT_HERSHEY_PLAIN, 2, 
                (255, 0, 255), 2)
        return img

    def __display_countdown(self, img, time_1, time_2):
        """Displays 3 second countdown on the display.

        Parameters
        ----------
        img : img
            Image frame of the video.
        time_1 : float
            Time of initiation of countdown.
        time_2 : float
            Time of frame initiation.
        """
        countdown = round((time_2 - time_1), 0)
        cv2.putText(img, f"Countdown: {4 - int(countdown)}", (200, 450), 
            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    
    def __display_hand_landmarks(self, img):
        """Displays hand landmarks using mediapipe hand tracking,
        see https://google.github.io/mediapipe/solutions/hands.

        Parameters
        ----------
        img : img
            Image frame of the video.

        Returns
        -------
        img
            Img frame with hand landmarks displayed.
        """
        results = self.__hands.process(img)
        if results.multi_hand_landmarks:
                for hand_lmks in results.multi_hand_landmarks:
                    self.__mp_draw.draw_landmarks(img, hand_lmks, 
                        self.__mp_hands.HAND_CONNECTIONS)
        return img

    def get_computer_choice(self) -> int:
        """Randomly chooses one of three options:
        0: Rock
        1: Paper
        2: Scissors

        Returns
        -------
        int
            Random choice of 0, 1, or 2, corresponding to roc, paper, and
            scissors, respectively.
        """
        return random.randint(0,2)
    
    def get_prediction(self) -> int:
        """Predicts the user's choice of rock, paper, or scissors via webcam
        using tensorflow model prediction.

        Returns
        -------
        int
            0: Rock
            1: Paper
            2: Scissors
            3: Nothing
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
            self.__display_hand_landmarks(frame)
            prediction = model.predict(data)
            # flip frame along horizontal axis
            flipped = flipped = cv2.flip(frame, 1)
            self.__display_frame_rate(flipped)
            time_2 = time.time()
            self.__display_countdown(flipped, time_1, time_2)
            cv2.imshow("Frame", flipped)
            
            # Press q to close the window
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # 3 second timer
            
            elif time_2 - time_1 > 3:
                break
        cap.release()
        cv2.destroyAllWindows()

        return prediction[0].argmax()

    def get_winner(self, computer_choice, user_choice) -> int:
        """Compares output of get_computer_choice and get_user_choice functions
        and returns an integer corresponding to the three outcomes of tie (0),
        computer win (1), or user win(2).

        Parameters
        ----------
        computer_choice : int
            Computer's choice of rock, paper, or scissors.
        user_choice : int
            User's choice of rock, paper, or scissors.

        Returns
        -------
        int
            0 (Tie)
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
        user_choice = game.get_prediction()
        # close window by pressing q key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if user_choice < 3:
            # print user choice and decide winner of the round
            print(f'You chose {game.choices_dict.get(user_choice)}')
            result = game.get_winner(computer_choice, user_choice)
            if result == 1:
                game.computer_wins += 1
            elif result == 2:
                game.user_wins += 1
        else:
            print('Input not recognised.')
        # Finish the game when one party achieves 3 wins.
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
#%%