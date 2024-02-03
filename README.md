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
![Screenshot 2024-02-03 122138](https://github.com/Siva0910/Django-CRUD/assets/95603330/50e2b1b3-37b8-4ad9-bd02-edcc375489f0)



Insert_page
![Insert](https://github.com/Siva0910/Django-CRUD/assets/95603330/01fc5caf-a788-4dba-937f-589797b3e459)



Update_page
![Update](https://github.com/Siva0910/Django-CRUD/assets/95603330/feec7ba8-9c6b-407a-a523-9a072b09f4b3)

