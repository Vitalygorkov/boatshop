from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200)
    locality = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"