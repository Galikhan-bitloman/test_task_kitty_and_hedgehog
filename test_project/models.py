from django.db import models
from django.contrib.auth import get_user_model
User1 = get_user_model()



# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    number_of_money = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name


class KittyandHedgehog(models.Model):
    species_select = (
        ("cat", "cat"),
        ("hedgehog", "hedgehog")
    )
    species = models.CharField(default="Cat or Hedgehog?", choices=species_select, max_length=100)
    name = models.CharField(max_length=100)
    owner_name = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.species, self.name, self.owner_name)


class Lot(models.Model):
    name = models.ForeignKey(KittyandHedgehog, max_length=100, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    owner_name = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)


class Bet(models.Model):
    number_of_bet = models.IntegerField(default=0)
    onwer_name = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)

    def __str__(self):
        return ' User - {} made a bet in {}  '.format(self.onwer_name, self.number_of_bet)


class Select_bet(models.Model):
    user_who_make_lot = models.ForeignKey(User, on_delete=models.CASCADE)
    which_lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    choice_of_user = models.ForeignKey(Bet, on_delete=models.CASCADE)


    def __str__(self):
        return '{} {}'.format(self.user_who_make_lot, self.choice_of_user)
