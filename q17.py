import re

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    1000: 'one thousand'
}

for i, word in ((20, 'twenty'), (30, 'thirty'), (40, 'forty'), (50, 'fifty'),
                (60, 'sixty'), (70, 'seventy'), (80, 'eighty'), (90, 'ninety')):
    words[i] = word
    for j in xrange(1, 10):
        words[i + j] = '%s-%s' % (word, words[j])

for i in xrange(100, 1000, 100):
    words[i] = '%s hundred' % words[i/100]
    for j in xrange(1, 100):
        words[i + j] = '%s hundred and %s' % (words[i / 100], words[j])

print sum(len(re.sub(r'[ -]', '', w)) for w in words.values())
