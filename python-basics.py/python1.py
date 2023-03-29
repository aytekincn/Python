a = int ( input ("A:"))
b = int ( input ("B:"))
c = int ( input ("C:"))

delta = b ** 2 - 4 * a * c
x1 = ( -b - delta ** 0.5 ) / ( 2 * a )
x2 = ( -b + delta ** 0.5 ) / ( 2 * a )

print ("Birinci Kök : {}\n İkinci Kök: {}\n".format (x1, x2))