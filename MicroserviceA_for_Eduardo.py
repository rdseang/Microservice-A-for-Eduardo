import time
import zmq
import json

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def browse_scholarships(action):
    '''
    Returns a list of the available scholarship objects from the json file to be displayed by the main program
    :param action: user input
    :return: a list of scholarship objects to be displayed by main program
    '''
    with open('scholarship_catalog.json', 'r') as infile:
        return json.load(infile)


def view_saved_scholarships(action):
    '''
    Goes through json file and returns a list of scholarship objects to be displayed by the main program
    :param action: input by user
    :return: a list of scholarship objects to be displayed by main program
    '''
    with open('saved_scholarships.json', 'r') as file:
        return json.load(file)


def add_scholarship(action):
    '''
    Adds a scholarship to the json file of saved scholarships
    :param action: input by user
    '''
    num_id = int(action[4:])

    # first find the scholarship in the catalog
    with open('scholarship_catalog.json', 'r') as infile:
        scholarship_catalog = json.load(infile)
        found = False
        for i in range(len(scholarship_catalog)):
            if scholarship_catalog[i]["id"] == num_id:
                found = True
                scholarship_to_add = scholarship_catalog[i]

        # if the scholarship is not found
        if found is False:
            return False

        # if the scholarship is found, add it to the list and return True
        else:
            with open('saved_scholarships.json', 'r') as infile:
                saved_scholarships = json.load(infile)
                saved_scholarships.append(scholarship_to_add)

            with open('saved_scholarships.json', 'w') as outfile:
                json.dump(saved_scholarships, outfile)
            return True


def delete_scholarship(action):
    '''
    Deletes a scholarship from the saved list based on the action
    '''
    num_id = int(action[6:])
    with open('saved_scholarships.json', 'r') as infile:
        saved_scholarships = json.load(infile)

    # finds the matching scholarship ID and deletes it
    for i in range(len(saved_scholarships)):
        if saved_scholarships[i]["id"] == num_id:
            saved_scholarships.remove(saved_scholarships[i])


    # writes updated data to json file
    with open('saved_scholarships.json', 'w') as outfile:
        json.dump(saved_scholarships, outfile)

    return True



# interacting with the main program ------------------------------------------------------------------
while True:

    message = socket.recv()

    print(f"Received request from the client: {message.decode()}")
    action = message.decode().lower()   # so user can enter any case

    if len(message) > 0:
        if action == 'q':
            break

        # sends back a list of the scholarship catalog json file to the main program to browse
        elif action == '1':
            sending_back = browse_scholarships(action)

        # sends back a list of the saved scholarships from the json file to the main program
        elif action == '2':
            sending_back = view_saved_scholarships(action)

        # adds to the list of the saved scholarships objects in the json file
        elif 'add' in action:            # assuming the user inputs a valid input
            sending_back = add_scholarship(action)

        # if removing a scholarship
        elif 'remove' in action:
            sending_back = delete_scholarship(action)

        else: # False means nothing happened, just so main program can continue
            sending_back = False

        time.sleep(3)

        socket.send_json(sending_back)

context.destroy()
