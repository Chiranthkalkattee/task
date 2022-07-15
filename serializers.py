from rest_framework import serializers
from .models import Employee_details,Department_details


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_details
        # fields = ['id', 'name', 'emp_id', 'designation']
        fields = '__all__'
class DepartmentSerializer(serializers.ModelSerializer):
    level = EmployeeSerializer(read_only=True)
    class Meta:
        model = Department_details
        fields = '__all__'

    # name = serializers.CharField(max_length=20)
    # emp_id = serializers.IntegerField()
    # designation = serializers.CharField(max_length=50)
    #
    # def create(self,validated_data):
    #     return Employee_details.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data('name', instance.name)
    #     instance.emp_id = validated_data('emp_id', instance.emp_id)
    #     instance.designation = validated_data('designation', instance.designation)
    #     instance.save()
    #     return instance


