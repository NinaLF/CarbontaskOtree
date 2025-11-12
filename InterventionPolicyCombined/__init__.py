from otree.api import *
from otree.api import BaseGroup
from statistics import mean

doc = """
intervention
"""

class Constants(BaseConstants):
    name_in_url = 'interventionCombined'
    players_per_group = None
    num_rounds = 1
    
    behavior_data = {
        "<b>Diet </b> <br> Based on an average adult's caloric needs for the duration of one year": {
            "Meat-based": 2.206,
            "Vegetarian": 1.338
        },
        "<b>Heating</b> <br> Space heating and hot water for one person and year": {
            "via heat pump": 0.624,
            "using mains gas (most common)": 1.560
        },
        "<b>Recycling</b>  <br> Materials such as paper, glass, metals for one year": {
            "Does not recycle": 0.0575,
            "Recycles": 0.0
        },
        "<b>Food</b>  <br> Foods and beverages bought and consumed for one year": {
            "More than 3/4 is regional": 0.0,
            "More than 3/4 is imported": 0.44
        },
        "<b>Commute</b> <br> 12.5 miles to and from work every day (one trip = 6.25 miles), 5 days a week for 48 weeks per year": {
            "By bus": 0.471,
            "By personal car": 1.595
        },
        "<b>Travel to go on vacation</b>": {
            "1x round-trip flight 3–6 hours (=2 flights)": 0.6213,
            "Via train (does not fly)": 0.0076
        }
    }

    # POLICY DATA (MtCO2 savings per year)
    policy_data = {
        "Electricity (carbon price on power generation)": {
            "Implemented": 11.1,
            "No tax": 0.0
        },
        "Road fuels (carbon price on petrol & diesel)": {
            "Implemented": 11.8,
            "No tax": 0.0
        },
        "Aviation (carbon price on air travel)": {
            "Implemented": 2.0,
            "No tax": 0.0
        },
        "Food (carbon price on meat & dairy)": {
            "Implemented": 6.8,
            "No tax": 0.0
        },
        "Imported foods (carbon price on food miles)": {
            "Implemented": 0.7,
            "No tax": 0.0
        },
        "Waste (carbon price on landfill)": {
            "Implemented": 0.3,
            "No tax": 0.0
        }
    }

    control_data = {
   
      
         "Streckendistanz von Frankfurt (Fahrstrecke nicht Luftlinie)": {
                "Frankfurt-Düsseldorf": 226,
                "Frankfurt-Berlin ": 548
            },
            "Streckendistanz von Berlin (Fahrstrecke nicht Luftlinie)": {
                "Berlin-Saarbrücken": 723,
                "Berlin-Köln": 575
            },
            "Streckendistanz von München (Fahrstrecke nicht Luftlinie)": {
                "München-Hamburg": 793,
                "München-Osnabrück": 641
            },
            "Streckendistanz von Hannover (Fahrstrecke nicht Luftlinie)": {
                "Hannover-Dresden": 364,
                "Hannover-Frankfurt": 569
            },
             "Streckendistanz von Stuttgart (Fahrstrecke nicht Luftlinie)": {
                "Stuttgart-Bonn": 350,
                "Stuttgart-Erfurt": 339
            },
             "Streckendistanz von Wiesbaden (Fahrstrecke nicht Luftlinie)": {
                "Wiesbaden-Nürnberg": 253,
                "Wiesbaden-Berlin": 573
            }
    }






class Subsession(BaseSubsession):


    def get_completed_count(self):
        players = self.get_players()
        return sum(1 for p in players if p.participant.group_assignment == "policy" )

  
class Group(BaseGroup):
    pass

def creating_session(subsession:Subsession):

    import itertools
    group_assignment = itertools.cycle(["active", "combined", "policyG","control"])
    for player in subsession.get_players():
        if subsession.round_number == 1:
            player.participant.group_assignment = next(group_assignment)


class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
        choices=[['10', 'Agree completely (10)'], ['9', '9'],['8', '8'],['7', '7'],
                 ['6', '6'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

    # Individual-level behaviors
    diet= models.StringField(choices = ["Meat-based","Vegetarian"] )
    laundry= models.StringField(choices =["via heat pump","mains gas heating"] )
    recycling= models.StringField(choices =["Does Not Recycle","Recycles"])
    food= models.StringField(choices =["Only Regional","Regional and Imported"])
    commute= models.StringField(choices =["By Bus","By Car"])
    vacation= models.StringField(choices = ["Flies Twice a Year","via train (does not fly)"])

    # policies
    electricity = models.StringField(choices = ["Implemented", "No tax"  ])
    road_fuels = models.StringField(choices =[ "No tax","Implemented"  ])
    aviation = models.StringField(choices = ["Implemented", "No tax" ] )
    food_policy =  models.StringField(choices =[ "No tax" ,"Implemented" ])
    imports = models.StringField(choices = [ "No tax", "Implemented"])
    waste = models.StringField(choices = ["Implemented", "No tax" ] )

    controlQuestion1 = models.StringField(label="How much tons CO<sub>2</sub> does the highest combination save?",
                                          choices=["1.22", "2.02", "3.66","4.04", "4.44" ])
    
    controlQuestion2 = models.StringField(label="Which behavior change saves the most emissions?",
                                          choices=["Changing to a plant-based diet", "Changing to heat pump", "Changing to recycling","Changing to mainly regional food", "Changing to bus commute", "Changing to taking the train"  ] )
    
    controlQuestion1pol = models.StringField(label="Which carbon tax targeting a behavior contributes most to the overall emission savings ?",
                                          choices=["Carbon tax on food (red meat)", "Carbon tax on electricity (power generation)", "Carbon tax on waste (landfill)","Carbon tax on imported foods", "Carbon tax on road fuels", "Carbon tax on private aviation"  ] )
    


    pretest_engaging = make_field('engaging')
    pretest_interesting = make_field('interesting')
    pretest_understandable = make_field('understandable')
    pretest_knowledge = make_field('helpful to increase my knowledge')


# PAGES
class TaskInfo(Page):
    pass


    
class CombinedIntro(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "combined"
    

class Combined1(Page):
 

    def is_displayed(self):
        return self.participant.group_assignment == "combined"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'behavior_data': Constants.behavior_data,
            'policy_data': Constants.policy_data,
            'selections': self.participant.vars.get('selections', {}),
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint': self.participant.vars.get('total_footprint', 0.0),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }
    
class Combined2(Page):
    def is_displayed(self):
        return self.participant.group_assignment == "combined"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'behavior_data': Constants.behavior_data,
            'policy_data': Constants.policy_data,
            'selections': self.participant.vars.get('selections', {}),
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint': self.participant.vars.get('total_footprint', 0.0),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }


    
class Combined3(Page):
    form_model = "player"
    form_fields= [ 'controlQuestion1', 'controlQuestion2', 'controlQuestion1pol' ]
    def is_displayed(self):
        return self.participant.group_assignment == "combined"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'behavior_data': Constants.behavior_data,
            'policy_data': Constants.policy_data,
            'selections': self.participant.vars.get('selections', {}),
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint': self.participant.vars.get('total_footprint', 0.0),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }
    
class PolicyIntro(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "policyG"
    

class Policy1(Page):
 
    def is_displayed(self):
        return self.participant.group_assignment == "policyG"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'policy_data': Constants.policy_data,
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }
    
class Policy2(Page):
    form_model = "player"
    form_fields= [ 'controlQuestion1pol' ]

    def is_displayed(self):
        return self.participant.group_assignment == "policyG"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'policy_data': Constants.policy_data,
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }
class Policy3(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "policyG"

    # Don't return a key named 'form' from vars_for_template
    def vars_for_template(self):
        return {
            'policy_data': Constants.policy_data,
            'selections_policy': self.participant.vars.get('selections_policy', {}),
            'total_footprint2': self.participant.vars.get('total_footprint2', 0.0),
        }

class Transition(Page):
    pass

class PretestQuestions(Page):
    def is_displayed(self):
        return self.participant.group_assignment != "control"
    
    form_model = 'player'
    form_fields= ['pretest_engaging', 'pretest_interesting', 'pretest_understandable', 'pretest_knowledge' ]



class Control(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'control_data': Constants.control_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class Control2(Page):
    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'control_data': Constants.control_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class Control3(Page):
  
    def is_displayed(self):
        return self.participant.group_assignment == "control"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.control_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})

        return {
            'control_data': Constants.control_data
    
        }
    
class ActiveSamplingIntro(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "active"
    

class ActiveSampling(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
class ActiveSamplingTree(Page):

    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class ActiveSampling2(Page):
    form_model = "player"
    form_fields= [ 'controlQuestion1', 'controlQuestion2' ]
  
    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
class ActiveSampling3(Page):
  
    def is_displayed(self):
        return self.participant.group_assignment == "active"

    def before_next_page(self, timeout_happened=False):
        total_footprint = 0
        
        selections = {}

        # Iterate through each behavior to calculate the total footprint and store selections
        for behavior, options in Constants.behavior_data.items():
            selected_option = selections.get(behavior.lower(), None)
            if selected_option is not None:
                total_footprint += options.get(selected_option, 0)

        # Store the total footprint and selections in participant variables
        self.participant.vars['total_footprint'] = total_footprint
        self.participant.vars['selections'] = selections

    def vars_for_template(self):
        # Get stored selections or use 'Not selected' as default
        selections = self.participant.vars.get('selections', {})
        diet_selection = selections.get('diet', 'Not selected')
        commute_selection = selections.get('commute', 'Not selected')

        return {
            'behavior_data': Constants.behavior_data,
            'diet_select': diet_selection,
            'commute_select': commute_selection
        }
    
page_sequence = [CombinedIntro, Combined1, Combined2 , Combined3,  
                 ActiveSamplingIntro, ActiveSampling, ActiveSampling3, ActiveSampling2 ,
                 PolicyIntro, Policy1,  Policy3, Policy2,
                 Control, Control2, Control3

                 
                 ]


