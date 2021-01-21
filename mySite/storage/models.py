from django.db import models

# Create your models here.

class Data(models.Model):
    source = models.FileField(upload_to='storage/')
    flow_count = models.CharField(max_length=16, verbose_name="Number of flows")
    packet_count = models.CharField(max_length=16, verbose_name="Number of Packets")
    size = models.CharField(max_length=16, verbose_name="Size (MB)")

    def __str__(self):
        return self.date