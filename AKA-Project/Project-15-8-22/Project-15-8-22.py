import requests_html
#------------------------------View Weather----------------------------------------------
def weather_view(loc,dts,dc,tm,pp,hm,ws):
    print("-"*75)
    print("Yer:\t\t\t\t",loc)
    print("Zaman:\t\t\t\t",dts)
    print("Durum:\t\t\t\t",dc)
    print("-"*75)
    print("Sıcaklık:\t\t\t",tm,"°C")
    print("Yağış:\t\t\t\t",pp)
    print("Nem:\t\t\t\t",hm)
    print("Rüzgar:\t\t\t\t",ws)
    print("-"*75)
#------------------------------weather offer---------------------------------------------
def weather_offer(a_state,a_heat, a_rain, a_demp, a_wind):
    a_state = str(a_state) # drum
    a_heat = int(a_heat) # sıcaklık
    a_rain = int(a_rain.rstrip("%")) # yağış
    a_demp = int(a_demp.rstrip("%")) # nem
    a_wind = int(a_wind.rstrip(" km/s")) # rüzgar
    #-----------------------------------------------------------
    if a_rain >= 30 and a_heat >= 15:
        print("şemsiye al")
    if a_rain >= 50 and a_heat >= 20 and a_wind >= 5:
        print("Hava", a_heat, "°C rüzgarlı yağmur ve sıcaklık var: şemsiyeni al ve düzgün giyin")
    if a_rain >= 45 and a_heat >= 15 and a_wind >= 5 and a_demp >= 45:
        print("Hava", a_heat, "°C, görünen o ki bunaltıcı bir yağış olabilir: şemsiye veya ince bir yağmurluk al")
    if a_heat >= 20 and a_wind >= 5 and a_demp >= 40:
        print("Hava ", a_heat, "°C normal giyin. hava sıcak, nemli ve rüzgarlı. İnce giyin, şapkanı ve gözlüğünü almayı unutma!!")
    if a_rain >= 50 and a_heat <= 15 and a_wind >= 5 and a_demp <= 45:
        print("Şiddetli ve soğuk bir yağış olabilir. >> mümkün mertebe kapalı alanda dur >> Kaban, bot, şemsiye veya yağmurlukları alsan iyi edersin")
    if a_rain <= 30 and a_wind >= 5 and a_demp >= 45:
        print("Hava ", a_heat, "°C ", a_demp," nem var ama esintili >> rahat kıyafetler giy")
    return a_state

#------------------------------Get Weather İnfo-----------------------------------------
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
    weather_view(location,date,state,heat,rain,demp,wind)
    #--------------------------------------------------------
    wOff = weather_offer(state, heat, rain, demp, wind)
    return wOff
#------------------------------Main-----------------------------------------------------
def main():
    while True:
        site = requests_html.HTMLSession()

        query = input("Lütfen Ülke veya Şehir ismi giriniz:\t")
        query.capitalize()
        url = f'https://www.google.com/search?q=weather+{query}'

        read = site.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
        wOff = weather_info(read)
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
        Case-8

bu projede hava durumuna ekstra olarak öeneri vermektedir.
öneri çeşidi isteğe ve alınan veriye göre değişmektedir.

şimdilik ideal bir kod parçasıdır.
ileri ki aşamalarda nesne yönelimli yapılıp kod biraz daha optimize edilebilir.
"""

# web sitesinden daha fazla veri çekilerek daha güzel bir öneri sistemi oluşturulabilir. Şimdilik durum bilgisine bağlı bir izlenim sergiliyelim
