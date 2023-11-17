from datetime import date


def get_birthday_per_week(users):
    date_today = date.today()
    my_dict = {}
    try:
        for user_dict in users:
            user_name = user_dict["name"].split(" ")[0]
            user_birthday_date = user_dict["birthday"]
            user_birthday_date_edit = date(date_today.year, user_birthday_date.month, user_birthday_date.day)
            day_of_week_str = user_birthday_date.strftime('%A')
            my_timedelta = (user_birthday_date_edit - date_today).days
            if 0 < my_timedelta < 7:
                if day_of_week_str == "Saturday" or day_of_week_str == "Sunday":
                    day_of_week_str = "Monday"
                try:
                    my_dict[day_of_week_str] = [user_name, ]
                except KeyError:
                    my_dict[day_of_week_str].append(user_name)
            else:
                continue
        return print(my_dict)
    except UnboundLocalError:
        return {}
