from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

User = get_user_model()

SM_SERVICES = (
    (1.7,'Facebook Groups'),
    (1.3,'Facebook Posts'),
    (1.9,'Instagram Posts'),
    (1.2,'Twitter Posts'),
    (1.1,'Twitter Trends'),
)


MEME_CHOICES = (
    ('5','Five'),
    ('10','Ten'),
    ('50','Fifty'),
    ('100','One Hundred'),
    ('200','Two Hundred'),
)

SERVICE_TYPE = (
    (1,'Use your own content'),
    (2,'Use our content / Memes Service'),
    (3,'Use both options')
)


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    budget = models.IntegerField()
    services = MultiSelectField(choices=SM_SERVICES, null=True, blank=True)
    service_type = models.IntegerField(choices=SERVICE_TYPE, null=True, blank=True)
    # submit_company_content = models.ImageField(upload_to='',null=True, blank=True) https://learn.justdjango.com/courses/getting-started-with-django/working-images
    description = models.TextField(blank=True,null=True)
    number_of_memes = models.CharField(choices=MEME_CHOICES,max_length=3, null=True)
    running = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user} - {self.title}'


    @property
    def est_views(self):
        est_views_var = 0
        for counter, services in enumerate(self.services):
            est_views_var += float(services)
            last_count = counter + 1
        est_views_var = est_views_var/last_count
        return self.budget/est_views_var
            
