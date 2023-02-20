import socket


class PortScanner:
    def __init__(self, ip_range, start_port, end_port):
        self.ip_range = ip_range
        self.start_port = start_port
        self.end_port = end_port

    def check_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print("Port {} is open".format(port))

        sock.close()

    def scan_ports(self):
        for ipv4_address in self.ip_range:
            question = str(ipv4_address)

            for port in range(int(self.start_port), int(self.end_port) + 1):
                self.check_port(question, port)

        # return port
