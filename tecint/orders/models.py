from django.db import models

# Create your models here.

#Model for verifying order status of the complete order.
class OrderNumber(models.Model):
    order_number = models.IntegerField()
    def __str__(self):
        return "ORD_" + str(self.order_number) + ' ' + str(self.pk)

        
class OrderLines(models.Model):
    #Class Status allows us to create a method to choose the status of the order
    class Status(models.TextChoices):
        SHIPPED = 'Shipped'
        PENDING = 'Pending'
        CANCELED = 'Cancelled'
    # Order number selects a foreign key attribute to filter correctly order number
    order_number = models.ForeignKey(OrderNumber, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.PENDING)
    def __str__(self):
        return "ORD_" + str(self.order_number) + " " + self.item_name + ' ' + self.status
class OrderStatus(models.Model):
   #Class allows us to save all the orders with the same ordernumber and verify the correct status
    class Status(models.TextChoices):
        SHIPPED = 'Shipped'
        PENDING = 'Pending'
        CANCELED = 'Cancelled'
    order = models.ForeignKey(OrderNumber, on_delete=models.CASCADE)
    #Stores each "OrderLine or Item to the Order Status"
    items = models.ManyToManyField(OrderLines, null=True, blank=True)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.PENDING)
    
    def __str__(self):
        return "ORD_" + str(self.order.order_number) + " " + self.status
            