from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Edbert Halim',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)