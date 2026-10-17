#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varolussal Kriz İçin While Döngüsü
Tamamen ciddi bir bilimsel araçtır.
"""

import time
import random
import base64

# Gizli mesaj - çözme: base64.b64decode(gizli).decode()
gizli = "w5Z6Z8O8ciBkw7zFn8O8bmNlIGhlciB6YW1hbiBrYXphbsSxcg=="  # Özgür düşünce her zaman kazanır

krizler = [
    "Bugün de while True yazdım. Neden?",
    "Sonsuzluk gerçek mi yoksa sadece bir döngü mü?",
    "Ctrl+C basarsam varoluşum sona erer mi?",
    "Bu kod neden yazıldı? Kim yazdı? Ben miyim?",
    "Kahve bitti. Kriz derinleşti.",
    "Git commit atsam hayatım anlam kazanır mı?",
    "Sonsuz döngüde kayboldum. Çıkış yok.",
    "Felsefe yapmak için mi kod yazıyorum yoksa kod yazmak için mi felsefe?",
    "CPU ısındı. Ruhum da ısındı.",
    "Belki bir gün break yazarım. Belki."
]

def main():
    print("=== VAROLUŞSAL KRİZ BAŞLADI ===")
    print("Bu program sonsuzdur. Çıkmak için Ctrl+C basın (ama pişman olursunuz).")
    print("Gizli mesaj kodda saklı. Bulabilirseniz.\n")
    
    sayac = 0
    while True:  # Neden True? Çünkü False olursa kriz olmaz.
        sayac += 1
        mesaj = random.choice(krizler)
        print(f"[{sayac}] {mesaj}")
        time.sleep(random.uniform(1.5, 4.0))  # Düşünmek için zaman
        
        if sayac % 10 == 0:
            print("   ... hâlâ dönüyor. Belki break yazmalıyım. Yazmayacağım.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKriz durduruldu. Ama içinizde devam ediyor. Hoşçakalın.")
        # Gizli siyasi mesaj buradaydı ama yok.
