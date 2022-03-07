from django.shortcuts import render,redirect
from employee_register.models import Employee
from employee_register.forms import Employeeform

# Create your views here.

def emp(request):
    if request.method=="POST":
        form=Employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = Employeeform()
    return render(request, 'index.html',{'form':form})

def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html',{'employees':employee})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form=Employeeform(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html',{'employee':employee})
    
def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


