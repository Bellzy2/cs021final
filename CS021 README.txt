Zoe Bell
CS021 A
29 October, 2022


Interstellar Explorer


        Travel through space and time! Have you ever wondered what it would be like to travel across the solar system in the same way that we travel to and from the grocery store? With this simulation you can get an idea of just how long space journeys like this theoretically take, and how time passage is warped once you leave Earth's orbit. Enter a planet and take a trip!


In this space traveler simulator a user is prompted to enter a planet in our solar system that they would like to travel to. If this planet is found in our solar system the program will calculate how long their journey will take them in hours and days traveling at the same speed as Nasa's Voyager II(15.9 km/sec). If the planet is not found, they will continue to be prompted until a valid input is provided. After finding out the time their travels will take, the user will then be prompted to enter how many hours on the given planet that they would like to spend. The program would use this entered information to calculate how many earth days and years would have passed over the course of the total amount of time they spent away (travel time plus time spent on the planet). 


A dictionary will be needed to store the data about the distance from Earth and number of hours in a sidereal day for every planet in the solar system. This project can be tested by trying a number of different user inputs of various Python types, and making sure that the program still runs or at least responds to any kind of input. It is also possible to hand calculate the results for every planet and compare them to the results from the program by keeping the hours spent on every planet consistent and then plugging that into the original written equations.


Calculations:

Travel time:
- calculates the amount of time in hours that it will take for the person to reach the planet and come back (ONLY calculates this time)
- Depending on the planet and its distance from earth, find how long it will take to travel that distance going at a speed of 15.9 km/sec. 
- take the distance and multiply by two to account for traveling both ways, convert distance to km, divide distance in km by 15.9


Earth days passed:
- calculates how many days on Earth will have passed during your time on the given planet
- find the ratio of sidereal day on chosen planet to sidereal day on earth, multiply this ratio by the number of hours entered for time spent on the planet.


Citations


Cain, Fraser. “How Far Is Mercury from Earth?” Universe Today, UniverseToday.com, 9 Aug. 
2016, https://www.universetoday.com/14165/distance-from-earth-to-mercury/. 


“How Long Is One Day on Other Planets?” NASA, NASA, 9 Feb. 2021, 
https://spaceplace.nasa.gov/days/en/. 


“In Depth.” NASA, NASA, 3 Aug. 2021, https://solarsystem.nasa.gov/planets/venus/in-depth/. 
“Mars Close Approach.” NASA, NASA, 19 July 2021, https://mars.nasa.gov/all-about-mars/night-sky/close-approach/. 


Tillman, Nola Taylor. “How Far Away Is Jupiter?” Space.com, Space, 1 June 2017, 
https://www.space.com/18383-how-far-away-is-jupiter.html. 


Tillman, Nola Taylor. “How Far Away Is Neptune?” Space.com, Space, 14 Dec. 2012, 
https://www.space.com/18923-neptune-distance.html. 


Tillman, Nola Taylor. “How Far Away Is Saturn?” Space.com, Space, 14 Nov. 2012, 
https://www.space.com/18477-how-far-away-is-saturn.html. 


Tillman, Nola Taylor. “How Far Is Uranus?” Space.com, Space, 28 Feb. 2018, 
https://www.space.com/18709-uranus-distance.html. 


“Voyager - NASA Probe Sees Solar Wind Decline.” NASA, NASA, 13 Dec. 2010, 
https://voyager.jpl.nasa.gov/news/details.php?article_id=20.