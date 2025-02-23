# src/smoke_tracker/main.py
import os
import typer

from .add_smoking_details import add_smoking_record  # Corrected import
from .datewise_details import view_records_by_date  # Corrected import
from .monthwise_details import view_records_by_month  # Corrected import
from typing import NoReturn  # Import for type hinting

app = typer.Typer()

def clear_screen() -> None:  # Add return type hint
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

@app.command()
def add() -> None:  # Add return type hint
    """Add a new smoking record."""
    add_smoking_record()

@app.command()
def date(date: str) -> None: # Add return type hint
    """View smoking records for a specific date (YYYY-MM-DD, 'today', or 'yesterday')."""
    clear_screen()
    view_records_by_date(date)

@app.command()
def month(month: str) -> None: # Add return type hint
    """View smoking records for a specific month (YYYY-MM)."""
    clear_screen()
    view_records_by_month(month)

@app.command() # added help for a better UX
def help() -> NoReturn:
    """Show the help message and exit."""
    typer.echo(app.info.help)
    raise typer.Exit()


def main() -> None:  # Add return type hint
    """Main entry point for the smoked-tracker CLI."""
    app()


if __name__ == "__main__":
    main()