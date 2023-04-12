from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title','description','email','address','jobType','education','industry','experience','salary','positions','company','point','lastDate','user','created_at']