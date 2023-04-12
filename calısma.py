def çift_mi(sayı):
    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError

liste = [23, 34, 54, 657, 64, 12, 234, 55]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass















