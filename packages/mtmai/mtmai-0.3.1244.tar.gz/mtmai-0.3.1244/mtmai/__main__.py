import click

from mtmai.core.bootstraps import bootstrap_core

bootstrap_core()


def main():
    from mtmai.cli.build import register_build_commands
    from mtmai.cli.clean import register_clean_commands
    from mtmai.cli.db import register_db_commands
    from mtmai.cli.dev import register_dev_commands
    from mtmai.cli.dp import register_deploy_commands
    from mtmai.cli.gen import register_gen_commands
    from mtmai.cli.init import register_init_commands
    from mtmai.cli.release import register_release_commands
    from mtmai.cli.selenium import register_selenium_commands
    from mtmai.cli.serve import register_serve_commands
    from mtmai.cli.tunnel import register_tunnel_commands
    from mtmai.cli.vnc import register_vnc_commands
    from mtmai.cli.worker import register_worker_commands

    @click.group()
    def cli():
        pass

    register_build_commands(cli)
    register_clean_commands(cli)
    register_db_commands(cli)
    register_deploy_commands(cli)
    register_gen_commands(cli)
    register_init_commands(cli)
    register_release_commands(cli)
    register_selenium_commands(cli)
    register_serve_commands(cli)
    register_tunnel_commands(cli)
    register_vnc_commands(cli)
    register_dev_commands(cli)
    register_worker_commands(cli)
    cli()


if __name__ == "__main__":
    main()
