from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from contact_form.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        contact = Contact(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            locality=validated_data['locality'],
            message=validated_data['message']
        )
        # contact.set_password(validated_data['password'])
        contact.save()
        return contact