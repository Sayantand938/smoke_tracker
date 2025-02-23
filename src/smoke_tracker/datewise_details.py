# src/smoke_tracker/datewise_details.py

from typing import List, Tuple
from rich.table import Table
from rich.console import Console
from .db_utils import get_records_by_date
from rich import print as rprint
import logging

logger = logging.getLogger(__name__)

# Define a type alias for a record
Record = Tuple[int, str, str, float]

def view_records_by_date(date_str: str) -> None:
    """
    View smoking records for a specific date.

    Args:
        date_str (str): The date for which to view records (YYYY-MM-DD), 'today', or 'yesterday'.
    """
    try:
        records: List[Record] = get_records_by_date(date_str)

        if not records:
            rprint(f"[yellow]No records found for {date_str}.[/yellow]")  # User-friendly message
            return

        title_date: str = records[0][1] if records and date_str.lower() in ('today', 'yesterday') else date_str

        table = Table(title=f"Smoking Records for {title_date}", show_lines=True)
        table.add_column("ID", justify="center")
        table.add_column("Date", justify="center")
        table.add_column("Brand", justify="center")
        table.add_column("Expense", justify="right")

        total_expense: float = 0.0

        for record in records:
            table.add_row(str(record[0]), record[1], record[2], f"₹{record[3]:.2f}")
            total_expense += record[3]

        console = Console()
        console.print(table)

        total_cigarettes: int = len(records)
        average_expense_per_cigarette: float = total_expense / total_cigarettes if total_cigarettes > 0 else 0.0

        # User-friendly summary
        rprint(
            f"[green]Total Expense: ₹{total_expense:.2f} | "
            f"Total Cigarettes: {total_cigarettes} | "
            f"Average Expense per Cigarette: ₹{average_expense_per_cigarette:.2f}[/green]"
        )

    except Exception as e:
        rprint(f"[red]An error occurred while fetching records for {date_str}.  Please try again.[/red]") # User-friendly error
        logger.error(f"Error in view_records_by_date: {e}") # Log the actual error