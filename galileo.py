import numpy
import math

def galileo(d,a,b):
    test = 1
    while (2/(math.sqrt(test)))>(1/(6**d)):
           test+=20
    arr = numpy.random.randint(1,7,size=(test,d))
    colsums = arr.sum(axis=1)

    sumb = numpy.equal(colsums,b)
    suma = numpy.equal(colsums,a)

    numb = numpy.count_nonzero(sumb)
    numa = numpy.count_nonzero(suma)

    probb = numb/(test)
    proba = numa/(test)

    if (proba-probb)<(-1/(2*(6**d))):
        return -1
    elif (proba-probb)>(1/(2*(6**d))):
        return 1
    else:
        return 0
