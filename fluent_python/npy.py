import numpy
import json


a = numpy.arange(12000000)
a.shape = 3000, 4000
print(a.dtype)
numpy.save('yukanp', a)


b = numpy.load('yukanp.npy', 'r+')


with open('yukatxt.txt', 'w+') as f:
    json.dump(b.tolist(), f, separators=(',', ':'))
