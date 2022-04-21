from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name


class KittyandHedgehog(models.Model):
    SPECIES_CHOICES = (
        ("cat", "cat"),
        ("hedgehog", "hedgehog"),
    )
    species = models.CharField(max_length=100, help_text="Cat or Hedgehog?", choices=SPECIES_CHOICES)
    name = models.CharField(max_length=100)

    owner = models.ForeignKey(User, models.CASCADE)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {} {}'.format(self.species, self.name, self.owner_name)


class Lot(models.Model):
    name = models.ForeignKey(KittyandHedgehog, models.CASCADE)
    price = models.IntegerField(default=0)
    owner_name = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)


class Bet(models.Model):
    number_of_bet = models.IntegerField(default=0)
    owner_name = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return ' User - {} made a bet in {}  '.format(self.owner_name, self.number_of_bet)


class SelectBet(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    which_lot = models.ForeignKey(Lot, models.CASCADE)
    choice_of_user = models.ForeignKey(Bet, models.CASCADE)


    def __str__(self):
        return '{} {}'.format(self.user_who_make_lot, self.choice_of_user)
