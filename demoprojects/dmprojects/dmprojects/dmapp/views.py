# from django.http import HttpResponse
from django.shortcuts import render
from.models import place

# Create your views here.
def dminmakes(request):
    obj = place.objects.all()
    return render(request, "index.html",{'result':obj})








# def addition(request):
#     x = int(request.GET["num1"])
#     y = int(request.GET["num2"])
#     res = x + y
#     return render(request, "result.html", {'addi': res})
#
#
# def multiplication(request):
#     a = int(request.GET["num3"])
#     b = int(request.GET["num4"])
#     m = a * b
#     return render(request, "result.html", {'mult': m})
#
#
# def division(request):
#     s = int(request.GET["num5"])
#     t = int(request.GET["num6"])
#     d = s % t
#     return render(request, "result.html", {'divi': d})


# def substraction(request):
#     u = int(request.GET["num7"])
#     v = int(request.GET["num8"])
#     s = u - v
#     return render(request, "result.html", {'subs': s})


# def calculate_view(request):
#     num1 = int(request.GET.get('num1', 0))
#     num2 = int(request.GET.get('num2', 0))
#     if calculate_view == 'add':
#         res = num1 + num2
#         # return HttpResponse(f"The sum is: {result}")
#     elif calculate_view == 'multiply':
#         m = num1 * num2
#         # return HttpResponse(f"The product is: {result}")
#
#     # s = int(request.GET["num5"])
#     # t = int(request.GET["num6"])
#     # d = s % t
#     # u = int(request.GET["num7"])
#     # v = int(request.GET["num8"])
#     # s = u - v
#     return render(request, "result.html", {'addi': res}, {'mult': m},{'divi': d}, {'subs': s} )
