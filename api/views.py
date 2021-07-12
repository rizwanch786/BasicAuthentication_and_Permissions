from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
class StudentMVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # # # permission_classes = [IsAuthenticated]
    # # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser] #It access the API if its STAFF Status is TRUE/Checked

