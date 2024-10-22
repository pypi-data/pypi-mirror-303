from django.db import models


class Constant(models.Model):
    key = models.SlugField("Key", max_length=50, primary_key=True)
    value = models.TextField("Value", default="", blank=True)
    context = models.TextField("Context", null=True, blank=True)

    def __str__(self):
        return f"Snart for [{self.key}]"

    class Meta:
        verbose_name_plural = "Constants"
        verbose_name = "Constant"
