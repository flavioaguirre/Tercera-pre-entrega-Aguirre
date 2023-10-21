from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader


# def blog(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

def blog(request):
    return render(request, 'inicio_blog/index.html', {})
