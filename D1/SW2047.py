# -*- coding: utf-8 -*-

sample = input()
result = ''

if len(sample) > 80:
    print(False)
else:
    result = sample.upper()
    print(result)