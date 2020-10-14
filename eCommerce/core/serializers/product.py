from rest_framework import serializers

from ..models.product import Item, Category, ItemSpecification, ItemFavorit, ItemPicture, ItemReturn, ItemReview, ItemReviewPictures, Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReview
        fields = '__all__'

class ItemPictSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPicture
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ItemReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReturn
        fields = '__all__'