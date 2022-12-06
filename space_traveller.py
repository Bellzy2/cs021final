"""
Zoe Bell
CS 021
Final Project
Space Traveller
"""
# major planets in our solar system
PLANETS = {'Mercury': {'distance': 77000000, 'siderealday': 1408},
           'Venus': {'distance': 61000000, 'siderealday': 5832},
           'Mars': {'distance': 54600000, 'siderealday': 25},
           'Jupiter': {'distance': 588000000, 'siderealday': 10}, 
           'Saturn': {'distance': 1200000000, 'siderealday': 11},
           'Uranus': {'distance': 2600000000, 'siderealday': 17},
           'Neptune': {'distance': 4300000000, 'siderealday': 16} 
           }

# travel speed of Voyager II in km/second
VOYAGER_SPEED = 15.9

def travel_time(distance, speed):
    time_seconds = float(distance / speed)
    time_hrs = (time_seconds / 60) / 60
    time_days = time_hrs / 24
    return time_days
    
def earth_days_passed(planet_time, time_away):
    ratio = planet_time / 24
    earth_hours = ratio * time_away
    return earth_hours

def planets_count(visited):
    visited = []
    if 
    
    
if __name__ == '__main__':
    
    while True:
        try:
            chosen_planet = input("Which planet in our solar system would you like to travel to? ").capitalize()
            if planet in PLANETS:
                planet_distance = PLANETS[planet]['distance']
                planet_hrs = int(PLANETS[planet]['siderealday'])
                break
        except KeyError:
            print("Not a planet in our solar system.")
    
    while True:
        try:
            user_input = input("How many hours would you like to spend on this planet? ")
            hours_away = int(user_input)
            if hours_away > 0:
                break
            elif hours_away < 0:
                print("Integer must be positive.")
        except ValueError:
            print("Please enter an integer.")
            
    while True:
        print(f'{earth_days_passed(hours_away, planet_hrs)} days will have passed on Earth while you were away.')
        print(f'In total, it will take {travel_time(planet_distance, VOYAGER_SPEED)} days for you to travel to {chosen_planet} going at the same speed as Voyager II (about 15.9 km/sec).')
        travel_again = input("Would you like to travel to another planet? ").lower()
        clean_input = travel_again.strip(characters)
        if clean_input == "yes":
            chosen_planet = input("Which planet in our solar system would you like to travel to? ")
            planet = chosen_planet.capitalize()
            if planet in PLANETS:
                planet_distance = PLANETS[planet]['distance']
                planet_hrs = int(PLANETS[planet]['siderealday'])
                break

        elif clean_input == "no":
            print(f'You traveled to {} planets in the solar system! ')
            break
            


        