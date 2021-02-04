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
    removed = models.BooleanField(
        verbose_name='removed', help_text='Supplier is removed', default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']


class Category(models.Model):

    name = models.CharField(
        verbose_name='name', max_length=45, help_text='Name of Category',
        blank=True
    )
    description = models.TextField(
        verbose_name='description', help_text='Description of Category', 
        blank=True
    )
    removed = models.BooleanField(
        verbose_name='removed', help_text='Category is removed', default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Brand(models.Model):

    name = models.CharField(
        verbose_name='name', max_length=45, help_text='Name of Brand',
        blank=True
    )
    description = models.TextField(
        verbose_name='description', help_text='Description of Brand', 
        blank=True
    )
    removed = models.BooleanField(
        verbose_name='removed', help_text='Brand is removed', default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']


class Item(models.Model):

    name = models.CharField(
        verbose_name='name', max_length=45, help_text='Name of Item',
        blank=True
    )
    volume = models.CharField(
        verbose_name='volume', max_length=45, help_text='Volume of Item',
        blank=True
    )
    code = models.CharField(
        verbose_name='code', max_length=10, help_text='Code of Item',
        blank=True
    )
    unit_cost = models.DecimalField(
        verbose_name='unit cost', max_digits=7, help_text='Unit Cost of Item',
        decimal_places=2, default=0
    )
    box_cost = models.DecimalField(
        verbose_name='box cost', max_digits=7, help_text='Box Cost of Item',
        decimal_places=2, default=0
    )
    safety_stock = models.IntegerField(
        verbose_name='box cost', help_text='Box Cost of Item', default=0
    )
    active = models.BooleanField(
        verbose_name='active', help_text='Is item active', default=True
    )
    removed = models.BooleanField(
        verbose_name='removed', help_text='Item is removed', default=False
    )
    supplier = models.ForeignKey(
        to=Supplier, verbose_name='supplier', related_name='item', 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        to=Category, verbose_name='category', related_name='item', 
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        to=Brand, verbose_name='brand', related_name='item', 
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        verbose_name='quantity', help_text='Quantity of item', default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['name']
