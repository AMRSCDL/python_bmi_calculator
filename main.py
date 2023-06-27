from tkinter import * #Bu şekilde yıldız dersek tkinter kütüphanesinin her şeyini import etmiş oluruz

#Burada tkinter penceremi oluşturdum
window = Tk()
window.title("Vücut Kitle İndeksi Hesaplama")
window.minsize(width=350,height=350)
window.config(padx=70,pady=70)

#Kullanıcıya kilosunu sordum ve kullanıcının girdi gireceği bir entry oluşturdum.
kilo = Label(text="Kg cinsinden kilonuzu girin")
kilo.pack()
kilo_entry = Entry()
kilo_entry.pack()


#Kilo yerine kullanıcı string türünde bir değer girdiyse
def kontrol_kilo_str():
    deger = kilo_entry.get()
    if not deger.isdigit():
        sonuc_label.config(text="Geçersiz değer girdiniz. Lütfen rakam giriniz")
        return #


#Kullanıcıya boyunu sordum ve kullanıcının girdi gireceği bir entry oluşturdum.
boy = Label(text="Cm cinsinden boyunuzu girin")
boy.pack()
boy_entry= Entry()
boy_entry.pack()

#Boy yerine kullanıcı string türünde bir değer girdiyse
def kontrol_boy_str():
    deger = boy_entry.get()
    if not deger.isdigit():
        sonuc_label.config(text="Geçersiz değer girdiniz. Lütfen rakam giriniz")
        return

#Vücut kitle indexini bu fonksiyon içerisinde hesapladım ve ekrana yazacağı değerleri tanımladım
def hesapla():
    k = getint(kilo_entry.get()) #girilen kilo değerini aldım
    b = getint(boy_entry.get()) #girilen boy değerini aldım
    vki = k / ((b * b)/100) #VKİ hesaplama
    sonuc = vki*100
    sonuc_ilk_dort=round(sonuc,2) #Çıktının daha düzgün görünmesi için ekranda gösterilecek kısmını ayarladım
    #Kullanıcıdan alınan verilerle elde edilen sonuca göre cevabı güncelleyecek şekilde if sorguları ekledim
    if sonuc_ilk_dort <=18.5:
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " Zayıfsınız. Bu durum çeşitli sağlık sorunlarına neden olabilir")
    if sonuc_ilk_dort >=18.6 and sonuc_ilk_dort <= 24.9 :
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " Normal ağırlıktasınız.")
    if sonuc_ilk_dort >=25.0 and sonuc_ilk_dort <= 29.9 :
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " Kilolusunuz. Bu durum çeşitli sağlık sorunlarına neden olabilir")
    if sonuc_ilk_dort >=30.0 and sonuc_ilk_dort <= 34.9 :
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " 1.derece obezitesiniz. Bu durum çeşitli sağlık sorunlarına neden olabilir. Destek almanız önerilir.")
    if sonuc_ilk_dort >=35.0 and sonuc_ilk_dort <= 39.9 :
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " 2.derece obezitesiniz. Bu durum çeşitli sağlık sorunlarına neden olabilir. Destek almanız önerilir.")
    if sonuc_ilk_dort >=40:
        sonuc_label.config(text="VKİ'niz: " + str(sonuc_ilk_dort) + " 3.derece obezitesiniz.Bu durum çeşitli sağlık sorunlarına neden olabilir. Destek almanız önerilir")

#Tüm fonksiyonları tek butonda kullanabilmek için hepsini bir fonksiyonun altında topladım
def tek_command():
    kontrol_boy_str()
    kontrol_kilo_str()
    hesapla()


#Buton oluşturdum
hesap_buton = Button(text="Hesapla",command=tek_command)
hesap_buton.pack()

#Sonucu yazacak bir label oluşturdum
sonuc_label = Label(text="VKİ'niz:")
sonuc_label.pack()



window.mainloop()


