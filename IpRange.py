from ipaddress import ip_address
from multiprocessing import Process, Lock


class IpRange:
    def __init__(self, start_ip, end_ip):
        self.start_ip = ip_address(start_ip)
        self.end_ip = ip_address(end_ip)
        self.range_ip = self.generate_ip_range()
        self.results = []
        self.lock = Lock()

    # def is_valid(self):
    #     try:
    #         ip_address(self.start_ip)
    #         ip_address(self.end_ip)
    #         return True
    #
    #     except ValueError:
    #         print(f"{self.start_ip} or {self.end_ip} is not valid.")
    #         return False


    def generate_ip_range(self):
        range_ip = []

        for ip in range(int(self.start_ip), int(self.end_ip) + 1):
            range_ip.append(ip_address(ip))

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
