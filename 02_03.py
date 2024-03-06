import logging as l
l.basicConfig(filename = 'error.log',level=l.ERROR)

try:
    result = 10/0
except ZeroDivisionError as e:
    l.error('Arrithmetic Exception Occurred : %s',e)
