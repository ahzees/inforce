from authentication.models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import CustomUserSerializer


# Create your views here.
class CreateCustomUserApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "created"}, status=status.HTTP_201_CREATED)
        return Response(
            {"status": "error - Invalid data"}, status=status.HTTP_406_NOT_ACCEPTABLE
        )
