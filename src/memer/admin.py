from django.contrib import admin

from .models import Meme, MemeImages


class MemeImageAdmin(admin.StackedInline):
    model = MemeImages


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    inlines = [MemeImageAdmin]

    class Meta:
        model = Meme


@admin.register(MemeImages)
class MemeImageAdmin(admin.ModelAdmin):
    pass


