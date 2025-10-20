import argparse
import asyncio
import time

from xutility import XComTCli


async def test_cli(cli: XComTCli):
    for i in range(5):
        print(f"======Test Msg {i}======")
        req_d = {"msg": i}
        print("Send:", req_d)
        rsp, err, server_ts = await cli.req(req_d)
        if err:
            print("Recv err msg:", err)
        else:
            print("Recv rsp:", rsp)
            if server_ts is not None:
                print("Recv latency: {}us".format(int(time.time() * 1e6) - server_ts))
        await asyncio.sleep(0.5)
        print()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--unix_sock", type=str, help="Unix sock")
    parser.add_argument("--host", type=str, help="Host")
    parser.add_argument("--port", type=str, help="Port")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    cli = XComTCli(
        unix_sock=args.unix_sock,
        host=args.host,
        port=args.port,
        req_type="test_req",
        tag="TesterTrans",
        debug=True,
    )
    asyncio.run(test_cli(cli))
