"""
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = list()

for i in liste1:
    liste2.append(i)
    print(liste2)
"""

# Üstteki listeden başka bir liste oluşturma yönteminin daha kısa yöntemi

"""
liste3 = [1, 2, 3, 4, 5, 6]

liste4 = [i for i in liste3 ]
print (liste4) 
"""

"""
liste = [3, 4, 5]
liste1 = [ i * 2 for i in liste ]
print(liste1)
"""

"""
liste = [ (1,2) , (3,4) , (5,6)]
liste1 = [ i * j for i,j in liste]
print(liste1)
"""


liste = [ [1,2,3] , [4,5,6] , [7,8 ,9], [10,11,12]]
liste1 = [ x for i in liste for x in i ]
print(liste1)


























