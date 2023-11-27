from xmlrpc import client

if __name__ == '__main__':
    s = client.ServerProxy("http://10.16.30.122:50000")
    print(s.twice(2))