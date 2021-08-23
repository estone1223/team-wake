from django.db import models
from django.conf import settings

# Create your models here.

class Member(models.Model):
    name = models.CharField('名前', max_length=12, blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作成者", on_delete=models.CASCADE)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name


class Wake(models.Model):
    name = models.CharField('Wake名', max_length=50)
    description = models.TextField('説明文', max_length=48, default='', null=False, blank=True)
    member = models.ManyToManyField(Member, related_name='members', related_query_name='member')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作成者", on_delete=models.CASCADE)

    class Meta:
        db_table = 'wakes'

    def __str__(self):
        return self.name
