from django.shortcuts import render, redirect
from .models import Car, Company
from .forms import CarForm, CompanyForm
from django.http import HttpResponse

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {'form': form})

def company_update(request, pk):
    company = Company.objects.filter(pk=pk).first()
    if company is None:
        return HttpResponse("Company not found")
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {'form': form})

def company_delete(request, pk):
    company = Company.objects.filter(pk=pk).first()
    if company is None:
        return HttpResponse("Company not found")
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'company_confirm_delete.html', {'company': company})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

def car_update(request, pk):
    car = Car.objects.filter(pk=pk).first()
    if car is None:
        return HttpResponse("Car not found")
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_form.html', {'form': form})

def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).first()
    if car is None:
        return HttpResponse("Car not found")
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})
