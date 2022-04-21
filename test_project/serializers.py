from rest_framework import serializers
from .models import *


class UserSerializers(serializers.Serializer):
    number_of_money = serializers.IntegerField(default=0)
    user_name = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number_of_money = validated_data.get("number_of_money", instance.number_of_money)
        instance.user_name = validated_data.get("user_name", instance.user_name)

        instance.save()
        return instance


class ASerializer(serializers.ModelSerializer):

    class Meta:
        model = KittyandHedgehog
        fields = ('species', 'name', 'owner_name', )


class KittyandHedgehogSerializers(serializers.Serializer):
    species = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    owner_name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return KittyandHedgehog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.species = validated_data.get("species ", instance.species)
        instance.name = validated_data.get("name", instance.name)
        instance.owner_name = validated_data.get("test_project_user.id", instance.owner_name)
        instance.save()
        return instance


"""class LotSerializers(serializers.Serializer):
    name = serializers.CharField(KittyandHedgehogSerializers)
    price = serializers.IntegerField(default=0)
    owner_name = serializers.CharField(UserSerializers)

    def create(self, validated_data):
        return LotSerializers.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.owner_name = validated_data.get("owner_name", instance.owner_name)
        instance.save()
        return instance
"""

"""class BetSerializers(serializers.Serializer):
    number_of_bet = serializers.IntegerField(default=0)
    onwer_name = serializers.CharField(UserSerializers, max_length=100)

    def create(self, validated_data):
        return BetSerializers.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.number_of_bet = validated_data.get("number_of_bet", instance.number_of_bet)
        instance.owner_name = validated_data.get("owner_name", instance.owner_name)
        instance.save()
        return instance"""
