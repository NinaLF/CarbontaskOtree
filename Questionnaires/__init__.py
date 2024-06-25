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
        choices=['1', '2', '3', '4', '5', '7', '8'],
        widget=widgets.RadioSelect,
        label="How many spontaneous trips do you make in one week in addition to those which you have indicated in the trip diary?")

    enough_options = models.StringField(
        choices=['No', 'Yes, I wanted to indicate more trips than were possible.'],
        widget=widgets.RadioSelect,
        label="Did you encounter any problems where you wanted to indicate more trips on a day than were possible?"
    )

    general_comment = models.LongStringField(
        label="Please describe whether you had any problems or difficulties filling in this survey. This will help us to make it better."
    )


class Spontaneous(Page):
    form_model = 'player'
    form_fields = ['spontaneous_trips']


class Comments(Page):
    form_model = 'player'
    form_fields = ['enough_options', 'general_comment']


page_sequence = [
    Spontaneous,
    Comments
]
