# Generated by Django 3.0.7 on 2020-06-21 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('budget', models.IntegerField()),
                ('services', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1.7, 'Facebook Groups'), (1.3, 'Facebook Posts'), (1.9, 'Instagram Posts'), (1.2, 'Twitter Posts'), (1.1, 'Twitter Trends')], max_length=19, null=True)),
                ('service_type', models.IntegerField(blank=True, choices=[(1, 'Use your own content'), (2, 'Use our content / Memes Service'), (3, 'Use both options')], null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('number_of_memes', models.CharField(choices=[('5', 'Five'), ('10', 'Ten'), ('50', 'Fifty'), ('100', 'One Hundred'), ('200', 'Two Hundred')], max_length=3, null=True)),
                ('running', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
