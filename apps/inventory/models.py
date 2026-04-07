from django.db import models
from apps.core.models import BaseModel
from apps.products.models import Product

class Inventory(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class StockMovement(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(
        max_length=10,
        choices=(
            ('IN', 'Entrada'),
            ('OUT', 'Saída'),
        )
    )

    def __str__(self):
        return f"{self.product.name} - {self.movement_type}"