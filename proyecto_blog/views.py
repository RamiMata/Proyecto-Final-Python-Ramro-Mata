from django.shortcuts import render

def pagina_no_encontrada(request, exception):
    return render(request, 'error/404.html', status=404)
