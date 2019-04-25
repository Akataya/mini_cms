from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=3000, null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)

    RED = 'Red'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    COLOR_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default=GREEN,
    )

    def __str__(self):
        return f'{self.title}'


class Section(models.Model):
    title = models.CharField(max_length=100)
    """Used in section previews"""
    description = models.TextField(max_length=300, null=True, blank=True)
    show = models.BooleanField(default=True)
    effective_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title}'


class SectionItem(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(max_length=5000)
    show = models.BooleanField(default=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    effective_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Office(models.Model):
    number = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3, null=True)
    address = models.CharField(max_length=300)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.abbreviation}'
