# src/smoke_tracker/add_smoking_details.py

from datetime import datetime
from rich import print as rprint
from rich.prompt import Prompt, IntPrompt
from .db_utils import add_smoking_record_db, initialize_database  # Corrected import
from typing import List, Dict, Tuple  # Import for type hinting


def add_smoking_record() -> None:  # Add return type hint
    """Adds a new smoking record to the database.

    Prompts the user for details about one or more cigarettes smoked
    and saves the information to the database.  Handles invalid input
    and gracefully exits on keyboard interrupt.
    """
    initialize_database()

    try:
        smoked_at: str = Prompt.ask(  # Add type hint
            "\nWhen did you smoke?",
            default=datetime.now().strftime('%Y-%m-%d')
        )

        num_cigarettes: int = IntPrompt.ask(
            "How many cigarettes did you smoke?", default=1
        )
        if num_cigarettes <= 0:
            rprint("[bold red]Number of cigarettes must be greater than 0. Please try again.[/bold red]")
            return

        records_added: bool = False  # Type hint

        for i in range(1, num_cigarettes + 1):
            rprint(f"\n[bold blue]Details for cigarette {i}:[/bold blue]")

            brand: str = Prompt.ask(  # Type hint
                f"What brand did you smoke for cigarette {i}?"
            ).strip()
            if not brand:
                rprint("[bold red]Brand cannot be empty. Skipping this cigarette.[/bold red]")
                continue

            while True: # Use a loop for retries
                try:
                    expense: float = float(  # Type hint
                        Prompt.ask(f"Total expense for cigarette {i}?")
                    )
                    if expense <= 0:
                        rprint("[bold red]Expense must be a positive number. Please try again.[/bold red]")
                        continue # Go to the next iteration of the inner loop
                    break  # Exit the inner loop if input is valid
                except ValueError:
                    rprint("[bold red]Invalid expense value. Please enter a valid number.[/bold red]")
                    # No need to continue here; the loop will repeat

            add_smoking_record_db(smoked_at, brand, expense)
            records_added = True

        if records_added:
            rprint("\n[bold green]Smoking records added successfully![/bold green]\n")
        else:
            rprint("\n[bold red]No valid smoking records were added.[/bold red]\n")

    except KeyboardInterrupt:
        rprint("\n[bold red]Operation cancelled by user. Exiting...[/bold red]\n")