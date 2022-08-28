import random
import pandas as pd

def nickname_choose(wordList_p):
    while True:
        check = input("Nickname'miniz hazır listeden mi seçilsin:(Y)(N)")
        # büyük harfleri küçük harfe çevirerek hata almayı önlüyoruz.
        # ya da >>>check == "y" or check == "n"<<< bu kodu aşağıda if ifadesine de ekleyebiliriz.
        if check == check.upper():
            check.lower()
        # koşula bağlayarak yanlış girilen değeri tekrar alıyoruz veya doğru ise devam
        if check == "y" or check == "n":
            # eğer seçim "y" ise hazır listeden seçim yap
            if check == "y":
                print("\t\tNickName_eng\t\t\t\tNickName_tr\n\n\t\t")
                # hazır listeden random 5 nick name veriyor
                for i in range(5):
                    temp = random.randint(0,119)
                    print(nickname_list_have.iloc[temp, 0],"\t\t\t\t" ,nickname_list_have.iloc[temp, 1])
                break
            # değilse kendi girdiği kelimeler ile seçim  yapıyor.
            else:
              print("O zaman en sevdiğin kelimeleri veya sayıları ekle")
              print("en az 10 adet kelime ekle")
              # burada girilen kelimeleri büyük-küçük duyarlılığını yaptıktan
              # sonra girilen değer "q" harfine eşit değil ise def içerisindeki parametreye
              # ekliyoruz.
              while True:
                  word = input("Lütfen eklemek istediğiniz kelşimeleri yazınız:(q=out)\t")
                  if check == check.upper():
                    check.lower()
                  if word == "q":
                      break
                  else:
                      wordList_p.append(word)
              break
            break
        else:
            print("lütfen sadece >>Y<< ya da >>N<< harflerini giriniz.!!")
    return check

wordList = [] # kelime listesi
new_wordList = [] # yeni kelime listesi
nickname_list_have = pd.read_csv("nickname_list.cvs", delimiter=",") # hazır da olan kelime listesi
print(">>>>\t\t\tHAZIR NİCKNAME LİSTESİNDEN ÖRNEKLER\n\n", nickname_list_have.head(10))
print("\n"*5)

#fonksiyonu çağırıyoruz ve return değeri olarak "check" değerini atıyoruz.
check = nickname_choose(wordList)

print("\n"*5)
# hazır listeden random 10 nickname veriyor
if check == "n":
    try:
        print("\t\tNickName")
        for j in range(5):
            text = "" # boş str
            for k in range(2):
                temp = random.randint(0, len(wordList)) # girilen kelimeler listesine göre random sayı üret
                text += wordList[temp] # text değişkeninin yanına ekle
            new_wordList.append(text) # yeni listenin sonuna ekle
    except Exception:
        print("Hata var:\t", Exception)

    print(*new_wordList,sep="\n")# listeyi bas
else:
    print(">>>>>>>>>>>>\tİşlem bitti\t\t<<<<<<<<<<<<")
