def selectseat(i, j, seats):
    price = -1
    if i < 0 or i > 9 or j < 0 or j > 10:
        return ('Selected number is out of bound!')
    elif seats[i][j] == 0:
        return ('This seat is already sold!')
    else:
        price = seats[i][j]
        seats[i][j] = 0
        return (f'Seat number [{i},{j}] is asigned to you and the price is: {price}')

def selectprice(price , seats):

    found = False
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == price and not found:
                found = True
                seats[i][j] = 0
                return (f'Seat number [{i},{j}] is asigned to you!')
    if not found:
        return ('There are no empty seats available at this price!')


def main():

    row0 = [10]*10
    row1 = [10]*10
    row2 = [10]*10
    row3 = [10,10,20,20,20,20,20,20,10,10]
    row4 = [10,10,20,20,20,20,20,20,10,10]
    row5 = [10,10,20,20,20,20,20,20,10,10]
    row6 = [20,20,30,30,40,40,30,30,20,20]
    row7 = [20,30,30,40,50,50,40,30,30,20]
    row8 = [30,40,50,50,50,50,50,50,40,30]
    seats = [row0, row1, row2, row3, row4, row5, row6, row7, row8]

    userInput = input('Enter "a" to select a seat, "b" for price and "Space" to exit: ')
    while userInput != ' ':
        if userInput == 'a':
            i = int(input('Please enter a row number(0-8): '))
            j = int(input('Please enter a column number(0-9): '))
            print(selectseat(i , j , seats))
        elif userInput == 'b':
            price = int(input('Please enter a price: '))
            print(selectprice(price, seats))
        userInput = input('Enter "a" to select a seat, "b" for price and "Space" to exit: ')

    print('Bye!')

if __name__ == '__main__':
    main()


