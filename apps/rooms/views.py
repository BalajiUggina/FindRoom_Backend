from rest_framework.views import APIView
from apps.rooms.serializers import CreateRoomSerializer,RoomDetailSerializer,RoomListSerializer,UpdateRoomSerializer
from apps.rooms.services import create_room,get_provider_rooms,get_room_by_id,delete_room,get_public_room_by_id,get_public_rooms
from rest_framework import permissions
from apps.common.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status
import logging
logger=logging.getLogger('apps.rooms')

class IsProvider(BasePermission):
    message = "Only providers can access this endpoint"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.role != "provider":
            logger.warning(f"Non-provider user {request.user.id} tried to access provider endpoint")
            return False

        return True
class CreateRoomView(APIView):
    permission_classes=[IsProvider]

    def post(self,request):
        roomSerializer=CreateRoomSerializer(data=request.data)
        roomSerializer.is_valid(raise_exception=True)
        room=create_room(user=request.user,data=roomSerializer.validated_data)
        return Response({
            "success":True,
            "message":f"Room created successfully by provider :{request.user.id}",
            "data":RoomDetailSerializer(room).data},
            status=status.HTTP_201_CREATED)
        
# end users able to see all rooms
class PublicRoomsView(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self,request):
        rooms=get_public_rooms()
        serializer=RoomListSerializer(rooms,many=True)
        return Response({
            "success":True,
            "message":f"Room are fetched successfully",
            "data":serializer.data},status=status.HTTP_200_OK)

#end user able to see particular room 
class PublicRoomDetailView(APIView):
    permission_classes=[permissions.AllowAny]

    def get(self,request,pk):
        room=get_public_room_by_id(room_id=pk)
        serializer=RoomDetailSerializer(room)
        return Response({
            "success":True,
            "message":f"Room :{pk} retrieved successfully",
            "data":serializer.data},status=status.HTTP_200_OK)

#rooms are accessed to provider itself 
class ProviderRoomsView(APIView):
    permission_classes=[IsProvider]

    def get(self,request):
        rooms=get_provider_rooms(user=request.user)
        serializer=RoomListSerializer(rooms,many=True)
        return Response({
            "success":True,
            "message":f"Provider :{request.user.id} rooms details",
            "data":serializer.data
        },status=status.HTTP_200_OK)

class ProviderRoomDetailView(APIView):
    permission_classes=[IsProvider]

    def get(self,request,pk):
        room=get_room_by_id(user=request.user,room_id=pk)
        return Response({
            "success":True,
            "message":f"Room :{pk} details fetched",
            "data":RoomDetailSerializer(room).data
        },status=status.HTTP_200_OK)



class UpdateRoomView(APIView):
    permission_classes=[IsProvider]

    def put(self,request,pk):
        room=get_room_by_id(user=request.user,room_id=pk)
        # 'partial=True' allows partial updates: only the fields provided in request.data will be updated.
        # Use 'partial=True' when you want to allow updating only some fields, not all required fields.
        serializer=UpdateRoomSerializer(room,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        updated_room=serializer.instance
        return Response({
            "success":True,
            "message":"Room details updated successfully",
            "data":RoomDetailSerializer(updated_room).data,
        })


class DeleteRoomView(APIView):
    permission_classes=[IsProvider]

    def delete(self,request,pk):
        delete_room(user=request.user,room_id=pk)
        return Response({"success":True,"message":"Room deleted successfully"},status=status.HTTP_200_OK)