import os 
import csv
import datetime

def title():
    line1 = '---------------------------------------'
    title = 'Contact Management System'
    line2 = '---------------------------------------'

    print(line1.center(120))
    print(title.center(120))
    print(line2.center(120))

class contact_function():
    contact_fields = ['Name','Mobile No.']
    contact_database = 'contacts.csv'
    contact_data = []

    #------------- create function -----------------
    def create(self):
        os.system('cls')
        title()
        print('--------------')
        print('Create Contact')
        print('--------------')

        for fields in self.contact_fields:
            contact_details = input('Enter ' + fields + ' :')
            print('')
            self.contact_data.append(contact_details)

        Date = datetime.datetime.today()
        d = Date.strftime('%B %d %Y')
        self.contact_data.append(d)

        with open(self.contact_database, 'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])
        
        self.contact_data = []
        print('Contact Created Successfully'.center(120))
        print('\n')

    #------------------- view function ------------------
    def view(self):
        os.system('cls')
        title()

        print('--------------')
        print('All Contacts')
        print('--------------')

        count = 0

        with open(self.contact_database,'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count = count + 1
            print('Total Contacts: ' ,count)
            print('')

        with open(self.contact_database,'r') as file:
            read =csv.reader(file)
            if os.path.getsize(self.contact_database)  == 0:
                print('Contact book is empty , please create contacts'.center(120))
            else:
                for fields in self.contact_fields:
                    print('{0:<10}'.format(fields).center(10),end='\t\t')
                print('{0:<10}'.format('Date'))
                print('{:<10}\t\t{:10}\t\t{:<10}'.format('------','------------','------'))
                print('\n')

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(10),end='\t\t')
                    print('')
        print('\n')
        input('\t\t\t\t Press Enter To Continue...')

    #------------------- search function ---------------------
    def search(self):
        os.system('cls')
        title()

        print('--------------')
        print('Search Contact')
        print('--------------')

        self.contact_match = 'False'
        search_value = input('Enter Your Name: ')
        print('')

        for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10),end='\t\t')
        print('{0:<10}'.format('Date'))
        print('{:<10}\t\t{:10}\t\t{:<10}'.format('------','------------','------'))
        print('\n')

        with open(self.contact_database,'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:10}\t\t{:<10}'.format(data[0],data[1],data[2]))
        if self.contact_match == 'False':
            print('')
            print('Sorry! There is no contact by this name'.center(120))
            print('')

    #---------------- delete function ---------------
    def delete(self):
        os.system('cls')
        title()

        print('--------------')
        print('Delete Contact')
        print('--------------')

        self.contact_match = 'False'
        delete_value = input('Enter Your Name: ')
        update_list = []

        with open(self.contact_database,'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'
        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print('')
                print('Contact is deleted successfully'.center(120))
        
        if self.contact_match == 'False':
            print('')
            print('Sorry! data not found')
            print('')

contact_class = contact_function()
os.system('cls')
title()

while True:
    print('1. View Contact  '.center(120))
    print('2. Create Contact'.center(120))
    print('3. Search Contact'.center(120))
    print('4. Delete Contact'.center(120))
    print('5. Exit           '.center(120))
    print('---------------------------------------'.center(120))
    option = input('\t\t\t\t\t\tChoose Your Option -> ')

    if option == '1':
        contact_class.view()
        title()

    elif option == '2':
        while True:
            contact_class.create()
            ans = input('\t\t\t\t\tdo you want to create another contact number?[Y/y or N/n]:')
            
            if ans == 'Y' or ans == 'y':
                continue
            else:
                break
        os.system('cls')
        title()
        
    elif option == '3':
            while True:
                contact_class.search()
                ans = input('\n\n\t\t\t\t\tdo you want to search another contact number?[Y/y or N/n]:')
            
                if ans == 'Y' or ans == 'y':
                    continue
                else:
                    break
            os.system('cls')
            title()  

    elif option == '4':
            while True:
                contact_class.delete()
                ans = input('\t\t\t\t\tdo you want to delete another contact number?[Y/y or N/n]:')
            
                if ans == 'Y' or ans == 'y':
                    continue
                else:
                    break
            os.system('cls')
            title()    
    elif option == '5':
        os.system('cls')
        line1 = '----------------------------------------------'
        title = 'Thank You For Using Contact Management System'
        line2 = '----------------------------------------------'

        print(line1.center(120))
        print(title.center(120))
        print(line2.center(120))
        break