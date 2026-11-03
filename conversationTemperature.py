list_temparature = [10,0,20.3,31.1,32.4]
fahrenheit = list(map(lambda c: (c * 1.8) + 32, list_temparature))
print (fahrenheit)