from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from api.models import MoringaMerch, Student
from .serializers import MerchSerializer, StdentSerializer
@api_view(['GET'])
def show_data(request):
    # student = {
    #     'name':'charles',
    #     'track': 'fullstack',
    # }

    students = Student.objects.all()
    serializer= StdentSerializer(students, many=True)
    return Response(serializer.data)

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = MerchSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)