from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
     #validators
    def start_with_s(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with s')
   
    name = serializers.CharField(validators=[start_with_s])
    
    
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city', 'state']
        
    
    #Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
            return value
        
        
    #object level validation
    def validate_object(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'suraj' and ct.lower() != 'ktm':
            raise serializers.ValidationError('city must ne ktm')
        return data 
    
   
    
    


    
            
    