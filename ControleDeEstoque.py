class Product:
    def __init__(self, name, price, code, quantity):
        self.name = name
        self.price = price
        self.code = code
        self.quantity = quantity

    def getName(self):
        return self.name

    def getCode(self):
        return self.code


# Array used to store the itens
listOfItens = []


# Function used for register a new product in the system
def productRegister(name, price, quantity):
    code = len(listOfItens) + 1
    newProduct = Product(name, price, code, quantity)
    listOfItens.append(newProduct)


# Function used for search for the product inserted by the user by name or code ignoring case sensitivy
def showProducts(search):
    found = False
    for product in listOfItens:
        if product.getName().lower() == search.lower() or str(product.getCode()).lower() == search.lower():
            print("\nPRODUCT: " + product.name)
            print("PRICE: " + product.price)
            print(f"QUANTITY ON STOCK: {product.quantity}")
            print(f"PRODUCT CODE: {product.code}")
            found = True
            break
    if not found:
        print("Produto não encontrado")

# function to list all the itens registered


def listAllProducts():
    for product in listOfItens:
        print(
            f"\nProduct: {product.name}, Quantity: {product.quantity}, Price: {product.price}, Code: {product.code}")


# function used to delete a product by its name or code
def deleteProduct(nameCode, password):
    found = False;
    for i, product in enumerate(listOfItens):
        if (product.getName().lower() == nameCode.lower() or str(product.getCode()).lower() == nameCode.lower()) and password == 'admin':
            del listOfItens[i]
            print("Product deleted")
            found = True;
            break;
        elif (product.getName().lower() == nameCode.lower() or str(product.getCode()).lower() == nameCode.lower()) and password != 'admin':
            found = True
            break;
    if not found:
        print("Product not found on stock");
    elif found and password != 'admin':
        print("Password incorrect!")

# function used to edit a item
#The user can choose wich atribute is gonna be edited or if all of then are going to be changed.
def editItem(nameCode):
    for product in listOfItens:
        if product.getName().lower() == nameCode.lower() or str(product.getCode()).lower() == nameCode.lower():
            print(f"\nProduct to be edited: {product.getName()}")
            print('1.Edit item name')
            print('2.Edit item price')
            print('3.Edit item quantity')
            print('4.Edit all the parameters')
            option = input('Choose a option: ')

            if option == '1':
                newName = input('Insert the new name of the product: ')
                product.name = newName
                print(f'Product name edited, new name: {newName}')
            elif option == '2':
                newPrice = input('Insert the new price of the product: ');
                product.price = newPrice;
                print(f'Product price edited, new price: {newPrice}');
            elif option == '3':
                newQuantity = input('Insert the new quantity of the item: ');
                product.quantity = newQuantity;
                print(f'Product quantity edited, new quantity: {newQuantity}');
            elif option == '4':
                newName = input('Insert the new name of the product: ');
                newPrice = input('Insert the new price of the item: ');
                newQuantity = input('Insert the new quantity of the item: ');
                product.name = newName;
                product.price = newPrice;
                product.quantity = newQuantity;
                print('Product edited!')
            else:
                print("Invalid option!!");
                return; 
            return;
    print("Product not found on stock")


# Loop to continue the code execution
while True:
    print("\n1.Register a new product")
    print("2.Search for a product on the stock")
    print("3.List all the itens on stock")
    print("4.Delete a item")
    print("5.Edit a item")
    print("6.Exit")

    option = input("Choose a option: \n")

    if option == '1':
        name = input('Product name: ')
        price = input('Product price: ')
        quantity = input('Product quantity: ')

        productRegister(name, price, quantity)
        print("Produto cadastrado")

    elif option == '2':
        search = input('Name or code of the product: ')
        showProducts(search)

    elif option == '3':
        listAllProducts()

    elif option == '4':
        nameCode = input('Enter the name or code of the item to be deleted: ')
        password = input('Type the admin password to delete the item: ')
        deleteProduct(nameCode, password)

    elif option == '5':
        nameCode = input(
            'Enter que the name or code of the product to be edited: ')
        editItem(nameCode)

    elif option == '6':
        break

    else:
        print("Opção inválida")
