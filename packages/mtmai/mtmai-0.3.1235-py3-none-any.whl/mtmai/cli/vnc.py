import logging

logger = logging.getLogger()



def register_vnc_commands(cli):
    @cli.command()
    def vnc():
        from mtmai.mtlibs.server.kasmvnc import run_kasmvnc

        run_kasmvnc()

        try:
            while True:
                # Keep the main process running
                import time

                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt. Shutting down VNC server...")