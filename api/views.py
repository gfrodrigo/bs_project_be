from decimal import Decimal

from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Business
from .serializers import BusinessSerializer

ANNUAL_REVENUE_LIMIT = 500000


@api_view(['GET'])
def get_data(request):
    business = Business.objects.all()
    serializer = BusinessSerializer(business, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_data(request):
    serializer = BusinessSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def validate_credit_approval(request):
    serializer = BusinessSerializer(data=request.data)
    print(request.data)
    result = "Declined"
    if serializer.is_valid():
        annual_revenue = Decimal(serializer.data["annual_revenue"])
        if annual_revenue == ANNUAL_REVENUE_LIMIT:
            result = "Undecided"
        if annual_revenue > ANNUAL_REVENUE_LIMIT:
            result = "Approved"
    return Response({"data": result})
