from django.shortcuts import render
from django.http import JsonResponse
from apps.orders.services import checkout


def checkout_view(request):
    user = request.user

    try:
        order = checkout(user)
        return JsonResponse({"message": "Pedido criado", "order_id": order.id})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)