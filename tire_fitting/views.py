from django.shortcuts import render


def TireFittingCatalogView(request):
    return render(request,'tire_fitting/tire_fitting_catalog.html')


def ChangeTireCatalogView(request):
    return render(request,'tire_fitting/change_tire.html')


def FixTireCatalogView(request):
    return render(request,'tire_fitting/fix_tire.html')


def LightweightCarsCatalogView(request):
    return render(request,'tire_fitting/lightweight_cars.html')


def MinubusesCatalogView(request):
    return render(request,'tire_fitting/minibuses.html')


def SuvCatalogView(request):
    return render(request,'tire_fitting/suv.html')

