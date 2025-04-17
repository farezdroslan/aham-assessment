from rest_framework import serializers
from .models import Fund

class FundSerializer(serializers.ModelSerializer):
    """
    Serializer for the Fund model.
    """

    class Meta:
        model = Fund  # Specify the model to serialize
        fields = '__all__'  # Serialize all fields of the Fund model