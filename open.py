import csv
import os
import locale

product_list = []

def load_data(filename):
    global products 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    
def get_products(products):
    for product in products:
        product_info = f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id

def get_product_by_id():
    id = int(input("Vilket id vill du ha"))
    print(product_list[id])

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
load_data('db_products.csv')

print(get_products(products))

get_product_by_id()


