from math_function import * #asteris sama dengan import all modul dalam sebuah file (modul).


def main():

    while True:
        try:
            data_1 = int(input("masukkan input 1 :"))
            data_2 = int(input("masukkan input 2 :"))
            if type(data_1) == int and type(data_2) == int:
                break
        except ValueError:
              print("Please Input an Integer.")        
    
    while True:
        operator = input("masukkan operator :")
        if operator == "+":
            result = addition(data_1, data_2)
            break
        elif operator == "*":
            result = multiplication(data_1, data_2)
            break
        elif operator == "/":
            result = division(data_1, data_2)
            break
        else:
            print("Operator belum ditambahkan, coba input ulang operator matematika seperti pertambahan(+), perkalian(*), dan pembagian(/)")


    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()