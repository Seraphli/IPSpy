import time

from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket

from ipspy import __version__
import ipspy.rpc.ipspyrpc.ipspyrpc as server
import ipspy.rpc.constants as constants
from ipspy.util import get_ip_detail


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._connect_to_server()

    def _connect_to_server(self):
        tsocket = TSocket.TSocket(self.host, self.port)
        transport = TTransport.TBufferedTransport(tsocket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self._client = server.Client(protocol)
        transport.open()
        begin = time.time()
        self._client.ping()
        response_time = int((time.time() - begin) * 1000)
        print(f'Connect to server. Response time {response_time}ms.')
        if self._client.version() != __version__:
            raise Exception('Version mismatch! Update project.')

    def upload_detail(self):
        country, ip = get_ip_detail()
        self._client.upload_detail(country, ip)


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='IPSpy client')
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1',
                        help='Host IP')
    parser.add_argument('-p', '--port', type=int, default=constants.PORT,
                        help='Host Port')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    Client(args.ip, args.port).upload_detail()
