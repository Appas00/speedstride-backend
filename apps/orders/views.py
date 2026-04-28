from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

@api_view(['POST'])
def create_order(request):
    print("DATA:", request.data)   # ✅ ADD THIS LINE

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Order placed successfully"
        })

    print("ERRORS:", serializer.errors)  # ✅ ALSO ADD THIS
    return Response(serializer.errors, status=400)