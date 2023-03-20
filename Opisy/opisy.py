import sys, os
def tagi():
    tagi_l = []
    tagi = input("Tagi: ")
    if tagi != '':
        tagi_temp = tagi.split()
        for tag in tagi_temp:
            tag = "#"+str(tag)
            tagi_l.append(tag)
        tagi_s = ' '.join(tagi_l)
    else:
        tagi_s = '#vintage #y2k #drip #moda #fashion'
    return tagi_s


def opis():
        nazwa = input("Nazwa: ")
        nazwa_l = nazwa + '\n'
        rozmiar = input("Rozmiar: ")
        rozmiar_l = f'Rozmiar: {rozmiar} \n'
        stan = input("Stan: ")
        stan_l = f'Stan: {stan} \n'
        tags = tagi()
        opis_all = str(nazwa_l+rozmiar_l+stan_l+ "!Cena do negocjacji! \nPo więcej zdjęć lub informacji pisz (:\n" + tags)
        return opis_all

def itemGenerator():
    flag = True
    item_num = os.listdir("items")
    print(len(item_num)) 
    i = len(item_num) ##what number of the files in the folder 
    while flag == True:
        itemki = "item{}.txt".format(i)
        file_path = os.path.join("items", itemki)
        with open(file_path, "w") as f:
            item = opis()
            f.write(item)
            i += 1
            ctn = input('continue? y/n: ') 
            if ctn == 'n':
                flag = False ##interupt

itemGenerator()