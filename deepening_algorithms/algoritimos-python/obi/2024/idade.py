a = int(input()) 
b = int(input()) 
c = int(input()) 

#cibele é a mais velha
#camila a do meior
#celeste a mais nova

idade_camila = 0

if (a > b and a < c):
    idade_camila = a
elif (b > a and b < c):
    idade_camila = b
else:
    idade_camila = c

print(idade_camila)

