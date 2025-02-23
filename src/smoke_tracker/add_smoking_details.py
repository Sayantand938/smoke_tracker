# src/smoke_tracker/add_smoking_details.py

from datetime import datetime
from rich import print as rprint
from rich.prompt import Prompt, IntPrompt
from .db_utils import add_smoking_record_db
import logging

logger = logging.getLogger(__name__)

def get_valid_date() -> str:
    """Prompt user for a valid smoking date."""
    while True:
        date_str = Prompt.ask("\nWhen did you smoke?", default=datetime.now().strftime('%Y-%m-%d'))
        try:
            datetime.strptime(date_str, '%Y-%m-%d')  # Validate date format
            return date_str
        except ValueError:
            rprint("[bold red]Invalid date format. Please use YYYY-MM-DD.[/bold red]")


def get_positive_int(prompt_text: str, default: int = 1) -> int:
    """Prompt user for a positive integer."""
    while True:
        value = IntPrompt.ask(prompt_text, default=default)
        if value > 0:
            return value
        rprint("[bold red]Value must be greater than 0. Please try again.[/bold red]")


def get_positive_float(prompt_text: str) -> float:
    """Prompt user for a positive float value."""
    while True:
        try:
            value = float(Prompt.ask(prompt_text))
            if value > 0:
                return value
            rprint("[bold red]Value must be a positive number. Please try again.[/bold red]")
        except ValueError:
            rprint("[bold red]Invalid input. Please enter a valid number.[/bold red]")


def add_smoking_record() -> None:
    """Adds a new smoking record to the database."""
    try:
        smoked_at = get_valid_date()
        num_cigarettes = get_positive_int("How many cigarettes did you smoke?", default=1)

        records_added = False

        for i in range(1, num_cigarettes + 1):
            rprint(f"\n[bold blue]Details for cigarette {i}:[/bold blue]")

            brand = Prompt.ask(f"What brand did you smoke for cigarette {i}?").strip()
            if not brand:
                rprint("[bold red]Brand cannot be empty. Skipping this cigarette.[/bold red]")
                continue

            expense = get_positive_float(f"Total expense for cigarette {i}?")

            add_smoking_record_db(smoked_at, brand, expense)
            records_added = True

        if records_added:
            rprint("\n[bold green]Smoking records added successfully![/bold green]\n")
        else:
            rprint("\n[bold red]No valid smoking records were added.[/bold red]\n")

    except KeyboardInterrupt:
        rprint("\n[bold red]Operation cancelled by user. Exiting...[/bold red]\n")