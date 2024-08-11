from django.contrib import admin
from .models import Article


# Register your models here.

class Articlep(admin.ModelAdmin):
    list_display = ["name", "email","messege","time"]
    list_filter = ["name", "email"]
    search_fields = ["name", "email","messege"]
    list_editable = ["messege"]
    list_display_links = ["name", "email"]

class Meta:
    model = Article

admin.site.register(Article,Articlep)