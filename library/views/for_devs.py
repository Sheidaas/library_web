from django.shortcuts import render


def render_for_devs(request):
    return render(request, 'for_devs/for_devs.html', {})
