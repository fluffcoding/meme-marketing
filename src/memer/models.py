from django.db import models
from business.models import Campaign
from django.contrib.auth import get_user_model

User = get_user_model()


class Meme(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    memer = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,null=True, blank=True)


class MemeImages(models.Model):
    parent_meme = models.ForeignKey(Meme, on_delete=models.CASCADE, null=True, related_name='memerconnect')
    image = models.ImageField(upload_to='memes/')

    class Meta:
        verbose_name_plural = 'Meme Images'
