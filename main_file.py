import datetime
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    now_date = datetime.now().date()  # --> ####-##-##
    my_dict = {}

    for user in users:
        his_date_of_birth = user['birthday']  # datetime(1955, 10, 28).date() --> 1995-10-28
        his_date_of_birth_in_this_year = datetime(now_date.year, his_date_of_birth.month, his_date_of_birth.day).date()
        delta = timedelta(weeks=1)

        if now_date + delta >= his_date_of_birth_in_this_year:
            the_day_of_birth = his_date_of_birth_in_this_year.strftime('%A')

            if the_day_of_birth in my_dict:
                my_dict[the_day_of_birth].append(user["name"])
            else:
                my_dict[the_day_of_birth] = [user["name"], ]

    return my_dict
