#%%
import cv2
import numpy as np
from keras.models import load_model
#%%
def get_prediction() -> int:
    model = load_model('keras_model.h5', compile=False)
    cap = cv2.VideoCapture(0) # webcam referenced by integer 0 argument
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return prediction[0].argmax()

#%%
user_input = get_prediction()

print(user_input)
# for i in user_input:
#     print(i)
#%%
my_array = np.ndarray(shape=(1,2,2,3), dtype=int)
zeros_array = np.zeros(shape=(3,4))