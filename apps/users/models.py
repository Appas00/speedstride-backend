from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()

    # ✅ MUST be this
    image = models.URLField()

    color = models.CharField(max_length=50)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name