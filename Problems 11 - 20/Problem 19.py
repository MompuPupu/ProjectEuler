# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.

#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.

#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def determine_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False


def determine_month_length(month, year):
	if month == 2:
		if determine_leap_year(year):
			return 29
		else:
			return 28
	elif month == 4 or month == 6 or month == 9 or month == 11:
		return 30
	else:
		return 31


if __name__ == '__main__':
	total_days = 1
	total_sundays = 0

	for month in range(1, 13):
		total_days += determine_month_length(month, 1900)

	for year in range(1901, 2001):
		for month in range(1, 13):
			if total_days % 7 == 0:
				total_sundays += 1
			total_days += determine_month_length(month, year)

	print('Total Sundays between 1901 and 2000 = ', total_sundays)
