cashInHand = []
gold = []
goldPricePerGram = int(input('What is the price per gram today? '))

def goldAndCashCal():
    while True:
        cash = int(input('How much have you got in hand? '))
        if cash == 0:
            break
        else:
            cashInHand.append(cash)

    while True:
        goldcal = int(input('How many gram do you have in savings? '))
        if goldcal == 0:
            break
        else:
            gold.append(goldcal)

def zakatCalculation():
    cash = round(sum(cashInHand))
    goldsav = round(sum(gold))
    goldSavings = goldsav * goldPricePerGram

    add = cash + goldSavings
    goldConvert = round(add / goldPricePerGram)

    print(' ')
    print('You have worth of £',add)
    print(' ')
    print('AND')
    print(' ')
    print('You have worth of',goldConvert,'Gram gold')
    print(' ')

    if goldConvert > 85:
        print('You have more than 85 Gram of gold')
        print(' ')
        print('You are eligible to pay Zakat this year')
        print(' ')

        percent = 2.5 / 100
        result = round(add * percent)

        print('You have to pay £',result,'from your savings')
    else:
        print('You are not eligible to pay Zakat this year')


goldAndCashCal()
zakatCalculation()
