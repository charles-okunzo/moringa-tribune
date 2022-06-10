
from rest_framework import serializers
from api.models import Student, MoringaMerch



class StdentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = '__all__'