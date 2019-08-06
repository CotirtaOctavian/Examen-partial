#Plecand de la a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]] folosind lambda,
# reduce si map calculati suma pe fiecare lista din interiorul listei a, rezultatul o sa fie o lista care
# contine suma numerelor pe fiecare lista. Din aceasta lista extrageti o alta lista
# care contin doar numere impare folosind lambda, filter.


import functools

a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

e = list(filter(lambda t: t%2, map(lambda z: functools.reduce(lambda x, y: x + y, z), a)))

print(e)






