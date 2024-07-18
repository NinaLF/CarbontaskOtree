from otree.api import *
from datetime import datetime

def convert_to_ampm(hour):
    return datetime.strptime(f'{hour:02}:00', '%H:%M').strftime('%I:%M %p')

class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_CHOICES = [(convert_to_ampm(h), convert_to_ampm(h)) for h in range(24)]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    departure_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you or someone in your household left your home for the first time with the electric car?"
    )

    arrival_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you or someone in your household returned home for the final time?"
    )

    departure_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you or someone in your household left your home for the first time with the electric car?"
    )

    arrival_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you or someone in your household returned home for the final time?"
    )

class MobilityIntro(Page):
    form_model = 'player'
    form_fields = ['departure_week', 'arrival_week', 'departure_weekend', 'arrival_weekend']

page_sequence = [
    MobilityIntro
]
