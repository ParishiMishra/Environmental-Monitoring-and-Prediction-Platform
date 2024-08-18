from django.shortcuts import render
from django.http import JsonResponse
from .models import EnvironmentalData

def predict_flood(request):
    # Placeholder for flood prediction logic
    return JsonResponse({'prediction': 'Flood likely'})

def predict_landslide(request):
    # Placeholder for landslide prediction logic
    return JsonResponse({'prediction': 'Landslide unlikely'})

def index(request):
    return render(request, 'index.html')
