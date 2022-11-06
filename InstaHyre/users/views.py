from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny
from .models import User
# Create your views here.
class CustomeUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Checking if the user with the given phone number exists or not
        req_data = request.data
        print("############")
        print(req_data)
        phone_number = req_data.get('phone_number', None)
        print("############")
        print(User.objects.filter(phone_number=phone_number).first())
        if User.objects.filter(phone_number=phone_number).exists():
            return Response(
                data="User with this phone number already exists",
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)