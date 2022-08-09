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