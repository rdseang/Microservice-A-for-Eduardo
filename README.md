# Microservice-A-for-Eduardo

## SETUP ZMQ

import zmq

context = zmq.Context() \
socket = context.socket(zmq.REQ)) \
socket.connect("tcp://localhost:5555) 

## How to Request Data / Assumptions
#action is a STRING
#the following calls to the microservice assume the user has a valid input

socket.send_string(action)    

## How to Receive Data
#receiving needs to use json to decode list objects sent back to the main program 

message = socket.recv_json()      

## View Scholarships and Browse Scholarships
Calling the microservice to view saved scholarships or browse scholarships
will return a LIST of scholarship objects to be processed by main program. \
\
socket.send_string('1')  # to browse scholarship catalog \
socket.send_string('2')  # to view saved scholarships

## Add Scholarship
Calling the microservice to add a scholarship will have it return True if it was added or False if it was not added / the desired scholarship ID was not found in the catalog. \
socket.send_string('add 3') # adds a scholarship to saved scholarships with ID 3 \

## Remove Scholarship
Calling the microservice to remove a scholarship will have it return True if it was removed or False if it was not removed / the desired scholarship ID was not found. \
socket.send_string('remove 2') # removes from saved scholarships the scholarship of ID 2 

## Quit
socket.send_string('Q')

[Sequence diagram for this microservice](/sequence_diagram.png)

