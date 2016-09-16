# -*- coding: utf-8 -*-
"""
Hellou
"""
SelectedMonth = 'September'
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsIndex = months.index(SelectedMonth)

print(monthsIndex)
print("The number of days in", SelectedMonth, "is", daysInMonths[monthsIndex])