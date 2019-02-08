from rest_framework import serializers


class ModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'
