from otree.api import *
import json

doc = """
Trip diary where participants can add trips dynamically.
"""


class C(BaseConstants):
    NAME_IN_URL = 'trip_diary'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_CHOICES = [(f'{h:02}:{m:02}', f'{h:02}:{m:02}') for h in range(24) for m in (0, 30)]
    DAYS = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    DAYS_tue = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    DAYS_wed = ['Thursday', 'Friday', 'Saturday', 'Sunday']
    DAYS_thu = ['Friday', 'Saturday', 'Sunday']
    DAYS_fri = ['Saturday', 'Sunday']
    DAYS_sat = ['Sunday']



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Tuesday = models.BooleanField(blank=True, initial=False)
    Wednesday = models.BooleanField(blank=True, initial=False)
    Thursday = models.BooleanField(blank=True, initial=False)
    Friday = models.BooleanField(blank=True, initial=False)
    Saturday = models.BooleanField(blank=True, initial=False)
    Sunday = models.BooleanField(blank=True, initial=False)

    Wednesday_tue = models.BooleanField(blank=True, initial=False)
    Thursday_tue = models.BooleanField(blank=True, initial=False)
    Friday_tue = models.BooleanField(blank=True, initial=False)
    Saturday_tue = models.BooleanField(blank=True, initial=False)
    Sunday_tue = models.BooleanField(blank=True, initial=False)

    Thursday_wed = models.BooleanField(blank=True, initial=False)
    Friday_wed = models.BooleanField(blank=True, initial=False)
    Saturday_wed = models.BooleanField(blank=True, initial=False)
    Sunday_wed = models.BooleanField(blank=True, initial=False)

    Friday_thu = models.BooleanField(blank=True, initial=False)
    Saturday_thu = models.BooleanField(blank=True, initial=False)
    Sunday_thu = models.BooleanField(blank=True, initial=False)

    Saturday_fri = models.BooleanField(blank=True, initial=False)
    Sunday_fri = models.BooleanField(blank=True, initial=False)

    Sunday_sat = models.BooleanField(blank=True, initial=False)

# Monday
    mo_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    mo_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    mo_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_1 = models.StringField(blank=True, default='')
    mo_distance_1 = models.StringField(blank=True, default='')

    mo_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_2 = models.StringField(blank=True, default='')
    mo_distance_2 = models.StringField(blank=True, default='')

    mo_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_3 = models.StringField(blank=True, default='')
    mo_distance_3 = models.StringField(blank=True, default='')

    mo_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_4 = models.StringField(blank=True, default='')
    mo_distance_4 = models.StringField(blank=True, default='')

    mo_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_5 = models.StringField(blank=True, default='')
    mo_distance_5 = models.StringField(blank=True, default='')

    mo_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_6 = models.StringField(blank=True, default='')
    mo_distance_6 = models.StringField(blank=True, default='')

    mo_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_7 = models.StringField(blank=True, default='')
    mo_distance_7 = models.StringField(blank=True, default='')

    mo_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_8 = models.StringField(blank=True, default='')
    mo_distance_8 = models.StringField(blank=True, default='')

    mo_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_9 = models.StringField(blank=True, default='')
    mo_distance_9 = models.StringField(blank=True, default='')

    mo_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    mo_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    mo_duration_10 = models.StringField(blank=True, default='')
    mo_distance_10 = models.StringField(blank=True, default='')


# Tuesday
    tue_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    tue_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    tue_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_1 = models.StringField(blank=True, default='')
    tue_distance_1 = models.StringField(blank=True, default='')

    tue_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_2 = models.StringField(blank=True, default='')
    tue_distance_2 = models.StringField(blank=True, default='')

    tue_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_3 = models.StringField(blank=True, default='')
    tue_distance_3 = models.StringField(blank=True, default='')

    tue_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_4 = models.StringField(blank=True, default='')
    tue_distance_4 = models.StringField(blank=True, default='')

    tue_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_5 = models.StringField(blank=True, default='')
    tue_distance_5 = models.StringField(blank=True, default='')

    tue_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_6 = models.StringField(blank=True, default='')
    tue_distance_6 = models.StringField(blank=True, default='')

    tue_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_7 = models.StringField(blank=True, default='')
    tue_distance_7 = models.StringField(blank=True, default='')

    tue_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_8 = models.StringField(blank=True, default='')
    tue_distance_8 = models.StringField(blank=True, default='')

    tue_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_9 = models.StringField(blank=True, default='')
    tue_distance_9 = models.StringField(blank=True, default='')

    tue_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    tue_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    tue_duration_10 = models.StringField(blank=True, default='')
    tue_distance_10 = models.StringField(blank=True, default='')


# Wednesday
    wed_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    wed_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    wed_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_1 = models.StringField(blank=True, default='')
    wed_distance_1 = models.StringField(blank=True, default='')

    wed_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_2 = models.StringField(blank=True, default='')
    wed_distance_2 = models.StringField(blank=True, default='')

    wed_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_3 = models.StringField(blank=True, default='')
    wed_distance_3 = models.StringField(blank=True, default='')

    wed_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_4 = models.StringField(blank=True, default='')
    wed_distance_4 = models.StringField(blank=True, default='')

    wed_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_5 = models.StringField(blank=True, default='')
    wed_distance_5 = models.StringField(blank=True, default='')

    wed_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_6 = models.StringField(blank=True, default='')
    wed_distance_6 = models.StringField(blank=True, default='')

    wed_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_7 = models.StringField(blank=True, default='')
    wed_distance_7 = models.StringField(blank=True, default='')

    wed_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_8 = models.StringField(blank=True, default='')
    wed_distance_8 = models.StringField(blank=True, default='')

    wed_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_9 = models.StringField(blank=True, default='')
    wed_distance_9 = models.StringField(blank=True, default='')

    wed_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    wed_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    wed_duration_10 = models.StringField(blank=True, default='')
    wed_distance_10 = models.StringField(blank=True, default='')


# Thursday
    thu_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    thu_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    thu_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_1 = models.StringField(blank=True, default='')
    thu_distance_1 = models.StringField(blank=True, default='')

    thu_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_2 = models.StringField(blank=True, default='')
    thu_distance_2 = models.StringField(blank=True, default='')

    thu_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_3 = models.StringField(blank=True, default='')
    thu_distance_3 = models.StringField(blank=True, default='')

    thu_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_4 = models.StringField(blank=True, default='')
    thu_distance_4 = models.StringField(blank=True, default='')

    thu_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_5 = models.StringField(blank=True, default='')
    thu_distance_5 = models.StringField(blank=True, default='')

    thu_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_6 = models.StringField(blank=True, default='')
    thu_distance_6 = models.StringField(blank=True, default='')

    thu_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_7 = models.StringField(blank=True, default='')
    thu_distance_7 = models.StringField(blank=True, default='')

    thu_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_8 = models.StringField(blank=True, default='')
    thu_distance_8 = models.StringField(blank=True, default='')

    thu_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_9 = models.StringField(blank=True, default='')
    thu_distance_9 = models.StringField(blank=True, default='')

    thu_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    thu_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    thu_duration_10 = models.StringField(blank=True, default='')
    thu_distance_10 = models.StringField(blank=True, default='')


# Friday
    fri_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    fri_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    fri_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_1 = models.StringField(blank=True, default='')
    fri_distance_1 = models.StringField(blank=True, default='')

    fri_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_2 = models.StringField(blank=True, default='')
    fri_distance_2 = models.StringField(blank=True, default='')

    fri_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_3 = models.StringField(blank=True, default='')
    fri_distance_3 = models.StringField(blank=True, default='')

    fri_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_4 = models.StringField(blank=True, default='')
    fri_distance_4 = models.StringField(blank=True, default='')

    fri_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_5 = models.StringField(blank=True, default='')
    fri_distance_5 = models.StringField(blank=True, default='')

    fri_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_6 = models.StringField(blank=True, default='')
    fri_distance_6 = models.StringField(blank=True, default='')

    fri_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_7 = models.StringField(blank=True, default='')
    fri_distance_7 = models.StringField(blank=True, default='')

    fri_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_8 = models.StringField(blank=True, default='')
    fri_distance_8 = models.StringField(blank=True, default='')

    fri_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_9 = models.StringField(blank=True, default='')
    fri_distance_9 = models.StringField(blank=True, default='')

    fri_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    fri_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    fri_duration_10 = models.StringField(blank=True, default='')
    fri_distance_10 = models.StringField(blank=True, default='')


# Saturday
    sat_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    sat_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    sat_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_1 = models.StringField(blank=True, default='')
    sat_distance_1 = models.StringField(blank=True, default='')

    sat_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_2 = models.StringField(blank=True, default='')
    sat_distance_2 = models.StringField(blank=True, default='')

    sat_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_3 = models.StringField(blank=True, default='')
    sat_distance_3 = models.StringField(blank=True, default='')

    sat_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_4 = models.StringField(blank=True, default='')
    sat_distance_4 = models.StringField(blank=True, default='')

    sat_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_5 = models.StringField(blank=True, default='')
    sat_distance_5 = models.StringField(blank=True, default='')

    sat_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_6 = models.StringField(blank=True, default='')
    sat_distance_6 = models.StringField(blank=True, default='')

    sat_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_7 = models.StringField(blank=True, default='')
    sat_distance_7 = models.StringField(blank=True, default='')

    sat_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_8 = models.StringField(blank=True, default='')
    sat_distance_8 = models.StringField(blank=True, default='')

    sat_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_9 = models.StringField(blank=True, default='')
    sat_distance_9 = models.StringField(blank=True, default='')

    sat_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sat_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sat_duration_10 = models.StringField(blank=True, default='')
    sat_distance_10 = models.StringField(blank=True, default='')


# Sunday
    sun_first_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Started day at:"
    )
    sun_last_trip = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        label="Ended day at:"
    )

    sun_additional_trip_1 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_1 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_1 = models.StringField(blank=True, default='')
    sun_distance_1 = models.StringField(blank=True, default='')

    sun_additional_trip_2 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_2 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_2 = models.StringField(blank=True, default='')
    sun_distance_2 = models.StringField(blank=True, default='')

    sun_additional_trip_3 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_3 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_3 = models.StringField(blank=True, default='')
    sun_distance_3 = models.StringField(blank=True, default='')

    sun_additional_trip_4 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_4 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_4 = models.StringField(blank=True, default='')
    sun_distance_4 = models.StringField(blank=True, default='')

    sun_additional_trip_5 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_5 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_5 = models.StringField(blank=True, default='')
    sun_distance_5 = models.StringField(blank=True, default='')

    sun_additional_trip_6 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_6 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_6 = models.StringField(blank=True, default='')
    sun_distance_6 = models.StringField(blank=True, default='')

    sun_additional_trip_7 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_7 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_7 = models.StringField(blank=True, default='')
    sun_distance_7 = models.StringField(blank=True, default='')

    sun_additional_trip_8 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_8 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_8 = models.StringField(blank=True, default='')
    sun_distance_8 = models.StringField(blank=True, default='')

    sun_additional_trip_9 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_9 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_9 = models.StringField(blank=True, default='')
    sun_distance_9 = models.StringField(blank=True, default='')

    sun_additional_trip_10 = models.StringField(
        choices=['Home', 'Work', 'School', 'Groceries', 'Errands', 'Social', 'Sports', 'Other'],
        blank=True,
        default=''
    )
    sun_start_time_10 = models.StringField(
        choices=C.TIME_CHOICES,
        blank=True,
        default=''
    )
    sun_duration_10 = models.StringField(blank=True, default='')
    sun_distance_10 = models.StringField(blank=True, default='')


class Instruction(Page):
    form_model = 'player'

    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Tuesday'] = player.Tuesday
        player.participant.vars['Wednesday'] = player.Wednesday
        player.participant.vars['Thursday'] = player.Thursday
        player.participant.vars['Friday'] = player.Friday
        player.participant.vars['Saturday'] = player.Saturday
        player.participant.vars['Sunday'] = player.Sunday
        player.participant.vars['Wednesday_tue'] = player.Wednesday_tue
        player.participant.vars['Thursday_tue'] = player.Thursday_tue
        player.participant.vars['Friday_tue'] = player.Friday_tue
        player.participant.vars['Saturday_tue'] = player.Saturday_tue
        player.participant.vars['Sunday_tue'] = player.Sunday_tue
        player.participant.vars['Thursday_wed'] = player.Thursday_wed
        player.participant.vars['Friday_wed'] = player.Friday_wed
        player.participant.vars['Saturday_wed'] = player.Saturday_wed
        player.participant.vars['Sunday_wed'] = player.Sunday_wed
        player.participant.vars['Friday_thu'] = player.Friday_thu
        player.participant.vars['Saturday_thu'] = player.Saturday_thu
        player.participant.vars['Sunday_thu'] = player.Sunday_thu
        player.participant.vars['Saturday_fri'] = player.Saturday_fri
        player.participant.vars['Sunday_fri'] = player.Sunday_fri
        player.participant.vars['Sunday_sat'] = player.Sunday_sat


class Monday(Page):
    form_model = 'player'
    form_fields = [
        'mo_first_trip', 'mo_last_trip', 'mo_additional_trip_1', 'mo_start_time_1', 'mo_duration_1', 'mo_distance_1',
        'mo_additional_trip_2', 'mo_start_time_2', 'mo_duration_2', 'mo_distance_2', 'mo_additional_trip_3',
        'mo_start_time_3', 'mo_duration_3', 'mo_distance_3', 'mo_additional_trip_4', 'mo_start_time_4',
        'mo_duration_4', 'mo_distance_4', 'mo_additional_trip_5', 'mo_start_time_5', 'mo_duration_5',
        'mo_distance_5', 'mo_additional_trip_6', 'mo_start_time_6', 'mo_duration_6', 'mo_distance_6',
        'mo_additional_trip_7', 'mo_start_time_7', 'mo_duration_7', 'mo_distance_7', 'mo_additional_trip_8',
        'mo_start_time_8', 'mo_duration_8', 'mo_distance_8', 'mo_additional_trip_9', 'mo_start_time_9',
        'mo_duration_9', 'mo_distance_9', 'mo_additional_trip_10', 'mo_start_time_10', 'mo_duration_10',
        'mo_distance_10', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'
    ]

    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Tuesday'] = player.Tuesday
        player.participant.vars['Wednesday'] = player.Wednesday
        player.participant.vars['Thursday'] = player.Thursday
        player.participant.vars['Friday'] = player.Friday
        player.participant.vars['Saturday'] = player.Saturday
        player.participant.vars['Sunday'] = player.Sunday
        player.participant.vars['mo_last_trip'] = player.mo_last_trip

    def vars_for_template(player: Player):
        mo_additional_trips = [
            getattr(player, f'mo_additional_trip_{i}', '') for i in range(1, 11)
        ]
        return {
            'additional_trips': mo_additional_trips,
            'days': C.DAYS
        }


class Tuesday(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Wednesday_tue'] = player.Wednesday_tue
        player.participant.vars['Thursday_tue'] = player.Thursday_tue
        player.participant.vars['Friday_tue'] = player.Friday_tue
        player.participant.vars['Saturday_tue'] = player.Saturday_tue
        player.participant.vars['Sunday_tue'] = player.Sunday_tue
        player.participant.vars['tue_last_trip'] = player.tue_last_trip

    form_model = 'player'
    form_fields = [
        'tue_first_trip', 'tue_last_trip', 'tue_additional_trip_1', 'tue_start_time_1', 'tue_duration_1', 'tue_distance_1',
        'tue_additional_trip_2', 'tue_start_time_2', 'tue_duration_2', 'tue_distance_2', 'tue_additional_trip_3',
        'tue_start_time_3', 'tue_duration_3', 'tue_distance_3', 'tue_additional_trip_4', 'tue_start_time_4',
        'tue_duration_4', 'tue_distance_4', 'tue_additional_trip_5', 'tue_start_time_5', 'tue_duration_5',
        'tue_distance_5', 'tue_additional_trip_6', 'tue_start_time_6', 'tue_duration_6', 'tue_distance_6',
        'tue_additional_trip_7', 'tue_start_time_7', 'tue_duration_7', 'tue_distance_7', 'tue_additional_trip_8',
        'tue_start_time_8', 'tue_duration_8', 'tue_distance_8', 'tue_additional_trip_9', 'tue_start_time_9',
        'tue_duration_9', 'tue_distance_9', 'tue_additional_trip_10', 'tue_start_time_10', 'tue_duration_10',
        'tue_distance_10', 'Wednesday_tue', 'Thursday_tue', 'Friday_tue', 'Saturday_tue', 'Sunday_tue'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        initial_values = {
            'tue_first_trip': player.mo_first_trip if player.participant.vars.get('Tuesday', False) else None,
            'tue_last_trip': player.mo_last_trip if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_1': player.mo_additional_trip_1 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_1': player.mo_start_time_1 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_1': player.mo_duration_1 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_1': player.mo_distance_1 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_2': player.mo_additional_trip_2 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_2': player.mo_start_time_2 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_2': player.mo_duration_2 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_2': player.mo_distance_2 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_3': player.mo_additional_trip_3 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_3': player.mo_start_time_3 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_3': player.mo_duration_3 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_3': player.mo_distance_3 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_4': player.mo_additional_trip_4 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_4': player.mo_start_time_4 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_4': player.mo_duration_4 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_4': player.mo_distance_4 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_5': player.mo_additional_trip_5 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_5': player.mo_start_time_5 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_5': player.mo_duration_5 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_5': player.mo_distance_5 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_6': player.mo_additional_trip_6 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_6': player.mo_start_time_6 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_6': player.mo_duration_6 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_6': player.mo_distance_6 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_7': player.mo_additional_trip_7 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_7': player.mo_start_time_7 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_7': player.mo_duration_7 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_7': player.mo_distance_7 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_8': player.mo_additional_trip_8 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_8': player.mo_start_time_8 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_8': player.mo_duration_8 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_8': player.mo_distance_8 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_9': player.mo_additional_trip_9 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_9': player.mo_start_time_9 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_9': player.mo_duration_9 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_9': player.mo_distance_9 if player.participant.vars.get('Tuesday', False) else None,

            'tue_additional_trip_10': player.mo_additional_trip_10 if player.participant.vars.get('Tuesday', False) else None,
            'tue_start_time_10': player.mo_start_time_10 if player.participant.vars.get('Tuesday', False) else None,
            'tue_duration_10': player.mo_duration_10 if player.participant.vars.get('Tuesday', False) else None,
            'tue_distance_10': player.mo_distance_10 if player.participant.vars.get('Tuesday', False) else None,
        }

        tue_additional_trips = [
            getattr(player, 'tue_additional_trip_1', '') or '',
            getattr(player, 'tue_additional_trip_2', '') or '',
            getattr(player, 'tue_additional_trip_3', '') or '',
            getattr(player, 'tue_additional_trip_4', '') or '',
            getattr(player, 'tue_additional_trip_5', '') or '',
            getattr(player, 'tue_additional_trip_6', '') or '',
            getattr(player, 'tue_additional_trip_7', '') or '',
            getattr(player, 'tue_additional_trip_8', '') or '',
            getattr(player, 'tue_additional_trip_9', '') or '',
            getattr(player, 'tue_additional_trip_10', '') or '',
        ]

        return {
            'initial_values': initial_values,
            'additional_trips': tue_additional_trips,
            'days': C.DAYS_tue
        }

    def get_form_fields(player: Player):
        fields = [
            'tue_first_trip', 'tue_last_trip', 'tue_additional_trip_1', 'tue_start_time_1', 'tue_duration_1', 'tue_distance_1',
            'tue_additional_trip_2', 'tue_start_time_2', 'tue_duration_2', 'tue_distance_2', 'tue_additional_trip_3',
            'tue_start_time_3', 'tue_duration_3', 'tue_distance_3', 'tue_additional_trip_4', 'tue_start_time_4',
            'tue_duration_4', 'tue_distance_4', 'tue_additional_trip_5', 'tue_start_time_5', 'tue_duration_5',
            'tue_distance_5', 'tue_additional_trip_6', 'tue_start_time_6', 'tue_duration_6', 'tue_distance_6',
            'tue_additional_trip_7', 'tue_start_time_7', 'tue_duration_7', 'tue_distance_7', 'tue_additional_trip_8',
            'tue_start_time_8', 'tue_duration_8', 'tue_distance_8', 'tue_additional_trip_9', 'tue_start_time_9',
            'tue_duration_9', 'tue_distance_9', 'tue_additional_trip_10', 'tue_start_time_10', 'tue_duration_10',
            'tue_distance_10', 'Wednesday_tue', 'Thursday_tue', 'Friday_tue', 'Saturday_tue', 'Sunday_tue'
        ]

        if player.participant.vars.get('Tuesday', False):
            player.tue_first_trip = player.mo_first_trip
            player.tue_last_trip = player.mo_last_trip

            player.tue_additional_trip_1 = player.mo_additional_trip_1
            player.tue_start_time_1 = player.mo_start_time_1
            player.tue_distance_1 = player.mo_distance_1
            player.tue_duration_1 = player.mo_duration_1

            player.tue_additional_trip_2 = player.mo_additional_trip_2
            player.tue_start_time_2 = player.mo_start_time_2
            player.tue_distance_2 = player.mo_distance_2
            player.tue_duration_2 = player.mo_duration_2

            player.tue_additional_trip_3 = player.mo_additional_trip_3
            player.tue_start_time_3 = player.mo_start_time_3
            player.tue_distance_3 = player.mo_distance_3
            player.tue_duration_3 = player.mo_duration_3

            player.tue_additional_trip_4 = player.mo_additional_trip_4
            player.tue_start_time_4 = player.mo_start_time_4
            player.tue_distance_4 = player.mo_distance_4
            player.tue_duration_4 = player.mo_duration_4

            player.tue_additional_trip_5 = player.mo_additional_trip_5
            player.tue_start_time_5 = player.mo_start_time_5
            player.tue_distance_5 = player.mo_distance_5
            player.tue_duration_5 = player.mo_duration_5

            player.tue_additional_trip_6 = player.mo_additional_trip_6
            player.tue_start_time_6 = player.mo_start_time_6
            player.tue_distance_6 = player.mo_distance_6
            player.tue_duration_6 = player.mo_duration_6

            player.tue_additional_trip_7 = player.mo_additional_trip_7
            player.tue_start_time_7 = player.mo_start_time_7
            player.tue_distance_7 = player.mo_distance_7
            player.tue_duration_7 = player.mo_duration_7

            player.tue_additional_trip_8 = player.mo_additional_trip_8
            player.tue_start_time_8 = player.mo_start_time_8
            player.tue_distance_8 = player.mo_distance_8
            player.tue_duration_8 = player.mo_duration_8

            player.tue_additional_trip_9 = player.mo_additional_trip_9
            player.tue_start_time_9 = player.mo_start_time_9
            player.tue_distance_9 = player.mo_distance_9
            player.tue_duration_9 = player.mo_duration_9

            player.tue_additional_trip_10 = player.mo_additional_trip_10
            player.tue_start_time_10 = player.mo_start_time_10
            player.tue_distance_10 = player.mo_distance_10
            player.tue_duration_10= player.mo_duration_10

        return fields


class Wednesday(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Thursday_wed'] = player.Thursday_wed
        player.participant.vars['Friday_wed'] = player.Friday_wed
        player.participant.vars['Saturday_wed'] = player.Saturday_wed
        player.participant.vars['Sunday_wed'] = player.Sunday_wed
        player.participant.vars['wed_last_trip'] = player.wed_last_trip

    form_model = 'player'
    form_fields = [
        'wed_first_trip', 'wed_last_trip', 'wed_additional_trip_1', 'wed_start_time_1', 'wed_duration_1', 'wed_distance_1',
        'wed_additional_trip_2', 'wed_start_time_2', 'wed_duration_2', 'wed_distance_2', 'wed_additional_trip_3',
        'wed_start_time_3', 'wed_duration_3', 'wed_distance_3', 'wed_additional_trip_4', 'wed_start_time_4',
        'wed_duration_4', 'wed_distance_4', 'wed_additional_trip_5', 'wed_start_time_5', 'wed_duration_5',
        'wed_distance_5', 'wed_additional_trip_6', 'wed_start_time_6', 'wed_duration_6', 'wed_distance_6',
        'wed_additional_trip_7', 'wed_start_time_7', 'wed_duration_7', 'wed_distance_7', 'wed_additional_trip_8',
        'wed_start_time_8', 'wed_duration_8', 'wed_distance_8', 'wed_additional_trip_9', 'wed_start_time_9',
        'wed_duration_9', 'wed_distance_9', 'wed_additional_trip_10', 'wed_start_time_10', 'wed_duration_10',
        'wed_distance_10', 'Thursday_wed', 'Friday_wed', 'Saturday_wed', 'Sunday_wed'
    ]

    def vars_for_template(player: Player):
        initial_values = {
            'wed_first_trip': player.tue_first_trip if player.participant.vars.get('Wednesday_tue', False) else player.mo_first_trip if player.participant.vars.get('Wednesday', False) else None,
            'wed_last_trip': player.tue_last_trip if player.participant.vars.get('Wednesday_tue', False) else player.mo_last_trip if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_1': player.tue_additional_trip_1 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_1 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_1': player.tue_start_time_1 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_1 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_1': player.tue_duration_1 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_1 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_1': player.tue_distance_1 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_1 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_2': player.tue_additional_trip_2 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_2 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_2': player.tue_start_time_2 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_2 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_2': player.tue_duration_2 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_2 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_2': player.tue_distance_2 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_2 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_3': player.tue_additional_trip_3 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_3 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_3': player.tue_start_time_3 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_3 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_3': player.tue_duration_3 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_3 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_3': player.tue_distance_3 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_3 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_4': player.tue_additional_trip_4 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_4 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_4': player.tue_start_time_4 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_4 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_4': player.tue_duration_4 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_4 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_4': player.tue_distance_4 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_4 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_5': player.tue_additional_trip_5 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_5 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_5': player.tue_start_time_5 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_5 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_5': player.tue_duration_5 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_5 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_5': player.tue_distance_5 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_5 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_6': player.tue_additional_trip_6 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_6 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_6': player.tue_start_time_6 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_6 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_6': player.tue_duration_6 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_6 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_6': player.tue_distance_6 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_6 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_7': player.tue_additional_trip_7 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_7 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_7': player.tue_start_time_7 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_7 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_7': player.tue_duration_7 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_7 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_7': player.tue_distance_7 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_7 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_8': player.tue_additional_trip_8 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_8 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_8': player.tue_start_time_8 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_8 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_8': player.tue_duration_8 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_8 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_8': player.tue_distance_8 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_8 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_9': player.tue_additional_trip_9 if player.participant.vars.get('Wednesday_tue',False) else player.mo_additional_trip_9 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_9': player.tue_start_time_9 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_9 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_9': player.tue_duration_9 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_9 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_9': player.tue_distance_9 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_9 if player.participant.vars.get('Wednesday', False) else None,

            'wed_additional_trip_10': player.tue_additional_trip_10 if player.participant.vars.get('Wednesday_tue', False) else player.mo_additional_trip_10 if player.participant.vars.get('Wednesday', False) else None,
            'wed_start_time_10': player.tue_start_time_10 if player.participant.vars.get('Wednesday_tue', False) else player.mo_start_time_10 if player.participant.vars.get('Wednesday', False) else None,
            'wed_duration_10': player.tue_duration_10 if player.participant.vars.get('Wednesday_tue', False) else player.mo_duration_10 if player.participant.vars.get('Wednesday', False) else None,
            'wed_distance_10': player.tue_distance_10 if player.participant.vars.get('Wednesday_tue', False) else player.mo_distance_10 if player.participant.vars.get('Wednesday', False) else None,

            'Wednesday_tue': player.participant.vars.get('Wednesday_tue', False),
            'Thursday_tue': player.participant.vars.get('Thursday_tue', False),
            'Friday_tue': player.participant.vars.get('Friday_tue', False),
            'Saturday_tue': player.participant.vars.get('Saturday_tue', False),
            'Sunday_tue': player.participant.vars.get('Sunday_tue', False)
        }

        wed_additional_trips = [
            getattr(player, 'wed_additional_trip_1', '') or '',
            getattr(player, 'wed_additional_trip_2', '') or '',
            getattr(player, 'wed_additional_trip_3', '') or '',
            getattr(player, 'wed_additional_trip_4', '') or '',
            getattr(player, 'wed_additional_trip_5', '') or '',
            getattr(player, 'wed_additional_trip_6', '') or '',
            getattr(player, 'wed_additional_trip_7', '') or '',
            getattr(player, 'wed_additional_trip_8', '') or '',
            getattr(player, 'wed_additional_trip_9', '') or '',
            getattr(player, 'wed_additional_trip_10', '') or '',
        ]
        return {
            'initial_values': initial_values,
            'additional_trips': wed_additional_trips,
            'days': C.DAYS_wed
        }

    def get_form_fields(player: Player):
        fields = [
            'wed_first_trip', 'wed_last_trip', 'wed_additional_trip_1', 'wed_start_time_1', 'wed_duration_1',
            'wed_distance_1',
            'wed_additional_trip_2', 'wed_start_time_2', 'wed_duration_2', 'wed_distance_2', 'wed_additional_trip_3',
            'wed_start_time_3', 'wed_duration_3', 'wed_distance_3', 'wed_additional_trip_4', 'wed_start_time_4',
            'wed_duration_4', 'wed_distance_4', 'wed_additional_trip_5', 'wed_start_time_5', 'wed_duration_5',
            'wed_distance_5', 'wed_additional_trip_6', 'wed_start_time_6', 'wed_duration_6', 'wed_distance_6',
            'wed_additional_trip_7', 'wed_start_time_7', 'wed_duration_7', 'wed_distance_7', 'wed_additional_trip_8',
            'wed_start_time_8', 'wed_duration_8', 'wed_distance_8', 'wed_additional_trip_9', 'wed_start_time_9',
            'wed_duration_9', 'wed_distance_9', 'wed_additional_trip_10', 'wed_start_time_10', 'wed_duration_10',
            'wed_distance_10', 'Thursday_wed', 'Friday_wed', 'Saturday_wed', 'Sunday_wed'
        ]

        if player.participant.vars.get('Wednesday_tue', False):
            player.wed_first_trip = player.tue_first_trip
            player.wed_last_trip = player.tue_last_trip

            player.wed_additional_trip_1 = player.tue_additional_trip_1
            player.wed_start_time_1 = player.tue_start_time_1
            player.wed_distance_1 = player.tue_distance_1
            player.wed_duration_1 = player.tue_duration_1

            player.wed_additional_trip_2 = player.tue_additional_trip_2
            player.wed_start_time_2 = player.tue_start_time_2
            player.wed_distance_2 = player.tue_distance_2
            player.wed_duration_2 = player.tue_duration_2

            player.wed_additional_trip_3 = player.tue_additional_trip_3
            player.wed_start_time_3 = player.tue_start_time_3
            player.wed_distance_3 = player.tue_distance_3
            player.wed_duration_3 = player.tue_duration_3

            player.wed_additional_trip_4 = player.tue_additional_trip_4
            player.wed_start_time_4 = player.tue_start_time_4
            player.wed_distance_4 = player.tue_distance_4
            player.wed_duration_4 = player.tue_duration_4

            player.wed_additional_trip_5 = player.tue_additional_trip_5
            player.wed_start_time_5 = player.tue_start_time_5
            player.wed_distance_5 = player.tue_distance_5
            player.wed_duration_5 = player.tue_duration_5

            player.wed_additional_trip_6 = player.tue_additional_trip_6
            player.wed_start_time_6 = player.tue_start_time_6
            player.wed_distance_6 = player.tue_distance_6
            player.wed_duration_6 = player.tue_duration_6

            player.wed_additional_trip_7 = player.tue_additional_trip_7
            player.wed_start_time_7 = player.tue_start_time_7
            player.wed_distance_7 = player.tue_distance_7
            player.wed_duration_7 = player.tue_duration_7

            player.wed_additional_trip_8 = player.tue_additional_trip_8
            player.wed_start_time_8 = player.tue_start_time_8
            player.wed_distance_8 = player.tue_distance_8
            player.wed_duration_8 = player.tue_duration_8

            player.wed_additional_trip_9 = player.tue_additional_trip_9
            player.wed_start_time_9 = player.tue_start_time_9
            player.wed_distance_9 = player.tue_distance_9
            player.wed_duration_9 = player.tue_duration_9

            player.wed_additional_trip_10 = player.tue_additional_trip_10
            player.wed_start_time_10 = player.tue_start_time_10
            player.wed_distance_10 = player.tue_distance_10
            player.wed_duration_10 = player.tue_duration_10

        elif player.participant.vars.get('Wednesday', False):
            player.wed_first_trip = player.mo_first_trip
            player.wed_last_trip = player.mo_last_trip

            player.wed_additional_trip_1 = player.mo_additional_trip_1
            player.wed_start_time_1 = player.mo_start_time_1
            player.wed_distance_1 = player.mo_distance_1
            player.wed_duration_1 = player.mo_duration_1

            player.wed_additional_trip_2 = player.mo_additional_trip_2
            player.wed_start_time_2 = player.mo_start_time_2
            player.wed_distance_2 = player.mo_distance_2
            player.wed_duration_2 = player.mo_duration_2

            player.wed_additional_trip_3 = player.mo_additional_trip_3
            player.wed_start_time_3 = player.mo_start_time_3
            player.wed_distance_3 = player.mo_distance_3
            player.wed_duration_3 = player.mo_duration_3

            player.wed_additional_trip_4 = player.mo_additional_trip_4
            player.wed_start_time_4 = player.mo_start_time_4
            player.wed_distance_4 = player.mo_distance_4
            player.wed_duration_4 = player.mo_duration_4

            player.wed_additional_trip_5 = player.mo_additional_trip_5
            player.wed_start_time_5 = player.mo_start_time_5
            player.wed_distance_5 = player.mo_distance_5
            player.wed_duration_5 = player.mo_duration_5

            player.wed_additional_trip_6 = player.mo_additional_trip_6
            player.wed_start_time_6 = player.mo_start_time_6
            player.wed_distance_6 = player.mo_distance_6
            player.wed_duration_6 = player.mo_duration_6

            player.wed_additional_trip_7 = player.mo_additional_trip_7
            player.wed_start_time_7 = player.mo_start_time_7
            player.wed_distance_7 = player.mo_distance_7
            player.wed_duration_7 = player.mo_duration_7

            player.wed_additional_trip_8 = player.mo_additional_trip_8
            player.wed_start_time_8 = player.mo_start_time_8
            player.wed_distance_8 = player.mo_distance_8
            player.wed_duration_8 = player.mo_duration_8

            player.wed_additional_trip_9 = player.mo_additional_trip_9
            player.wed_start_time_9 = player.mo_start_time_9
            player.wed_distance_9 = player.mo_distance_9
            player.wed_duration_9 = player.mo_duration_9

            player.wed_additional_trip_10 = player.mo_additional_trip_10
            player.wed_start_time_10 = player.mo_start_time_10
            player.wed_distance_10 = player.mo_distance_10
            player.wed_duration_10 = player.mo_duration_10

        return fields


class Thursday(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Friday_thu'] = player.Friday_thu
        player.participant.vars['Saturday_thu'] = player.Saturday_thu
        player.participant.vars['Sunday_thu'] = player.Sunday_thu
        player.participant.vars['thu_last_trip'] = player.thu_last_trip

    form_model = 'player'
    form_fields = [
        'thu_first_trip', 'thu_last_trip', 'thu_additional_trip_1', 'thu_start_time_1', 'thu_duration_1', 'thu_distance_1',
        'thu_additional_trip_2', 'thu_start_time_2', 'thu_duration_2', 'thu_distance_2', 'thu_additional_trip_3',
        'thu_start_time_3', 'thu_duration_3', 'thu_distance_3', 'thu_additional_trip_4', 'thu_start_time_4',
        'thu_duration_4', 'thu_distance_4', 'thu_additional_trip_5', 'thu_start_time_5', 'thu_duration_5',
        'thu_distance_5', 'thu_additional_trip_6', 'thu_start_time_6', 'thu_duration_6', 'thu_distance_6',
        'thu_additional_trip_7', 'thu_start_time_7', 'thu_duration_7', 'thu_distance_7', 'thu_additional_trip_8',
        'thu_start_time_8', 'thu_duration_8', 'thu_distance_8', 'thu_additional_trip_9', 'thu_start_time_9',
        'thu_duration_9', 'thu_distance_9', 'thu_additional_trip_10', 'thu_start_time_10', 'thu_duration_10',
        'thu_distance_10', 'Friday_thu', 'Saturday_thu', 'Sunday_thu'
    ]

    def vars_for_template(player: Player):

        initial_values = {
            'thu_first_trip': player.tue_first_trip if player.participant.vars.get('Thursday_tue', False) else player.mo_first_trip if player.participant.vars.get('Thursday', False) else player.wed_first_trip if player.participant.vars.get('Thursday_wed', False) else None,
            'thu_last_trip': player.tue_last_trip if player.participant.vars.get('Thursday_tue', False) else player.mo_last_trip if player.participant.vars.get('Thursday', False) else player.wed_first_trip if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_1': player.tue_additional_trip_1 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_1 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_1 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_1': player.tue_start_time_1 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_1 if player.participant.vars.get('Thursday', False) else player.wed_start_time_1 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_1': player.tue_duration_1 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_1 if player.participant.vars.get('Thursday', False) else player.wed_duration_1 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_1': player.tue_distance_1 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_1 if player.participant.vars.get('Thursday', False) else player.wed_distance_1 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_2': player.tue_additional_trip_2 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_2 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_2 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_2': player.tue_start_time_2 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_2 if player.participant.vars.get('Thursday', False) else player.wed_start_time_2 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_2': player.tue_duration_2 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_2 if player.participant.vars.get('Thursday', False) else player.wed_duration_2 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_2': player.tue_distance_2 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_2 if player.participant.vars.get('Thursday', False) else player.wed_distance_2 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_3': player.tue_additional_trip_3 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_3 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_3 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_3': player.tue_start_time_3 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_3 if player.participant.vars.get('Thursday', False) else player.wed_start_time_3 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_3': player.tue_duration_3 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_3 if player.participant.vars.get('Thursday', False) else player.wed_duration_3 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_3': player.tue_distance_3 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_3 if player.participant.vars.get('Thursday', False) else player.wed_distance_3 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_4': player.tue_additional_trip_4 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_4 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_4 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_4': player.tue_start_time_4 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_4 if player.participant.vars.get('Thursday', False) else player.wed_start_time_4 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_4': player.tue_duration_4 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_4 if player.participant.vars.get('Thursday', False) else player.wed_duration_4 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_4': player.tue_distance_4 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_4 if player.participant.vars.get('Thursday', False) else player.wed_duration_4 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_5': player.tue_additional_trip_5 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_5 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_5 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_5': player.tue_start_time_5 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_5 if player.participant.vars.get('Thursday', False) else player.wed_start_time_5 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_5': player.tue_duration_5 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_5 if player.participant.vars.get('Thursday', False) else player.wed_duration_5 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_5': player.tue_distance_5 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_5 if player.participant.vars.get('Thursday', False) else player.wed_distance_5 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_6': player.tue_additional_trip_6 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_6 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_6 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_6': player.tue_start_time_6 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_6 if player.participant.vars.get('Thursday', False) else player.wed_start_time_6 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_6': player.tue_duration_6 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_6 if player.participant.vars.get('Thursday', False) else player.wed_duration_6 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_6': player.tue_distance_6 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_6 if player.participant.vars.get('Thursday', False) else player.wed_distance_6 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_7': player.tue_additional_trip_7 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_7 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_7 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_7': player.tue_start_time_7 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_7 if player.participant.vars.get('Thursday', False) else player.wed_start_time_7 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_7': player.tue_duration_7 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_7 if player.participant.vars.get('Thursday', False) else player.wed_duration_7 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_7': player.tue_distance_7 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_7 if player.participant.vars.get('Thursday', False) else player.wed_distance_7 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_8': player.tue_additional_trip_8 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_8 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_8 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_8': player.tue_start_time_8 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_8 if player.participant.vars.get('Thursday', False) else player.wed_start_time_8 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_8': player.tue_duration_8 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_8 if player.participant.vars.get('Thursday', False) else player.wed_duration_8 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_8': player.tue_distance_8 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_8 if player.participant.vars.get('Thursday', False) else player.wed_distance_8 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_9': player.tue_additional_trip_9 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_9 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_9 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_9': player.tue_start_time_9 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_9 if player.participant.vars.get('Thursday', False) else player.wed_start_time_9 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_9': player.tue_duration_9 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_9 if player.participant.vars.get('Thursday', False) else player.wed_duration_9 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_9': player.tue_distance_9 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_9 if player.participant.vars.get('Thursday', False) else player.wed_distance_9 if player.participant.vars.get('Thursday_wed', False)else None,

            'thu_additional_trip_10': player.tue_additional_trip_10 if player.participant.vars.get('Thursday_tue', False) else player.mo_additional_trip_10 if player.participant.vars.get('Thursday', False) else player.wed_additional_trip_10 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_start_time_10': player.tue_start_time_10 if player.participant.vars.get('Thursday_tue', False) else player.mo_start_time_10 if player.participant.vars.get('Thursday', False) else player.wed_start_time_10 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_duration_10': player.tue_duration_10 if player.participant.vars.get('Thursday_tue', False) else player.mo_duration_10 if player.participant.vars.get('Thursday', False) else player.wed_duration_10 if player.participant.vars.get('Thursday_wed', False)else None,
            'thu_distance_10': player.tue_distance_10 if player.participant.vars.get('Thursday_tue', False) else player.mo_distance_10 if player.participant.vars.get('Thursday', False) else player.wed_distance_10 if player.participant.vars.get('Thursday_wed', False)else None,

            'Thursday_wed': player.participant.vars.get('Thursday_wed', False),
            'Friday_wed': player.participant.vars.get('Friday_wed', False),
            'Saturday_wed': player.participant.vars.get('Saturday_wed', False),
            'Sunday_wed': player.participant.vars.get('Sunday_wed', False)
        }

        thu_additional_trips = [
            getattr(player, 'thu_additional_trip_1', '') or '',
            getattr(player, 'thu_additional_trip_2', '') or '',
            getattr(player, 'thu_additional_trip_3', '') or '',
            getattr(player, 'thu_additional_trip_4', '') or '',
            getattr(player, 'thu_additional_trip_5', '') or '',
            getattr(player, 'thu_additional_trip_6', '') or '',
            getattr(player, 'thu_additional_trip_7', '') or '',
            getattr(player, 'thu_additional_trip_8', '') or '',
            getattr(player, 'thu_additional_trip_9', '') or '',
            getattr(player, 'thu_additional_trip_10', '') or '',
        ]
        return {
            'initial_values': initial_values,
            'additional_trips': thu_additional_trips,
            'days': C.DAYS_thu
        }

    def get_form_fields(player: Player):
        fields = [
            'thu_first_trip', 'thu_last_trip',
            'thu_additional_trip_1', 'thu_start_time_1', 'thu_duration_1', 'thu_distance_1',
            'thu_additional_trip_2', 'thu_start_time_2', 'thu_duration_2', 'thu_distance_2', 'thu_additional_trip_3',
            'thu_start_time_3', 'thu_duration_3', 'thu_distance_3', 'thu_additional_trip_4', 'thu_start_time_4',
            'thu_duration_4', 'thu_distance_4', 'thu_additional_trip_5', 'thu_start_time_5', 'thu_duration_5',
            'thu_distance_5', 'thu_additional_trip_6', 'thu_start_time_6', 'thu_duration_6', 'thu_distance_6',
            'thu_additional_trip_7', 'thu_start_time_7', 'thu_duration_7', 'thu_distance_7', 'thu_additional_trip_8',
            'thu_start_time_8', 'thu_duration_8', 'thu_distance_8', 'thu_additional_trip_9', 'thu_start_time_9',
            'thu_duration_9', 'thu_distance_9', 'thu_additional_trip_10', 'thu_start_time_10', 'thu_duration_10',
            'thu_distance_10', 'Friday_thu', 'Saturday_thu', 'Sunday_thu'
        ]

        if player.participant.vars.get('Thursday_tue', False):
            player.thu_first_trip = player.tue_first_trip
            player.thu_last_trip = player.tue_last_trip

            player.thu_additional_trip_1 = player.tue_additional_trip_1
            player.thu_start_time_1 = player.tue_start_time_1
            player.thu_distance_1 = player.tue_distance_1
            player.thu_duration_1 = player.tue_duration_1

            player.thu_additional_trip_2 = player.tue_additional_trip_2
            player.thu_start_time_2 = player.tue_start_time_2
            player.thu_distance_2 = player.tue_distance_2
            player.thu_duration_2 = player.tue_duration_2

            player.thu_additional_trip_3 = player.tue_additional_trip_3
            player.thu_start_time_3 = player.tue_start_time_3
            player.thu_distance_3 = player.tue_distance_3
            player.thu_duration_3 = player.tue_duration_3

            player.thu_additional_trip_4 = player.tue_additional_trip_4
            player.thu_start_time_4 = player.tue_start_time_4
            player.thu_distance_4 = player.tue_distance_4
            player.thu_duration_4 = player.tue_duration_4

            player.thu_additional_trip_5 = player.tue_additional_trip_5
            player.thu_start_time_5 = player.tue_start_time_5
            player.thu_distance_5 = player.tue_distance_5
            player.thu_duration_5 = player.tue_duration_5

            player.thu_additional_trip_6 = player.tue_additional_trip_6
            player.thu_start_time_6 = player.tue_start_time_6
            player.thu_distance_6 = player.tue_distance_6
            player.thu_duration_6 = player.tue_duration_6

            player.thu_additional_trip_7 = player.tue_additional_trip_7
            player.thu_start_time_7 = player.tue_start_time_7
            player.thu_distance_7 = player.tue_distance_7
            player.thu_duration_7 = player.tue_duration_7

            player.thu_additional_trip_8 = player.tue_additional_trip_8
            player.thu_start_time_8 = player.tue_start_time_8
            player.thu_distance_8 = player.tue_distance_8
            player.thu_duration_8 = player.tue_duration_8

            player.thu_additional_trip_9 = player.tue_additional_trip_9
            player.thu_start_time_9 = player.tue_start_time_9
            player.thu_distance_9 = player.tue_distance_9
            player.thu_duration_9 = player.tue_duration_9

            player.thu_additional_trip_10 = player.tue_additional_trip_10
            player.thu_start_time_10 = player.tue_start_time_10
            player.thu_distance_10 = player.tue_distance_10
            player.thu_duration_10 = player.tue_duration_10

        elif player.participant.vars.get('Thursday', False):
            player.thu_first_trip = player.mo_first_trip
            player.thu_last_trip = player.mo_last_trip

            player.thu_additional_trip_1 = player.mo_additional_trip_1
            player.thu_start_time_1 = player.mo_start_time_1
            player.thu_distance_1 = player.mo_distance_1
            player.thu_duration_1 = player.mo_duration_1

            player.thu_additional_trip_2 = player.mo_additional_trip_2
            player.thu_start_time_2 = player.mo_start_time_2
            player.thu_distance_2 = player.mo_distance_2
            player.thu_duration_2 = player.mo_duration_2

            player.thu_additional_trip_3 = player.mo_additional_trip_3
            player.thu_start_time_3 = player.mo_start_time_3
            player.thu_distance_3 = player.mo_distance_3
            player.thu_duration_3 = player.mo_duration_3

            player.thu_additional_trip_4 = player.mo_additional_trip_4
            player.thu_start_time_4 = player.mo_start_time_4
            player.thu_distance_4 = player.mo_distance_4
            player.thu_duration_4 = player.mo_duration_4

            player.thu_additional_trip_5 = player.mo_additional_trip_5
            player.thu_start_time_5 = player.mo_start_time_5
            player.thu_distance_5 = player.mo_distance_5
            player.thu_duration_5 = player.mo_duration_5

            player.thu_additional_trip_6 = player.mo_additional_trip_6
            player.thu_start_time_6 = player.mo_start_time_6
            player.thu_distance_6 = player.mo_distance_6
            player.thu_duration_6 = player.mo_duration_6

            player.thu_additional_trip_7 = player.mo_additional_trip_7
            player.thu_start_time_7 = player.mo_start_time_7
            player.thu_distance_7 = player.mo_distance_7
            player.thu_duration_7 = player.mo_duration_7

            player.thu_additional_trip_8 = player.mo_additional_trip_8
            player.thu_start_time_8 = player.mo_start_time_8
            player.thu_distance_8 = player.mo_distance_8
            player.thu_duration_8 = player.mo_duration_8

            player.thu_additional_trip_9 = player.mo_additional_trip_9
            player.thu_start_time_9 = player.mo_start_time_9
            player.thu_distance_9 = player.mo_distance_9
            player.thu_duration_9 = player.mo_duration_9

            player.thu_additional_trip_10 = player.mo_additional_trip_10
            player.thu_start_time_10 = player.mo_start_time_10
            player.thu_distance_10 = player.mo_distance_10
            player.thu_duration_10 = player.mo_duration_10

        elif player.participant.vars.get('Thursday_wed', False):
            player.thu_first_trip = player.wed_first_trip
            player.thu_last_trip = player.wed_last_trip

            player.thu_additional_trip_1 = player.wed_additional_trip_1
            player.thu_start_time_1 = player.wed_start_time_1
            player.thu_distance_1 = player.wed_distance_1
            player.thu_duration_1 = player.wed_duration_1

            player.thu_additional_trip_2 = player.wed_additional_trip_2
            player.thu_start_time_2 = player.wed_start_time_2
            player.thu_distance_2 = player.wed_distance_2
            player.thu_duration_2 = player.wed_duration_2

            player.thu_additional_trip_3 = player.wed_additional_trip_3
            player.thu_start_time_3 = player.wed_start_time_3
            player.thu_distance_3 = player.wed_distance_3
            player.thu_duration_3 = player.wed_duration_3

            player.thu_additional_trip_4 = player.wed_additional_trip_4
            player.thu_start_time_4 = player.wed_start_time_4
            player.thu_distance_4 = player.wed_distance_4
            player.thu_duration_4 = player.wed_duration_4

            player.thu_additional_trip_5 = player.wed_additional_trip_5
            player.thu_start_time_5 = player.wed_start_time_5
            player.thu_distance_5 = player.wed_distance_5
            player.thu_duration_5 = player.wed_duration_5

            player.thu_additional_trip_6 = player.wed_additional_trip_6
            player.thu_start_time_6 = player.wed_start_time_6
            player.thu_distance_6 = player.wed_distance_6
            player.thu_duration_6 = player.wed_duration_6

            player.thu_additional_trip_7 = player.wed_additional_trip_7
            player.thu_start_time_7 = player.wed_start_time_7
            player.thu_distance_7 = player.wed_distance_7
            player.thu_duration_7 = player.wed_duration_7

            player.thu_additional_trip_8 = player.wed_additional_trip_8
            player.thu_start_time_8 = player.wed_start_time_8
            player.thu_distance_8 = player.wed_distance_8
            player.thu_duration_8 = player.wed_duration_8

            player.thu_additional_trip_9 = player.wed_additional_trip_9
            player.thu_start_time_9 = player.wed_start_time_9
            player.thu_distance_9 = player.wed_distance_9
            player.thu_duration_9 = player.wed_duration_9

            player.thu_additional_trip_10 = player.wed_additional_trip_10
            player.thu_start_time_10 = player.wed_start_time_10
            player.thu_distance_10 = player.wed_distance_10
            player.thu_duration_10 = player.wed_duration_10

        return fields


class Friday(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Saturday_fri'] = player.Saturday_fri
        player.participant.vars['Sunday_fri'] = player.Sunday_fri
        player.participant.vars['fri_last_trip'] = player.fri_last_trip

    form_model = 'player'
    form_fields = [
        'fri_first_trip', 'fri_last_trip', 'fri_additional_trip_1', 'fri_start_time_1', 'fri_duration_1', 'fri_distance_1',
        'fri_additional_trip_2', 'fri_start_time_2', 'fri_duration_2', 'fri_distance_2', 'fri_additional_trip_3',
        'fri_start_time_3', 'fri_duration_3', 'fri_distance_3', 'fri_additional_trip_4', 'fri_start_time_4',
        'fri_duration_4', 'fri_distance_4', 'fri_additional_trip_5', 'fri_start_time_5', 'fri_duration_5',
        'fri_distance_5', 'fri_additional_trip_6', 'fri_start_time_6', 'fri_duration_6', 'fri_distance_6',
        'fri_additional_trip_7', 'fri_start_time_7', 'fri_duration_7', 'fri_distance_7', 'fri_additional_trip_8',
        'fri_start_time_8', 'fri_duration_8', 'fri_distance_8', 'fri_additional_trip_9', 'fri_start_time_9',
        'fri_duration_9', 'fri_distance_9', 'fri_additional_trip_10', 'fri_start_time_10', 'fri_duration_10',
        'fri_distance_10', 'Saturday_fri', 'Sunday_fri'
    ]

    def vars_for_template(player: Player):
        initial_values = {
            'fri_first_trip': player.tue_first_trip if player.participant.vars.get('Friday_tue', False) else player.mo_first_trip if player.participant.vars.get('Friday', False) else player.wed_first_trip if player.participant.vars.get('Friday_wed', False) else player.thu_first_trip if player.participant.vars.get('Friday_thu', False) else None,
            'fri_last_trip': player.tue_last_trip if player.participant.vars.get('Friday_tue', False) else player.mo_last_trip if player.participant.vars.get('Friday', False) else player.wed_first_trip if player.participant.vars.get('Friday_wed', False) else player.thu_first_trip if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_1': player.tue_additional_trip_1 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_1 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_1 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_1 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_1': player.tue_start_time_1 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_1 if player.participant.vars.get('Friday', False) else player.wed_start_time_1 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_1 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_1': player.tue_duration_1 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_1 if player.participant.vars.get('Friday', False) else player.wed_duration_1 if player.participant.vars.get('Friday_wed', False) else player.thu_duration_1 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_distance_1': player.tue_distance_1 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_1 if player.participant.vars.get('Friday', False) else player.wed_distance_1 if player.participant.vars.get('Friday_wed', False) else player.thu_distance_1 if player.participant.vars.get('Friday_thu', False) else None,

            'fri_additional_trip_2': player.tue_additional_trip_2 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_2 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_2 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_2 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_2': player.tue_start_time_2 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_2 if player.participant.vars.get('Friday', False) else player.wed_start_time_2 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_2 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_2': player.tue_duration_2 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_2 if player.participant.vars.get('Friday', False) else player.wed_duration_2 if player.participant.vars.get('Friday_wed', False) else player.thu_duration_2 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_distance_2': player.tue_distance_2 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_2 if player.participant.vars.get('Friday', False) else player.wed_distance_2 if player.participant.vars.get('Friday_wed', False) else player.thu_distance_2 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_3': player.tue_additional_trip_3 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_3 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_3 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_3 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_3': player.tue_start_time_3 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_3 if player.participant.vars.get('Friday', False) else player.wed_start_time_3 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_3 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_3': player.tue_duration_3 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_3 if player.participant.vars.get('Friday', False) else player.wed_duration_3 if player.participant.vars.get('Friday_wed', False) else player.thu_duration_3 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_distance_3': player.tue_distance_3 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_3 if player.participant.vars.get('Friday', False) else player.wed_distance_3 if player.participant.vars.get('Friday_wed', False) else player.thu_distance_3 if player.participant.vars.get('Friday_thu', False) else None,

            'fri_additional_trip_4': player.tue_additional_trip_4 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_4 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_4 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_4 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_4': player.tue_start_time_4 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_4 if player.participant.vars.get('Friday', False) else player.wed_start_time_4 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_4 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_4': player.tue_duration_4 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_4 if player.participant.vars.get('Friday', False) else player.wed_duration_4 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_4 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_4': player.tue_distance_4 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_4 if player.participant.vars.get('Friday', False) else player.wed_duration_4 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_4 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_5': player.tue_additional_trip_5 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_5 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_5 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_5 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_start_time_5': player.tue_start_time_5 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_5 if player.participant.vars.get('Friday', False) else player.wed_start_time_5 if player.participant.vars.get('Friday_wed', False)else player.thu_start_time_5 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_duration_5': player.tue_duration_5 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_5 if player.participant.vars.get('Friday', False) else player.wed_duration_5 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_5 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_distance_5': player.tue_distance_5 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_5 if player.participant.vars.get('Friday', False) else player.wed_distance_5 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_5 if player.participant.vars.get('Friday_thu', False) else None,

            'fri_additional_trip_6': player.tue_additional_trip_6 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_6 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_6 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_6 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_start_time_6': player.tue_start_time_6 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_6 if player.participant.vars.get('Friday', False) else player.wed_start_time_6 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_6 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_6': player.tue_duration_6 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_6 if player.participant.vars.get('Friday', False) else player.wed_duration_6 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_6 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_6': player.tue_distance_6 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_6 if player.participant.vars.get('Friday', False) else player.wed_distance_6 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_6 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_7': player.tue_additional_trip_7 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_7 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_7 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_7 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_7': player.tue_start_time_7 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_7 if player.participant.vars.get('Friday', False) else player.wed_start_time_7 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_7 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_7': player.tue_duration_7 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_7 if player.participant.vars.get('Friday', False) else player.wed_duration_7 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_7 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_7': player.tue_distance_7 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_7 if player.participant.vars.get('Friday', False) else player.wed_distance_7 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_7 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_8': player.tue_additional_trip_8 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_8 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_8 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_8 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_8': player.tue_start_time_8 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_8 if player.participant.vars.get('Friday', False) else player.wed_start_time_8 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_8 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_8': player.tue_duration_8 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_8 if player.participant.vars.get('Friday', False) else player.wed_duration_8 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_8 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_8': player.tue_distance_8 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_8 if player.participant.vars.get('Friday', False) else player.wed_distance_8 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_8 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_9': player.tue_additional_trip_9 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_9 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_9 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_9 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_9': player.tue_start_time_9 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_9 if player.participant.vars.get('Friday', False) else player.wed_start_time_9 if player.participant.vars.get('Friday_wed', False) else player.thu_start_time_9 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_duration_9': player.tue_duration_9 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_9 if player.participant.vars.get('Friday', False) else player.wed_duration_9 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_9 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_9': player.tue_distance_9 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_9 if player.participant.vars.get('Friday', False) else player.wed_distance_9 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_9 if player.participant.vars.get('Friday_thu', False)else None,

            'fri_additional_trip_10': player.tue_additional_trip_10 if player.participant.vars.get('Friday_tue', False) else player.mo_additional_trip_10 if player.participant.vars.get('Friday', False) else player.wed_additional_trip_10 if player.participant.vars.get('Friday_wed', False) else player.thu_additional_trip_10 if player.participant.vars.get('Friday_thu', False) else None,
            'fri_start_time_10': player.tue_start_time_10 if player.participant.vars.get('Friday_tue', False) else player.mo_start_time_10 if player.participant.vars.get('Friday', False) else player.wed_start_time_10 if player.participant.vars.get('Friday_wed', False)else player.thu_start_time_10 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_duration_10': player.tue_duration_10 if player.participant.vars.get('Friday_tue', False) else player.mo_duration_10 if player.participant.vars.get('Friday', False) else player.wed_duration_10 if player.participant.vars.get('Friday_wed', False)else player.thu_duration_10 if player.participant.vars.get('Friday_thu', False)else None,
            'fri_distance_10': player.tue_distance_10 if player.participant.vars.get('Friday_tue', False) else player.mo_distance_10 if player.participant.vars.get('Friday', False) else player.wed_distance_10 if player.participant.vars.get('Friday_wed', False)else player.thu_distance_10 if player.participant.vars.get('Friday_thu', False)else None,


            'Friday_thu': player.participant.vars.get('Friday_thu', False),
            'Saturday_thu': player.participant.vars.get('Saturday_thu', False),
            'Sunday_thu': player.participant.vars.get('Sunday_thu', False)
        }
        fri_additional_trips = [
            getattr(player, 'fri_additional_trip_1', '') or '',
            getattr(player, 'fri_additional_trip_2', '') or '',
            getattr(player, 'fri_additional_trip_3', '') or '',
            getattr(player, 'fri_additional_trip_4', '') or '',
            getattr(player, 'fri_additional_trip_5', '') or '',
            getattr(player, 'fri_additional_trip_6', '') or '',
            getattr(player, 'fri_additional_trip_7', '') or '',
            getattr(player, 'fri_additional_trip_8', '') or '',
            getattr(player, 'fri_additional_trip_9', '') or '',
            getattr(player, 'fri_additional_trip_10', '') or '',
        ]
        return {
            'initial_values': initial_values,
            'additional_trips': fri_additional_trips,
            'days': C.DAYS_fri
        }

    def get_form_fields(player: Player):
        fields = [
            'fri_first_trip', 'fri_last_trip', 'fri_additional_trip_1', 'fri_start_time_1', 'fri_duration_1', 'fri_distance_1',
            'fri_additional_trip_2', 'fri_start_time_2', 'fri_duration_2', 'fri_distance_2', 'fri_additional_trip_3',
            'fri_start_time_3', 'fri_duration_3', 'fri_distance_3', 'fri_additional_trip_4', 'fri_start_time_4',
            'fri_duration_4', 'fri_distance_4', 'fri_additional_trip_5', 'fri_start_time_5', 'fri_duration_5',
            'fri_distance_5', 'fri_additional_trip_6', 'fri_start_time_6', 'fri_duration_6', 'fri_distance_6',
            'fri_additional_trip_7', 'fri_start_time_7', 'fri_duration_7', 'fri_distance_7', 'fri_additional_trip_8',
            'fri_start_time_8', 'fri_duration_8', 'fri_distance_8', 'fri_additional_trip_9', 'fri_start_time_9',
            'fri_duration_9', 'fri_distance_9', 'fri_additional_trip_10', 'fri_start_time_10', 'fri_duration_10',
            'fri_distance_10', 'Saturday_fri', 'Sunday_fri'
        ]

        if player.participant.vars.get('Friday_tue', False):
            player.fri_first_trip = player.tue_first_trip
            player.fri_last_trip = player.tue_last_trip

            player.fri_additional_trip_1 = player.tue_additional_trip_1
            player.fri_start_time_1 = player.tue_start_time_1
            player.fri_distance_1 = player.tue_distance_1
            player.fri_duration_1 = player.tue_duration_1

            player.fri_additional_trip_2 = player.tue_additional_trip_2
            player.fri_start_time_2 = player.tue_start_time_2
            player.fri_distance_2 = player.tue_distance_2
            player.fri_duration_2 = player.tue_duration_2

            player.fri_additional_trip_3 = player.tue_additional_trip_3
            player.fri_start_time_3 = player.tue_start_time_3
            player.fri_distance_3 = player.tue_distance_3
            player.fri_duration_3 = player.tue_duration_3

            player.fri_additional_trip_4 = player.tue_additional_trip_4
            player.fri_start_time_4 = player.tue_start_time_4
            player.fri_distance_4 = player.tue_distance_4
            player.fri_duration_4 = player.tue_duration_4

            player.fri_additional_trip_5 = player.tue_additional_trip_5
            player.fri_start_time_5 = player.tue_start_time_5
            player.fri_distance_5 = player.tue_distance_5
            player.fri_duration_5 = player.tue_duration_5

            player.fri_additional_trip_6 = player.tue_additional_trip_6
            player.fri_start_time_6 = player.tue_start_time_6
            player.fri_distance_6 = player.tue_distance_6
            player.fri_duration_6 = player.tue_duration_6

            player.fri_additional_trip_7 = player.tue_additional_trip_7
            player.fri_start_time_7 = player.tue_start_time_7
            player.fri_distance_7 = player.tue_distance_7
            player.fri_duration_7 = player.tue_duration_7

            player.fri_additional_trip_8 = player.tue_additional_trip_8
            player.fri_start_time_8 = player.tue_start_time_8
            player.fri_distance_8 = player.tue_distance_8
            player.fri_duration_8 = player.tue_duration_8

            player.fri_additional_trip_9 = player.tue_additional_trip_9
            player.fri_start_time_9 = player.tue_start_time_9
            player.fri_distance_9 = player.tue_distance_9
            player.fri_duration_9 = player.tue_duration_9

            player.fri_additional_trip_10 = player.tue_additional_trip_10
            player.fri_start_time_10 = player.tue_start_time_10
            player.fri_distance_10 = player.tue_distance_10
            player.fri_duration_10 = player.tue_duration_10

        elif player.participant.vars.get('Friday', False):
            player.fri_first_trip = player.mo_first_trip
            player.fri_last_trip = player.mo_last_trip

            player.fri_additional_trip_1 = player.mo_additional_trip_1
            player.fri_start_time_1 = player.mo_start_time_1
            player.fri_distance_1 = player.mo_distance_1
            player.fri_duration_1 = player.mo_duration_1

            player.fri_additional_trip_2 = player.mo_additional_trip_2
            player.fri_start_time_2 = player.mo_start_time_2
            player.fri_distance_2 = player.mo_distance_2
            player.fri_duration_2 = player.mo_duration_2

            player.fri_additional_trip_3 = player.mo_additional_trip_3
            player.fri_start_time_3 = player.mo_start_time_3
            player.fri_distance_3 = player.mo_distance_3
            player.fri_duration_3 = player.mo_duration_3

            player.fri_additional_trip_4 = player.mo_additional_trip_4
            player.fri_start_time_4 = player.mo_start_time_4
            player.fri_distance_4 = player.mo_distance_4
            player.fri_duration_4 = player.mo_duration_4

            player.fri_additional_trip_5 = player.mo_additional_trip_5
            player.fri_start_time_5 = player.mo_start_time_5
            player.fri_distance_5 = player.mo_distance_5
            player.fri_duration_5 = player.mo_duration_5

            player.fri_additional_trip_6 = player.mo_additional_trip_6
            player.fri_start_time_6 = player.mo_start_time_6
            player.fri_distance_6 = player.mo_distance_6
            player.fri_duration_6 = player.mo_duration_6

            player.fri_additional_trip_7 = player.mo_additional_trip_7
            player.fri_start_time_7 = player.mo_start_time_7
            player.fri_distance_7 = player.mo_distance_7
            player.fri_duration_7 = player.mo_duration_7

            player.fri_additional_trip_8 = player.mo_additional_trip_8
            player.fri_start_time_8 = player.mo_start_time_8
            player.fri_distance_8 = player.mo_distance_8
            player.fri_duration_8 = player.mo_duration_8

            player.fri_additional_trip_9 = player.mo_additional_trip_9
            player.fri_start_time_9 = player.mo_start_time_9
            player.fri_distance_9 = player.mo_distance_9
            player.fri_duration_9 = player.mo_duration_9

            player.fri_additional_trip_10 = player.mo_additional_trip_10
            player.fri_start_time_10 = player.mo_start_time_10
            player.fri_distance_10 = player.mo_distance_10
            player.fri_duration_10 = player.mo_duration_10

        elif player.participant.vars.get('Friday_wed', False):
            player.fri_first_trip = player.wed_first_trip
            player.fri_last_trip = player.wed_last_trip

            player.fri_additional_trip_1 = player.wed_additional_trip_1
            player.fri_start_time_1 = player.wed_start_time_1
            player.fri_distance_1 = player.wed_distance_1
            player.fri_duration_1 = player.wed_duration_1

            player.fri_additional_trip_2 = player.wed_additional_trip_2
            player.fri_start_time_2 = player.wed_start_time_2
            player.fri_distance_2 = player.wed_distance_2
            player.fri_duration_2 = player.wed_duration_2

            player.fri_additional_trip_3 = player.wed_additional_trip_3
            player.fri_start_time_3 = player.wed_start_time_3
            player.fri_distance_3 = player.wed_distance_3
            player.fri_duration_3 = player.wed_duration_3

            player.fri_additional_trip_4 = player.wed_additional_trip_4
            player.fri_start_time_4 = player.wed_start_time_4
            player.fri_distance_4 = player.wed_distance_4
            player.fri_duration_4 = player.wed_duration_4

            player.fri_additional_trip_5 = player.wed_additional_trip_5
            player.fri_start_time_5 = player.wed_start_time_5
            player.fri_distance_5 = player.wed_distance_5
            player.fri_duration_5 = player.wed_duration_5

            player.fri_additional_trip_6 = player.wed_additional_trip_6
            player.fri_start_time_6 = player.wed_start_time_6
            player.fri_distance_6 = player.wed_distance_6
            player.fri_duration_6 = player.wed_duration_6

            player.fri_additional_trip_7 = player.wed_additional_trip_7
            player.fri_start_time_7 = player.wed_start_time_7
            player.fri_distance_7 = player.wed_distance_7
            player.fri_duration_7 = player.wed_duration_7

            player.fri_additional_trip_8 = player.wed_additional_trip_8
            player.fri_start_time_8 = player.wed_start_time_8
            player.fri_distance_8 = player.wed_distance_8
            player.fri_duration_8 = player.wed_duration_8

            player.fri_additional_trip_9 = player.wed_additional_trip_9
            player.fri_start_time_9 = player.wed_start_time_9
            player.fri_distance_9 = player.wed_distance_9
            player.fri_duration_9 = player.wed_duration_9

            player.fri_additional_trip_10 = player.wed_additional_trip_10
            player.fri_start_time_10 = player.wed_start_time_10
            player.fri_distance_10 = player.wed_distance_10
            player.fri_duration_10 = player.wed_duration_10

        elif player.participant.vars.get('Friday_thu', False):
            player.fri_first_trip = player.thu_first_trip
            player.fri_last_trip = player.thu_last_trip

            player.fri_additional_trip_1 = player.thu_additional_trip_1
            player.fri_start_time_1 = player.thu_start_time_1
            player.fri_distance_1 = player.thu_distance_1
            player.fri_duration_1 = player.thu_duration_1

            player.fri_additional_trip_2 = player.thu_additional_trip_2
            player.fri_start_time_2 = player.thu_start_time_2
            player.fri_distance_2 = player.thu_distance_2
            player.fri_duration_2 = player.thu_duration_2

            player.fri_additional_trip_3 = player.thu_additional_trip_3
            player.fri_start_time_3 = player.thu_start_time_3
            player.fri_distance_3 = player.thu_distance_3
            player.fri_duration_3 = player.thu_duration_3

            player.fri_additional_trip_4 = player.thu_additional_trip_4
            player.fri_start_time_4 = player.thu_start_time_4
            player.fri_distance_4 = player.thu_distance_4
            player.fri_duration_4 = player.thu_duration_4

            player.fri_additional_trip_5 = player.thu_additional_trip_5
            player.fri_start_time_5 = player.thu_start_time_5
            player.fri_distance_5 = player.thu_distance_5
            player.fri_duration_5 = player.thu_duration_5

            player.fri_additional_trip_6 = player.thu_additional_trip_6
            player.fri_start_time_6 = player.thu_start_time_6
            player.fri_distance_6 = player.thu_distance_6
            player.fri_duration_6 = player.thu_duration_6

            player.fri_additional_trip_7 = player.thu_additional_trip_7
            player.fri_start_time_7 = player.thu_start_time_7
            player.fri_distance_7 = player.thu_distance_7
            player.fri_duration_7 = player.thu_duration_7

            player.fri_additional_trip_8 = player.thu_additional_trip_8
            player.fri_start_time_8 = player.thu_start_time_8
            player.fri_distance_8 = player.thu_distance_8
            player.fri_duration_8 = player.thu_duration_8

            player.fri_additional_trip_9 = player.thu_additional_trip_9
            player.fri_start_time_9 = player.thu_start_time_9
            player.fri_distance_9 = player.thu_distance_9
            player.fri_duration_9 = player.thu_duration_9

            player.fri_additional_trip_10 = player.thu_additional_trip_10
            player.fri_start_time_10 = player.thu_start_time_10
            player.fri_distance_10 = player.thu_distance_10
            player.fri_duration_10 = player.thu_duration_10

        return fields


class Saturday(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['Sunday_sat'] = player.Sunday_sat
        player.participant.vars['sat_last_trip'] = player.sat_last_trip

    form_model = 'player'
    form_fields = [
        'sat_first_trip', 'sat_last_trip', 'sat_additional_trip_1', 'sat_start_time_1', 'sat_duration_1',
        'sat_distance_1',
        'sat_additional_trip_2', 'sat_start_time_2', 'sat_duration_2', 'sat_distance_2', 'sat_additional_trip_3',
        'sat_start_time_3', 'sat_duration_3', 'sat_distance_3', 'sat_additional_trip_4', 'sat_start_time_4',
        'sat_duration_4', 'sat_distance_4', 'sat_additional_trip_5', 'sat_start_time_5', 'sat_duration_5',
        'sat_distance_5', 'sat_additional_trip_6', 'sat_start_time_6', 'sat_duration_6', 'sat_distance_6',
        'sat_additional_trip_7', 'sat_start_time_7', 'sat_duration_7', 'sat_distance_7', 'sat_additional_trip_8',
        'sat_start_time_8', 'sat_duration_8', 'sat_distance_8', 'sat_additional_trip_9', 'sat_start_time_9',
        'sat_duration_9', 'sat_distance_9', 'sat_additional_trip_10', 'sat_start_time_10', 'sat_duration_10',
        'sat_distance_10', 'Sunday_sat'
    ]

    def vars_for_template(player: Player):
        initial_values = {
            'sat_first_trip': player.tue_first_trip if player.participant.vars.get('Saturday_tue', False) else player.mo_first_trip if player.participant.vars.get('Saturday', False) else player.wed_first_trip if player.participant.vars.get('Saturday_wed', False) else player.thu_first_trip if player.participant.vars.get('Saturday_thu', False) else player.fri_first_trip if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_last_trip': player.tue_last_trip if player.participant.vars.get('Saturday_tue', False) else player.mo_last_trip if player.participant.vars.get('Saturday', False) else player.wed_first_trip if player.participant.vars.get('Saturday_wed', False) else player.thu_first_trip if player.participant.vars.get('Saturday_thu', False) else player.fri_first_trip if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_1': player.tue_additional_trip_1 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_1 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_1 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_1 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_1 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_1': player.tue_start_time_1 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_1 if player.participant.vars.get('Saturday', False) else player.wed_start_time_1 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_1 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_1 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_1': player.tue_duration_1 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_1 if player.participant.vars.get('Saturday', False) else player.wed_duration_1 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_1 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_1 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_1': player.tue_distance_1 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_1 if player.participant.vars.get('Saturday', False) else player.wed_distance_1 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_1 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_1 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_2': player.tue_additional_trip_2 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_2 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_2 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_2 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_2 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_2': player.tue_start_time_2 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_2 if player.participant.vars.get('Saturday', False) else player.wed_start_time_2 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_2 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_2 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_2': player.tue_duration_2 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_2 if player.participant.vars.get('Saturday', False) else player.wed_duration_2 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_2 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_2 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_2': player.tue_distance_2 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_2 if player.participant.vars.get('Saturday', False) else player.wed_distance_2 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_2 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_2 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_3': player.tue_additional_trip_3 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_3 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_3 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_3 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_3 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_3': player.tue_start_time_3 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_3 if player.participant.vars.get('Saturday', False) else player.wed_start_time_3 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_3 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_3 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_3': player.tue_duration_3 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_3 if player.participant.vars.get('Saturday', False) else player.wed_duration_3 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_3 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_3 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_3': player.tue_distance_3 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_3 if player.participant.vars.get('Saturday', False) else player.wed_distance_3 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_3 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_3 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_4': player.tue_additional_trip_4 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_4 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_4 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_4 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_4 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_4': player.tue_start_time_4 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_4 if player.participant.vars.get('Saturday', False) else player.wed_start_time_4 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_4 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_4 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_4': player.tue_duration_4 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_4 if player.participant.vars.get('Saturday', False) else player.wed_duration_4 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_4 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_4 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_4': player.tue_distance_4 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_4 if player.participant.vars.get('Saturday', False) else player.wed_duration_4 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_4 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_4 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_5': player.tue_additional_trip_5 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_5 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_5 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_5 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_5 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_5': player.tue_start_time_5 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_5 if player.participant.vars.get('Saturday', False) else player.wed_start_time_5 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_5 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_5 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_5': player.tue_duration_5 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_5 if player.participant.vars.get('Saturday', False) else player.wed_duration_5 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_5 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_5 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_5': player.tue_distance_5 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_5 if player.participant.vars.get('Saturday', False) else player.wed_distance_5 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_5 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_5 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_6': player.tue_additional_trip_6 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_6 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_6 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_6 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_6 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_6': player.tue_start_time_6 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_6 if player.participant.vars.get('Saturday', False) else player.wed_start_time_6 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_6 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_6 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_6': player.tue_duration_6 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_6 if player.participant.vars.get('Saturday', False) else player.wed_duration_6 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_6 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_6 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_6': player.tue_distance_6 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_6 if player.participant.vars.get('Saturday', False) else player.wed_distance_6 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_6 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_6 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_7': player.tue_additional_trip_7 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_7 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_7 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_7 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_7 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_7': player.tue_start_time_7 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_7 if player.participant.vars.get('Saturday', False) else player.wed_start_time_7 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_7 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_7 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_7': player.tue_duration_7 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_7 if player.participant.vars.get('Saturday', False) else player.wed_duration_7 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_7 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_7 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_7': player.tue_distance_7 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_7 if player.participant.vars.get('Saturday', False) else player.wed_distance_7 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_7 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_7 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_8': player.tue_additional_trip_8 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_8 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_8 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_8 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_8 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_8': player.tue_start_time_8 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_8 if player.participant.vars.get('Saturday', False) else player.wed_start_time_8 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_8 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_8 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_8': player.tue_duration_8 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_8 if player.participant.vars.get('Saturday', False) else player.wed_duration_8 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_8 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_8 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_8': player.tue_distance_8 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_8 if player.participant.vars.get('Saturday', False) else player.wed_distance_8 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_8 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_8 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_9': player.tue_additional_trip_9 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_9 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_9 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_9 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_9 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_9': player.tue_start_time_9 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_9 if player.participant.vars.get('Saturday', False) else player.wed_start_time_9 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_9 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_9 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_9': player.tue_duration_9 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_9 if player.participant.vars.get('Saturday', False) else player.wed_duration_9 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_9 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_9 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_9': player.tue_distance_9 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_9 if player.participant.vars.get('Saturday', False) else player.wed_distance_9 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_9 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_9 if player.participant.vars.get('Saturday_fri', False) else None,

            'sat_additional_trip_10': player.tue_additional_trip_10 if player.participant.vars.get('Saturday_tue', False) else player.mo_additional_trip_10 if player.participant.vars.get('Saturday', False) else player.wed_additional_trip_10 if player.participant.vars.get('Saturday_wed', False) else player.thu_additional_trip_10 if player.participant.vars.get('Saturday_thu', False) else player.fri_additional_trip_10 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_start_time_10': player.tue_start_time_10 if player.participant.vars.get('Saturday_tue', False) else player.mo_start_time_10 if player.participant.vars.get('Saturday', False) else player.wed_start_time_10 if player.participant.vars.get('Saturday_wed', False) else player.thu_start_time_10 if player.participant.vars.get('Saturday_thu', False) else player.fri_start_time_10 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_duration_10': player.tue_duration_10 if player.participant.vars.get('Saturday_tue', False) else player.mo_duration_10 if player.participant.vars.get('Saturday', False) else player.wed_duration_10 if player.participant.vars.get('Saturday_wed', False) else player.thu_duration_10 if player.participant.vars.get('Saturday_thu', False) else player.fri_duration_10 if player.participant.vars.get('Saturday_fri', False) else None,
            'sat_distance_10': player.tue_distance_10 if player.participant.vars.get('Saturday_tue', False) else player.mo_distance_10 if player.participant.vars.get('Saturday', False) else player.wed_distance_10 if player.participant.vars.get('Saturday_wed', False) else player.thu_distance_10 if player.participant.vars.get('Saturday_thu', False) else player.fri_distance_10 if player.participant.vars.get('Saturday_fri', False) else None,

            'Saturday_fri': player.participant.vars.get('Saturday_fri', False),
            'Sunday_fri': player.participant.vars.get('Sunday_fri', False)
        }

        sat_additional_trips = [
            getattr(player, 'sat_additional_trip_1', '') or '',
            getattr(player, 'sat_additional_trip_2', '') or '',
            getattr(player, 'sat_additional_trip_3', '') or '',
            getattr(player, 'sat_additional_trip_4', '') or '',
            getattr(player, 'sat_additional_trip_5', '') or '',
            getattr(player, 'sat_additional_trip_6', '') or '',
            getattr(player, 'sat_additional_trip_7', '') or '',
            getattr(player, 'sat_additional_trip_8', '') or '',
            getattr(player, 'sat_additional_trip_9', '') or '',
            getattr(player, 'sat_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': sat_additional_trips,
            'days': C.DAYS_sat,
            'initial_values': initial_values
        }

    def get_form_fields(player: Player):
        fields = [
            'sat_first_trip', 'sat_last_trip', 'sat_additional_trip_1', 'sat_start_time_1', 'sat_duration_1','sat_distance_1',
            'sat_additional_trip_2', 'sat_start_time_2', 'sat_duration_2', 'sat_distance_2', 'sat_additional_trip_3',
            'sat_start_time_3', 'sat_duration_3', 'sat_distance_3', 'sat_additional_trip_4', 'sat_start_time_4',
            'sat_duration_4', 'sat_distance_4', 'sat_additional_trip_5', 'sat_start_time_5', 'sat_duration_5',
            'sat_distance_5', 'sat_additional_trip_6', 'sat_start_time_6', 'sat_duration_6', 'sat_distance_6',
            'sat_additional_trip_7', 'sat_start_time_7', 'sat_duration_7', 'sat_distance_7', 'sat_additional_trip_8',
            'sat_start_time_8', 'sat_duration_8', 'sat_distance_8', 'sat_additional_trip_9', 'sat_start_time_9',
            'sat_duration_9', 'sat_distance_9', 'sat_additional_trip_10', 'sat_start_time_10', 'sat_duration_10',
            'sat_distance_10', 'Sunday_sat'
        ]

        if player.participant.vars.get('Saturday_tue', False):
            player.sat_first_trip = player.tue_first_trip
            player.sat_last_trip = player.tue_last_trip

            player.sat_additional_trip_1 = player.tue_additional_trip_1
            player.sat_start_time_1 = player.tue_start_time_1
            player.sat_distance_1 = player.tue_distance_1
            player.sat_duration_1 = player.tue_duration_1

            player.sat_additional_trip_2 = player.tue_additional_trip_2
            player.sat_start_time_2 = player.tue_start_time_2
            player.sat_distance_2 = player.tue_distance_2
            player.sat_duration_2 = player.tue_duration_2

            player.sat_additional_trip_3 = player.tue_additional_trip_3
            player.sat_start_time_3 = player.tue_start_time_3
            player.sat_distance_3 = player.tue_distance_3
            player.sat_duration_3 = player.tue_duration_3

            player.sat_additional_trip_4 = player.tue_additional_trip_4
            player.sat_start_time_4 = player.tue_start_time_4
            player.sat_distance_4 = player.tue_distance_4
            player.sat_duration_4 = player.tue_duration_4

            player.sat_additional_trip_5 = player.tue_additional_trip_5
            player.sat_start_time_5 = player.tue_start_time_5
            player.sat_distance_5 = player.tue_distance_5
            player.sat_duration_5 = player.tue_duration_5

            player.sat_additional_trip_6 = player.tue_additional_trip_6
            player.sat_start_time_6 = player.tue_start_time_6
            player.sat_distance_6 = player.tue_distance_6
            player.sat_duration_6 = player.tue_duration_6

            player.sat_additional_trip_7 = player.tue_additional_trip_7
            player.sat_start_time_7 = player.tue_start_time_7
            player.sat_distance_7 = player.tue_distance_7
            player.sat_duration_7 = player.tue_duration_7

            player.sat_additional_trip_8 = player.tue_additional_trip_8
            player.sat_start_time_8 = player.tue_start_time_8
            player.sat_distance_8 = player.tue_distance_8
            player.sat_duration_8 = player.tue_duration_8

            player.sat_additional_trip_9 = player.tue_additional_trip_9
            player.sat_start_time_9 = player.tue_start_time_9
            player.sat_distance_9 = player.tue_distance_9
            player.sat_duration_9 = player.tue_duration_9

            player.sat_additional_trip_10 = player.tue_additional_trip_10
            player.sat_start_time_10 = player.tue_start_time_10
            player.sat_distance_10 = player.tue_distance_10
            player.sat_duration_10 = player.tue_duration_10

        elif player.participant.vars.get('Saturday', False):
            player.sat_first_trip = player.mo_first_trip
            player.sat_last_trip = player.mo_last_trip

            player.sat_additional_trip_1 = player.mo_additional_trip_1
            player.sat_start_time_1 = player.mo_start_time_1
            player.sat_distance_1 = player.mo_distance_1
            player.sat_duration_1 = player.mo_duration_1

            player.sat_additional_trip_2 = player.mo_additional_trip_2
            player.sat_start_time_2 = player.mo_start_time_2
            player.sat_distance_2 = player.mo_distance_2
            player.sat_duration_2 = player.mo_duration_2

            player.sat_additional_trip_3 = player.mo_additional_trip_3
            player.sat_start_time_3 = player.mo_start_time_3
            player.sat_distance_3 = player.mo_distance_3
            player.sat_duration_3 = player.mo_duration_3

            player.sat_additional_trip_4 = player.mo_additional_trip_4
            player.sat_start_time_4 = player.mo_start_time_4
            player.sat_distance_4 = player.mo_distance_4
            player.sat_duration_4 = player.mo_duration_4

            player.sat_additional_trip_5 = player.mo_additional_trip_5
            player.sat_start_time_5 = player.mo_start_time_5
            player.sat_distance_5 = player.mo_distance_5
            player.sat_duration_5 = player.mo_duration_5

            player.sat_additional_trip_6 = player.mo_additional_trip_6
            player.sat_start_time_6 = player.mo_start_time_6
            player.sat_distance_6 = player.mo_distance_6
            player.sat_duration_6 = player.mo_duration_6

            player.sat_additional_trip_7 = player.mo_additional_trip_7
            player.sat_start_time_7 = player.mo_start_time_7
            player.sat_distance_7 = player.mo_distance_7
            player.sat_duration_7 = player.mo_duration_7

            player.sat_additional_trip_8 = player.mo_additional_trip_8
            player.sat_start_time_8 = player.mo_start_time_8
            player.sat_distance_8 = player.mo_distance_8
            player.sat_duration_8 = player.mo_duration_8

            player.sat_additional_trip_9 = player.mo_additional_trip_9
            player.sat_start_time_9 = player.mo_start_time_9
            player.sat_distance_9 = player.mo_distance_9
            player.sat_duration_9 = player.mo_duration_9

            player.sat_additional_trip_10 = player.mo_additional_trip_10
            player.sat_start_time_10 = player.mo_start_time_10
            player.sat_distance_10 = player.mo_distance_10
            player.sat_duration_10 = player.mo_duration_10

        elif player.participant.vars.get('Saturday_wed', False):
            player.sat_first_trip = player.wed_first_trip
            player.sat_last_trip = player.wed_last_trip

            player.sat_additional_trip_1 = player.wed_additional_trip_1
            player.sat_start_time_1 = player.wed_start_time_1
            player.sat_distance_1 = player.wed_distance_1
            player.sat_duration_1 = player.wed_duration_1

            player.sat_additional_trip_2 = player.wed_additional_trip_2
            player.sat_start_time_2 = player.wed_start_time_2
            player.sat_distance_2 = player.wed_distance_2
            player.sat_duration_2 = player.wed_duration_2

            player.sat_additional_trip_3 = player.wed_additional_trip_3
            player.sat_start_time_3 = player.wed_start_time_3
            player.sat_distance_3 = player.wed_distance_3
            player.sat_duration_3 = player.wed_duration_3

            player.sat_additional_trip_4 = player.wed_additional_trip_4
            player.sat_start_time_4 = player.wed_start_time_4
            player.sat_distance_4 = player.wed_distance_4
            player.sat_duration_4 = player.wed_duration_4

            player.sat_additional_trip_5 = player.wed_additional_trip_5
            player.sat_start_time_5 = player.wed_start_time_5
            player.sat_distance_5 = player.wed_distance_5
            player.sat_duration_5 = player.wed_duration_5

            player.sat_additional_trip_6 = player.wed_additional_trip_6
            player.sat_start_time_6 = player.wed_start_time_6
            player.sat_distance_6 = player.wed_distance_6
            player.sat_duration_6 = player.wed_duration_6

            player.sat_additional_trip_7 = player.wed_additional_trip_7
            player.sat_start_time_7 = player.wed_start_time_7
            player.sat_distance_7 = player.wed_distance_7
            player.sat_duration_7 = player.wed_duration_7

            player.sat_additional_trip_8 = player.wed_additional_trip_8
            player.sat_start_time_8 = player.wed_start_time_8
            player.sat_distance_8 = player.wed_distance_8
            player.sat_duration_8 = player.wed_duration_8

            player.sat_additional_trip_9 = player.wed_additional_trip_9
            player.sat_start_time_9 = player.wed_start_time_9
            player.sat_distance_9 = player.wed_distance_9
            player.sat_duration_9 = player.wed_duration_9

            player.sat_additional_trip_10 = player.wed_additional_trip_10
            player.sat_start_time_10 = player.wed_start_time_10
            player.sat_distance_10 = player.wed_distance_10
            player.sat_duration_10 = player.wed_duration_10

        elif player.participant.vars.get('Saturday_thu', False):
            player.sat_first_trip = player.thu_first_trip
            player.sat_last_trip = player.thu_last_trip

            player.sat_additional_trip_1 = player.thu_additional_trip_1
            player.sat_start_time_1 = player.thu_start_time_1
            player.sat_distance_1 = player.thu_distance_1
            player.sat_duration_1 = player.thu_duration_1

            player.sat_additional_trip_2 = player.thu_additional_trip_2
            player.sat_start_time_2 = player.thu_start_time_2
            player.sat_distance_2 = player.thu_distance_2
            player.sat_duration_2 = player.thu_duration_2

            player.sat_additional_trip_3 = player.thu_additional_trip_3
            player.sat_start_time_3 = player.thu_start_time_3
            player.sat_distance_3 = player.thu_distance_3
            player.sat_duration_3 = player.thu_duration_3

            player.sat_additional_trip_4 = player.thu_additional_trip_4
            player.sat_start_time_4 = player.thu_start_time_4
            player.sat_distance_4 = player.thu_distance_4
            player.sat_duration_4 = player.thu_duration_4

            player.sat_additional_trip_5 = player.thu_additional_trip_5
            player.sat_start_time_5 = player.thu_start_time_5
            player.sat_distance_5 = player.thu_distance_5
            player.sat_duration_5 = player.thu_duration_5

            player.sat_additional_trip_6 = player.thu_additional_trip_6
            player.sat_start_time_6 = player.thu_start_time_6
            player.sat_distance_6 = player.thu_distance_6
            player.sat_duration_6 = player.thu_duration_6

            player.sat_additional_trip_7 = player.thu_additional_trip_7
            player.sat_start_time_7 = player.thu_start_time_7
            player.sat_distance_7 = player.thu_distance_7
            player.sat_duration_7 = player.thu_duration_7

            player.sat_additional_trip_8 = player.thu_additional_trip_8
            player.sat_start_time_8 = player.thu_start_time_8
            player.sat_distance_8 = player.thu_distance_8
            player.sat_duration_8 = player.thu_duration_8

            player.sat_additional_trip_9 = player.thu_additional_trip_9
            player.sat_start_time_9 = player.thu_start_time_9
            player.sat_distance_9 = player.thu_distance_9
            player.sat_duration_9 = player.thu_duration_9

            player.sat_additional_trip_10 = player.thu_additional_trip_10
            player.sat_start_time_10 = player.thu_start_time_10
            player.sat_distance_10 = player.thu_distance_10
            player.sat_duration_10 = player.thu_duration_10

        elif player.participant.vars.get('Saturday_fri', False):
            player.sat_first_trip = player.fri_first_trip
            player.sat_last_trip = player.fri_last_trip

            player.sat_additional_trip_1 = player.fri_additional_trip_1
            player.sat_start_time_1 = player.fri_start_time_1
            player.sat_distance_1 = player.fri_distance_1
            player.sat_duration_1 = player.fri_duration_1

            player.sat_additional_trip_2 = player.fri_additional_trip_2
            player.sat_start_time_2 = player.fri_start_time_2
            player.sat_distance_2 = player.fri_distance_2
            player.sat_duration_2 = player.fri_duration_2

            player.sat_additional_trip_3 = player.fri_additional_trip_3
            player.sat_start_time_3 = player.fri_start_time_3
            player.sat_distance_3 = player.fri_distance_3
            player.sat_duration_3 = player.fri_duration_3

            player.sat_additional_trip_4 = player.fri_additional_trip_4
            player.sat_start_time_4 = player.fri_start_time_4
            player.sat_distance_4 = player.fri_distance_4
            player.sat_duration_4 = player.fri_duration_4

            player.sat_additional_trip_5 = player.fri_additional_trip_5
            player.sat_start_time_5 = player.fri_start_time_5
            player.sat_distance_5 = player.fri_distance_5
            player.sat_duration_5 = player.fri_duration_5

            player.sat_additional_trip_6 = player.fri_additional_trip_6
            player.sat_start_time_6 = player.fri_start_time_6
            player.sat_distance_6 = player.fri_distance_6
            player.sat_duration_6 = player.fri_duration_6

            player.sat_additional_trip_7 = player.fri_additional_trip_7
            player.sat_start_time_7 = player.fri_start_time_7
            player.sat_distance_7 = player.fri_distance_7
            player.sat_duration_7 = player.fri_duration_7

            player.sat_additional_trip_8 = player.fri_additional_trip_8
            player.sat_start_time_8 = player.fri_start_time_8
            player.sat_distance_8 = player.fri_distance_8
            player.sat_duration_8 = player.fri_duration_8

            player.sat_additional_trip_9 = player.fri_additional_trip_9
            player.sat_start_time_9 = player.fri_start_time_9
            player.sat_distance_9 = player.fri_distance_9
            player.sat_duration_9 = player.fri_duration_9

            player.sat_additional_trip_10 = player.fri_additional_trip_10
            player.sat_start_time_10 = player.fri_start_time_10
            player.sat_distance_10 = player.fri_distance_10
            player.sat_duration_10 = player.fri_duration_10

        return fields


class Sunday(Page):
    form_model = 'player'
    form_fields = [
        'sun_first_trip', 'sun_last_trip', 'sun_additional_trip_1', 'sun_start_time_1', 'sun_duration_1',
        'sun_distance_1',
        'sun_additional_trip_2', 'sun_start_time_2', 'sun_duration_2', 'sun_distance_2', 'sun_additional_trip_3',
        'sun_start_time_3', 'sun_duration_3', 'sun_distance_3', 'sun_additional_trip_4', 'sun_start_time_4',
        'sun_duration_4', 'sun_distance_4', 'sun_additional_trip_5', 'sun_start_time_5', 'sun_duration_5',
        'sun_distance_5', 'sun_additional_trip_6', 'sun_start_time_6', 'sun_duration_6', 'sun_distance_6',
        'sun_additional_trip_7', 'sun_start_time_7', 'sun_duration_7', 'sun_distance_7', 'sun_additional_trip_8',
        'sun_start_time_8', 'sun_duration_8', 'sun_distance_8', 'sun_additional_trip_9', 'sun_start_time_9',
        'sun_duration_9', 'sun_distance_9', 'sun_additional_trip_10', 'sun_start_time_10', 'sun_duration_10',
        'sun_distance_10'
    ]

    def vars_for_template(player: Player):
        initial_values = {
            'sun_first_trip': player.tue_first_trip if player.participant.vars.get('Sunday_tue', False) else player.mo_first_trip if player.participant.vars.get('Sunday', False) else player.wed_first_trip if player.participant.vars.get('Sunday_wed', False) else player.thu_first_trip if player.participant.vars.get('Sunday_thu', False) else player.fri_first_trip if player.participant.vars.get('Sunday_fri', False) else player.sat_first_trip if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_last_trip': player.tue_last_trip if player.participant.vars.get('Sunday_tue', False) else player.mo_last_trip if player.participant.vars.get('Sunday', False) else player.wed_first_trip if player.participant.vars.get('Sunday_wed', False) else player.thu_first_trip if player.participant.vars.get('Sunday_thu', False) else player.fri_first_trip if player.participant.vars.get('Sunday_fri', False) else player.sat_first_trip if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_1': player.tue_additional_trip_1 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_1 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_1 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_1 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_1 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_1 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_1': player.tue_start_time_1 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_1 if player.participant.vars.get('Sunday', False) else player.wed_start_time_1 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_1 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_1 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_1 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_1': player.tue_duration_1 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_1 if player.participant.vars.get('Sunday', False) else player.wed_duration_1 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_1 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_1 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_1 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_1': player.tue_distance_1 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_1 if player.participant.vars.get('Sunday', False) else player.wed_distance_1 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_1 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_1 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_1 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_2': player.tue_additional_trip_2 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_2 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_2 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_2 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_2 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_2 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_2': player.tue_start_time_2 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_2 if player.participant.vars.get('Sunday', False) else player.wed_start_time_2 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_2 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_2 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_2 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_2': player.tue_duration_2 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_2 if player.participant.vars.get('Sunday', False) else player.wed_duration_2 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_2 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_2 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_2 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_2': player.tue_distance_2 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_2 if player.participant.vars.get('Sunday', False) else player.wed_distance_2 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_2 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_2 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_2 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_3': player.tue_additional_trip_3 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_3 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_3 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_3 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_3 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_3 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_3': player.tue_start_time_3 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_3 if player.participant.vars.get('Sunday', False) else player.wed_start_time_3 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_3 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_3 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_3 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_3': player.tue_duration_3 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_3 if player.participant.vars.get('Sunday', False) else player.wed_duration_3 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_3 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_3 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_3 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_3': player.tue_distance_3 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_3 if player.participant.vars.get('Sunday', False) else player.wed_distance_3 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_3 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_3 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_3 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_4': player.tue_additional_trip_4 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_4 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_4 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_4 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_4 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_4 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_4': player.tue_start_time_4 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_4 if player.participant.vars.get('Sunday', False) else player.wed_start_time_4 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_4 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_4 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_4 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_4': player.tue_duration_4 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_4 if player.participant.vars.get('Sunday', False) else player.wed_duration_4 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_4 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_4 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_4 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_4': player.tue_distance_4 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_4 if player.participant.vars.get('Sunday', False) else player.wed_duration_4 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_4 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_4 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_4 if player.participant.vars.get('Sunday_sat', False)else None,

            'sun_additional_trip_5': player.tue_additional_trip_5 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_5 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_5 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_5 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_5 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_5 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_5': player.tue_start_time_5 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_5 if player.participant.vars.get('Sunday', False) else player.wed_start_time_5 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_5 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_5 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_5 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_5': player.tue_duration_5 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_5 if player.participant.vars.get('Sunday', False) else player.wed_duration_5 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_5 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_5 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_5 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_5': player.tue_distance_5 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_5 if player.participant.vars.get('Sunday', False) else player.wed_distance_5 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_5 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_5 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_5 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_6': player.tue_additional_trip_6 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_6 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_6 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_6 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_6 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_6 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_6': player.tue_start_time_6 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_6 if player.participant.vars.get('Sunday', False) else player.wed_start_time_6 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_6 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_6 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_6 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_6': player.tue_duration_6 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_6 if player.participant.vars.get('Sunday', False) else player.wed_duration_6 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_6 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_6 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_6 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_6': player.tue_distance_6 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_6 if player.participant.vars.get('Sunday', False) else player.wed_distance_6 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_6 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_6 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_6 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_7': player.tue_additional_trip_7 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_7 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_7 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_7 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_7 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_7 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_7': player.tue_start_time_7 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_7 if player.participant.vars.get('Sunday', False) else player.wed_start_time_7 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_7 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_7 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_7 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_7': player.tue_duration_7 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_7 if player.participant.vars.get('Sunday', False) else player.wed_duration_7 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_7 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_7 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_7 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_7': player.tue_distance_7 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_7 if player.participant.vars.get('Sunday', False) else player.wed_distance_7 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_7 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_7 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_7 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_8': player.tue_additional_trip_8 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_8 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_8 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_8 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_8 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_8 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_8': player.tue_start_time_8 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_8 if player.participant.vars.get('Sunday', False) else player.wed_start_time_8 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_8 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_8 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_8 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_8': player.tue_duration_8 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_8 if player.participant.vars.get('Sunday', False) else player.wed_duration_8 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_8 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_8 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_8 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_8': player.tue_distance_8 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_8 if player.participant.vars.get('Sunday', False) else player.wed_distance_8 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_8 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_8 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_8 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_9': player.tue_additional_trip_9 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_9 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_9 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_9 if player.participant.vars.get('Sunday_thu', False) else player.fri_additional_trip_9 if player.participant.vars.get('Sunday_fri', False) else player.sat_additional_trip_9 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_9': player.tue_start_time_9 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_9 if player.participant.vars.get('Sunday', False) else player.wed_start_time_9 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_9 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_9 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_9 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_9': player.tue_duration_9 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_9 if player.participant.vars.get('Sunday', False) else player.wed_duration_9 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_9 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_9 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_9 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_9': player.tue_distance_9 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_9 if player.participant.vars.get('Sunday', False) else player.wed_distance_9 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_9 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_9 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_9 if player.participant.vars.get('Sunday_sat', False) else None,

            'sun_additional_trip_10': player.tue_additional_trip_10 if player.participant.vars.get('Sunday_tue', False) else player.mo_additional_trip_10 if player.participant.vars.get('Sunday', False) else player.wed_additional_trip_10 if player.participant.vars.get('Sunday_wed', False) else player.thu_additional_trip_10 if player.participant.vars.get('Sunday_thu', False) else player.sat_additional_trip_10 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_start_time_10': player.tue_start_time_10 if player.participant.vars.get('Sunday_tue', False) else player.mo_start_time_10 if player.participant.vars.get('Sunday', False) else player.wed_start_time_10 if player.participant.vars.get('Sunday_wed', False) else player.thu_start_time_10 if player.participant.vars.get('Sunday_thu', False) else player.fri_start_time_10 if player.participant.vars.get('Sunday_fri', False) else player.sat_start_time_10 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_duration_10': player.tue_duration_10 if player.participant.vars.get('Sunday_tue', False) else player.mo_duration_10 if player.participant.vars.get('Sunday', False) else player.wed_duration_10 if player.participant.vars.get('Sunday_wed', False) else player.thu_duration_10 if player.participant.vars.get('Sunday_thu', False) else player.fri_duration_10 if player.participant.vars.get('Sunday_fri', False) else player.sat_duration_10 if player.participant.vars.get('Sunday_sat', False) else None,
            'sun_distance_10': player.tue_distance_10 if player.participant.vars.get('Sunday_tue', False) else player.mo_distance_10 if player.participant.vars.get('Sunday', False) else player.wed_distance_10 if player.participant.vars.get('Sunday_wed', False) else player.thu_distance_10 if player.participant.vars.get('Sunday_thu', False) else player.fri_distance_10 if player.participant.vars.get('Sunday_fri', False) else player.sat_distance_10 if player.participant.vars.get('Sunday_sat', False) else None,

            'Sunday_sat': player.participant.vars.get('Sunday_sat', False)
        }

        sun_additional_trips = [
            getattr(player, 'sun_additional_trip_1', '') or '',
            getattr(player, 'sun_additional_trip_2', '') or '',
            getattr(player, 'sun_additional_trip_3', '') or '',
            getattr(player, 'sun_additional_trip_4', '') or '',
            getattr(player, 'sun_additional_trip_5', '') or '',
            getattr(player, 'sun_additional_trip_6', '') or '',
            getattr(player, 'sun_additional_trip_7', '') or '',
            getattr(player, 'sun_additional_trip_8', '') or '',
            getattr(player, 'sun_additional_trip_9', '') or '',
            getattr(player, 'sun_additional_trip_10', '') or '',
        ]
        return {
            'additional_trips': sun_additional_trips,
            'initial_values': initial_values
        }

    def get_form_fields(player: Player):
        fields = [
            'sun_first_trip', 'sun_last_trip', 'sun_additional_trip_1', 'sun_start_time_1', 'sun_duration_1',
            'sun_distance_1',
            'sun_additional_trip_2', 'sun_start_time_2', 'sun_duration_2', 'sun_distance_2', 'sun_additional_trip_3',
            'sun_start_time_3', 'sun_duration_3', 'sun_distance_3', 'sun_additional_trip_4', 'sun_start_time_4',
            'sun_duration_4', 'sun_distance_4', 'sun_additional_trip_5', 'sun_start_time_5', 'sun_duration_5',
            'sun_distance_5', 'sun_additional_trip_6', 'sun_start_time_6', 'sun_duration_6', 'sun_distance_6',
            'sun_additional_trip_7', 'sun_start_time_7', 'sun_duration_7', 'sun_distance_7', 'sun_additional_trip_8',
            'sun_start_time_8', 'sun_duration_8', 'sun_distance_8', 'sun_additional_trip_9', 'sun_start_time_9',
            'sun_duration_9', 'sun_distance_9', 'sun_additional_trip_10', 'sun_start_time_10', 'sun_duration_10',
            'sun_distance_10'
        ]

        if player.participant.vars.get('Sunday_tue', False):
            player.sun_first_trip = player.tue_first_trip
            player.sun_last_trip = player.tue_last_trip

            player.sun_additional_trip_1 = player.tue_additional_trip_1
            player.sun_start_time_1 = player.tue_start_time_1
            player.sun_distance_1 = player.tue_distance_1
            player.sun_duration_1 = player.tue_duration_1

            player.sun_additional_trip_2 = player.tue_additional_trip_2
            player.sun_start_time_2 = player.tue_start_time_2
            player.sun_distance_2 = player.tue_distance_2
            player.sun_duration_2 = player.tue_duration_2

            player.sun_additional_trip_3 = player.tue_additional_trip_3
            player.sun_start_time_3 = player.tue_start_time_3
            player.sun_distance_3 = player.tue_distance_3
            player.sun_duration_3 = player.tue_duration_3

            player.sun_additional_trip_4 = player.tue_additional_trip_4
            player.sun_start_time_4 = player.tue_start_time_4
            player.sun_distance_4 = player.tue_distance_4
            player.sun_duration_4 = player.tue_duration_4

            player.sun_additional_trip_5 = player.tue_additional_trip_5
            player.sun_start_time_5 = player.tue_start_time_5
            player.sun_distance_5 = player.tue_distance_5
            player.sun_duration_5 = player.tue_duration_5

            player.sun_additional_trip_6 = player.tue_additional_trip_6
            player.sun_start_time_6 = player.tue_start_time_6
            player.sun_distance_6 = player.tue_distance_6
            player.sun_duration_6 = player.tue_duration_6

            player.sun_additional_trip_7 = player.tue_additional_trip_7
            player.sun_start_time_7 = player.tue_start_time_7
            player.sun_distance_7 = player.tue_distance_7
            player.sun_duration_7 = player.tue_duration_7

            player.sun_additional_trip_8 = player.tue_additional_trip_8
            player.sun_start_time_8 = player.tue_start_time_8
            player.sun_distance_8 = player.tue_distance_8
            player.sun_duration_8 = player.tue_duration_8

            player.sun_additional_trip_9 = player.tue_additional_trip_9
            player.sun_start_time_9 = player.tue_start_time_9
            player.sun_distance_9 = player.tue_distance_9
            player.sun_duration_9 = player.tue_duration_9

            player.sun_additional_trip_10 = player.tue_additional_trip_10
            player.sun_start_time_10 = player.tue_start_time_10
            player.sun_distance_10 = player.tue_distance_10
            player.sun_duration_10 = player.tue_duration_10

        elif player.participant.vars.get('Sunday', False):
            player.sun_first_trip = player.mo_first_trip
            player.sun_last_trip = player.mo_last_trip

            player.sun_additional_trip_1 = player.mo_additional_trip_1
            player.sun_start_time_1 = player.mo_start_time_1
            player.sun_distance_1 = player.mo_distance_1
            player.sun_duration_1 = player.mo_duration_1

            player.sun_additional_trip_2 = player.mo_additional_trip_2
            player.sun_start_time_2 = player.mo_start_time_2
            player.sun_distance_2 = player.mo_distance_2
            player.sun_duration_2 = player.mo_duration_2

            player.sun_additional_trip_3 = player.mo_additional_trip_3
            player.sun_start_time_3 = player.mo_start_time_3
            player.sun_distance_3 = player.mo_distance_3
            player.sun_duration_3 = player.mo_duration_3

            player.sun_additional_trip_4 = player.mo_additional_trip_4
            player.sun_start_time_4 = player.mo_start_time_4
            player.sun_distance_4 = player.mo_distance_4
            player.sun_duration_4 = player.mo_duration_4

            player.sun_additional_trip_5 = player.mo_additional_trip_5
            player.sun_start_time_5 = player.mo_start_time_5
            player.sun_distance_5 = player.mo_distance_5
            player.sun_duration_5 = player.mo_duration_5

            player.sun_additional_trip_6 = player.mo_additional_trip_6
            player.sun_start_time_6 = player.mo_start_time_6
            player.sun_distance_6 = player.mo_distance_6
            player.sun_duration_6 = player.mo_duration_6

            player.sun_additional_trip_7 = player.mo_additional_trip_7
            player.sun_start_time_7 = player.mo_start_time_7
            player.sun_distance_7 = player.mo_distance_7
            player.sun_duration_7 = player.mo_duration_7

            player.sun_additional_trip_8 = player.mo_additional_trip_8
            player.sun_start_time_8 = player.mo_start_time_8
            player.sun_distance_8 = player.mo_distance_8
            player.sun_duration_8 = player.mo_duration_8

            player.sun_additional_trip_9 = player.mo_additional_trip_9
            player.sun_start_time_9 = player.mo_start_time_9
            player.sun_distance_9 = player.mo_distance_9
            player.sun_duration_9 = player.mo_duration_9

            player.sun_additional_trip_10 = player.mo_additional_trip_10
            player.sun_start_time_10 = player.mo_start_time_10
            player.sun_distance_10 = player.mo_distance_10
            player.sun_duration_10 = player.mo_duration_10

        elif player.participant.vars.get('Sunday_wed', False):
            player.sun_first_trip = player.wed_first_trip
            player.sun_last_trip = player.wed_last_trip

            player.sun_additional_trip_1 = player.wed_additional_trip_1
            player.sun_start_time_1 = player.wed_start_time_1
            player.sun_distance_1 = player.wed_distance_1
            player.sun_duration_1 = player.wed_duration_1

            player.sun_additional_trip_2 = player.wed_additional_trip_2
            player.sun_start_time_2 = player.wed_start_time_2
            player.sun_distance_2 = player.wed_distance_2
            player.sun_duration_2 = player.wed_duration_2

            player.sun_additional_trip_3 = player.wed_additional_trip_3
            player.sun_start_time_3 = player.wed_start_time_3
            player.sun_distance_3 = player.wed_distance_3
            player.sun_duration_3 = player.wed_duration_3

            player.sun_additional_trip_4 = player.wed_additional_trip_4
            player.sun_start_time_4 = player.wed_start_time_4
            player.sun_distance_4 = player.wed_distance_4
            player.sun_duration_4 = player.wed_duration_4

            player.sun_additional_trip_5 = player.wed_additional_trip_5
            player.sun_start_time_5 = player.wed_start_time_5
            player.sun_distance_5 = player.wed_distance_5
            player.sun_duration_5 = player.wed_duration_5

            player.sun_additional_trip_6 = player.wed_additional_trip_6
            player.sun_start_time_6 = player.wed_start_time_6
            player.sun_distance_6 = player.wed_distance_6
            player.sun_duration_6 = player.wed_duration_6

            player.sun_additional_trip_7 = player.wed_additional_trip_7
            player.sun_start_time_7 = player.wed_start_time_7
            player.sun_distance_7 = player.wed_distance_7
            player.sun_duration_7 = player.wed_duration_7

            player.sun_additional_trip_8 = player.wed_additional_trip_8
            player.sun_start_time_8 = player.wed_start_time_8
            player.sun_distance_8 = player.wed_distance_8
            player.sun_duration_8 = player.wed_duration_8

            player.sun_additional_trip_9 = player.wed_additional_trip_9
            player.sun_start_time_9 = player.wed_start_time_9
            player.sun_distance_9 = player.wed_distance_9
            player.sun_duration_9 = player.wed_duration_9

            player.sun_additional_trip_10 = player.wed_additional_trip_10
            player.sun_start_time_10 = player.wed_start_time_10
            player.sun_distance_10 = player.wed_distance_10
            player.sun_duration_10 = player.wed_duration_10

        elif player.participant.vars.get('Sunday_thu', False):
            player.sun_first_trip = player.thu_first_trip
            player.sun_last_trip = player.thu_last_trip

            player.sun_additional_trip_1 = player.thu_additional_trip_1
            player.sun_start_time_1 = player.thu_start_time_1
            player.sun_distance_1 = player.thu_distance_1
            player.sun_duration_1 = player.thu_duration_1

            player.sun_additional_trip_2 = player.thu_additional_trip_2
            player.sun_start_time_2 = player.thu_start_time_2
            player.sun_distance_2 = player.thu_distance_2
            player.sun_duration_2 = player.thu_duration_2

            player.sun_additional_trip_3 = player.thu_additional_trip_3
            player.sun_start_time_3 = player.thu_start_time_3
            player.sun_distance_3 = player.thu_distance_3
            player.sun_duration_3 = player.thu_duration_3

            player.sun_additional_trip_4 = player.thu_additional_trip_4
            player.sun_start_time_4 = player.thu_start_time_4
            player.sun_distance_4 = player.thu_distance_4
            player.sun_duration_4 = player.thu_duration_4

            player.sun_additional_trip_5 = player.thu_additional_trip_5
            player.sun_start_time_5 = player.thu_start_time_5
            player.sun_distance_5 = player.thu_distance_5
            player.sun_duration_5 = player.thu_duration_5

            player.sun_additional_trip_6 = player.thu_additional_trip_6
            player.sun_start_time_6 = player.thu_start_time_6
            player.sun_distance_6 = player.thu_distance_6
            player.sun_duration_6 = player.thu_duration_6

            player.sun_additional_trip_7 = player.thu_additional_trip_7
            player.sun_start_time_7 = player.thu_start_time_7
            player.sun_distance_7 = player.thu_distance_7
            player.sun_duration_7 = player.thu_duration_7

            player.sun_additional_trip_8 = player.thu_additional_trip_8
            player.sun_start_time_8 = player.thu_start_time_8
            player.sun_distance_8 = player.thu_distance_8
            player.sun_duration_8 = player.thu_duration_8

            player.sun_additional_trip_9 = player.thu_additional_trip_9
            player.sun_start_time_9 = player.thu_start_time_9
            player.sun_distance_9 = player.thu_distance_9
            player.sun_duration_9 = player.thu_duration_9

            player.sun_additional_trip_10 = player.thu_additional_trip_10
            player.sun_start_time_10 = player.thu_start_time_10
            player.sun_distance_10 = player.thu_distance_10
            player.sun_duration_10 = player.thu_duration_10

        elif player.participant.vars.get('Sunday_fri', False):
            player.sun_first_trip = player.fri_first_trip
            player.sun_last_trip = player.fri_last_trip

            player.sun_additional_trip_1 = player.fri_additional_trip_1
            player.sun_start_time_1 = player.fri_start_time_1
            player.sun_distance_1 = player.fri_distance_1
            player.sun_duration_1 = player.fri_duration_1

            player.sun_additional_trip_2 = player.fri_additional_trip_2
            player.sun_start_time_2 = player.fri_start_time_2
            player.sun_distance_2 = player.fri_distance_2
            player.sun_duration_2 = player.fri_duration_2

            player.sun_additional_trip_3 = player.fri_additional_trip_3
            player.sun_start_time_3 = player.fri_start_time_3
            player.sun_distance_3 = player.fri_distance_3
            player.sun_duration_3 = player.fri_duration_3

            player.sun_additional_trip_4 = player.fri_additional_trip_4
            player.sun_start_time_4 = player.fri_start_time_4
            player.sun_distance_4 = player.fri_distance_4
            player.sun_duration_4 = player.fri_duration_4

            player.sun_additional_trip_5 = player.fri_additional_trip_5
            player.sun_start_time_5 = player.fri_start_time_5
            player.sun_distance_5 = player.fri_distance_5
            player.sun_duration_5 = player.fri_duration_5

            player.sun_additional_trip_6 = player.fri_additional_trip_6
            player.sun_start_time_6 = player.fri_start_time_6
            player.sun_distance_6 = player.fri_distance_6
            player.sun_duration_6 = player.fri_duration_6

            player.sun_additional_trip_7 = player.fri_additional_trip_7
            player.sun_start_time_7 = player.fri_start_time_7
            player.sun_distance_7 = player.fri_distance_7
            player.sun_duration_7 = player.fri_duration_7

            player.sun_additional_trip_8 = player.fri_additional_trip_8
            player.sun_start_time_8 = player.fri_start_time_8
            player.sun_distance_8 = player.fri_distance_8
            player.sun_duration_8 = player.fri_duration_8

            player.sun_additional_trip_9 = player.fri_additional_trip_9
            player.sun_start_time_9 = player.fri_start_time_9
            player.sun_distance_9 = player.fri_distance_9
            player.sun_duration_9 = player.fri_duration_9

            player.sun_additional_trip_10 = player.fri_additional_trip_10
            player.sun_start_time_10 = player.fri_start_time_10
            player.sun_distance_10 = player.fri_distance_10
            player.sun_duration_10 = player.fri_duration_10

        elif player.participant.vars.get('Sunday_sat', False):
            player.sun_first_trip = player.sat_first_trip
            player.sun_last_trip = player.sat_last_trip

            player.sun_additional_trip_1 = player.sat_additional_trip_1
            player.sun_start_time_1 = player.sat_start_time_1
            player.sun_distance_1 = player.sat_distance_1
            player.sun_duration_1 = player.sat_duration_1

            player.sun_additional_trip_2 = player.sat_additional_trip_2
            player.sun_start_time_2 = player.sat_start_time_2
            player.sun_distance_2 = player.sat_distance_2
            player.sun_duration_2 = player.sat_duration_2

            player.sun_additional_trip_3 = player.sat_additional_trip_3
            player.sun_start_time_3 = player.sat_start_time_3
            player.sun_distance_3 = player.sat_distance_3
            player.sun_duration_3 = player.sat_duration_3

            player.sun_additional_trip_4 = player.sat_additional_trip_4
            player.sun_start_time_4 = player.sat_start_time_4
            player.sun_distance_4 = player.sat_distance_4
            player.sun_duration_4 = player.sat_duration_4

            player.sun_additional_trip_5 = player.sat_additional_trip_5
            player.sun_start_time_5 = player.sat_start_time_5
            player.sun_distance_5 = player.sat_distance_5
            player.sun_duration_5 = player.sat_duration_5

            player.sun_additional_trip_6 = player.sat_additional_trip_6
            player.sun_start_time_6 = player.sat_start_time_6
            player.sun_distance_6 = player.sat_distance_6
            player.sun_duration_6 = player.sat_duration_6

            player.sun_additional_trip_7 = player.sat_additional_trip_7
            player.sun_start_time_7 = player.sat_start_time_7
            player.sun_distance_7 = player.sat_distance_7
            player.sun_duration_7 = player.sat_duration_7

            player.sun_additional_trip_8 = player.sat_additional_trip_8
            player.sun_start_time_8 = player.sat_start_time_8
            player.sun_distance_8 = player.sat_distance_8
            player.sun_duration_8 = player.sat_duration_8

            player.sun_additional_trip_9 = player.sat_additional_trip_9
            player.sun_start_time_9 = player.sat_start_time_9
            player.sun_distance_9 = player.sat_distance_9
            player.sun_duration_9 = player.sat_duration_9

            player.sun_additional_trip_10 = player.sat_additional_trip_10
            player.sun_start_time_10 = player.sat_start_time_10
            player.sun_distance_10 = player.sat_distance_10
            player.sun_duration_10 = player.sat_duration_10

        return fields


page_sequence = [Instruction, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
