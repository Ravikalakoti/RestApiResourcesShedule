from rest_framework import serializers
from .models import MyResource

class MySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyResource
        fields =('id','resource_name','shedule','start_time','end_time','details')