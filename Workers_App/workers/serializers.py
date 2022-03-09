from rest_framework import serializers
from .models import Workers


class WorkersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ['id',"employee_id",'name','last_name','email','phone_number','hire_date','job_id','salary','department_id','image','slug','manager']


