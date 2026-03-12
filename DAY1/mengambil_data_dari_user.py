#input user

# data yang dimasukan pasti string
data = input("masukan data: ")
print("data = ",data,"type =",type(data))

# jika ingin mengambil int and float, maka
data_float = float(input("masukan float: "))
print("data = ",data_float,",type =",type(data_float))
data_int = int(input("masukan angka: "))
print("data = ",data_int,",type =",type(data_int))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data: ",biner,",type: ",type(biner))