from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path
from typing import Annotated, Optional

import typer
from xdg_base_dirs import xdg_data_home

import tringa.repl
from tringa import cli as cli
from tringa.cli.output import console as console
from tringa.db import DBConfig


@dataclass
class GlobalOptions:
    artifact_globs: Optional[list[str]]
    since: timedelta
    db_config: DBConfig
    json: bool
    nosync: bool
    tui: bool
    verbose: int
    table_row_limit: int = 20


options: GlobalOptions


def set_options(
    artifact_globs: Optional[list[str]] = None,
    since_days: int = 90,
    db_path: Optional[Path] = None,
    json: bool = False,
    nosync: Annotated[
        bool, typer.Option("--nosync", "-n", help="Do not fetch data.")
    ] = False,
    tui: bool = False,
    verbose: int = 1,
):
    if tui and json:
        raise typer.BadParameter("--tui and --json cannot be used together")

    if db_path is None:
        dir = Path(xdg_data_home()) / "tringa"
        dir.mkdir(parents=True, exist_ok=True)
        db_path = dir / "tringa.db"
    elif db_path == ":memory:":
        db_path = None
    elif not db_path.exists():
        raise typer.BadParameter(f"DB path {db_path} does not exist")

    global options
    options = GlobalOptions(
        artifact_globs=artifact_globs,
        since=timedelta(days=since_days),
        db_config=DBConfig(path=db_path),
        json=json,
        nosync=nosync,
        tui=tui,
        verbose=verbose,
    )


set_options()


def validate_repl(repl: Optional[tringa.repl.Repl]):
    if repl == tringa.repl.Repl.SQL and not options.db_config.path:
        raise typer.BadParameter(
            "The --repl sql option requires --db-path."
            "\n\n"
            "SQL REPLs cannot be used with an in-memory db, since the Python app and the SQL REPL are different processes. "
            "However, the duckdb Python REPL can be used with an in-memory db.",
        )
