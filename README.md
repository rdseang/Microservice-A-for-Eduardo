# Microservice-A-for-Eduardo

SETUP ZMQ

import zmq

context = zmq.Context()\n
socket = context.socket(zmq.REQ)\n
socket.connect("tcp://localhost:5555")\n
