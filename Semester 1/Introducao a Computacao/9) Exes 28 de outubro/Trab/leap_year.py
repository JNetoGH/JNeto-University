def is_leap_year(year: int) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and not ((year % 100 == 0) and not (year % 400 == 0))):
        return True
    return False

print(is_leap_year(200))
print(is_leap_year(2004))
print(is_leap_year(2005))
