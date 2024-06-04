from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.get_content_selenium import get_content_selenium


# Create your views here.

@api_view(['GET'])
def search(request):
  link = request.data.get("link", "")
  print("link:", link)
  link_content = get_content_selenium(link)
  print(link_content)
  return Response({"message": "search"})
