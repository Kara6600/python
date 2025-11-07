def is_year_leap(year):
    return year % 4 == 0

year_input = input("Введите год: ")

try:
    year = int(year_input)
    result = is_year_leap(year)
    print(f"год {year}: {result}")
# по приколу и на всякий случай
except ValueError:
    print("Пожалуйста, введите корректный числовой год.")  