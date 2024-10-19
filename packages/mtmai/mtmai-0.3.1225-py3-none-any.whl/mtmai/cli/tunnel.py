import logging

logger = logging.getLogger()


def register_tunnel_commands(cli):
    @cli.command()
    def tunnel():
        import asyncio

        from mtmlib import tunnel

        asyncio.run(tunnel.start_cloudflared())
