print('keterangan:')
bensin      = int(input('masukkan harga bensin   :'))
solar       = int(input('masukkan harga solar    :' ))
pertamax    = int(input('masukkan harga pertamax :'))

liter   = int(input('masukkan liter : '))

print('harga bensin     : Rp,',bensin)
print('harga solar      : Rp,',solar)
print('harga pertamax   : Rp,',pertamax)

nm_variable     = int(input("masukkan pilihan : "))

match nm_variable:
        case minyak if nm_variable == 1: harga = bensin
        case minyak if nm_variable == 2: harga = solar
        case minyak if nm_variable == 3: harga = pertamax
        case _:print('tidak ada harga')

if harga != 0 :
        jumlah = liter
        for i in range (jumlah) :
                harga += harga

        print("total pembayaran : Rp,", harga)
