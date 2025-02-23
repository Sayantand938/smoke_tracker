# src/smoke_tracker/main.py


import os
import typer
from typing import NoReturn

from .add_smoking_details import add_smoking_record
from .datewise_details import view_records_by_date
from .monthwise_details import view_records_by_month

app = typer.Typer()

def clear_screen() -> None:
    """Clears the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

@app.command()
def add() -> None:
    """Add a new smoking record."""
    add_smoking_record()

@app.command()
def date(date: str) -> None:
    """View smoking records for a specific date (YYYY-MM-DD, 'today', or 'yesterday')."""
    clear_screen()
    view_records_by_date(date)

@app.command()
def month(month: str) -> None:
    """View smoking records for a specific month (YYYY-MM)."""
    clear_screen()
    view_records_by_month(month)

@app.command()
def show_help(ctx: typer.Context) -> NoReturn:
    """Show the help message and exit."""
    typer.echo(ctx.get_help())
    raise typer.Exit()

def main() -> None:
    """Main entry point for the smoke-tracker CLI."""
    app()

if __name__ == "__main__":
    main()
