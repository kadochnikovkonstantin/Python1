def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        return "Зима"
    elif month <= 5:
        return "Весна"
    elif month >= 9 and month <= 11:
        return "Осень"
    else:
        return "Лето"
print(month_to_season(7))
