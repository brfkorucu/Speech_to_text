toplam_net_ucret = 0
toplam_gelir_vergisi = 0
aylk_toplam_brut_ucret = 0
calisan_say = 1
dusuk_net_ucret = 0
max_brut_tc_no = ""
max_brut_ad_soyad = ""
max_brut_aylk_tplm_brt_ucrt = 0
max_brut_glr_vrgs = 0
max_brut_net_ucret = 0
max_net_tc_no = ""
max_net_ad_soyad = ""
max_net_aylk_tplm_brt_ucrt = 0
max_net_glr_vrgs = 0
max_net_ucret = 0
evli = 0
bekar = 0
es_calisan = 0
cocuk_sahibi_cal_say = 0
cocuk_say = 0
fazla_cocuk = 0
engelli_say = 0
gelir_vergisi_onbes = 0
gelir_vergisi_yirmi = 0
gelir_vergisi_yirmiyedi = 0
gelir_vergisi_otuzbes = 0
t_ikiyuz_banknot = 0
t_yuz_banknot = 0
t_elli_banknot = 0
t_yirmi_banknot = 0
t_on_banknot = 0
t_bes_banknot = 0
t_bir_tl = 0
t_elli_kr = 0
t_yirmibes_kr = 0
t_on_kr = 0
t_bes_kr = 0
t_bir_kr = 0

print("\n----------------------------------------------",
      "Maaş İşleri Bürosu Bilgi Sistemine Hoşgeldiniz",
      "----------------------------------------------",sep="\n",end="")

while True :
    tc_no = input("\n\nTC kimlik numaranızı giriniz : ")
    ad_soyad = input("Adınızı ve soyadınızı giriniz : ")

    brut_ucret = float(input("Aylık brüt asgari ücretinizi giriniz (TL) : "))
    while True :
        if brut_ucret < 1777.50 :
            print("Hatalı veri girişi ! Aylık brüt ücretiniz 1777.50 TL'den düşük olamaz.")
            brut_ucret = float(input("Aylık brüt asgari ücretinizi giriniz (TL) : "))
        else :
            break
    aylk_toplam_brut_ucret += brut_ucret
    
    es_odenek = 0
    medeni_durumu = input("Medeni durumunuzu giriniz (e/E/b/B) : " )
    while True :
        if medeni_durumu.lower() == "e" :
            evli += 1
            es_sor = input("Eşiniz çalışıyor mu ? (e/E/h/H) : ")
            if es_sor.lower() == "h" :
                es_odenek = 220
                break
            elif es_sor.lower() == "e" :
                es_odenek = 0
                es_calisan += 1
                break
            else :
                print("Hatalı veri girişi ! Lütfen belirtilen kriterlerde bir cevap giriniz.")
                continue
        elif medeni_durumu.lower() == "b" :
            bekar += 1
            break
        else :
            print("Hatalı veri girişi. Lütfen belirtilen kriterlere uygun bir cevap giriniz")
            medeni_durumu = input("Medeni durumunuzu giriniz (e/E/b/B) : " )

    cocuk_odenek = 0
    cocuk_sayisi = int(input("Bakmakla yükümlü olduğunuz çocuk sayısını giriniz (0 ya da daha büyük) : "))
    if cocuk_sayisi > 3 :
        fazla_cocuk +=1
    while True :
        if cocuk_sayisi > 0 :
            buyuk_cocuk = int(input("Yaşı 6'dan büyük olan kaç tane çocuğunuz var ? : "))
            if buyuk_cocuk > cocuk_sayisi :
                print("Hatalı veri girişi.")
                continue
            cocuk_sahibi_cal_say += 1
            cocuk_say += cocuk_sayisi
            kucuk_cocuk = cocuk_sayisi - buyuk_cocuk
            cocuk_odenek = (buyuk_cocuk * 45) + (kucuk_cocuk * 25 )
            break
        elif cocuk_sayisi == 0 :
            break
        else :
            print("Hatalı veri girişi.Lütfen çocuk sayısına belirtilen kriterlere uygun bir cevap giriniz")
            cocuk_sayisi = int(input("Bakmakla yükümlü olduğunuz çocuk sayısını giriniz (0 ya da daha büyük) : "))

    muaf_miktar = 0
    engelli_sor = input("Hayatınızı etkileyen sağlık probleminiz(engeliniz) var mı (e/E/h/H) : ")
    while True :
        if engelli_sor.lower() == "e" :
            engelli_say += 1
            engelli_orani = int(input("Engellik oranınız (%1-%100) : % "))
            if engelli_orani >= 80 :
                engelli_durumu = "1. Derece Engelli"
                muaf_miktar += 900
                break
            elif 60 <= engelli_orani < 80 :
                engelli_durumu = "2. Derece Engelli"
                muaf_miktar += 470
                break
            else :
                engelli_durumu = "3. Derece Engelli"
                muaf_miktar += 210
                break
        elif engelli_sor.lower() == "h" :
            break
        else :
            print("Hatalı veri girişi.Lütfen belirtilen kriterlerde bir cevap giriniz.")
            engelli_sor = input("Engel durumunuz var mı (e/E/h/H) : ")

    toplam_burut_ucret = es_odenek + cocuk_odenek + brut_ucret
                
    if toplam_burut_ucret < 2000 :
        gelir_vergisi = ((toplam_burut_ucret-muaf_miktar) * 15) / 100
        gelir_vergisi_onbes += 1
    elif 2000 <= toplam_burut_ucret < 5000 :
        gelir_vergisi = ((toplam_burut_ucret-muaf_miktar) * 20) / 100
        gelir_vergisi_yirmi += 1
    elif 5000 <= toplam_burut_ucret < 10000 :
        gelir_vergisi = ((toplam_burut_ucret-muaf_miktar) * 27) / 100
        gelir_vergisi_yirmiyedi += 1
    else :
        gelir_vergisi = ((toplam_burut_ucret-muaf_miktar) * 35) /100
        gelir_vergisi_otuzbes += 1

    net_ucret = toplam_burut_ucret - gelir_vergisi

    ikiyuz_banknot = 0
    yuz_banknot = 0
    elli_banknot = 0
    yirmi_banknot = 0
    on_banknot = 0
    bes_banknot = 0
    bir_tl = 0
    elli_kr = 0
    yirmibes_kr = 0
    on_kr = 0
    bes_kr = 0
    bir_kr = 0

    ikiyuz_banknot = int(net_ucret / 200)
    t_ikiyuz_banknot += ikiyuz_banknot
    for_yuz = (net_ucret % 200)    
    yuz_banknot = int(for_yuz / 100)
    t_yuz_banknot += yuz_banknot
    for_elli = for_yuz % 100    
    elli_banknot = int(for_elli / 50)
    t_elli_banknot += elli_banknot
    for_yirmi = for_elli % 50
    yirmi_banknot = int(for_yirmi / 20)
    t_yirmi_banknot += yirmi_banknot
    for_on = for_yirmi % 20
    on_banknot = int(for_on / 10)
    t_on_banknot += on_banknot
    for_bes = for_on % 10
    bes_banknot = int(for_bes / 5)
    t_bes_banknot += bes_banknot
    for_birtl = for_bes % 5
    bir_tl = int(for_birtl / 1 )
    t_bir_tl += bir_tl
    for_ellikr = for_birtl % 1
    elli_kr = int(for_ellikr / 0.5)
    t_elli_kr += elli_kr
    for_yirmibeskr = round(for_ellikr % 0.5,2)
    yirmibes_kr = int(for_yirmibeskr / 0.25)
    t_yirmibes_kr += yirmibes_kr
    for_onkr = round(for_yirmibeskr % 0.25,2)
    on_kr = int(for_onkr / 0.10 )
    t_on_kr += on_kr
    for_beskr = round(for_onkr % 0.10,2)
    bes_kr = int(for_beskr / 0.05)
    t_bes_kr += bes_kr
    for_birkr = round(for_beskr % 0.05,2)
    bir_kr = int(for_birkr / 0.01)
    t_bir_kr += bir_kr

    if net_ucret > max_net_ucret :
        max_net_tc_no = tc_no
        max_net_ad_soyad = ad_soyad
        max_net_aylk_tplm_brt_ucrt = toplam_burut_ucret
        max_net_glr_vrgs = gelir_vergisi
        max_net_ucret = net_ucret

    if toplam_burut_ucret > max_brut_aylk_tplm_brt_ucrt :
        max_brut_tc_no = tc_no
        max_brut_ad_soyad = ad_soyad
        max_brut_aylk_tplm_brt_ucrt = toplam_burut_ucret
        max_brut_glr_vrgs = gelir_vergisi
        max_brut_net_ucret = net_ucret

    if net_ucret < 2000 :
        dusuk_net_ucret += 1
        
    toplam_net_ucret += net_ucret
    toplam_gelir_vergisi += gelir_vergisi
    
    print("\nTC kimlik numarası : {} \nAdı ve Soyadı : {} ".format(tc_no,ad_soyad))
    print("Aylık brüt ücreti : {} TL ".format(brut_ucret))
    print("Eş için alınıcak aile yardım desteği : {} TL ".format(es_odenek))
    print("Çocuk için aile yardımı ödeneği : {} TL ".format(cocuk_odenek))
    print("Aylık toplam brüt ücret : {} TL ".format(toplam_burut_ucret))
    print("Gelir vergisi kesintisi : {:.2f} TL ".format(gelir_vergisi))
    if engelli_sor.lower() == "e" :
        print("Engelli vergi indiriminden yararlanıyor - {}".format(engelli_durumu))
    print("Aylık alınan net ücret : {:.2f} TL\n ".format(net_ucret))
    print("Aylık net ücret için gerekli banknot ve madeni paralar :\n\n\t 200 TL : {} adet\n\t 100 TL {} adet\n\t 50 TL {} adet\n\t 20 TL {} adet\n\t 10 TL {} adet\n\t 5 TL {} adet\n\t 1 TL {} adet\n\t 50 kr {} adet\n\t 25 kr {} adet\n\t 10 kr {} adet\n\t 5 kr {} adet\n\t 1 kr {} adet"
          .format(ikiyuz_banknot,yuz_banknot,elli_banknot,yirmi_banknot,on_banknot,bes_banknot,bir_tl,elli_kr,yirmibes_kr,on_kr,bes_kr,bir_kr))

    calisan_sor = input("\nVerileri girilmeyen başka çalışan var mı (e/E/h/H) ? : ")
    if calisan_sor.lower() == "e" :
        calisan_say += 1
        continue
    else :
        break

print("\nTüm çalışanlara bir ayda ödenen aylık toplam net ücret tutarı : {:.2f} TL\nDevlete aktarılan aylık toplam gelir vergisi tutarı : {:.2f} TL "
      .format(toplam_net_ucret,toplam_gelir_vergisi))
print("\nTüm çalışanların aylık toplam brüt ücretlerinin ortalaması : {:.2f} TL\nNet ücretlerinin ortalaması : {:.2f} TL "
      .format((aylk_toplam_brut_ucret/calisan_say),(toplam_net_ucret/calisan_say)))
print("2000 TL’nin altında aylık net ücret alan çalışanların sayısı : {} ".format(dusuk_net_ucret))
print("\nGelir sayısı oranları için çalışan sayısı ve yüzdeleri :\n\n\t %15 için çalışan sayısı {} ve yüzdesi % {}\n\t %20 için çalışan sayısı {} ve yüzdesi % {}\n\t %27 için çalışan sayısı {} ve yüzdesi % {}\n\t %35 için çalışan sayısı {} ve yüzdesi % {}"
      .format(gelir_vergisi_onbes,(gelir_vergisi_onbes*100)/calisan_say,gelir_vergisi_yirmi,(gelir_vergisi_yirmi*100)/calisan_say,gelir_vergisi_yirmiyedi,(gelir_vergisi_yirmiyedi*100)/calisan_say,gelir_vergisi_otuzbes,(gelir_vergisi_otuzbes*100)/calisan_say))                                      
print("Bütün çalışanların aylık net ücretleri için gereken banknot ve madeni paralar :\n\n\t 200 TL : {} adet\n\t 100 TL {} adet\n\t 50 TL {} adet\n\t 20 TL {} adet\n\t 10 TL {} adet\n\t 5 TL {} adet\n\t 1 TL {} adet\n\t 50 kr {} adet\n\t 25 kr {} adet\n\t 10 kr {} adet\n\t 5 kr {} adet\n\t 1 kr {} adet"
      .format(t_ikiyuz_banknot,t_yuz_banknot,t_elli_banknot,t_yirmi_banknot,t_on_banknot,t_bes_banknot,t_bir_tl,t_elli_kr,t_yirmibes_kr,t_on_kr,t_bes_kr,t_bir_kr))
print("\nAylık toplam brüt ücreti en yüksek olan çalışanın :\n\n\tTC kimlik numarası : {}\n\tAdı soyadı : {}\n\tAylık toplam brüt ücreti : {} TL\n\tGelir vergisi kesintisi : {:.2f} TL\n\tAylık net ücreti : {:.2f} TL"
      .format(max_brut_tc_no,max_brut_ad_soyad,max_brut_aylk_tplm_brt_ucrt,max_brut_glr_vrgs,max_brut_net_ucret))
print("\nAylık net ücreti en yüksek olan çalışanın :\n\n\tTC kimlik numarası : {}\n\tAdı soyadı : {}\n\tAylık toplam brüt ücreti : {} TL\n\tGelir vergisi kesintisi : {:.2f} TL\n\tAylık net ücreti : {:.2f} TL"
      .format(max_net_tc_no,max_net_ad_soyad,max_net_aylk_tplm_brt_ucrt,max_net_glr_vrgs,max_net_ucret))
print("\nTüm çalışanlar içinde : \n\n\tEvli olanların yüzdesi : %{:.2f}\n\tBekar olanların yüzdesi : %{:.2f}"
      .format(((evli*100)/calisan_say),((bekar*100)/calisan_say)))
print("\nEvli olan çalışanların içinde çalışan eşlerin yüzdesi : %{:.2f}".format((es_calisan*100)/evli))
print("Bakmakla yükümlü çocuk sahibi olan çalışanların, çocuk sayılarının ortalaması : {:.2f}".format(cocuk_say/cocuk_sahibi_cal_say))
print("Bakmakla yükümlü olduğu çocuk sayısı 3’ten fazla olan çalışanların sayısı : {}".format(fazla_cocuk))
print("\nEngelli çalışanların sayısı : {}\nTüm çalışanlar içindeki yüzdesi : %{:.2f} ".format(engelli_say,((engelli_say*100)/calisan_say)))
