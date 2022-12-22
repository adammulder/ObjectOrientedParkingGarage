class Garage():
    '''This is a Class full of methods to run a parking garage
    the attributes for are tickets, parking spaces, and current ticket
    tickets: expected to be an empty list
    parkingSpaces: expected to be an empty list
    currentTicket: expected to be a dictionary {'paid':False}
    popTicket: should be an empty list, used for popped tickets
    popSpaces: should be an empty list, used for popped Spaces
    '''

    def __init__(self, tickets, parkingSpaces, currentTicket, popTicket, popSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.popTicket = popTicket
        self.popSpaces =popSpaces

    def generateTicketsSpaces(self, numTickets, numSpaces, numPopTicket =10, numPopSpaces = 10):
        self.numTickets = numTickets
        self.numSpaces = numSpaces
        self.numPopTicket = numPopTicket
        self.numPopSpaces = numPopSpaces

        # Generate ticket numbers for tickets and parking spaces, can change if you want more or less
        x = range(self.numTickets)
        [self.tickets.append(i) for i in x]
        y = range(self.numSpaces)
        [self.parkingSpaces.append(j) for j in y]
        # Generate numbers for pop lists, better to have some numbers in here so we avoid error
        a = range(self.numPopTicket)
        [self.popTicket.append(k) for k in a]
        b = range(self.numPopSpaces)
        [self.popSpaces.append(l) for l in b]


    def takeTicket(self):
        taken_Ticket = self.tickets.pop()
        self.popTicket.append(taken_Ticket)
        taken_Space = self.parkingSpaces.pop()
        self.popSpaces.append(taken_Space)
        print(f'Tickets remaining: {len(self.tickets)}')
        print(f'Spaces remaining: {len(self.parkingSpaces)}')


    def payForParking(self):
        gimme_your_money = input('(Parking Fee: $15) Enter full amount or "exit" to pay on exiting: ')
        if gimme_your_money == '15':
            self.currentTicket['paid'] = True
            print('Ticket is paid, parking lasts for 15 minutes')
        else:
            self.currentTicket['paid'] = False
            print('Please pay when you leave the Garage')
        

    def leaveGarage(self):
        replaced_Ticket = self.popTicket.pop()
        self.tickets.append(replaced_Ticket)
        replaced_Space = self.popSpaces.pop()
        self.parkingSpaces.append(replaced_Space)
        print(f'Tickets remaining: {len(self.tickets)}')
        print(f'Spaces remaining: {len(self.parkingSpaces)}')
        if self.currentTicket['paid'] == True:
            print('Thank you have a nice day!')
        elif self.currentTicket['paid'] == False:
            print('Please pay parking fee of $15')
            please_Pay = input('Amount to pay: ')
            if please_Pay == '15':
                print('Thank you, have a nice day!')
            else:
                while please_Pay != '15':
                    print('Please enter full amount')
                    please_Pay = input('Amount to pay: ')
                print('Thank you, have a nice day!')

my_Garage = Garage([], [], {'paid': False},[],[])

def run():
    # input the amount of tickets and spaces you want for your garage!
    my_Garage.generateTicketsSpaces(10, 10)
    while True:
        user_Response = input("Adam's Parking Garage: ticket/leave: ")
        if user_Response.lower() == 'ticket':
            my_Garage.takeTicket()
            my_Garage.payForParking()
        elif user_Response.lower() == 'leave':
            my_Garage.leaveGarage()
            break
        
        

run()




