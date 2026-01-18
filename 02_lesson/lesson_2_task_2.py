def is_year_leap(year: int) -> bool:
    if year % 4 == 0:
        return True
    return False


year = int(input("Введите год: "))

print(f"Год {year}: {is_year_leap(year)}")
