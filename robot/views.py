from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getAsk(request):
    print(request)
    return JsonResponse({"aaa":"哈哈"})