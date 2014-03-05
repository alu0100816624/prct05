n = int(raw_input('Numero de intervalos: '))
suma = 0.0
if n <= 0:
  print'Introduzca un numero positivo'
else:
  for i in range(1,n+1):
    a = float(i-1)/n
    b = float(i)/n
    x_i= float(i-0.5)/n
    fx_i= float(4.0/ (1.0 + x_i*x_i))
    suma += fx_i
    print 'subintervalo[%4.5f , %4.5f ] %4.5f %4.5f' % (a,b,x_i,fx_i)
aprox = suma/n
print 'El valor aproximado de PI es: %2.20f' % aprox
pi= 3.1415926535897931159979634685441852
print 'La constante pi con treinta y cinco decimales es: %2.35f' % (pi)
  
  
  