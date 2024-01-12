import random

MAX_LINES = 3 #global constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3

symbol_count = {
     "A": 2,
     "B": 4,
     "C": 6,
     "D": 8
}

symbol_value = {
     "A": 5,
     "B": 4,
     "C": 3,
     "D": 2
}

def check_winnings(columns, lines, bet, values):
     winnings = 0 
     winning_lines = []
     for line in range(lines):
          symbol = columns[0][line]
          for column in columns:
               symbol_to_check = column[line]
               if symbol != symbol_to_check:
                    break
          else:
               winnings += values[symbol] * bet
               winning_lines.append(line+1)
     
     return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
     all_symbols = []
     for symbol, symbol_count in symbols.items():
          for _ in range(symbol_count):
               all_symbols.append(symbol)

     columns = []
     for col in range(cols):
          column = []
          current_symbols = all_symbols[:]
          for row in range(rows):
               value = random.choice(all_symbols)
               current_symbols.remove(value)
               column.append(value)
          
          columns.append(column)
     
     return columns

def print_slot_machines(columns):
     for row in range(len(columns[0])):
          for i, column in enumerate(columns):
               if i != len(columns)-1:
                    print(column[row], end = "|")
               else:
                    print(column[row], end="")
          print()

#collecting users input (user's deposits and bets)
def deposit():
    while True: #continuously ask user for deposit amount until they give the input
         amount = input("What is your deposit amount? $")
         
         if amount.isdigit(): #if it is a valid whole number
              amount = int(amount) #convert it to int
              if amount > 0:
                   break #terminates the while loop 
              else:
                   print("Amount must be greater than 0.")
            
         else: #if the amount is not a digit
              print("Please enter a number.")
    #print("The amount is: $", amount)         
    return amount

def get_number_of_lines():
     while True:
          lines = input("Enter the number of lies to bet on (1 -" + str(MAX_LINES) + ")? ")
          if lines.isdigit():
               lines = int(lines)
               if 1<= lines <= MAX_LINES:
                    break
               else:
                    print("Enter a valid number of lines. ")
          else:
               print("Enter a valid number.")
     return lines
               
def get_bet():
     while True:
          bet = input("What would you like to bet? $")
          if bet.isdigit():
               bet = int(bet)
               if MIN_BET <= bet <= MAX_BET:
                    break
               else:
                    print(f"Bet must be in range  ${MIN_BET} - ${MAX_BET}.")
          else:
               print("Enter a valid betting amount.")
     return bet

def spin(balance):
     lines = get_number_of_lines()
     while True:
          bet = get_bet()
          total_bet = bet * lines
          if total_bet <= balance:
               break
          else:
               print(f"Your total bet exceeded the deposit amount. Your current balance is: ${balance}")
     print(f"You are betting ${bet} on {lines} lines. Total bey is equal to ${total_bet}")

     slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
     print_slot_machines(slots)
     winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
     print(f"You won ${winnings}")
     print(f"Youn won on lines:", *winning_lines) 
     return winnings - total_bet

def main():
     balance = deposit()
     while True:
          print(f"current balance is ${balance}")
          prompt = input("Press enter to play (q to quit).")
          if prompt == "q":
               break
          balance += spin(balance)
     print(f"You left with ${balance}")
main()



