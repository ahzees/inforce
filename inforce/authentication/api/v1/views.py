from authentication.models import CustomUser
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import CustomUserSerializer


@extend_schema(description="Create a new user")
# Create your views here.
class CreateCustomUserApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "created"}, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "error - Invalid data"}, status=status.HTTP_406_NOT_ACCEPTABLE
        )
