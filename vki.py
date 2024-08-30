import tkinter as tk
from tkinter import messagebox

def hesapla():
    try:
        boy = int(entry_boy.get())
        kilo = float(entry_kilo.get())
        indeks = kilo / ((boy / 100) ** 2)
        indeks_rounded = round(indeks, 2)
        sonuc_label.config(text=f"Beden kitle indeksiniz: {indeks_rounded}")

        if indeks <= 18.5:
            durum = "Zayıf"
            kilo_alma = round(18.5 * ((boy / 100) ** 2) - kilo, 2)
            tavsiye = f"{kilo_alma} kilogram almanız gerekiyor."
        elif 18.5 < indeks <= 24.9:
            durum = "Normal"
            tavsiye = ""
        elif 24.9 < indeks <= 29.9:
            durum = "Fazla Kilolu"
            kilo_verme = round(kilo - 24.9 * ((boy / 100) ** 2), 2)
            tavsiye = f"{kilo_verme} kilogram vermeniz gerekiyor."
        elif 29.9 < indeks <= 39.9:
            durum = "Obez"
            kilo_verme = round(kilo - 24.9 * ((boy / 100) ** 2), 2)
            tavsiye = f"{kilo_verme} kilogram vermeniz gerekiyor."
        else:
            durum = "Aşırı Obez"
            kilo_verme = round(kilo - 24.9 * ((boy / 100) ** 2), 2)
            tavsiye = f"{kilo_verme} kilogram vermeniz gerekiyor."

        durum_label.config(text=f"Durumunuz: {durum}")
        tavsiye_label.config(text=tavsiye)

    except ValueError:
        messagebox.showerror("HATA", "Lütfen geçerli bir değer girin.")

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Vücut Kitle İndeksi Hesaplayıcı")

# Boy girişi
tk.Label(pencere, text="Boyunuzu giriniz (cm):").pack()
entry_boy = tk.Entry(pencere)
entry_boy.pack()

# Kilo girişi
tk.Label(pencere, text="Kilonuzu giriniz:").pack()
entry_kilo = tk.Entry(pencere)
entry_kilo.pack()

# Hesapla butonu
hesapla_button = tk.Button(pencere, text="Hesapla", command=hesapla)
hesapla_button.pack()

# Sonuç label'ları
sonuc_label = tk.Label(pencere, text="")
sonuc_label.pack()

durum_label = tk.Label(pencere, text="")
durum_label.pack()

tavsiye_label = tk.Label(pencere, text="")
tavsiye_label.pack()

# Pencereyi çalıştır
pencere.mainloop()
