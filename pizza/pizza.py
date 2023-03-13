import csv
import datetime


print("aşkolar pizzaya hoşgeldiniz")
print("siparişinizi oluşturunuz")
toplamucret = 0
menü = print("""
pizza tabanı seçiniz
1:klasik(50₺)
*domates sos,peynir
2: Margarita(60₺) 
*domates sos, mozarella,fesleğen
3: tükrpizza(80₺)
*domates sos,peynir,sucuk
4: sade pizza(40₺)
*domates sos
-------------
lütfen ekstra malzemleri seçiniz
11: zeytin(5₺)
12: Mantar(10₺) 
13: keçi peyniri (20₺)
14: et (30₺)
15: soğan (3₺)
16: mısır(7₺)
----------------



""")
while True:
     secim = input("lütfen pizza tabanı ve ektra malzemeleri seçiniz:")
     adet = int(input("kaç adet istersiniz?:"))
     if secim == "1":
        toplamucret += adet * 50
     elif secim == "2":
         toplamucret += adet * 60
    
     elif secim == "3":
        toplamucret += adet * 80
     elif secim == "4":
        toplamucret += adet * 40
     elif secim == "11":
         toplamucret += 5
     elif secim == "12" :
         toplamucret += 10
     elif secim == "13" :
         toplamucret += 20
     elif secim == "14" :
         toplamucret += 30
     elif secim == "15" :
         toplamucret += 3
     elif secim == "16" :
         toplamucret += 7
     sor = input("başka isteğiniz var mı?(e/h):")
     if sor == "h":
        print("toplam ücret:",toplamucret,"₺")  
     

        break
while True:
    print("----sipariş bilgileri----")
    name = input("isminizi giriniz:")
    kartno = input("16 haneli kart numaranızı giriniz:")
    sifre = input("şifrenizi girinizi:")
    time_of_order = datetime.datetime.now()
    print("siparişiniz onaylandı")
      
    break
from datetime import datetime
suan = datetime.now()
tarih = datetime.ctime(suan)

print(tarih)
      

       
     

     
              