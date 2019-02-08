from .views import ModelsImportView, ModelDetailView, ModelInstanceDetailView
from django.urls import path


urlpatterns = [
    path('import/', ModelsImportView.as_view(), name='import'),
    path('detail/<model_name>/<int:pk>', ModelInstanceDetailView.as_view(), name='model-instance-detail'),
    path('detail/<model_name>/', ModelDetailView.as_view(), name='model-detail'),
]
