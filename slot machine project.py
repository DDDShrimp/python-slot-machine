import random   #damit wir die slot machine values random generieren wollen

MAX_LINES = 3  # das ist ein global konstant, es ist in Capital weil es ein Konstantanter wert ist welches nicht geändert wird
MAX_BET = 100  #außerdem ist es auch konstent, damit man die überall im code benutzten kann also max lines, max bet und min bet
MIN_BET = 1

ROWS = 3   #die slot machine wird nur so gemacht, da quasi geschaut wird wie viel waagrecht richtig ist anstaat horizontal
COLS = 3

symbol_count = {        #wir wollen hier schauen wie viele symbolen in diesen cols sind, wie viele wir haben wollen insgesamt und was die sein sollen, btw das ist ein dictionary
    "♠": 3,    #most valuable
    "♥": 5,
    "♦": 6,
    "♣": 6
}

symbol_value = {        
    "♠": 8,    
    "♥": 5,
    "♦": 3,
    "♣": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  #[0] weil wir haben alle column aber nicht alle reihen, also zuerst column, dann line 0, 1, 2
        for column in columns: 
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break #break weil wenn ein symbol nicht = zu vorherigen symbol ist wird gebreaked, if not the same
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) #+1 weil es ein index ist
            
    return winnings, winning_lines
    

def get_slo_machine_spin(rows, cols, symbols):  #wir wollen hier generieen, was der outcome von der slot machine ist von den values von symbol, rows und cols. in dieser funktion generien wird weclehes symbol in welchen colom kommt based of frequenzy von den symbolen die wir haben, für jeden colom random generiert
    all_symbols = []  #hier kommen alle values die possibly bekommen könnten und random 3 dieser values wählen können, und wenn wir ein value chosen removen wir es von der liste und choosen again. (NICHT MOST EFFICIENT ALOGITHEM)
    for symbol, symbol_count in symbols.items():    #for loop damit geadded wird wie viele symbols wir in der all_symbols liste haben. .items gibt key und value von dictionary
        for _ in range(symbol_count):    # es ist _ anstatt i weil mir die zahl egal ist, also random
            all_symbols.append(symbol)  #es wird durch dictionary geloopt z.b ich habe ♠ zuerst und symbol count ist 3, dann kommt die nächste for loop wo man durch symbol count looped, und da es 3 ist wird es 3 mal gelooped in den all symbols list


    columns = []    #das ist eine nested list, welches alle values in den colums bekommt. normaler weise macht man nested list so  [[0, 0], [0, 1], []]  aber hier wird es andersrum gemacht wo each of the nested list die value representiert in unserem colum
    for _ in range(cols):    #für jeden colum, generieren wir eine certain number von symbolen
        column = []
        current_symbols = all_symbols[:] #so koopiert man eine liste ohne dass die og liste irgendwie beinflusst wird
        for _ in range(rows):
            value = random.choice(current_symbols)   #wir benutzen nicht all symbols sonder copy, denn wir müssen eine value holen und müssen es von der liste removen, damit wir den value nicht wieder choosen können. sprich wir haben nur 3 ♠, weshalb wir nicht 4 bekommen können
            current_symbols.remove(value) #es such nach den first instance in der liste und löscht es von der koopie liste
            column.append(value)
            
        columns.append(column) #zuerst haben wir eine liste gemacht, dann generieren wir ein column, für jeden single column den wir haben dann werden random values für jede row in columns. dann wird gelooped through the values of numbers we need to generate, welches equal to the number of rows ist welches wir in unsere slot machine haben, wird random gewählt, gelöscht damit nicht zu viel von symbol benutzt ist, und wird dann hinzugefügt in column liste
        
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) -1:  #max index was wir haben, index max 3
                print(column[row], end=" | ") #end damit keine zeile runter geprinted wird sondern nebeneinander
            else:
                print(column[row], end="")
                
        print() #damit quasi neue zeile wo alles nebenan geprinted wird
            
    

def deposit():     #for collecting user input that gets the deposite from the user
    while True:             #while loop weil wir fragen user deposite amount zu entern bis die einen valid amount geben, wenn nicht valid gehts solange bis der amount valid ist
        amount = input("What would you like to deposit? $")
        if amount.isdigit():   #is.digit ist damit geschaut wird ob im input wirklich nur eine zahl eingegeben wird und nicht ein str, oder bool oder etc, negative nummer geht nicht
            amount = int(amount)    #weil input wird davor als str geschrieben und weil wir es als zahl haben konvertieren wir es von str zu integer, aber damit nicht str zu int gemacht wird ist if amount.isdigit da um zu schauen, ob es wirklich eine zahl ist
            if amount > 0:
                break    #break ist hier um den loop zu stoppen wenn man eine zahl höher als 0 eingibt
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount           #hier wird dann der amount wiedergegeben bzw den wert
    
def get_number_of_lines():    #hier fragen wir den spiler eine zahl von 1 bis 3
    while True:             
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #Max lines wurde in den str hinzugefügt, basic, es muss als str konvertiert werden, weil würde man 2 str schreiben wäre es eng und wenn eine zahl reingeschreiben wird wäre es eine exception im programm
        if lines.isdigit():   
            lines = int(lines) #hier wird gechecked ob die lines in der grenze sind also 1 bis 3  
            if 1 <= lines <= MAX_LINES: #so checked man wen ein wert zwischen 2 werten ist, hier wird geschaut wenn die linie größer gleich eins ist und weniger als max lines wird die loop gebreaked
                break    
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
            
    return lines 
    
def get_bet():  # die funktion ist damit man weiß vie wiel geld man für jede linie wetten will
    while True:             
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #hier wird wieder auch gechecked ob amount eine zahl ist 
            amount = int(amount)   # da wirds wieder zu einem integer konvertiert  
            if MIN_BET <= amount <= MAX_BET:  #hier wird gechecked ob amount zwischen min bet und max bet ist
                break    
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #dies ist ein f string, kann man easy irgendeine variable reinschreiben in {}, es wird dann automatisch in str konvertiert wenn es geht
        else:
            print("Please enter a number.")
            
    return amount 
 
 
def spin(balance):
    lines = get_number_of_lines()
    while True:     #wir müssen auch checken ob die anzahl was die wetten , ob die noch so viel geld haben, da die nicht mehr wetten können als die haben
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}") #hier möchen wir in die hauptfunktion dass quasi alles gesagt wird also wiederholt wird was bisher gesagt wurde 
    
    slots = get_slo_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) #splat opperator es passed jede line from winning lines, in die print funktion you won on lines
    return winnings - total_bet
    
    
def main():     #main, ist wenn wir unser programm enden, rufen wir die funktion wieder und es reruned wieder die Funktion anstatt dass es nur 1 mal ausgeführt wird
    balance = deposit()    #um die funktion aufzurufen damit alles gestartet wird
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"Your left with ${balance}")

    
main()  # damit funktion wieder gerufen wird