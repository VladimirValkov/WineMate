from django.shortcuts import render


def index(req):
    context = {
        'name': 'Vlado',
    }

    return render(req, 'index.html', context)
