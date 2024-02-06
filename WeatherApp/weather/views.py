from django.shortcuts import render
from SimpleWeather import city_search

# Create your views here.


def weather_view(request):

    if request.method == 'GET':
        return render(request, 'weather/weather_form.html')

    elif request.method == 'POST':
        city_name = request.POST.get('city_name')

        weather_data = city_search(city_name)

        return render(request, 'weather/weather_result.html', {'weather_data': weather_data})

    return render(request, 'weather/weather_form.html')
