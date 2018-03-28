from django.shortcuts import render,redirect,HttpResponse
from emp.models import Employee
from emp.forms import EmployeeForm


# Create your views here.

def home(request):
	print "home"
	empobj = Employee.objects.all().order_by('emp_name')
	return render(request,'home.html',{'empobj':empobj})

def add(request):
	print "add"
	if request.method == 'POST':
		print(request.POST)
		form = EmployeeForm(request.POST)
		if form.is_valid:
			print form,"===================="
			form.save()
			print "saved successfully......"
		return redirect('/')

	else:
		form=EmployeeForm()
		return render(request,'addemployee.html',{'form':form})
def edit(request,emp_id):
	print "emp_id",emp_id
	empobj = Employee.objects.get(emp_id=emp_id)
	if request.method == 'POST':
		form = EmployeeForm(request.POST,instance=empobj)
		if form.is_valid:
			form.save()
			return redirect('/')
		else:
			form = EmployeeForm(instance=empobj)
			return render(request,'addemployee.html',{'empobj':empobj})
			
	else:
		form = EmployeeForm(instance=empobj)
		return render(request,'addemployee.html',{'empobj':empobj})

def delete(request,emp_id):
	empobj = Employee.objects.get(emp_id=emp_id)
	empobj.delete()
	return redirect('/')
