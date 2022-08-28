import requests_html
#------------------------------View Weather---------------------------------------------
def weather(loc,dts,dc,tm,pp,hm,ws):
    print("-"*75)
    print("Yer:\t\t\t\t",loc)
    print("Zaman:\t\t\t\t",dts)
    print("Durum:\t\t\t\t",dc)
    print("-"*75)
    print("Sıcaklık:\t",tm,"°C")
    print("Yağış:\t\t",pp)
    print("Nem:\t\t",hm)
    print("Rüzgar:\t\t",ws)
    print("-"*75)
#---------------------------------------------------------------------------------------
#------------------------------Weather İnfo---------------------------------------------
def weather_info(a_read):
    #--------------------------------------------------------
    location = a_read.html.find('div#wob_loc', first=True).text
    date = a_read.html.find('div#wob_dts', first=True).text
    state = a_read.html.find('span#wob_dc', first=True).text
    #--------------------------------------------------------
    heat = a_read.html.find('span#wob_tm', first=True).text
    rain = a_read.html.find('span#wob_pp', first=True).text
    demp = a_read.html.find('span#wob_hm', first=True).text
    wind = a_read.html.find('span#wob_ws', first=True).text
    #--------------------------------------------------------
    weather(location,date,state,heat,rain,demp,wind)
#------------------------------Main---------------------------------------------
def main():
    while True:
        site = requests_html.HTMLSession()

        query = input("Lütfen Ülke veya Şehir ismi giriniz:\t")
        query.capitalize()
        url = f'https://www.google.com/search?q=weather+{query}'

        read = site.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
        weather_info(read)
        try:
            select = input("devam etmek için 'y' veya çıkmak için 'n' tuşlayın:\t")
            if select == "y":
                pass
            else:
                break
        except Exception:
            print("hata var")

if __name__ == '__main__':
    main()


"""
        Case-7
"""