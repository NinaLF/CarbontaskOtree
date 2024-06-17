from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Consent fields
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)


class introduction_consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "participantlabel": player.participant.label,
        }  # add ?participant_label={{%PROLIFIC_PID%}} to link on prolific


page_sequence = [
    introduction_consent
]
