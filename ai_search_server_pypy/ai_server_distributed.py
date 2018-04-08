'''
Copyright (C) BCIT AI/ML Option 2018 Team with Members Following - All Rights Reserved.
- Jake Jonghun Choi     jchoi179@my.bcit.ca
- Justin Carey          justinthomascarey@gmail.com
- Pashan Irani          pashanirani@gmail.com
- Tony Huang	        tonyhuang1996@hotmail.ca
- Chil Yuqing Qiu       yuqingqiu93@gmail.com
Unauthorized copying of this file, via any medium is strictly prohibited.
Written by Jake Jonghun Choi <jchoi179@my.bcit.ca>
'''
import copy, threading, ai_search_distributed, ai_state_space_generator
import time, pickle, socket, sys, os

initial_game_board_state_german_daisy = [
    [-9, -9, -9, -9,  0,  0,  1,  1,  0],
    [-9, -9, -9,  0,  0,  1,  1,  1,  0],
    [-9, -9,  2,  2,  0,  1,  1,  0,  0],
    [-9,  2,  2,  2,  0,  0,  0,  0,  0],
    [ 0,  2,  2,  0,  0,  0,  2,  2,  0],
    [ 0,  0,  0,  0,  0,  2,  2,  2, -9],
    [ 0,  0,  1,  1,  0,  2,  2, -9, -9],
    [ 0,  1,  1,  1,  0,  0, -9, -9, -9],
    [ 0,  1,  1,  0,  0, -9, -9, -9, -9]
]

information_from_client_to_server_for_search_request = {
    'state_to_search': [],
    'color': '',
    'time_limitation': 0,
    'init_board_configuration': '',
    'move_taken_already': 0
}

# Global all search thread lists for management.
global_searching_threads = []

# Run the main server.
def run_server():
    HOST = 'localhost'  # Symbolic name, meaning all available interfaces
    PORT = 6666  # Arbitrary non-privileged port
    WAITING_QUEUE_SIZE = 100
    RECEIVER_BUFFER = 4096
    SERVER_TIME_OVERHEAD = 0 # Server will be generous time-wise.

    print('======== ======== AI Search Server ======== ========')

    # Create a socket for the server.
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('AI Search Server: Socket created @' + str(HOST) + ':' + str(PORT) + '...')

    # Bind socket to local host and port.
    socket_server.bind((HOST, PORT))
    print('AI Search Server: Socket bind complete...')

    # Start listening on socket.
    socket_server.listen(WAITING_QUEUE_SIZE)
    print('AI Search Server: Socket now listening for a request...')

    # Compile process for pypy3.
    print('======== ======== Initiating Server, Wait Several Seconds ======== ========')
    client_socket_fake = 0
    start_search(client_socket_fake, initial_game_board_state_german_daisy, 'black', 10, 'german_daisy', 10)
    print('======== ======== Server Ready to Go ======== ========')

    # Keep talking with the client and respond to the request.
    while True:
        try:
            # Wait to accept a connection.
            (client_socket, address) = socket_server.accept()

            # Print out the request and the detail
            print('======== ======== ======== ======== Search Request From: ' + str(address[0])
                  + ':' + str(address[1]) + ' ======== ======== ======== ========')
            print('#### Currnetly Running Searching Threads: ' + str(global_searching_threads.__len__()) + ' ####')
            information = client_socket.recv(RECEIVER_BUFFER)
            information_from_client_to_server_for_search_request_to_receive = pickle.loads(information)

            # Finally start the search with given information.
            start_search(client_socket,
                         information_from_client_to_server_for_search_request_to_receive['state_to_search'],
                         information_from_client_to_server_for_search_request_to_receive['color'],
                         information_from_client_to_server_for_search_request_to_receive['time_limitation'] + SERVER_TIME_OVERHEAD,
                         information_from_client_to_server_for_search_request_to_receive['init_board_configuration'],
                         information_from_client_to_server_for_search_request_to_receive['move_taken_already'])
        except Exception:
            pass
        finally:
            pass

    socket_server.close()

# Start the search.
def start_search(client_socket, state_to_search, color, time_limitation, init_board_configuration, move_taken_already):
    global global_searching_threads

    try:
        thread = threading.Thread(target=ai_search_distributed.iterative_deepening_search_with_time_constraint,
                                  args=(client_socket, state_to_search, color,
                                        time_limitation, init_board_configuration, move_taken_already,))
        global_searching_threads.append(thread)
        thread.start()
    except Exception:
        print('ERROR: Can NOT create a search thread!')
    finally:
        thread.join()
        print('#### Search Thread Terminated: ' + str(thread) + ' ####')
        global_searching_threads.remove(thread)

if __name__ == '__main__':
    run_server()











