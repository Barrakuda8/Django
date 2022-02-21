from django.conf import settings
from django.db import models
from lootapp.models import Material
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q


class Order(models.Model):

    STATUS_FORMING = 'FM'
    STATUS_SEND_TO_PAYMENT = 'STP'
    STATUS_PAID = 'PD'
    STATUS_DONE = 'DN'
    STATUS_CANCELED = 'CN'

    STATUSES = ((STATUS_FORMING, "Forming"),
                (STATUS_SEND_TO_PAYMENT, "Waiting for payment"),
                (STATUS_PAID, "Paid"),
                (STATUS_DONE, "Done"),
                (STATUS_CANCELED, "Canceled"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, default=STATUS_FORMING, max_length=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def total_cost(self):
        _items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.cost, _items)))

    @property
    def total_quantity(self):
        _items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, _items)))

    def delete(self):
        self.is_active = False
        self.status = self.STATUS_CANCELED
        self.save()


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Material')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')

    @property
    def cost(self):
        return self.material.price_rp * self.quantity


# не знаю как реализовать более адекватно
# первая часть функции убирает из заказа товары с 0 количества
# вторая часть делает так, чтобы в одном заказе у одного товара был только один OrderItem
@receiver(post_save, sender=OrderItem)
def item_post_save_adjustments(sender, update_fields, instance, **kwargs):
    if instance.quantity == 0:
        instance.delete()
    try:
        item = OrderItem.objects.get(Q(order=instance.order, material=instance.material), ~Q(pk=instance.pk))
        item.quantity += instance.quantity
        instance.delete()
        item.save()
    except OrderItem.DoesNotExist:
        pass






