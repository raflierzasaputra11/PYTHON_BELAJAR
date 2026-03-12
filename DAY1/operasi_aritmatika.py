# operasi aritmatika

a = 10
b = 3

print("====ARITMATIKA====")
# operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus %
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division //
hasil = a // b
print(a,"//",b,"=",hasil)

print("====PENJUMLAHAN====")
# prioritas operasi
'''
    1. ()
    2. EXPONE **
    3. PERKALIAN DAN TEMAN TEMAN * / ** % //
    4. PERTAMBAHAN DAN PENGURANGAN + -
'''
x = 3
y = 2
z = 4

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)