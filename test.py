import socket
import sys
import struct
import time
import Adafruit_DHT as dht
import time

def start_tcp_server(ip, port):
    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    # bind port
    print("starting listen on ip %s, port %s" % server_address)
    sock.bind(server_address)
    # start listening, allow only one connection
    try:
        sock.listen(1)
    except socket.error:
        print("fail to listen on port %s" % e)
        sys.exit(1)
    while True:
        print("waiting for connection")
        client, addr = sock.accept()
        print("having a connection")
        break
    while True:
        h,t = dht.read_retry(dht.DHT22,21)
        print(round(t,2))
        print(round(h,2))
        msg = ("temp  %.2f ,humi  %.2f" % (t,h))
        client.send(msg.encode('utf-8'))
        print("send len is : [%d]" % len(msg))
        time.sleep(8)
    print("finish test, close connect")
    client.close()
    sock.close()
    print(" close client connect ")

if __name__=='__main__':
    start_tcp_server('0.0.0.0',6000)
