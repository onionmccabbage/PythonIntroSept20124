from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('''
                        <h3>Welcome</h3>
                        <p>django is a fully-featured CMS</p>
                        <hr/>
                        <b>Warning: Do not use Django server for production</b>
                        ''')