from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
from tzadik_api.models import Category
from tzadik_api.serializers import CategorySerializer


class CategoryView(ViewSet):
    def list(self, request):
        ''' Get a list of categories. '''

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' Returns a single category. '''

        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
