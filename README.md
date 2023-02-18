# Automated-Port-Scanner

This program automates the process of scanning a network for open ports on a specified range of IP addresses. The program uses socket programming to establish a connection with each IP address and port in the range to determine whether it is open or closed.

The program starts by prompting the user to enter a range of IP addresses and a range of ports to scan. The program then uses threading to establish connections with each IP address and port in the range simultaneously, rather than sequentially, which can significantly reduce the time required to complete the scan.

For each connection, the program sends a request to the specified IP address and port using the socket library's socket.connect_ex() method. If the connection is successful, the port is marked as open, and the program prints the IP address and port number to the console. If the connection is unsuccessful, the port is marked as closed.
