# Microservice-A-for-Eduardo

SETUP ZMQ

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")..
