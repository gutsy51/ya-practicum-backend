from django.shortcuts import render


def handler403(request, exception):
    template = 'pages/403csrf.html'
    return render(request, template, status=403)


def handler404(request, exception):
    template = 'pages/404.html'
    return render(request, template, status=404)


def handler500(request):
    template = 'pages/500.html'
    return render(request, template, status=500)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)


def about(request):
    template = 'pages/about.html'
    return render(request, template)
