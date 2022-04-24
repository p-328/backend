from django.shortcuts import render
from django.http import JsonResponse
import datetime
import time
# Create your views here.


def index(request):
    return JsonResponse({
        'RightNow': '{}'.format(datetime.datetime.now()),
        'Unix': '{}'.format(int(round(time.time() * 1000)))
    })
def get_date(request, date):
    date_info = date.split('-')
    for number in date_info:
        try:
            _ = int(number)
        except ValueError:
            return JsonResponse({'error': 'Invalid date'})
    numbers = [int(number) for number in date_info]
    try:
        _ = datetime.date(numbers[0], numbers[1], numbers[2])
    except ValueError:
        return JsonResponse({'error': 'Invalid date'})
    except IndexError:
        return JsonResponse({'error': 'Invalid date'})
    date_info = datetime.date(numbers[0], numbers[1], numbers[2])
    date_info_string = date_info.strftime('%a %b %d %Y')
    unix_time = int(time.mktime(date_info.timetuple())*1000)
    return JsonResponse({ 
        'time': '{}'.format(date_info_string),
        'unix': '{}'.format(unix_time)
    })
