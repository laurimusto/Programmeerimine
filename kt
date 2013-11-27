import math
#
f = raw_input('Sisesta esimene arv: ')
g = raw_input('Sisesta teine arv: ')
a = float(f)
b = float(g)

#esimene ylesanne

print a, ' + ', b, ' = ', a+b
print a, ' - ', b, ' = ', a-b, ' ja ', b, ' - ', a, ' = ', b-a
print a, ' * ', b, ' = ', a*b
print a, ' / ', b, ' = ', a/b, ' ja ', b, ' / ', a, ' = ', b/a
print a, ' ^ ', b, ' = ', a**b
print " "
#teine ylesanne

print a, '=', math.radians(a), 'radiaani'
print a, '=', math.degrees(a), 'kraadi'
print a, '=', math.sin(a)
print b, '=', math.atan(b)
print 'PII =', math.pi
print " "
#kolmas ylesanne
e = math.e
tanh = (e**a-e**-a)/(e**a+e**-a)
print a, 'Hyperboloid tangens = ', tanh
x = a
snd = ((1/math.sqrt(2*math.pi)))*(e**-math.sqrt(x**2))
print snd
#neljas ylesanne
ab = int(a)
ba = int(b)

print "{:04d}, {:04d}".format(ab, ba)
print "{:.3f}, {:.3f}".format(ab, ba)
#viies ylesanne
print "Arvu", a, "ymardamine ylespoole =", math.ceil(a)
print "Arvu", b, "ymardamine alla =", math.floor(b)
