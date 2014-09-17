from itertools import cycle, islice

months = [
    lambda y: 31,  # jan
    lambda y: 29 if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) else 28,  # feb
    lambda y: 31,  # mar
    lambda y: 30,  # apr
    lambda y: 31,  # may
    lambda y: 30,  # jun
    lambda y: 31,  # jul
    lambda y: 31,  # aug
    lambda y: 30,  # sept
    lambda y: 31,  # oct
    lambda y: 30,  # nov
    lambda y: 31,  # dec
]
days = cycle(range(7))  # 5 is sun
count = 0

for year in xrange(1901, 2001):
    for month in months:
        if list(islice(days, month(year)))[0] == 5:
            count += 1
print count
