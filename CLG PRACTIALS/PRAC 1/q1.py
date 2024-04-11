from datetime import datetime as dt
import calendar as cld

birth_date = 5 
birth_year = 1947
birth_month = 6

cur_date = dt.now()

age = (cur_date - dt(birth_year,birth_month,birth_date)).days // 365

print(f"my grandfather is {age} years old")

print("CALENDER")
print(cld.month(dt(birth_year,birth_month,birth_date).year , dt(birth_year,birth_month,birth_date).month))