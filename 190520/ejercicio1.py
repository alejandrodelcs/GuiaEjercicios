#!/usr/bin/env python3

def valor_total_inventario(stock):
    for inventario in stock.values():
        total = inventario[0]*inventario[1]

    print(total)
        
    
def main():
    stock = {1:[2,300], 2:[5000,3],5:[60,400]}
    valor_total_inventario(stock)


main()