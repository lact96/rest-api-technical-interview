from django.db import models

# Create your models here.
class CustomerOrders(models.Model):
    order_id = models.CharField(max_length=22)
    order_date = models.DateField()
    quantity_ordered = models.IntegerField(default=1)
    def __str__(self):
        return self.order_id + ' ordered on ' + str(self.order_date)

class OrderSeason(models.Model):
    class Season(models.TextChoices):
        #Allow us to have only 4 possible choices Winter, Spring, Summer, Fall
        WINTER = "Winter"
        SPRING = "Spring"
        SUMMER = "Summer"
        FALL = "Fall"
        
    order_id = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE)
    season = models.CharField(max_length=6, choices=Season.choices, default=Season.SUMMER)