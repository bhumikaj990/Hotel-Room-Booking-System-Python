hotel={101:{"room type":"single","booking status":"available","customer name":""},
       102:{"room type":"double","booking status":"booked","customer name":"bhumika"},
       103:{"room type":"single","booking status":"booked","customer name":"tushar"},
       104:{"room type":"double","booking status":"available","customer name":""}}

def view_rooms():
    print("------display all hotel rooms------" .center(40))
    for details in hotel.values():
        print(details)

# view_rooms()

def book_room():
    room_no = int(input("enter the room number :"))
    if room_no in hotel:
        if hotel[room_no]["booking status"] == "available":
            print("room is available")
            name = input("enter the customer name :")
            hotel[room_no]["customer name"] = name
            hotel[room_no]["booking status"] = "booked"
            print("successful booking")
        else:
            print("room is already booked")
    else:
        print("invalid room number")

# book_room()  

def cancel_booking():
    room_no=int(input("enter the room number :"))
    if room_no in hotel:
        if hotel[room_no]["booking status"] == "booked":
            hotel[room_no]["customer name"] = ""
            hotel[room_no]["booking status"] = "available"
            print("booking cancelled successfully")
        else:
            print("room is not booked")
    else:
        print("invalid room number")
# # cancel_booking()    

def check_booking_status():
    room_no=int(input("enter the room number :"))
    room=hotel[room_no]
    print(room)

# check_booking_status()   

def exit():
    print("thank you")

# exit()

def menu():
    while True:
        print("----display hotel menu----")
        print('''
                1.view all rooms
                2.book room
                3.cancel booking
                4.check booking status
                5.exit
                ''')
        ch=int(input("enter your choice :"))
        if ch==1:
            view_rooms()
        elif ch==2:
            book_room()  
        elif ch==3:
            cancel_booking()
        elif ch==4:
            check_booking_status() 
        elif ch==5:
            print("thank you")
            break
        else:
            print("invalid choice")
menu()            