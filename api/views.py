# adapted from https://stackoverflow.com/questions/30831731/create-a-generic-serializer-with-a-dynamic-model-in-meta

from rest_framework import viewsets
from api.serializers import GeneralSerializer
import sys
from api.models import * 

class GeneralViewSet(viewsets.ModelViewSet):

     def get_queryset(self):
         model =  getattr(sys.modules[__name__], self.kwargs.get('model').capitalize())
         print(f"get_queryset: {self.kwargs.get('model')} {self.action}")
         return model.objects.all()           

     def get_serializer_class(self):
         GeneralSerializer.Meta.model = getattr(sys.modules[__name__], self.kwargs.get('model').capitalize())
         print(f"get_serializer_class: {self.kwargs.get('model')} {self.action}")
         return GeneralSerializer  