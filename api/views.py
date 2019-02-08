from rest_framework import views, mixins, generics
from django.apps import apps
from .serializers import *
from .tools import json_to_models


# Endpoint: /import/

class ModelsImportView(views.APIView, mixins.CreateModelMixin):
    def post(self, request):
        instances_list = request.data
        json_to_models(instances_list)


# Endpoint: /detail/<model_name>

class ModelDetailView(generics.ListAPIView):
    def get_queryset(self):
        model_name = self.kwargs["model_name"]
        model = apps.get_model('api', model_name)
        return model.objects.all()

    def get_serializer_class(self):
        model_name = self.kwargs["model_name"]
        ModelDetailSerializer.Meta.model = apps.get_model('api', model_name)
        return ModelDetailSerializer


# Endpoint: /detail/<model_name>/<pk>

class ModelInstanceDetailView(generics.RetrieveAPIView):
    lookup_field = 'pk'

    def get_queryset(self):
        model_name = self.kwargs["model_name"]
        model = apps.get_model('api', model_name)
        return model.objects.all()

    def get_serializer_class(self):
        model_name = self.kwargs["model_name"]
        ModelDetailSerializer.Meta.model = apps.get_model('api', model_name)
        return ModelDetailSerializer
