user_input = 'random'
data = []
def show_menu():
    print('Menu:')
    print('1. Add an Item')
    print('2. Mark as Done')
    print('3. View Iteams')
    print('4. Exit')

while user_input != '4':
    show_menu()
    user_input = input('Enter Your Choice:')

    if user_input == '1':
        item = input('What is to be done?')
        data.append(item)
        print('Added Item',item)
    elif user_input == '2':
        item = input('What is to be Marked as Done')
        if item in data:
            data.remove(item)
            print('Removed Item',item)
        else:
            print('Item Not Found')
    elif user_input == '3':
        print('List of to do items')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Good Bye')
    else:
        print('Please Enter 1 , 2 , 3 or 4')
