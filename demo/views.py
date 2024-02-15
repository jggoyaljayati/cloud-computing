from django.shortcuts import render, HttpResponse
# from django_pandas import pandas as pd
import pandas as pd
# import csv

data = pd.read_csv('Classification Results on Face Dataset (1000 images).csv')
def home(request):
    file = str(request.FILES['inputFile'])[:-4]
    result = data[data['Image'] == file].Results.item()
    return HttpResponse(("{}:{}").format(file, result))