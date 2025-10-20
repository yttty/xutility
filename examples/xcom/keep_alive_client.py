import argparse
import asyncio

from xutility import XComKACli


class KeepAliveWsClientTester:
    def __init__(self, unix_sock, host, port) -> None:
        self.cli = XComKACli("test_req", unix_sock, host, port, tag="TesterKA", debug=False)
        self.cli.register_msg_callback(self.on_message)

    async def on_message(self, rsp):
        print("Recv:", rsp)

    async def send(self):
        for i in range(5):
            print(f"======Test Msg {i}======")
            await asyncio.sleep(0.1)
            req_d = {"msg": i}
            err = await self.cli.send(req_d)
            if err is None:
                print("Sent:", req_d)
            else:
                print("Failed:", err)
            await asyncio.sleep(0.5)
            print()

    async def run(self):
        try:
            async with asyncio.TaskGroup() as tg:
                _ = tg.create_task(self.cli.run())
                _ = tg.create_task(self.send())
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--unix_sock", type=str, help="Unix sock")
    parser.add_argument("--host", type=str, help="Host")
    parser.add_argument("--port", type=str, help="Port")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(KeepAliveWsClientTester(args.unix_sock, args.host, args.port).run())
