from django.shortcuts import render

def home(request):
    import json
    import requests
    from lookup.config_file import api_key
    # Comment and more

    # Create the api request:
    api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=73101&distance=50&API_KEY={api_key}")

    # Error handling of the api request:
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Errror..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
