import socket
import json
import time
import sys_setup

if __name__ == '__main__':
    Host = "192.168.0.10"
    Port = 30000

    # Create a socket object
    s = socket.socket()

    # Connect to the server
    #s.connect((Host, Port))

    # Send object location to the server
    place_position = 255
    object_location = [0.17,0.17,0.37,0.0,3.14,0]
    #s.send(str.encode(json.dumps(object_location)))
    def multiply_convert(floats):
         return [int(x * 100) for x in floats]

    # setup connection between computer and client robot using TCP/IPV4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # server setup
        s.bind((Host, Port))
        s.listen()
        s.settimeout(40)
        print("Awaiting robot response")

        conn, ctlient_address = s.accept()
        with conn:
                try_connection = ''
                while try_connection != 'robot start':
                    try_connection = bytes.decode(conn.recv(1024))
                print('Received from robot: ', try_connection)
                conn.send(str.encode('server start'))
                time.sleep(5)
                result = multiply_convert(object_location)
                signs = []
                for i in result:
                    if i < 0:
                        signs.append(0)
                    else:
                        signs.append(1)

                #conn.send(str.encode(object_location))
                for i in result:
    
                    conn.send(i.to_bytes(4, 'big'))
                for i in signs:
                    conn.send(i.to_bytes(4, 'big'))
                print('Connection setup, both server and robot initialized')

    # Close the socket connection
    s.close()

