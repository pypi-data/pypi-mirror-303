import click
import orjson
import tabulate
from dotenv import load_dotenv

from illallangi.tripit.__version__ import __version__
from illallangi.tripit.client import TripItClient

load_dotenv(
    override=True,
)

json_output_format_option = click.option(
    "--json",
    "output_format",
    flag_value="json",
    help="Output as JSON.",
)

table_output_format_option = click.option(
    "--table",
    "output_format",
    flag_value="table",
    default=True,
    help="Output as a table (default).",
)

tripit_access_token_option = click.option(
    "--tripit-access-token",
    type=click.STRING,
    envvar="TRIPIT_ACCESS_TOKEN",
    required=True,
)

tripit_access_token_secret_option = click.option(
    "--tripit-access-token-secret",
    type=click.STRING,
    envvar="TRIPIT_ACCESS_TOKEN_SECRET",
    required=True,
)

tripit_client_token_option = click.option(
    "--tripit-client-token",
    type=click.STRING,
    envvar="TRIPIT_CLIENT_TOKEN",
    required=True,
)

tripit_client_token_secret_option = click.option(
    "--tripit-client-token-secret",
    type=click.STRING,
    envvar="TRIPIT_CLIENT_TOKEN_SECRET",
    required=True,
)

version_option = click.version_option(
    version=__version__,
    prog_name="rdf-tools",
)


@click.group()
@click.pass_context
@tripit_access_token_option
@tripit_access_token_secret_option
@tripit_client_token_option
@tripit_client_token_secret_option
@version_option
def cli(
    ctx: click.Context,
    *args: list,
    **kwargs: dict,
) -> None:
    ctx.obj = TripItClient(
        *args,
        **kwargs,
    )


@cli.command()
@click.pass_context
@json_output_format_option
@table_output_format_option
def flights(
    ctx: click.Context,
    *args: list,
    **kwargs: dict,
) -> None:
    output(
        *args,
        fn=ctx.obj.get_flights,
        **kwargs,
    )


@cli.command()
@click.pass_context
@json_output_format_option
@table_output_format_option
def profiles(
    ctx: click.Context,
    *args: list,
    **kwargs: dict,
) -> None:
    output(
        *args,
        fn=ctx.obj.get_profiles,
        **kwargs,
    )


@cli.command()
@click.pass_context
@json_output_format_option
@table_output_format_option
def trips(
    ctx: click.Context,
    *args: list,
    **kwargs: dict,
) -> None:
    output(
        *args,
        fn=ctx.obj.get_trips,
        **kwargs,
    )


def output(
    fn: callable,
    *args: list,
    output_format: str,
    **kwargs: dict,
) -> None:
    objs = fn(
        *args,
        **kwargs,
    )

    if not objs:
        return

    # JSON output
    if output_format == "json":
        click.echo(
            orjson.dumps(
                [
                    {
                        **obj,
                    }
                    for obj in objs
                ],
                option=orjson.OPT_SORT_KEYS,
            ),
        )
        return

    # Table output
    if output_format == "table":
        click.echo(
            tabulate.tabulate(
                [
                    {k: v for k, v in obj.items() if not k.startswith("@")}
                    for obj in objs
                ],
                headers="keys",
                tablefmt="presto",
                numalign="left",
                stralign="left",
            )
        )
        return

    raise NotImplementedError
