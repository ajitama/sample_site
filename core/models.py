from django.db import models

# Create your models here.
CHOICE = (
    ('obj1', 'obj1'),
    ('obj2', 'obj2'),
    ('obj3', 'obj3'),
)

class Article(models.Model):
    subject = models.CharField(max_length=90,)
    text_field1 = models.CharField(max_length=100, blank=True, null=True)
    text_field2 = models.CharField(max_length=100, blank=True, null=True)
    text_field3 = models.CharField(max_length=100, choices=CHOICE, blank=True, null=True)
    text_field4 = models.TextField(max_length=2000,  blank=True, null=True)
    bool_field = models.BooleanField(default=False,)
    date_field1 = models.DateField(auto_now=True, auto_now_add=False,)
    date_field2 = models.DateField(auto_now=False, auto_now_add=True,)
    datetime_field1 = models.DateTimeField(auto_now=True, auto_now_add=False,)
    datetime_field2 = models.DateTimeField(auto_now=False, auto_now_add=True,)

    def __str__(self):
        return self.text_field1

    @classmethod
    def all(cls):
        """ All data get api(old type) """
        articles = cls.objects.all().order_by('subject')

        data = []
        for r in articles:
            data.append({
                "id": r.id,
                "subject": r.subject,
                "text_field1": r.text_field1,
                "text_field2": r.text_field2,
                "text_field3": r.text_field3,
                "text_field4": r.text_field4,
                "bool_field": r.bool_field,
                "date_field1": r.date_field1,
                "date_field2": r.date_field2,
                "datetime_field1": r.datetime_field1,
                "datetime_field2": r.datetime_field2,
        })
        return data
