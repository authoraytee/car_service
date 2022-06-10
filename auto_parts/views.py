from django.shortcuts import render

def AutopartsView(request):
    return render(request,'auto_parts/auto_parts.html')
