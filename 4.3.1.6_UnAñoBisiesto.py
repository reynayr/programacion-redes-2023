'''
    Nombre: Reyna Yazmin Ríos Martínez 
    Laboratorio: 4.3.1.6
    Fecha: 14/Oct/2023
'''

def is_year_leap(year):
    if year < 1582:
        print("No está en el calendario Gregoriano")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year 5 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")