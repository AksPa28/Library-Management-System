import mysql.connector

# SOURCE CODE FOR LIBRARY
try:
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='akshit')
    print()
    print(" /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ || WELCOME TO LIBRARY MANAGEMENT SYSTEM || /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")

    #CREATING DATABASE
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists library")
    mycursor.execute("use library")

    #CREATING REQUIRED TABLES
    mycursor.execute("create table if not exists library_master(cardno char(6) PRIMARY KEY,name_of_person varchar(30),phone_no char(10),address varchar(100),dob date)")
    mycursor.execute("create table if not exists books(book_name varchar(30),book_no char(5) primary key,genre varchar(30),authors_name varchar(100),language varchar(15))")
    mycursor.execute("create table if not exists library_transaction(cardno char(6),foreign key(cardno) REFERENCES library_master(cardno) ON DELETE CASCADE,book_name varchar(20),date_of_lend date,date_of_return date)") 
    mycursor.execute("create table if not exists buy_new_books(orderno varchar(6) primary key,name_of_book varchar(20),del_date date,price char(6))")
    mydb.commit()  # To execute the commands above

    while True: 
    #Only for head librarians ---->
    #Sign In 
        print("\n ******* ENTER THE FOLLOWING DETAILS TO CONTINUE AS HEAD LIBRARIAN ******* ")
        name=input("Enter your name:")
        username=input("Enter username:")
        passwd=input('Enter Password:')
        details = username+"\n"+passwd

        try:
            file1=open("{}.txt".format(name),"r")
            crosscheck=file1.read()
            if crosscheck==details:
                print("LOG IN SUCCESSFULL\n")
                _continue_=input('Press any key to continue : ')
                print()

                if _continue_.isalnum()==True or _continue_.isalnum()==False or _continue_.isspace():
                    while True: 
                        print("1. Create a New Student Account")   
                        print("2. See the Account info. ")   
                        print("3. Update Card Holder info.")   
                        print("4. Delete Account") 
                        print("5. Show all the accounts")  
                        print("6. Add new Book")    
                        print("7. Books List")
                        print("8. Update Book Details")       
                        print("9. Search Books")    
                        print("10. Delete Book")
                        print("11. Lend a Book")         
                        print("12. Return a Book")    
                        print("13. Calculate late fee")     
                        print("14. Display lending history")         
                        print("15. Order a New Book")               
                        print("16. Update Order Details")              
                        print("17. Display Ordering History")   
                        print("18. Exit the program")              
                        print()

                        ch=int(input("Enter Your Choice :"))

                    #TO CREATE A LIBRARY ACCOUNT
                        if ch==1:
                                print("FILL ALL PERSONAL DETAILS OF ACCOUNT HOLDER :-")
                                cardno=str(input("Enter card no:"))
                                name_of_person=str(input("Enter Name (Limit 30 characters) :"))
                                phone_no=str(input("Enter Phone No :"))
                                address=str(input("Enter the Address (max 100 words) :"))
                                dob=str(input("Enter DOB(yyyy-mm-dd) :"))
                                mycursor.execute("insert into library_master values('{}','{}','{}','{}','{}')".format(cardno,name_of_person,phone_no,address,dob))
                                mydb.commit()
                                print("ACCOUNT IS SUCCESSFULLY CREATED!!!")

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
                                
                    #TO SEE DETAILS OF CARD HOLDER
                                
                        if ch==2:
                            cardno=str(input("Enter card no:"))
                            mycursor.execute("select  *  from library_master where cardno='{}'".format(cardno))
                            print("_CARD NO._ , _NAME_ , _PHONE NO._ , _ADDRESS_ , D.O.B_")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                                
                    #TO UPDATE CARD HOLDER INFORMATION
                                
                        if ch==3:
                            print("Press 1 to Update Name ")
                            print("Press 2 to Update Phone No.")
                            print("Press 3 to Update Address")
                            print("Press 4 to Update DOB")

                            ch1=int(input("Enter your choice: "))
                            
                    #TO UPDATE NAME
                            
                            if ch1==1:
                                cardno=str(input("Enter Card No. :"))
                                name_of_person=str(input("Enter new name:"))
                                mycursor.execute("update library_master set name_of_person='{}' where cardno='{}'".format(name_of_person,cardno))
                                mydb.commit()
                                print("*Name has been updated*")
                                mycursor.execute("select * from library_master where cardno='"+cardno+"'")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
                                    
                    #TO UPDATE PHONE NUMBER
                                    
                            if ch1==2:
                                cardno=str(input("Enter card no:"))
                                phone_no=str(input("Enter new phone no:"))
                                mycursor.execute("update library_master set phone_no='{}' where cardno='{}'".format(phone_no,cardno))
                                mydb.commit()
                                print("*Number has been updated*\n")
                                mycursor.execute("select * from library_master where cardno='"+cardno+"'")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break

                    #TO UPDATE ADDRESS

                            if ch1==3:
                                cardno=str(input("Enter Card No. :"))
                                address=str(input("Enter new Address:"))
                                mycursor.execute("update library_master set address='{}' where cardno='{}'".format(address,cardno))
                                mydb.commit()
                                print("*Address has been updated*\n")
                                mycursor.execute("select * from library_master where cardno='"+cardno+"'")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break

                    #TO UPDATE DATE OF BIRTH
                                    
                            if ch1==4:
                                cardno=str(input("Enter Card No. :"))
                                dob=str(input("Enter new DOB(yyyy-mm-dd):"))
                                mycursor.execute("update library_master set dob='{}' where cardno='{}'".format(dob,cardno))
                                mydb.commit()
                                print("*Date of Birth has been updated*\n")
                                mycursor.execute("select * from library_master where cardno='"+cardno+"'")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
                                    
                    #TO DELETE AN ACCOUNT
                                    
                        if ch==4:
                            cardno=str(input("Enter cardno to be removed:"))
                            mycursor.execute("delete from library_master where cardno='{}'".format(cardno))
                            mydb.commit()
                            print("*Removed the account successfully :)*")

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break

                    #TO SHOW ALL THE REGISTERED ACCOUNTS
                        
                        if ch==5:
                            print("--- THE REGISTERED ACCOUNTS ARE ---")
                            print("_CARD NO._ , _NAME_ , _PHONE NO._ , _ADDRESS_ , D.O.B_")
                            mycursor.execute("select * from library_master")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                                    
                    #TO ADD NEW BOOK
                                    
                        if ch==6:
                            print("FILL ALL BOOK DETAILS BELOW :")
                            book_name=str(input("Enter Book  Name:"))
                            book_name.upper()
                            book_no=str(input("Enter Book No.(limit 5 characters):"))
                            genre=str(input("Enter Genre:"))
                            authors_name=str(input("Enter the Author's Name:"))
                            language=str(input("Enter the Language of Book:"))
                            mycursor.execute("insert into books values('{}','{}','{}','{}','{}')".format(book_name,book_no,genre,authors_name,language))
                            mydb.commit()
                            print("Book added succesfully*")

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break                      
                            
                    #TO SEE BOOK DETAILS
                            
                        if ch==7:
                            print("We have the the following books :)\n")
                            print("_BOOK NAME_ , _BOOK NO._ , _GENRE_ , _AUTHOR'S NAME_ , _LANGUAGE_")
                            mycursor.execute("select  *  from books")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                                
                    #TO UPDATE BOOK DETAILS
                                
                        if ch==8:
                            print("Press 1 to Update Book Name")
                            print("Press 2 to Update Genre")
                            print("Press 3 to Update Author's Name")
                            print("Press 4 to Update Language")
                            print(" ")
                            ch1=int(input("Enter your choice:"))

                    #TO UPDATE NAME

                            if ch1==1:
                                mycursor.execute("select * from books")
                                for i in mycursor:
                                    print(i)
                                book_no=str(input("Enter Book No. :"))
                                name_of_book=str(input("Enter new name:"))
                                mycursor.execute("update books set book_name='"+name_of_book+"' where book_no='"+book_no+"'")
                                mydb.commit()
                                print("*Book Name has been updated *")
                                mycursor.execute("select * from books where book_name={}".format(name_of_book))
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
                                    
                    #TO UPDATE GENRE
                                    
                            if ch1==2:
                                mycursor.execute("select * from books")
                                for i in mycursor:
                                    print(i)
                                book_no=str(input("Enter Card No. :"))
                                genre=str(input("Enter New Genre:"))
                                mycursor.execute("update books set genre='"+genre+"' where book_no='"+book_no+"'")
                                mydb.commit()
                                print("*Genre has been updated*")
                                mycursor.execute("select * from books")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break

                    #TO UPDATE AUTHOR NAME
                                    
                            if ch1==3:
                                # mycursor.execute("select * from books")
                                # for i in mycursor:
                                #     print(i)
                                book_no=str(input("Enter book no:"))
                                author=str(input("Enter new authors name:"))
                                mycursor.execute("update books set authors_name='"+author+"' where book_no='"+book_no+"'")
                                mydb.commit()
                                print("*Authors name has been updated*")
                                mycursor.execute("select * from books where book_no={}".format(book_no))
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
                                    
                    #TO UPDATE LANGUAGE
                                    
                            if ch1==4:
                                mycursor.execute("select * from books")
                                for i in mycursor:
                                    print(i)
                                book_no=str(input("Enter book no:"))
                                language=str(input("Enter new language:"))
                                mycursor.execute("update books set language='"+language+"' where book_no='"+book_no+"'")
                                mydb.commit()
                                print("*Language has been updated*")
                                mycursor.execute("select * from books")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break

                    #TO SEARCH BOOKS

                        if ch==9:
                            print("Press to search books by --")
                            print("   1. By Genre")
                            print("   2. By Author")
                            print("   3. By Language")
                            ch1=int(input("Enter you choice:"))

                            if ch1==1:
                                search_genre=input("Enter the genre you want to search :")
                                mycursor.execute("select *  from books where genre='"+search_genre+"'")
                                print("_BOOK NAME_ , _BOOK NO._ , _GENRE_ , _AUTHOR'S NAME_ , _LANGUAGE_")
                                for i in mycursor:
                                    print(i)
                            
                            elif ch1==2:
                                search_author=input("Enter the name of Author:")
                                mycursor.execute('select * from books where authors_name="{}"'.format(search_author))
                                print("_BOOK NAME_ , _BOOK NO._ , _GENRE_ , _AUTHOR'S NAME_ , _LANGUAGE_")
                                for i in mycursor:
                                    print(i)

                            elif ch1==3:
                                search_language=input("Enter Lanuage of book you want :")
                                mycursor.execute("select * from books where language='{}'".format(search_language))
                                print("_BOOK NAME_ , _BOOK NO._ , _GENRE_ , _AUTHOR'S NAME_ , _LANGUAGE_")
                                for i in mycursor:
                                    print(i)
                        
                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                    print()
                                    continue
                            else:
                                    break
                    #TO DELETE A BOOK
                                    
                        if ch==10:
                            mycursor.execute("select * from books")
                            for i in mycursor:
                                print(i)
                            book_no=str(input("Enter book no:"))
                            mycursor.execute("delete from books where book_no='"+book_no+"'")
                            mydb.commit()
                            print("*Removed succesfully*")
                            mycursor.execute("select * from books")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break

                    #TO LEND A BOOK
                                
                        if ch==11:
                            cardno=str(input("Enter card no:"))
                            book_name=str(input("Enter the name of the book:"))
                            date_of_lend=str(input("Enter date of Lending(yyyy-mm-dd):"))
                            mycursor.execute("insert into library_transaction(cardno,book_name,date_of_lend) values('"+cardno+"','"+book_name+"','"+date_of_lend+"')")
                            mydb.commit()
                            print("*Data successfully submitted*")

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                                
                    #TO RETURN A BOOK
                                
                        if ch==12:
                                cardno=str(input("Enter card no:"))
                                book_name=input("Enter book name:")
                                date_of_return=str(input("Enter date of Returning(yyyy-mm-dd):"))
                                mycursor.execute("update library_transaction set date_of_return='"+date_of_return+"' where cardno='"+cardno+"'and book_name='"+book_name+"'")
                                mydb.commit()
                                print("*Data successfully submitted*")

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break

                    # TO CALCULATE THE LATE FEE    
                        if ch ==13:
                                cardno = str(input("Enter card no.: "))
                                book_name = str(input("Enter book name: "))
                                mycursor.execute("select DATEDIFF(date_of_return,date_of_lend) from library_transaction where cardno='{}' AND book_name='{}'".format(cardno,book_name))

                                for i in mycursor:
                                    days = i

                                if (days[0])>15:
                                    print("You have exceeded the maximum day limit of returning the book...")
                                    fine = (days[0] - 15) * 20
                                    print("Your late fee is: Rs.",fine)
                                else:
                                    print("You have given the book in time !! ")    
                                    print("THANK YOU FOR YOUR COOPERATION")

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                    break
    

                    #TO SEE LENDING HISTORY
                                
                        if ch==14:
                            cardno=str(input("Enter card no:"))
                            mycursor.execute("select book_name,date_of_lend,date_of_return from library_transaction where cardno={}".format(cardno))
                            print("_NAME OF BOOK_,_DATE OF LENDING_,_DATE OF RETURNING_")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                                
                    #TO ORDER A NEW BOOK

                        if ch==15:
                            orderno=str(input("Enter the order no:"))
                            name_of_book=str(input("Enter the name of the book:"))
                            del_date=str(input("Enter the expected delivery date of books(yyyy-mm-dd):"))
                            price=str(input("Enter the price of the book:"))
                            mycursor.execute("insert into buy_new_books values('"+orderno+"','"+name_of_book+"','"+del_date+"','"+price+"')")
                            mydb.commit()
                            print("*Data successfully submitted*")
                            
                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break
                            
                    #TO UPDATE ORDER DETAILS        

                        if ch==16:
                            print("Press 1 to update Name of Book")
                            print("Press 2 to Update Delivery Date")
                            print("Press 3 to Update Price")
                            
                            ch1=int(input("Enter your choice:"))
                            
                    #TO UPDATE BOOK NAME        

                            if ch1==1:
                                mycursor.execute("select * from buy_new_books")
                                for i in mycursor:
                                    print(i)
                                orderno=str(input("Enter Order No. :"))
                                name_of_book=str(input("Enter new name:"))
                                mycursor.execute("update buy_new_books set name_of_book='"+name_of_book+"' where orderno='"+orderno+"'")
                                mydb.commit()
                                print("*Name has been updated*")
                                mycursor.execute("select * from buy_new_books")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                        break

                    #TO UPDATE DELIVERY DATE
                                    
                            if ch1==2:
                                mycursor.execute("select * from buy_new_books")
                                for i in mycursor:
                                    print(i)
                                orderno=str(input("Enter Order No. :"))
                                del_date=str(input("Enter new delivery date(yyyy-mm-dd):"))
                                mycursor.execute("update buy_new_books set del_date='"+del_date+"' where orderno='"+orderno+"'")
                                mydb.commit()
                                print("*Delivery date has been updated*")
                                mycursor.execute("select * from buy_new_books")
                                for i in mycursor:
                                    print(i)

                                abc=input("\nDo you want to continue with library management system (Y/N):")
                                if abc=="Y" or abc=="y":
                                    print()
                                    continue
                                else:
                                        break

                        if ch==17:
                            orderno = str(input("Enter order number: "))
                            mycursor.execute("select * from buy_new_books where orderno='{}'".format(orderno))
                            print("_ORDER NO_ , _BOOK NAME_ , _GENRE_ , _DATE OF DELIVERY_ , _PRICE_")
                            for i in mycursor:
                                print(i)

                            abc=input("\nDo you want to continue with library management system (Y/N):")
                            if abc=="Y" or abc=="y":
                                print()
                                continue
                            else:
                                break    
                        
                        if ch==18:
                            print("Thank you for using our serivce.")
                            break 

                        else:
                            print("Wrong input")
                            print("Enter valid input again. ")
                            continue

                break  # for totally exiting the statement if abc gets a 'n'

        except FileNotFoundError:
            print("User not found !!!")
            print("   Exiting the program !!    ")
            break

except mysql.connector.errors.ProgrammingError:
     print('\nUnable to connect to the database !!')
     print("|| Please check the password and user for MySQL once again. ||\n")

