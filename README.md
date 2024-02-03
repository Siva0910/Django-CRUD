# Django-CRUD
This is to implement basic record based CRUD operations in Django

**Versions**
django : 5.0.1
bootstrap : 3.4
MySQL : 8

**Important Changes**
1)Settings.py
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MYSQL_CRUD',
        'USER': 'root',
        'PASSWORD': '2003',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']
CRISPY_TEMPLATE_PACK = 'bootstrap5'

2)forms.py
class MyRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ['name', 'age', 'address', 'contact', 'email']



3)models.py
class RegisterForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        db_table = 'datas'


Home Page

![Screenshot 2024-02-03 122138](https://github.com/Siva0910/Django-CRUD/assets/95603330/10500ef8-96ef-424f-9225-5c5c5e09b8cd)

Insert_page
![Insert](https://github.com/Siva0910/Django-CRUD/assets/95603330/7e5ae942-6104-4965-9d5d-1ae12228b18e)


Update_page

![Update](https://github.com/Siva0910/Django-CRUD/assets/95603330/fc5841a2-ef4b-4613-a12f-36f3e85f7c8c)
