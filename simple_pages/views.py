from django.shortcuts import render


def HomeView(request):
    return render(request,'home.html')

def ContactsView(request):
    return render(request,'contacts.html')

def AboutView(request):
    return render(request,'about.html')

def DiscountsView(request):
    return render(request,'discounts.html')
