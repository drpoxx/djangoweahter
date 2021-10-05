from django.shortcuts import render

def home(request):
    import json
    import requests

    # Create the api request:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=73101&distance=50&API_KEY=35D35F74-7912-40CE-98DB-3DD932F6960C")

    # Error handling of the api request:
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Errror..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
