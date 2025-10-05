from rest_framework import serializers
from products.models import ProductsModel

class ProductsSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ProductsModel
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    # 'obj' is the instance of the 'product' model
    def get_my_discount(self, obj):
        try:
            if not hasattr(obj, "id"):
                return None
           
            if not isinstance(obj, ProductsModel):
                return None
           
            return obj.get_discount() + "%"

        except:
            None
    



