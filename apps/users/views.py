from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from apps.users.serializers import RegisterSerializer,UserSerializer,RoleUpdateSerializer
from apps.users.services import register_user,update_user_role,login_user

# RegisterView

class RegisterView(APIView):
    permission_classes=[permissions.AllowAny]
    
    def post(self,request):
        
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=register_user(data=serializer.validated_data)
            return Response({
                "success":True,
                "message":"User registered successfully",
                "data":UserSerializer(user).data
            },status=status.HTTP_201_CREATED)
    

# Loginview

class LoginView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        tokens = login_user(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        return Response({
            "success":True,
            "message":"User Login Successful",
            "data":{**tokens},
        },status=status.HTTP_200_OK)
    
class ProfileView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response({
            "success":True,
            "message":"User profile retrieved successfully",
            "data":serializer.data},status=status.HTTP_200_OK)
    
class UpdateRoleView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def put(self,request):
        roleSerializer=RoleUpdateSerializer(data=request.data)
        if roleSerializer.is_valid(raise_exception=True):
            user=update_user_role(user=request.user,role=roleSerializer.validated_data["role"])
            return Response({
                "success":True,
                "message":"Role Updated Successfully",
                "data":UserSerializer(user).data},status=status.HTTP_200_OK)
    
