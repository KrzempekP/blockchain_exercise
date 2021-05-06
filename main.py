import random

from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()
    while True:
        print("Co chcesz zrobic?")
        print("1. Wykonaj nowa transakcje")
        print("2. Zobacz ilosc oczekujacych transakcji")
        print("3. Zobacz liczbe blokow w lancuchu")
        print("4. Stworz nowy blok")
        wybor = int(input("Wybor(podaj liczbe): "))

        if wybor == 1:
            sender = input("Podaj nadawca: ")
            recipient = input("Podaj odbiorce: ")
            amount = input("Podaj ile znaczkow: ")
            t1 = blockchain.new_transaction(sender, recipient, amount)
            print("Transakcja oczekuje na potwierdzenie")
        elif wybor == 2:
            print(blockchain.get_pending())
        elif wybor == 3:
            print(blockchain.get_block_count())
        elif wybor == 4:
            blockchain.new_block(random.randint(1, 10000000))
        else:
            print("Zle wybrano numer")
