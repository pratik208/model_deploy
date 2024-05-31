import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
from .serializers import DiabeticTypeSerializer

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_diabetictype(request):
    serializer = DiabeticTypeSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        try:
            # Extract the validated data
            age = data['age']
            bs_fast = data['bs_fast']
            bs_pp = data['bs_pp']
            plasma_r = data['plasma_r']
            plasma_f = data['plasma_f']
            hbA1c = data['hbA1c']

            result = [age, bs_fast, bs_pp, plasma_r, plasma_f, hbA1c]

            model_path = 'ml_model/model.pkl'
            classifier = pickle.load(open(model_path, 'rb'))

            prediction = classifier.predict([result])[0]
            conf_score = np.max(classifier.predict_proba([result])) * 100

            predictions = {
                'error': '0',
                'message': 'Successful',
                'prediction': prediction,
                'confidence_score': conf_score
            }
        except Exception as e:
            predictions = {
                'error': '2',
                'message': str(e)
            }
    else:
        predictions = {
            'error': '1',
            'message': 'Invalid Parameters',
            'errors': serializer.errors
        }

    return Response(predictions)
