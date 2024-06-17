from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_CHOICES = [(f'{h:02}:{m:02}', f'{h:02}:{m:02}') for h in range(24) for m in (0, 30)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Consent fields
    mobility_change = models.StringField(
        choices=['No', 'Yes'],
        widget=widgets.RadioSelect,
        label="Has your mobility behavior changed since you took the survey on electric vehicle charging preferences last year in September? Think about whether you use your car more or less, maybe due to a new job or other changes in your life.")

    departure_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="Please think about last year in September: On a typical day during the week (Monday to Friday), what was typically the time you (or someone in your household) left your home for the first time with the electric car?"
    )

    arrival_week = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you (or someone in your household) returned home for the final time (i.e., after which you no longer left your home in your EV)?"
    )

    departure_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="On a typical day of the weekend, what was typically the time you (or someone in your household) left your home for the first time with the electric car?"
    )

    arrival_weekend = models.StringField(
        choices=C.TIME_CHOICES,
        label="What was typically the time you (or someone in your household) returned home for the final time (i.e., after which you no longer left your home in your EV)?"
    )




class MobilityIntro(Page):
    form_model = 'player'
    form_fields = ['mobility_change', 'departure_week', 'arrival_week','departure_weekend', 'arrival_weekend']


page_sequence = [
    MobilityIntro
]