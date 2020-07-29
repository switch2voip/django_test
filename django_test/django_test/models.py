from django.db import models

class form(models.Model):
    id = models.AutoField(primary_key='true')
    first_name = models.Charfield(max_lenght=20)
    first_name = models.CharField(max_lenght=20)
    last_name = models.Charfield(max_lenght=20,default='')
    email = models.Charfield(mex_lenght=25)
    password = models.CharField(max_lenght=16)
    Address = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50,default='')
    city = models.CharField(max_lenght=15)
    state = models.Charfield(max_lenght=25)
    zip = models.Charfield(max_lenght=15)