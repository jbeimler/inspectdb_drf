# Code adapted from https://stackoverflow.com/questions/30831731/create-a-generic-serializer-with-a-dynamic-model-in-meta

from rest_framework import serializers

class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'