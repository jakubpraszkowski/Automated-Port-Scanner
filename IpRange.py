from ipaddress import IPv4Address
from multiprocessing import Process, Lock


class IpRange:
    def __init__(self, start_ip, end_ip):
        self.start_ip = IPv4Address(start_ip)
        self.end_ip = IPv4Address(end_ip)
        self.range_ip = self.generate_ip_range()
        self.results = []
        self.lock = Lock()

    def generate_ip_range(self):
        range_ip = []

        for ip in range(int(self.start_ip), int(self.end_ip) + 1):
            range_ip.append(IPv4Address(ip))

        return range_ip

    def scan_ip(self, ip):
        self.results.append(ip)

    def scan_ips(self):
        threads = []

        for ip in self.range_ip:
            t = Process(target=self.scan_ip, args=(ip,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
