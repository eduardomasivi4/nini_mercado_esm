from django.db import transaction
from apps.cart.models import Cart, CartItem
from apps.orders.models import Order, OrderItem
from apps.inventory.models import Inventory, StockMovement

@transaction.atomic
def checkout(user):
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        raise Exception("Carrinho vazio")

    order = Order.objects.create(user=user, total=0)
    total = 0

    for item in cart_items:
        product = item.product
        quantity = item.quantity

        inventory = Inventory.objects.get(product=product)
        inventory = Inventory.objects.select_for_update().get(product=product)

        # 🔴 Verificar estoque
        if inventory.quantity < quantity:
            raise Exception(f"Estoque insuficiente para {product.name}")

        # 🧾 Criar item do pedido
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

        # 📊 Atualizar total
        total += product.price * quantity

        # 📉 Baixar estoque
        inventory.quantity -= quantity
        inventory.save()

        # 📝 Registrar movimentação
        StockMovement.objects.create(
            product=product,
            quantity=quantity,
            movement_type='OUT'
        )

    # 💰 Atualizar total do pedido
    order.total = total
    order.save()

    # 🧹 Limpar carrinho
    cart_items.delete()

    return order