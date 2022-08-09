from ast import While
import random

destinations_list = ['Punta Cana', 'Turks and Caicos', 'Greenland', 'Sweden', 'United Kingdom']
restaurants_list = ['Mexican', 'Italian', 'Greek', 'Lebanese', 'Caribbean']
mode_of_transport_list = ['Train', 'Car', 'Bus', 'Boat', 'Moped'] 
entertainment_list = ['Circus', 'Concert', 'Adventure Park', 'Movies', 'Magic show']

def main_generator():
   generated_trip = [random.choice(destinations_list), random.choice(restaurants_list), random.choice(mode_of_transport_list), random.choice(entertainment_list)]

   displayed_greeting()
   while True:                                                                                                                     
        displayed_trip(generated_trip)
        user_input = input('Does this trip suit you? if Yes type yes, if No type no: ')
        if user_input == "yes":
            break
        elif user_input == "no":
            generated_trip = reselect_trip_option(generated_trip)
        else:
            print("That's not an option.")

   displayed_ending()

   displayed_trip(generated_trip)

def displayed_greeting():
    print('So I heard you need need a randomly generated trip? Here is your randomly generated trip!')

def displayed_ending():
    print('Awesome! Glad to help pick out your perfect trip:')

def displayed_trip(list_of_trip_options):
    trip_strings = ''
    trip_titles = ['Destination', 'Restaurant', 'Transportation', 'Entertainment']
    for index in range(len(list_of_trip_options)):
        trip_strings += f' {trip_titles[index]}: {list_of_trip_options[index]} \n'

    print(trip_strings)

def reselect_trip_option(list_of_trip_options):
    user_input = input('Which feature of the trip would you like to change? ')

    if user_input == 'Destination':
        list_of_trip_options[0] = random.choice(destinations_list)
    elif user_input == 'Restaurant':
        list_of_trip_options[1] = random.choice(restaurants_list)
    elif user_input == 'Transportation':
        list_of_trip_options[2] = random.choice(mode_of_transport_list)
    elif user_input == 'Entertainment':
        list_of_trip_options[3] = random.choice(entertainment_list)
    
    return list_of_trip_options

main_generator()