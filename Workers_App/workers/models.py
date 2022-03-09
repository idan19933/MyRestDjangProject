from django.db import models


class Workers(models.Model):
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    hire_date = models.CharField(max_length=100)
    job_id = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    department_id = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(default='default_slug')
    manager = models.ForeignKey('self', on_delete=models.CASCADE, default=None,blank=True)


    def __str__(self):
        return self.name
