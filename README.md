# exceed-mini-project

## Hardward feature

* Detect the light density and change it to the binary state (show 0 and 1 in every seconds).

## Front-end feature

* Instant of 2 states, we seperate to 3 states of parking.
  - Normal State : this state is the normal state that do not have car parking in the slot.
  - Parking State : the state that the car parking in the slot and start to count the time of parking car.
  - Last State : the state will show the time duration of the car that park in the slot and the total cost of parking.
  This state have a little feature. Therefore, it will be showed for 3 seconds(I forget to change it back to 10 seconds), then it will return to the normal state.
  
* There is the graph to show the relation between money-cost and time durations of parking car.
  - Do not combine in the html page.
