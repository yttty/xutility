import argparse
import asyncio

from xutility import XComSvr


async def echo(req):
    return {"ack": req["msg"]}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--unix_sock", type=str, help="Unix sock")
    parser.add_argument("--host", type=str, help="Host")
    parser.add_argument("--port", type=str, help="Port")
    parser.add_argument("-d", "--debug", action="store_true", help="Debug")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    svr = XComSvr(
        msg_callbacks={"test_req": echo},
        unix_sock=args.unix_sock,
        host=args.host,
        port=args.port,
        keep_alive=True,
        tag="TestServer",
        debug=args.debug,
    )
    asyncio.run(svr.run())
