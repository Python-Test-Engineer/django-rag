from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def people(request):
    people = [
        {"name": "Mark", "image": "https://picsum.photos/id/237/200/300"},
        {"name": "Jeff", "image": "https://picsum.photos/seed/picsum/200/300"},
    ]
    import time

    time.sleep(0.20)
    return JsonResponse(people, safe=False)
