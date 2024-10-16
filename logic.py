import random
from decouple import Config, RepositoryIni

config = Config(RepositoryIni('settings.ini'))

min_number = config('min_number', default=1, cast=int)  
max_number = config('max_number', default=10, cast=int)  
attempts = config('attempts', default=5, cast=int)       
starting_balance = config('starting_balance', default=1000, cast=int)  #

def guess_number_game():
    balance = starting_balance
    target_number = random.randint(min_number, max_number)
    print(f"У вас {attempts} попыток угадать число от {min_number} до {max_number}.")
    
    for i in range(attempts):
        print(f"Текущий баланс: {balance}")
        bet = int(input("Сделайте ставку: "))
        if bet > balance:
            print("Недостаточно средств для ставки.")
            continue
        
        guess = int(input("Введите ваше предположение: "))
        
        if guess == target_number:
            print("Вы угадали!")
            balance += bet * 2
            break
        else:
            print("Неправильно, вы теряете ставку.")
            balance -= bet
        
        if balance <= 0:
            print("Вы потеряли все деньги.")
            break

    print(f"Игра окончена. Ваш баланс: {balance}")
