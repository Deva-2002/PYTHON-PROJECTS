import random

MAX_LINES=3

MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count ={
    "A" :2,
    "B" :4,
    "C" :6,
    "D" :8
}

symbol_value ={
    "A" :5,
    "B" :4,
    "C" :3,
    "D" :2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range (rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end="|")
            else:
                print(column[row],end="")

        print()



def deposit():

    while True:
        amount=input("enter the amount to be deposited($): ")

        if amount.isdigit():
            amount=int(amount)

            if amount>0:
                break
            else:
                print("amount must be greater than zero")

        else:
            print("please enter a numeric value")

    return amount

def no_of_lines():

    while True():
        lines=input("enter the no of lines you want to bet on ( 1 -" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("please enter a value between (1 and" + MAX_LINES + ")" )
        else:
            print("please enter a numeric value")
    return lines

def get_bet():

    while True():
        bet=input("enter the amount you want to bet")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<= bet <= MAX_BET:
                break
            else:
                print(f"please enter a value between {MIN_BET} - {MAX_BET}" )
        else:
            print("please enter a numeric value")
    return bet


def games():
    lines = no_of_lines()
    while True:
        balance=deposit()
        bet = get_bet()
        total_bet = lines * bet
        if total_bet >= balance:
            print(f"you dont have enough balance, your current account balance is {balance}")
        else:
            break
    print(f"You are betting an amount of {bet} on {lines} lines , the total betting amount is {total_bet}")
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}")
    print(f"you won on lines:", *winning_lines)
def main():

    balance=deposit()
    while True:
        print(f"current balance is $(balance)")
        spin=input("press enter to play( q to quit)")
        if spin=="q":
            break
        balance+=spin()
        print(f"you left with balance {balance}")

main()