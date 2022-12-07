from django.shortcuts import render
import cv2
import threading

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html', context={})


class VideoCamera(object):
    def __init__(self):
        pass

    def __del__(self):
        pass
