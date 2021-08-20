from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField('名前', max_length=12, blank=False)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name


class Wake(models.Model):
    name = models.CharField(('Wake名'), max_length=50)
    member = models.ManyToManyField(Member, related_name='wakes', related_query_name='wake')
    class Meta:
        db_table = 'wakes'

    def __str__(self):
        return self.name
