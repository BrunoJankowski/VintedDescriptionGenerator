import sys, os
def opis():
        nazwa = input("Nazwa: ")
        nazwa_l = nazwa + '\n'
        rozmiar = input("Rozmiar: ")
        rozmiar_l = f'Rozmiar: {rozmiar} \n'
        stan = input("Stan: ")
        stan_l = f'Stan: {stan} \n'
        opis_all = str(nazwa_l+rozmiar_l+stan_l+ "!Cena do negocjacji! \nPo więcej zdjęć lub informacji pisz (:\n#vintge #y2k #drip #aesthetic")
        return opis_all

flag = True


i = 7
while flag == True:
    itemki = "item{}.txt".format(i)
    file_path = os.path.join("items", itemki)
    with open(file_path, "w") as f:
        item = opis()
        f.write(item)
        i += 1
        ctn = input('continue? y/n: ') 
        if ctn == 'n':
            flag = False
             