from itertools import cycle, islice

months = [
    lambda year: 31,  # jan
    lambda year: 29 if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 28,  # feb
    lambda year: 31,  # mar
    lambda year: 30,  # apr
    lambda year: 31,  # may
    lambda year: 30,  # jun
    lambda year: 31,  # jul
    lambda year: 31,  # aug
    lambda year: 30,  # sept
    lambda year: 31,  # oct
    lambda year: 30,  # nov
    lambda year: 31,  # dec
]
days = cycle(range(7))  # 5 is sun
count = 0

for year in xrange(1901, 2001):
    for m, month in enumerate(months):
        md = list(islice(days, month(year)))
        if md[0] == 5:
            count += 1
print count
