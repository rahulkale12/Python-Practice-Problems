#2. coins= [1,5,10,25]
#amount = 63
#output = 6
#write a python code which return number of coins to make the amount 63 here the optimal solution is 25+25+10+1+1+1 



def calculate_coins(coins,amount):
    coins.sort(reverse = True)
    count = 0

    for coin in coins:
        while amount>=coin:
            amount -= coin
            count+=1

            if amount == 0:
                break
    return count

coins = [1,5,10,25]
amount = 63

print(calculate_coins(coins,amount))