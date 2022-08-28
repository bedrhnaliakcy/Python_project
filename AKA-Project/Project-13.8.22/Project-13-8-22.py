import random
def screen_show(num):
    if no == 1:
        print("[---]")
        print("[   ]")
        print("[ 0 ]")
        print("[   ]")
        print("[---]")
    if no == 2:
        print("[---]")
        print("[ 0 ]")
        print("[   ]")
        print("[ 0 ]")
        print("[---]")
    if no == 3:
        print("[---]")
        print("[   ]")
        print("[000]")
        print("[   ]")
        print("[---]")
    if no == 4:
        print("[---]")
        print("[0 0]")
        print("[   ]")
        print("[0 0]")
        print("[---]")
    if no == 5:
        print("[---]")
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
        print("[---]")
    if no == 6:
        print("[---]")
        print("[000]")
        print("[   ]")
        print("[000]")
        print("[---]")
x = "y"
while x == "y":
    for i in range(2):
        no = random.randint(1,6)
        print(i+1, ". Yüzü")
        screen_show(no)
    try:
        x=str(input("Çıkmak için 'n' veya devam etmek için 'y' basın:\t"))
    except (Exception,ValueError):
        print("Hata var!!!", Exception)
    finally:
        if x != "y":
            print("\n>>>Tanımlanamayan bir hata oluştu.<<<\n ÇIKIŞ YAPILIYOR...")
            exit(0)
        else:
            pass