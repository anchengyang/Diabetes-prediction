import numpy as np
import pickle
import streamlit
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Make predictive system using the loaded model
def predict(input_data, model):
    
    # change input_data to np array
    input_data_np = np.asarray(input_data)

    # reshape array as we are predicting 1 instance cos the model is expecting 768 points
    input_data_reshaped = input_data_np.reshape(1, -1)

    # standardize the input data same as how we standardized the training data
    # std_data = scaler.transform(input_data_reshaped)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    if __name__ == "__main__":
        streamlit.write("hi")
        not_diabetic_input = (4, 110, 92, 0, 0, 37.6, 0.191, 30)
        loaded = pickle.load(open('trained_model.sav', 'rb'))
        predict(not_diabetic_input, loaded)
main()
