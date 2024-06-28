from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    spontaneous_trips = models.StringField(
        choices=['0', '1', '2', '3', '4', '5', '7', '8'],
        label="How many spontaneous trips do you typically make in one week in addition to the planned trips recorded in your trip diary?")


class Spontaneous(Page):
    form_model = 'player'
    form_fields = ['spontaneous_trips']


page_sequence = [
    Spontaneous
]
