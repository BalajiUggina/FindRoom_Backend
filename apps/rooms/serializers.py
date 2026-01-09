from rest_framework import serializers
from apps.rooms.models import StandaloneRoom,StandaloneRoomImage
from apps.users.serializers import UserSerializer
class StandaloneRoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandaloneRoomImage
        fields = ["id", "image"]
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=StandaloneRoom
        fields=['occupancy','rent_per_month','bills_included','extra_bills','facilities','rules','gender_allowed','address','area','city']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model=StandaloneRoom
        fields=['id','area','city','rent_per_month','occupancy','gender_allowed','availability_status']


class RoomDetailSerializer(serializers.ModelSerializer):
    images = StandaloneRoomImageSerializer(many=True, read_only=True)
    provider=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=StandaloneRoom
        fields=['id','provider','occupancy','rent_per_month','bills_included','extra_bills','facilities','rules','gender_allowed','address','area','city','availability_status','images']
    

class UpdateRoomSerializer(serializers.ModelSerializer):
     class Meta:
        model=StandaloneRoom
        fields=['occupancy','rent_per_month','bills_included','extra_bills','facilities','rules','gender_allowed','address','area','city']
