from datetime import datetime
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from tzadik_api.models import Order#, Album, OrderedAlbum
from tzadik_api.serializers import OrderSerializer


class OrderView(ViewSet):
    def list(self, request):
        ''' Get a list of the current user's orders. '''

        orders = Order.objects.filter(user=request.auth.user)
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        ''' Get a user's specific order. '''

        order = Order.objects.filter(pk=pk, user=request.auth.user)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def destroy(self, request, pk):
        ''' Delete an existing order associated with the current user. '''

        try:
            order = Order.objects.get(pk=pk, user=request.auth.user)
            order.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=True)
    def edit_order(self, request, pk):
        ''' Edit an existing order. '''

        try:
            order = Order.objects.get(pk=pk, user=request.auth.user)
            order.save()
            return Response({'message': 'Order Updated.'})
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=True)
    def complete(self, request, pk):
        ''' Complete an order. '''

        try:
            order = Order.objects.get(pk=pk, user=request.auth.user)
            order.submission_datetime = datetime.now()
            order.save()    
            return Response({'message': "Order Completed."})
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    @action(methods=['GET'], detail=False)
    def current(self, request):
        ''' Get the user's current order. '''

        try:
            order = Order.objects.get(submission_datetime=None, user=request.auth.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response(
                {'message': 'You do not have an open order.'},
                status=status.HTTP_404_NOT_FOUND
                )
