def is_twodigit_odd(number):
    if number > 9:
        if number < 100:
            return True
    return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if sudo_mode:
        return True
    if writable_by_others:
        return True
    if user == file_owner:
        if writable_by_owner:
            return True
    if file_group in users_groups:
        if writable_by_group:
            return True
    return False


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False


def is_sunday(day, weekday_of_first):
    weekday = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]

    if (day + weekday.index(weekday_of_first)) % 7 == 0:
        return True
    return False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
