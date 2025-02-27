import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Scalest1'
    NUM_ROUNDS = 1
    PLAYERS_PER_GROUP = None

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass



#region functions
def make_likert10():
        return models.IntegerField(
            choices=[1,2,3,4,5,6,7,8,9,10],
            widget=widgets.RadioSelect,
            label= 'label'
        )

def make_likert9():
        return models.IntegerField(
            choices=[-1,0,1,2,3,4,5,6,7],
            widget=widgets.RadioSelect,
            label= 'label'
        )

def make_likert5():
        return models.IntegerField(
            choices=[1,2,3,4,5],
            widget=widgets.RadioSelect,
            label= 'label'
        )
def make_likert4():
        return models.IntegerField(
            choices=[1,2,3,4],
            widget=widgets.RadioSelect,
            label= 'label'
        )

#endregion



#endregion
def make_likert_n(n):
    nchoices = list(range(1, n+1))
    return models.IntegerField(
        choices=nchoices,
        widget=widgets.RadioSelect,
)



class Player(BasePlayer):

    def make_field(label):
        return models.IntegerField(
        choices=[['10', 'Agree completely (10)'], ['9', '9'],['8', '8'],['7', '7'],
                 ['6', '6'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )
  

    ## trust in own and foreign governments
    
    pit1 = make_likert10()
    pit2 = make_likert10()


    ### Belief
    belief1Happening= make_likert_n(10)

    beliefHuman1 = make_likert_n(10)
    beliefHuman2 = make_likert_n(10)
    beliefHuman3 = make_likert_n(10)

    beliefConseqences1 = make_likert_n(10)
    beliefConseqences2 = make_likert_n(10)
    beliefConseqences3 = make_likert_n(10)


    ## behaviors


    footprint_food_overall1 =  models.StringField(widget=widgets.RadioSelect , 
                                                  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label='Rindfleisch')
    
    footprint_food_overall2 =  models.StringField(widget=widgets.RadioSelect,
                                                    choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label = 'Lamm oder Hammelfleisch' )
    
    footprint_food_overall3 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Schweinefleisch')
    
    footprint_food_overall4 =  models.StringField(widget=widgets.RadioSelect ,   choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Geflügel (z.B. Huhn)')
    
    footprint_food_overall5 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ] ] , label= 'Fisch')
    
    footprint_food_overall6 =  models.StringField(widget=widgets.RadioSelect ,  choices = [
        ['never', 'Nie'],
        ['oncePerMonth', 'Einmal pro Monat' ],
        ['2-3PerMonth',  '2-3 Mal pro Monat'],
        ['oncePerWeek',  'Einmal pro Woche' ],
        ['2-3PerWeek', '2-3 Mal pro Woche' ],
        ['4-6PerWeek',  '4-6 Mal pro Woche' ],
        ['oncePerDay',  'Einmal pro Tag'  ],
        ['MultiplePerDay', '2 oder mehrmals pro Tag'  ]] , label= 'Milchprodukte (z.B. Milch oder Käse)' )

    # further behavior items
    footprint_flying_short = models.IntegerField(min=0, max= 300, 
                                             label = "Wie viele <b> Kurzstreckenflüge (<3 Stunden)</b> haben Sie in den letzten zwei Jahren durchschnittlich unternommen? <i> Ein Hin- und Rückflug zählt als zwei Flüge. Wenn Sie also von San Francisco nach Los Angeles und zurück geflogen sind, zählt das als 2 Flüge. </i>")
    
    footprint_flying_mid = models.IntegerField(min=0, max= 300 , 
                                           label = "Wie viele <b> Mittelstreckenflüge (3-6 Stunden) </b> haben Sie in den letzten zwei Jahren durchschnittlich unternommen? <i> Ein Hin- und Rückflug zählt als zwei Flüge. Wenn Sie also von New York nach San Francisco und zurück geflogen sind, zählt das als 2 Flüge. </i>")
    
    footprint_flying_long = models.IntegerField(min=0, max= 300,
                                             label= "Wie viele <b> Langstreckenflüge (>6 Stunden) </b> haben Sie in den letzten zwei Jahren durchschnittlich unternommen? <i> Ein Hin- und Rückflug zählt als zwei Flüge. Wenn Sie also von Miami nach London und zurück geflogen sind, zählt das als 2 Flüge. </i>")
    
    footprint_commute_car =  models.IntegerField(min=0, max=200 , 
                                             label= "Wie viele Kilometer haben Sie an einem typischen Arbeitstag in den letzten 2 Wochen mit dem Auto zur Arbeit zurückgelegt (als Fahrer oder Beifahrer)? <br> Bitte geben Sie die durchschnittlichen Kilometer <b> pro Arbeitstag </b> an")

    
    footprint_commute_car =  models.IntegerField( min=0, max=200 , 
                                                 label= "Wie viele Kilometer sind Sie an einem typischen Arbeitstag in den letzten 2 Wochen mit dem Auto gependelt (als Fahrer oder Beifahrer), um zur Arbeit zu gelangen? <br> Bitte geben Sie die durchschnittlichen Kilometer <b> pro Arbeitstag </b> an")
                                                
    footprint_commute_car2 =  models.IntegerField( min=0, max=200 , 
                                                 label= "Wie viele Kilometer sind Sie durchschnittlich für andere Zwecke (als Fahrer oder Beifahrer) für Freizeitaktivitäten, Besorgungen/Einkäufe oder andere Gründe gefahren? <br> Bitte geben Sie die durchschnittlichen Kilometer <b> pro Tag </b> an")
                                                
    footprint_commute_car_type=  models.StringField( label = 'Welche Art von Kraftstoff nutzt Ihr Auto?', widget=widgets.RadioSelectHorizontal ,
                                                    choices = [  ['none', 'Ich habe kein Auto' ],
                                                        ['Electric_green',  'Elektrisch (grüne Energie)'  ],
                                                        ['Eletric_conv', 'Elektrisch (konventionelle Energie)' ],
                                                        ['Biogas', 'Biogas' ],
                                                        ['NaturalGas',  'Erdgas' ],
                                                        ['Diesel', 'Benzin/Diesel/Hybrid' ]]
                                                   )
    footprint_commute_pt =  models.StringField(label="Wie viele Kilometer sind Sie in den letzten 2 Wochen pro Woche mit öffentlichen Verkehrsmitteln (Zug, Bus usw.) oder einem E-Bike gependelt? Bitte berechnen Sie alle privaten Fahrten einschließlich des Arbeitswegs, aber keine Geschäftsreisen <b>basierend auf einer Woche.</b>" ,
                                                widget=widgets.RadioSelectHorizontal, 
                                               choices = [ ['lessA', '1 - 39 Meilen' ],
                                               ['AtoB',  '40 - 50 Meilen' ],
                                               ['BtoC', '50 -149 Meilen'  ],
                                               ['CtoD', '150 - 224 Meilen' ],
                                               ['DtoE',  '225 - 370 Meilen' ],
                                               ['most', 'mehr als 370 Meilen'  ] ] )

    footprint_regional =  models.StringField(label = 'Welcher Prozentsatz Ihrer Lebensmittel ist regional (aus Ihrem Land oder Ihrer Region, nicht importiert)?', widget=widgets.RadioSelectHorizontal ,
                                             choices = [  
                                                  [ 'less_than' , 'Weniger als ein Viertel'],
                                                        ['quarter' , 'Etwa ein Viertel'  ],
                                                        [  'half' , 'Etwa die Hälfte'  ],
                                                        [  'three_quarter' , 'Etwa drei Viertel' ],
                                                        [  'more_than' , 'Der größte Teil ist regional'] ]
                                             )                                       
                                                

   

    footprint_laundry1 =  models.IntegerField( min=0, max=10 , 
                                                 label= "Wie oft haben Sie in den letzten 4 Wochen durchschnittlich Ihre Wäsche im Trockner getrocknet? <br> Bitte geben Sie die durchschnittliche Anzahl an <b> pro Woche </b>")
    footprint_laundry2 =  models.IntegerField( min=0, max=10 , 
                                                 label= "Wie oft haben Sie in den letzten 4 Wochen durchschnittlich Ihre Wäsche luftgetrocknet? <br> Bitte geben Sie die durchschnittliche Anzahl an <b> pro Woche </b>")

    ## policy scales
    policy_commute =	'Erhöhung oder Einführung von Steuern auf Kraftstoff für Fahrzeuge (z. B. Diesel und Benzin). '
    policy_flying =	'Erhöhung oder Einführung von Steuern auf Flugreisen.'
    policy_electricity ='Erhöhung oder Einführung von Steuern auf fossile Brennstoffe als Energiequelle (z. B. Gas, Öl und Kohle).'
    policy_diet =	'Erhöhung oder Einführung von Steuern auf rotes Fleisch (z. B. Rindfleisch, Lammfleisch, Kalbfleisch).'
    policy_recycling =	'Erhöhung oder Einführung von Steuern auf nicht wiederverwertbare (=nicht recyclebare) Materialien.'
    policy_regional =	'Erhöhung oder Einführung von Steuern auf Lebensmittelprodukte, die per Flugzeug importiert werden.'
    

 # demographics
    age = models.IntegerField(label='Wie alt sind Sie', min=18, max=90)
    
    gender = models.StringField( label='Welchem Geschlecht fühlen Sie sich zugehörig?',
        choices=[['Male', 'Männlich'], ['Female', 'Weiblich'], 
        ['prefer not to answer/ diverse', 'divers/keine Angabe']],
        widget = widgets.RadioSelect
    )
    education = models.StringField( label='Was ist Ihr höchster Bildungsabschluss?',
        choices=[['No formal education', 'keine formelle Bildung abgeschlossen'],
                ['Compulsory education', 'obligatorische Schule'], 
                 ['Further education', 'Sekundarstufe: Matura / Berufsbildung / Allgemeinbildung '],
                 ['Higher education (Bachelor, Master, PhD)', 'höhere Berufsbildung: Hochschulabschluss / Bachelor / Master / Doktor']],
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

    climate_change_concern1 = make_field('Ich mache mir Sorgen, dass sich das Klima verändert. ')
    climate_change_concern2 = make_field('Klimaschutz ist wichtig für unsere Zukunft.')
    climate_change_concern3 = make_field('Wir müssen das Gleichgewicht des Klimas schützen.')
    climate_change_concern4 = make_field('Der Klimawandel hat schwerwiegende Folgen für Mensch und Natur.')
    
## https://www.researchgate.net/publication/29870461_Need_for_cognition_Eine_Skala_zur_Erfassung_von_Engagement_und_Freude_bei_Denkaufgaben_Presentation_and_validation_of_a_German_version_of_the_Need_for_Cognition_Scale
    nfc_1 = make_field('Ich würde komplizierte Probleme einfachen Problemen vorziehen.')
    nfc_2 = make_field('Ich trage nicht gerne die Verantwortung für eine Situation, die sehr viel Denken erfordert.')
    nfc_3 = make_field('Denken entspricht nicht dem, was ich unter Spaß verstehe.') # reverse coded
    nfc_4 = make_field('Ich würde lieber etwas tun, das wenig Denken erfordert, als etwas, das mit Sicherheit meine Denkfähigkeit herausfordert.') # reverse coded
    nfc_5 = make_field('Die Aufgabe, neue Lösungen für Probleme zu finden, macht mir wirklich Spaß.')
    nfc_6 = make_field('Ich würde lieber eine Aufgabe lösen, die Intellegenz erfordert, schwierig und bedeutend ist, als eine Aufgabe, die zwar irgendwie wichtig ist, aber nicht viel Nachdenken erfordert.')

    numeracy1 = models.IntegerField(min=0, max=100)


    UnitUnderstanding =  models.IntegerField( widget=widgets.RadioSelect,  label="Wie schwierig war es für Sie, „kg CO<sub>2</sub> “ zu verstehen und sich vorzustellen? ",
                                          choices=[['1', ' gar nicht schwierig (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'sehr schwierig(10)'] ] ) 
    
    generalFeedback = models.StringField(max_length=3000, blank=True, label='Haben Sie irgendwelche Kommentare, Rückmeldungen oder Ideen? Danke für Ihre Ideen und Ihr Feedback.')
    
    

    subjectiveKnowledgePost = models.IntegerField(widget=widgets.RadioSelect,  label= 'Wie kenntnisreich fühlen Sie sich über die Auswirkungen verschiedener Verhaltensweisen auf den CO<sub>2</sub>-Fußabdruck? Das heißt, wie viel denken Sie wissen Sie, über die Menge an CO<sub>2</sub>-Emissionen, die durch verschiedene Handlungen verursacht wird?',
                                              choices=[['1', 'überhaupt nicht viel (1)'], ['2', '2'],['3', '3'],['4', '4'],
                                                       ['5', '5'], ['6', '6'],  ['7', '7'], ['8', '8'],['9', '9'], ['10', 'sehr viel (10)'] ]   )




    
   

# < 18.000£          > 45.001£ 18.000£ to 23.000£ 23.001£ to 30.500£ 30.501£ to 45.000£     


class ClimateConcern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3', 'climate_change_concern4']

    
class BehaviorsFood(Page):
    form_model = 'player'
    form_fields= ['footprint_food_overall1', 'footprint_food_overall2', 'footprint_food_overall3', 'footprint_food_overall4', 'footprint_food_overall5', 'footprint_food_overall6']
    
    
class BehaviorsTransport(Page):
    form_model = 'player'
    form_fields= ['footprint_commute_car', 'footprint_commute_car2',  'footprint_commute_car_type', 'footprint_commute_pt']
    

class BehaviorLaundry(Page):
    form_model = 'player'
    form_fields= ['footprint_laundry1', 'footprint_laundry2'] 
     
    
class Trust(Page):
    form_model = 'player'
    form_fields= ['pit1', 'pit2']
    form_field_labels = ['lokale Regierung', 'nationale Regierung']

class NFC(Page):
    form_model = 'player'
    form_fields= ['nfc_1', 'nfc_2', 'nfc_3', 'nfc_4', 'nfc_5', 'nfc_6' ]

class Numeracy(Page):
    form_model = 'player'
    form_fields= ['numeracy1']
   

class policyScales(Page):
    form_model = 'player'
    form_fields= ['policy_commute', 'policy_flying', 'policy_electricity', 'policy_diet', 'policy_recycling', 'policy_regional' ]
   
class unit(Page):
    form_model = 'player'
    form_fields= ['UnitUnderstanding' , 'generalFeedback']
    
class Demographics(Page):
     form_model = 'player'
     form_fields= [ 'age', 'gender', 'education', 'income', 'polOrientation' , 'generalFeedback']
       

class End(Page):
     form_model = 'player'
       



page_sequence = [ # BehaviorsFlying,  BehaviorsFood2,BehaviorsTransport, BehaviorsFood,
                  ClimateConcern, policyScales,  BehaviorLaundry, BehaviorsTransport, BehaviorsFood, Trust,  Numeracy, NFC,   Demographics, End 
    # Belief,  Belief1, CCEmotion,
     #            BehaviorsFood, BehaviorsFood2, BehaviorsTransport, BehaviorsFlying, 
             #    PITrust, IBValues ,
              #   policyScales,
               #  DemographicsEnd
                 ]