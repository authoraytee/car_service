from django.shortcuts import render


def TireFittingCatalogView(request):
    return render(request,'tire_fitting/tire_fitting_catalog.html')


def AllCarsCatalogView(request):
    return render(request,'tire_fitting/all_cars.html')


def ChangeTireCatalogView(request):
    return render(request,'tire_fitting/change_tire.html')


def FixTireCatalogView(request):
    return render(request,'tire_fitting/fix_tire.html')

