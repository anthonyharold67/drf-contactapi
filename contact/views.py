from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from rest_framework import status
from .serializers import ContactSerializer
from rest_framework import generics

@api_view(['GET', 'POST'])
def contact_list(request):
    if request.method == 'GET':
        contact_list = Contact.objects.all()
        serializer = ContactSerializer(contact_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class ContactRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
            