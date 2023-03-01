from socket import socket, AF_INET, SOCK_STREAM, error, SOCK_DGRAM


class PortScanner:
    def __init__(self, ip_range, start_port, end_port):
        self.ip_range = ip_range
        self.start_port = start_port
        self.end_port = end_port

    def check_port_protocol(self, ip, port):
        sock = socket(AF_INET, SOCK_STREAM)

        try:
            sock.connect((ip, port))
            print(f"Port {port} is open and uses TCP protocol")

        except error:
            try:
                sock = socket(AF_INET, SOCK_DGRAM)
                sock.connect((ip, port))
                print(f"Port {port} is open and uses UDP protocol")

            except error:
                print(f"Cannot determine the network protocol of port: {port}.")

        finally:
            sock.close()

    def scan_ports(self):
        for ip_address in self.ip_range:
            question = str(ip_address)
            print(f"Ports for {question}:")

            for port in range(int(self.start_port), int(self.end_port) + 1):
                self.check_port_protocol(question, port)
