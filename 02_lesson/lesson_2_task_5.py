def month_to_season(month: int) -> str:
    if month <= 2 or month == 12:
        return "Зима"
    elif 2 < month <= 5:
        return "Весна"
    elif 5 < month <= 8:
        return "Лето"
    elif 8 < month <= 11:
        return "Осень"
    else:
        return "Введите правильный номер месяца"

print(month_to_season(int(input("Введите номер месяца: "))))
