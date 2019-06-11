# IP Spy

Upload client's public IP to server.

## Usage

`git clone https://github.com/Seraphli/ipspy.git && cd ipspy && pip install .`

### Server

`python -m ipspy.server`

### Client

`python -m ipspy.client`

You can execute this with `crontab`, for example:

`15 * * * * /env/bin/python -m ipspy.client`

This task will update the ip every 15 minutes.

## Other

Test on Python 3.6.5

### Generate thrift python package

`cd ipspy/rpc/thrift_idl && thrift -out .. --gen py rpc.thrift && cd -`
