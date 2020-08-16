from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    CHECK = 0
    CASH = 1

    PAYMENT_TERM_CHOICES = [
        (CHECK, 'Check'),
        (CASH, 'Cash')
    ]

    name = models.CharField(
        verbose_name='name', max_length=45, help_text='Name of Supplier',
        blank=True
    )
    lead_time = models.DurationField(
        verbose_name='lead_time', help_text='Lead Time of Supplier', 
        default=timezone.timedelta(days=3)
    )
    payment_terms = models.PositiveSmallIntegerField(
        verbose_name='payment_terms', help_text='Terms of Payment for the Supplier', 
        choices=PAYMENT_TERM_CHOICES, default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']