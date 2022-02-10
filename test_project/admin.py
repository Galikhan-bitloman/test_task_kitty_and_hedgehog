from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(KittyandHedgehog)
admin.site.register(Lot)
admin.site.register(Bet)
admin.site.register(Select_bet)

