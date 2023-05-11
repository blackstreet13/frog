from django.db import models

class Frogs(models.Model):
    class Meta:
        db_table = 'frogs'
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    year = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name},{self.color}'
