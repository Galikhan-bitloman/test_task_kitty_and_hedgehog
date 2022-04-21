from django.contrib import admin
from test_task_kitty_and_hedgehog.models import User, KittyandHedgehog, Lot, Bet, SelectBet
# Register your models here.

admin.site.register(User)
admin.site.register(KittyandHedgehog)
admin.site.register(Lot)
admin.site.register(Bet)
admin.site.register(SelectBet)

