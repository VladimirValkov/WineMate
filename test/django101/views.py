from django.shortcuts import render


def index(req):
    context = {
        'name': 'PPMG team',
    }

    return render(req, 'index.html', context)
