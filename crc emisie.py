# inputul poate fi doar de tip binar
# se introduce mesajul pe care vrem sa il emitem
message = input("Introduceti mesajul aici: ")
# introducem polinomul generator
polinom_generator = input("Introduceti polinomul generator aici: ")
# convertim polinomul generator la int
int_polinom_generator = int(polinom_generator)
# calculez lungimea polinomului generator
length_polinom_generator = len(polinom_generator)
# calculez coeficientul puterii lui x(doi) cu care inmultesc mesajul initial
coeficientul_cu_care_inmultesc = length_polinom_generator - 1
# print(length_polinom_generator)
length_message = len(message)
# convertim mesajul la int
int_message = int(message)

# functie sa imi converteasca un numar in baza doi intr-un numar in baza 10


def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
    return decimal


# scriu mesajul original in baza 10
message_in_decimal = binaryTodecimal(int_message)
# print(message_in_decimal)
# scriu polinomul generator in baza 10
polinom_generator_in_decimal = binaryTodecimal(int_polinom_generator)
# print(polinom_generator_in_decimal)
# calculez puterea lui x cu care inmultesc polinomul ce rezulta din mesaj
puterea_cu_care_inmultesc = pow(2, coeficientul_cu_care_inmultesc)
# calculez mesajul care urmeaza sa fie impartit la polinomul generator
mesaj_la_care_se_face_impartirea = message_in_decimal * puterea_cu_care_inmultesc
# print(mesaj_la_care_se_face_impartirea)
# calculez catul si il fac de tip int
catul = int(mesaj_la_care_se_face_impartirea / polinom_generator_in_decimal)
#print(f"Catul este {catul}")
# calculez restul care va fi ulterior adaugat la mesajul initial
restul = mesaj_la_care_se_face_impartirea - catul * polinom_generator_in_decimal
# print(restul)

# functie care converteste un numar din baza 10 in baza 2


def decimalToBinary(n):
    return bin(n).replace("0b", "")


# calculez restul in binar
restul_in_binar = decimalToBinary(restul)
print(f"Restul este: {restul_in_binar}")
# calculez si afisez mesajul emis
mesajul_emis = message + str(restul_in_binar)
print(f"Mesajul emis este: {mesajul_emis}")
