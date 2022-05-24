from rest_framework import serializers
from .models import Candidate
import datetime
#Candidate Serializer
class CandidateSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.education = validated_data.get('education', instance.education)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.country = validated_data.get('country', instance.country) 
        instance.resume = validated_data.get('resume', instance.resume)       
        instance.updated_at = datetime.datetime.now()
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    created_at = serializers.DateTimeField(format="%d-%m-%Y|%H:%M:%S", read_only=True)
    # updated_at = serializers.DateTimeField(format="%d-%m-%Y|%H:%M:%S")
    class Meta:
        model = Candidate
        fields = '__all__'
        read_only_fields = ('id','created_at')   
     