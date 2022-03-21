from django.shortcuts import render

def handle404(request, exeption=None, template_name='errors/page-404.html'):
    return render(request,template_name,{},status=404)


def handle400(request, exeption=None, template_name='errors/page-400.html'):
    return render(request,template_name,{},status=400)


def handle500(request, exeption=None, template_name='errors/page-500.html'):
    return render(request,template_name,{},status=500)


def handle403(request, exeption=None, template_name='errors/page-403.html'):
    return render(request,template_name,{},status=403)
