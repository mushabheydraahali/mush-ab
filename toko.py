 product = {
    "caffe americano": 37000,
    "caramel macchiato": 59000,
    "asian dolce latte": 55000,
    "carramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,
 }


 def toko():
   print("selamat datang selamat berbelanja")
   print("dan ini daftar belanjanya")
   for product, price in product.item():
      print(f"{product}: RP{price}")

      total_product = 0
      while true:
         product_dipilih = input("masukkan product yangn ingin anda beli(atau 'selesai' untuk selesai)")
         if product_dipilih.lower() == 'selesai':
            break
         if product_dipilih not in product:
            print("maaf, kami kekurangan bahan tersebut")
            continue
         jumlah = float(input(f"berapabanya coffe {product_dipilih} yang anda inginkan?"))
        total_belanja += product[product_dipilih] * jumlah
    print(f"total belanja anda adalah: RP{total_belanja}")
    