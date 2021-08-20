from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField('名前', max_length=12, blank=False)
<<<<<<< HEAD
=======
    is_Sniper = models.BooleanField('SRか', default=False)
    clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)
    memo = models.TextField('メモ', max_length=255, blank=True, null=True)
>>>>>>> parent of 7a865a3 (editted templates next->create model)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name


<<<<<<< HEAD
class Wake(models.Model):
    name = models.CharField(('Wake名'), max_length=50)
    member = models.ManyToManyField(Member, related_name='wakes', related_query_name='wake')
    class Meta:
        db_table = 'wakes'

    def __str__(self):
        return self.name
=======
>>>>>>> parent of 7a865a3 (editted templates next->create model)



