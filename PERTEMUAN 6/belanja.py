product = {
    "beras"; 18000,
    "gula"; 12500,
    "telur"; 35000,
    "susu"; 19000,
}

def belanja():
    print("selamat datang, selamat berbelanja")
    print("berikut adalah daftar barang yang tersedia:")
    for bararng, harga in product.items():
        print(f"{barang}: rp{harga} per kg")

        total_belanja = 0
        while true:
            barang_dipilih = input = ("masukan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai':
            break
        if barang_dipilih not in product:
            print("maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"berapaberapa kg {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah: RP{total_belanja}")

