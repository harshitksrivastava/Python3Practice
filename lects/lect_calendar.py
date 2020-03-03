
import calendar

# technique 1
weekdays = {1: 'MONDAY', 2: 'TUESDAY', 3: 'WEDNESDAY', 4: 'THURSDAY', 5: 'FRIDAY', 6: 'SATURDAY', 0: 'SUNDAY'}
day, month, year = map(int, input().split())
# calendar.TextCalendar.setfirstweekday(6)
print(calendar.TextCalendar(6).formatweekday((calendar.weekday(year, month, day)), width=9).upper())


#
# # technique 2
# list_week = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
# list_week1 = list(enumerate(list_week, start=0))
# day, month, year = map(int, input().split())
# print(list_week1[(calendar.weekday(year, month, day))][1])
