from .models import Onsen, OnsenInn
from rest_framework import serializers

class OnsenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onsen
        fields = '__all__'

class OnsenInnSerializer(serializers.ModelSerializer):

    onsen = OnsenSerializer()

    class Meta:
        model = OnsenInn        
        #filter_fields = ('id', 'category')
        fields = '__all__'
        
