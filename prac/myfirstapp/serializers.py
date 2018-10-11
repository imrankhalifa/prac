from rest_framework.serializers import  ModelSerializer
from .models import Stock


class StockSerializers(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'



