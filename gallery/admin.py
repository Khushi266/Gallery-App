from django.contrib import admin
from .models import Artwork,Bid,Transaction
# Register your models here.
admin.site.register(Artwork)
admin.site.register(Bid)
admin.site.register(Transaction)