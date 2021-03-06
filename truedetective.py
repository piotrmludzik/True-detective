def is_twodigit_odd(number):
    return True if (number > 9 and number < 100) else False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return True if any([sudo_mode, writable_by_others, (file_owner == user and writable_by_owner), (file_group in users_groups and writable_by_group)]) else False


def is_leap_year(year):
    return True if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else False


def is_sunday(day, weekday_of_first):
    return True if (day + ["M", "Tu", "W", "Th", "F", "Sa", "Su"].index(weekday_of_first)) % 7 == 0 else False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return True if wind_scale < 7 and any([rains, cloudy and any([red_sky, strong_flower_smell, spiders_down, lying_cattle]), strong_sunshine]) else False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    return True if want_to and all([have_10m or have_30m, mad_boss is False, after_4pm is False, trouble_sleeping is False]) else False
