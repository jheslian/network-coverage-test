from django.db import models


# Create your models here.
class Network(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NetworkMobile(models.Model):
    operator = models.ForeignKey(Network, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    g2 = models.BooleanField(verbose_name='2G')
    g3 = models.BooleanField(verbose_name='3G')
    g4 = models.BooleanField(verbose_name='4G')
    coordinate_x = models.FloatField(null=True)
    coordinate_y = models.FloatField(null=True)

    def __str__(self):
        return str(self.operator)
