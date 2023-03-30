import joblib
import pickle
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pandas as pd
import numpy as np
from django.http import JsonResponse
from .models import PredResults
from sklearn.model_selection import train_test_split
from sklearn import svm

# Create your views here.
def predict(request):
    # template = loader.get_template('predict.html')
    # return HttpResponse("Hello")
    return render(
        request,
        'predict/predict.html'
    )

def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        pregnancies = int(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        diabetes_pedigree_function = float(request.POST.get('diabetes_pedigree_function'))
        age = int(request.POST.get('age'))

        # Unpickle model
        model = pd.read_pickle(r"C:\Users\cheng yang\Diabetes Prediction\mysite\predict\MLmodel\new_model.pickle")   
        input_data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)     
        input_data_np = np.asarray(input_data)

        # reshape array as we are predicting 1 instance cos the model is expecting 768 points
        input_data_reshaped = input_data_np.reshape(1, -1)

        # standardize the input data same as how we standardized the training data
        scaler = pickle.load(open(r"C:\Users\cheng yang\Diabetes Prediction\mysite\predict\MLmodel\scaler.pkl", "rb"))
        std_data = scaler.transform(input_data_reshaped)

        # make prediction
        result = model.predict(std_data)

        if result[0] == 0:
            classification = 'The person is not diabetic'
        else:
            classification = 'The person is diabetic'

        PredResults.objects.create(pregnancies= pregnancies, glucose= glucose, blood_pressure= blood_pressure, 
                                   skin_thickness= skin_thickness, insulin= insulin, bmi= bmi, 
                                   diabetes_pedigree_function= diabetes_pedigree_function, age= age, classification=classification)

        return JsonResponse({'result': classification, 'age': age, 'pregnancies': pregnancies, 
                             'glucose': glucose, 'blood_pressure': blood_pressure, 'bmi': bmi, 
                             'skin_thickness': skin_thickness, 'insulin': insulin, 
                             'diabetes_pedigree_function': diabetes_pedigree_function},
                            safe=False)
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)