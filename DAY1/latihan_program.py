# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukan nilai celcius: "))
print("suhu adalah ",celcius," celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur," reamur")

#fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah ",fahrenheit," fahrenheit")

#kelvin
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah ",kelvin," kelvin")


print("====TUGAS====")
# fahrenheit ke kelvin
faren_kelvin = (fahrenheit - 32) * 5/9 + 273.15
print("suhu farenheit ke kelvin adalah ",faren_kelvin," kelvin")

# kelvin ke faranheit
kelvin_faren = (kelvin - 273.15) * 9/5 + 32
print("suhu kelvin ke farenheit adalah ",kelvin_faren," farenheit")