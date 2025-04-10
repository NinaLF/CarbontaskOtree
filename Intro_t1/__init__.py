from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Introt1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

   
# consent
    def make_field(label):
        return models.IntegerField(
        choices=[1,2,3,4,5,6,7,8,9,10],                           
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)

    subjectiveKnowledgePre = models.StringField(widget=widgets.RadioSelect,  
                                                 label= '  How knowledgeable do you feel about the effect of different behaviors on carbon footprints? That is, how much do you feel you know about how many CO<sub>2</sub> emissions are caused by differen actions?',
                                              choices=[['1', 'not much at all (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', '7'], ['8', '8'],['9', '9'], ['10', 'A great deal (10)'] ]   )
    

 # demographics
    age = models.IntegerField(label='How old are you', min=18, max=90)
    
    gender = models.StringField( label='How do you identify?',
        choices=[['Male', 'Male'], ['Female', 'Female'], 
        ['prefer not to answer/ diverse', 'prefer not to answer/ diverse']],
        widget = widgets.RadioSelect
    )
    education = models.StringField( label='What is your <b>highest education</b>?',
        choices=[['No formal education', 'No formal education'],
                ['Compulsory education', 'Compulsory education (secondary school)'], 
                 ['Further education', 'Further education'],
                 ['Higher education (Bachelor, Master, PhD)', 'Higher education (Bachelor, Master, PhD)']],
                 widget = widgets.RadioSelect
    )

    income = models.StringField(
                                label='How high is your <b>yearly personal income before tax </b>?',
        choices=[['< 18.000£', '< 18.000£'],
                 ['18.000£ to 23.000£', '18.000£ to 23.000£'], 
                 ['23.001£ to 30.500£', '23.001£ to 30.500£'], 
                 ['30.501£ to 45.000£', '30.500£ to 45.000£'], 
                 ['> 45.001£', '> 45.001£']],
                  widget = widgets.RadioSelect
    )
    polOrientation =  models.IntegerField( widget=widgets.RadioSelect,  
                                          choices=[['1', 'extremely left (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'extremely right (10)'] ] ) 
    
    climate_change_concern1 = make_field('I worry about the climate´s state.')
    climate_change_concern2 = make_field('Climate protection is important for our future.')
    climate_change_concern3 = make_field('We must protect the climate´s delicate equilibrium.')
    climate_change_concern4 = make_field('Climate change has severe consequences for humans and nature.')
    
    attention_check = make_field('To demonstrate that you are reading attentively, please mark the rightmost circle ("completely agree").')

    screenoutWV = models.BooleanField(initial=False)

    
    
# FUNCTIONS
# PAGES


class Consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']

    @staticmethod
    def vars_for_template(player: Player):
        # while testing this experiment do not check for prolificID (replace False with commented code) (make nolabel and prolificID Missing false for testing)
        return {
            "particpantlabel": player.participant.label,
            }


class Instructions(Page):
    form_model = 'player'

class Baseline(Page):
    form_model = 'player'
    form_fields= [ 'subjectiveKnowledgePre' ]
    
class Demographics(Page):
     form_model = 'player'
     form_fields= [ 'age', 'gender', 'education', 'polOrientation', 'income' ]

class ClimateConcern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'attention_check',  'climate_change_concern3', 'climate_change_concern4']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        correct = player.attention_check == 10
        if( correct == False ):
               player.screenoutWV = True


class Screenout(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return{
             'participantlabel':player.participant.label
        } 
    @staticmethod
    def is_displayed(player: Player):
        return (player.screenoutWV )


# Page sequence
page_sequence = [
    Consent, Demographics, ClimateConcern, Screenout, Baseline
    
]