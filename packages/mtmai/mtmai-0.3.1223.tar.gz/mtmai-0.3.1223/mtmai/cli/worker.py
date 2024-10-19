from mtmlib.mtutils import bash


def register_worker_commands(cli):
    @cli.command()
    def worker():
        print("starting workflow worker")
        from mtmai.mtlibs.prefect.mtprefect import start_prefect_deployment

        start_prefect_deployment()

    @cli.command()
    def prefect():
        print("启动 prefect server")

        bash("sudo kill -9 $(lsof -t -i:4200)")
        bash(
            "prefect config set PREFECT_API_URL=https://colab-4200.yuepa8.com/api && prefect server start"
        )
