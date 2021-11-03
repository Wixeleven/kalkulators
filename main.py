# Varbutiba kalkulators
# Aleksejs Žukovskis
# Darums 03.11.2021 V2V


def statistiska():


    q = float(input(" Geben Sie die Gesamtanzahl von Ereignis A ein: "))
    w = float(input(" Geben Sie ein, wie oft das A-Ereignis auftritt: "))

    e = q/w
    r = e*100

    if q<0:
        return print("Ihre erste Zahl darf nicht negativ sein, bitte versuchen Sie es erneut")
    elif w<0:
         return print("Ihre zweite Zahl darf nicht negativ sein, bitte versuchen Sie es erneut")
    print("Ist ein " + format( r,",.2f")+"%", "Wahrscheinlichkeit, dass aus", q ,"Gelegentlich tritt ein Ereignis auf ",w," mal")


def geometriksa():


    q = float(input("볼륨 및 반경: "))
    w = int(input("가장자리 길이): "))
    π = 3.14

    e = (w * w)/(q * q)*π

    r = e * 100

    print("확률은" + format( r, ",.2f")+"%")
    if r>100:
        print("확률은 100%를 초과해서는 안 됩니다.")


def klasiska():


    q = int(input("好意的なイベントの数を入力してください: "))
    w = int(input("イベントの総数を教えてください: "))

    e = q/w
    d = e * 100

    print("確率は = " + format(d, ",.2f")+"%")


if __name__ == '__main__':
    choice = input("Kada veida varbutibas aprekini Tev šodien padoma? \n"
                   "Ievadi burtu:\n-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n")
    if choice.lower() == 'k':
        klasiska()
    if choice.lower() == 'g':
        geometriksa()
    if choice.lower() == 's':
        statistiska()
    else:
        exit(0)