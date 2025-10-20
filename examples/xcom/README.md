# Websockets client and server example

## Use unix sock
- Server: `python server.py -u /tmp/test.sock`
- Client:
    - Keep-alive: `python keep_alive_client.py -u /tmp/test.sock`
    - Transient: `python transient_client.py -u /tmp/test.sock`

## Use TCP sock
- Server: `python server.py --host localhost --port 9898`
- Client:
    - Keep-alive: `python keep_alive_client.py --host localhost --port 9898`
    - Transient: `python transient_client.py --host localhost --port 9898`
