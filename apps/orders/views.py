from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


# ✅ CREATE ORDER
@api_view(['POST'])
def create_order(request):
    print("DATA:", request.data)   # Debug log

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Order placed successfully"
        })

    print("ERRORS:", serializer.errors)  # Debug log
    return Response(serializer.errors, status=400)


# ✅ GET ALL ORDERS
@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)