from django.db import models

class Dorixona(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    description = models.TextField()
    soni = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/", default='defaults/default.jpeg ', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Dorixona"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

