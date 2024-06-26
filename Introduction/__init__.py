from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_CHOICES = [(f'{h:02}:00', f'{h:02}:00') for h in range(24)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Consent fields

    departure_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="On a typical day during the week (Monday to Friday), what is typically the time you (or someone in your household) leave your home for the first time with the electric car?"
    )

    arrival_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="What is typically the time you (or someone in your household) return home for the final time (i.e., after which you no longer leave your home in your EV)?"
    )

    departure_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="On a typical day of the weekend, what is typically the time you (or someone in your household) leave your home for the first time with the electric car?"
    )

    arrival_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="What is typically the time you (or someone in your household) return home for the final time (i.e., after which you no longer leave your home in your EV)?"
    )




class MobilityIntro(Page):
    form_model = 'player'
    form_fields = ['departure_week', 'arrival_week','departure_weekend', 'arrival_weekend']


page_sequence = [
    MobilityIntro
]
