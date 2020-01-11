def receive_message(self):
    try:
        print("Recieving --------")
        data = self.s.recv(BYTE_SIZE)

        print("\nRecieved .......................")

        if self.previous_data != data:
            fileIO.create_file(data)
            self.previous_data = data

        return data
    except KeyboardInterrupt:
        self.send_disconnect_signal()
