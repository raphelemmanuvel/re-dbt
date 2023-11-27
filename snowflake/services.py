import typer
import os

from rich import print

from dbt.cli.main import dbtRunner

import snowflake.connector

app = typer.Typer(
    rich_markup_mode="rich",
    add_completion=False,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)

# initialize dbtRunner
dbt = dbtRunner()


def auth_snowflake():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
    )
    return conn


def setup_snowflake():
    conn = auth_snowflake()
    # Create Database
    conn.cursor().execute(
        f"CREATE OR REPLACE DATABASE {os.getenv('SNOWFLAKE_DATABASE')}"
    )
    # Create Warehouse
    conn.cursor().execute(
        f"CREATE OR REPLACE WAREHOUSE {os.getenv('SNOWFLAKE_WAREHOUSE')} WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 60 AUTO_RESUME = TRUE MIN_CLUSTER_COUNT = 1 MAX_CLUSTER_COUNT = 1 INITIALLY_SUSPENDED = TRUE"
    )


def teardown_snowflake():
    conn = auth_snowflake()
    # Drop Database
    # conn.cursor().execute(f"DROP DATABASE IF EXISTS {os.getenv('SNOWFLAKE_DATABASE')}")
    # Drop Warehouse
    conn.cursor().execute(
        f"DROP WAREHOUSE IF EXISTS {os.getenv('SNOWFLAKE_WAREHOUSE')}"
    )


def main(cmd: str = typer.Option(..., help="The service to be executed.")):
    if cmd == "teardown":
        teardown_snowflake()
    else:
        if cmd == "build" or cmd == "seed" or cmd == "run":
            setup_snowflake()

        cli_args = [f"{cmd}"]
        dbt.invoke(cli_args)


if __name__ == "__main__":
    typer.run(main)
