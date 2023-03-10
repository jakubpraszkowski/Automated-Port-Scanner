from socket import socket, AF_INET, SOCK_STREAM, error, getservbyport
from Save import Save


class PortScanner:
    def __init__(self, ip_range, start_port, end_port):
        self.ip_range = ip_range
        self.start_port = start_port
        self.end_port = end_port

    def check_port_protocol(self, ip, port):
        try:
            sock = socket(AF_INET, SOCK_STREAM, proto=0)

        except error as e:
            print("Error creating socket:", e)

        else:
            try:
                sock.connect((ip, port))

            except TimeoutError:
                sock.close()
                print("Connection timed out")

            except InterruptedError:
                sock.close()
                print("Connection interrupted")

            except error as e:
                sock.close()

            else:
                service = getservbyport(port, 'tcp')
                print(f"Port: {port} / tcp / {service}")
                # data = f"Port: {port} / tcp / {service}"
                # obj_save = Save(data)
                # obj_save.writing_to_txt()

                sock.close()

    def scan_ports(self):
        for ip_address in self.ip_range:
            question = str(ip_address)
            print(f"Ports for {question}:")

            for port in range(int(self.start_port), int(self.end_port) + 1):
                self.check_port_protocol(question, port)
