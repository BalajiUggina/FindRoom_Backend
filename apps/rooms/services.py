from apps.rooms.models import StandaloneRoom
from apps.common.exceptions import NotFound
import logging

logger=logging.getLogger('apps.rooms')

def create_room(*,user,data):
    room=StandaloneRoom.objects.create(provider=user,**data)
    logger.info("room created successfully")
    return room

def get_public_rooms():
    rooms=StandaloneRoom.objects.order_by("-created_at")
    logger.info("rooms are fetched successfully")
    return rooms

def get_public_room_by_id(*,room_id):
    try:
        room=StandaloneRoom.objects.get(id=room_id)
    except StandaloneRoom.DoesNotExist:
        logger.info(f"room with id:{room_id} not found")
        raise NotFound("room not found")
    logger.info(f"room with id:{room_id} fetched successfully")
    return room
    

# used to get rooms of provider only
def get_provider_rooms(*,user):
    rooms= user.standalone_rooms.order_by("-created_at")
    logger.info(f"provider :{user.id} fetched their rooms")
    return rooms

def get_room_by_id(*,user,room_id):
    try:
        room=user.standalone_rooms.get(id=room_id)
        logger.info(f"Room retrieved: {room.id} by provider {user.id}")
        return room
    except StandaloneRoom.DoesNotExist:
        logger.warning(f"room with id:{room_id} not found")
        raise NotFound("Room Not found")

def delete_room(*,user,room_id):
    try:
        room=StandaloneRoom.objects.get(id=room_id,provider=user)   
    except StandaloneRoom.DoesNotExist:
        raise NotFound(f"room :{room_id} does not exist")
    room.delete()
    logger.info(f"room :{room_id} deleted by provider :{user.id}")
    return True