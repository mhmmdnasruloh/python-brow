nama = input ("masukan nama anda = ")
usia = int(input("Berapa usia anda = "))

print ( """
<><><>FILM APA YANG INGIN ANDA TONTON<><><> 
1. cinta segitiga (18+)
2. Perusak rumah tangga (18+)
3. Boboboi
4. spongebob
5. upin & ipin 
6. dibalik kamar mandi bersama (18+)
""")

film = int(input("film apa yang ingin anda tonton (1-6) = "))

hasil_usia = () 

if usia >= 1 and  usia < 18 :
    hasil_usia = "anda belum cukup umur"
else :
    hasil_usia = "anda sudah cukup usia "
    
if film in [1,2,6] and usia <18 :
    print(f"maaf {nama}, {hasil_usia} untuk menonton film 18 + ini")
elif film in [3,4,5] and usia >= 18 :
    print(f"{nama}, {hasil_usia} untuk menonton film ini")
elif film in [3,4,5] and usia <18 :
    print(f"{nama}, {hasil_usia} untuk menonton film ini")




    