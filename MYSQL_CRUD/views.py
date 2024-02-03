from django.shortcuts import render, redirect
from .forms import MyRegistrationForm
from django.contrib import messages
from .models import RegisterForm


# crispy forms is installed pip install django-crispy-forms
# in settings.py INSTALLED_APPS = ['crispy_forms',]
# in settings.py CRISPY_TEMPLATE_PACK = 'bootstrap4'
def home(request):
    datas = RegisterForm.objects.all()
    if datas != '':
        return render(request, 'home.html', {'datas': datas})
    return render(request, 'home.html', )


def insert(request):
    print(request.method)
    if request.method == 'POST':
        print("request: ")
        form = MyRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration completed successfully')
                return redirect('Home')
            except:
                pass
    else:
        form = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})


def update(request, id):
    data = RegisterForm.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST['name']
        data.age = request.POST['age']
        data.email = request.POST['email']
        data.contact = request.POST['contact']
        data.address = request.POST['address']
        data.save()
        messages.success(request, 'Updated successfully')
        return redirect('Home')
    return render(request, 'update.html', {'data': data})


def delete(request, id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request, 'Deleted successfully')
    return redirect('Home')
