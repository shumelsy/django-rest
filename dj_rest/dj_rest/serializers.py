from rest_framework import serializers
from .models import GENDER_CHOICES, User


# normal serializer [similar to forms.Form]
class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    phone = serializers.CharField(max_length=20)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
#    address = serializers.TextField()
    address = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255) 

    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
       password = validated_data.pop("password")
       user = User.objects.create(**validated_data)
       if password:
           user.set_password(password)
           user.save()
       return user
    
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
       password = validated_data.pop("password")
       instance.__dict__.update(validated_data)
       if password:
           instance.set_password(password)
       instance.save()
       return instance


# model serializer [similar to forms.ModelForm]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "username", "dob", "phone", "gender", "address")

