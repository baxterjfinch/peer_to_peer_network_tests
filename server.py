def handler(self, connection, a):
    try:
        while True:
            #server receives the message
            data = connection.recv(BYTE_SIZE
            for connection in self.connections:

                # the peer that is connected wants to disconnect
                if data and data.decode('utf-8')[0].lower() == 'q':

                    #disconnect peer
                    self.disconnect(connection, a)
                    return
                elif data and data.decode('utf-8') == REQUEST_STRING:
                    print("-" * 21 + " UPLOADING " + "-" * 21)
                    #if the connection is still active we send it back the data
                    #this part deals with uploading of the file
                    connection.send(self.msg)
    except Exception as e:
        sys.exit()

class p2p:
    peers = ['127.0.0.1']
