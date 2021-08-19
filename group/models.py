from django.db import models

# Create your models here.

class Wake(models.Model):
    name = models.CharField(('Wake名'), max_length=50)
    
    class Meta:
        db_table = 'wakes'

    def __str__(self):
        return self.name

# class Clan(models.Model):
#     name = models.CharField('クラン名', max_length=12)
#     description = models.TextField('説明文', max_length=255, null=False)
    
#     class Meta:
#         db_table = 'clans'

#     def __str__(self):
#         return self.name

class Member(models.Model):
    name = models.CharField('名前', max_length=12, blank=False)
    # is_Sniper = models.BooleanField('SRか', default=False)
    # # clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True, blank=True)
    # memo = models.TextField('メモ', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.name


class MemberWakes(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, blank=False, null=False)
    wake_id = models.ForeignKey(Wake, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'member_wakes'



