class Target():

    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)

    def __str__(self):
        return f'{self.host}:{self.port}'

    def __eq__(self, other):
        return self.host == other.host \
               and self.port == other.port