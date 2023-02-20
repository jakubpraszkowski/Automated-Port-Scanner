import queue
import socket
import threading


class PortScanner:
    def __init__(self, ip_range, start_port, end_port):
        self.ip_range = ip_range
        self.start_port = start_port
        self.end_port = end_port
        self.results = queue.Queue()

    def check_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))

        if result == 0:
            self.results.put(port)

        sock.close()

    def scan_ports(self):
        threads = []

        for ipv4_address in self.ip_range:
            question = str(ipv4_address)

            for port in range(int(self.start_port), int(self.end_port) + 1):
                thread = threading.Thread(target=self.check_port, args=(question, port))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

        while not self.results.empty():
            port = self.results.get()
            print("Port {} is open".format(port))

        return port
