from django.db import models
from business.models import Campaign
from django.contrib.auth import get_user_model

User = get_user_model()


class Meme(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    memer = models.ForeignKey(User, on_delete=models.CASCADE)
    #meme_image = models.ImageField(upload_to='/memes/')
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.meme.campaign.name) + self.memer.email


class MemeImages(models.Model):
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='memes/')

    class Meta:
        verbose_name_plural = 'Meme Images'

    def __str__(self):
        return str(self.meme.campaign.name) + self.memer.email + self.id