from django.shortcuts import render
# from django.views.generic.list import ListView


def HomeView(request):
    return render(request,'home.html')

def ContactsView(request):
    return render(request, 'сontacts.html')