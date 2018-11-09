from django.db import models

# Create your models here.
CHOICE = (
    ('obj1', 'obj1'),
    ('obj2', 'obj2'),
    ('obj3', 'obj3'),
)

class Article(models.Model):
    text_field1 = models.CharField(max_length=100, blank=True, null=True)
    text_field2 = models.CharField(max_length=100, blank=True, null=True)
    text_field3 = models.CharField(max_length=100, choices=CHOICE, blank=True, null=True)
    text_field4 = models.TextField(max_length=2000, choices=CHOICE, blank=True, null=True)
    bool_field = models.BooleanField(default=False,)
    date_field1 = models.DateField(auto_now=True, auto_now_add=False,)
    date_field2 = models.DateField(auto_now=False, auto_now_add=True,)
    datetime_field1 = models.DateTimeField(auto_now=True, auto_now_add=False,)
    datetime_field2 = models.DateTimeField(auto_now=False, auto_now_add=True,)

    def __str__(self):
        return self.name



