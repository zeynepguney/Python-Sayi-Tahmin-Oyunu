"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın
** "random modülü" için "python random" şekilde arama yapın
** 100 üzerinde puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

- Oyun hakkında : 
Tahmin edilen sayıyı soracak. Tahmin büyükse : aşağı, küçükse : yukarı gibi yönlendirmeler yapacak
Hak = 5(varsayılan olarak) Her bilemediği hakda puanı 100 üzerinden 20 puan aşağı inecek
Daha sonraki aşamada Hak bilgisi kullanıcı tarafından belirlenecek. 10 hak ise her soru 10 puan 
"""

import random

rnd = random.randint(1,100)
can = int(input("Kaç hakkınız olsun : "))
hak = can
sayac = 0
puan = 100
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin : "))
    if (rnd == tahmin):
        print(f"Tebrikler sayıyı {sayac}. defada bildiniz. Puanınız : {100-(100/can)*(sayac-1)}")
        break
    elif (rnd > tahmin):
        print("Daha büyük bir sayı deneyin.")
    else:
        print("Daha küçük bir sayı deneyin.")        

    if hak == 0:
        print(f"Tahmin hakkınız bitti! Tutulan sayı = {rnd}") 