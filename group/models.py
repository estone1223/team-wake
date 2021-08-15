from django.db import models

# Create your models here.

class Clan(models.Model):
    name = models.CharField('クラン名', max_length=12)
    description = models.TextField('説明文', max_length=255, null=False)
    
    class Meta:
        db_table = 'clans'

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField('名前', max_length=12, blank=False)
    is_Sniper = models.BooleanField('SRか', default=False)
    clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)
    memo = models.TextField('メモ', max_length=255, null=True)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name





