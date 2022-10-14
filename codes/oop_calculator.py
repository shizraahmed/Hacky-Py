# Bima Rakajati
# A11.2020.13088


class Kalkulator(object):
    "kalkulator PBO"

    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2

    def addition(self):
        return self.bil1 + self.bil2

    def subtraction(self):
        return self.bil1 - self.bil2

    def multiplication(self):
        return self.bil1 * self.bil2

    def division(self):
        return self.bil1 // self.bil2

    def modulus(self):
        return self.bil1 % self.bil2


def main():
    jawab = "yes"

    while jawab == "yes":
        # Menu kalkulator
        print("OPERATION MENU")
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Distribution")
        print("5. Remaining Divide")

        # Input dari user
        pilihan = input("\nEnter option(1-5): ")
        bil1 = int(input("Enter the first number: "))
        bil2 = int(input("Enter the second number: "))
        calc = Kalkulator(bil1, bil2)

        if pilihan == "1":  # Penjumlahan
            print("Sum Result =", calc.addition())
        elif pilihan == "2":  # Pengurangan
            print("Subtraction Result =", calc.subtraction())
        elif pilihan == "3":  # Perkalian
            print("Multiplication Result =", calc.multiplication())
        elif pilihan == "4":  # Pembagian
            print("Dividend Result =", calc.division())
        elif pilihan == "5":  # Modulus
            print("Dividend Remaining Result =", calc.modulus())
        else:  # Input salah apabila user memasukkan selain angka 1-5
            print("Wrong input")

        # Agar program bisa ke menu setelah selesai melakukan operasi
        jawab = input("\nWant to return to menu (yes/no)? ").lower()


if __name__ == "__main__":
    main()
