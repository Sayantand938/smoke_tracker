# src/smoke_tracker/datewise_details.py
from rich import print as rprint
from rich.table import Table
from .db_utils import get_records_by_date  # Corrected import
from typing import List, Tuple, Union  # Import for type hinting

# Define a type alias for a record.  Makes type hints cleaner.
Record = Tuple[int, str, str, float]

def view_records_by_date(date_str: str) -> None:  # Add return type hint
    """View smoking records for a specific date.

    Args:
        date_str: The date for which to view records (YYYY-MM-DD),
            'today', or 'yesterday'.
    """
    records: List[Record] = get_records_by_date(date_str)  # Type hint

    if not records:
        rprint(f"\n[bold red]No records found for {date_str}.[/bold red]\n")
        return

    if date_str.lower() in ('today', 'yesterday'):
        title_date: str = records[0][1] if records else date_str
    else:
        title_date: str = date_str

    table = Table(title=f"\n[bold]Smoking Records for {title_date}[/bold]", show_lines=True)
    table.add_column("ID", style="", justify="center")
    table.add_column("Date", style="", justify="center")
    table.add_column("Brand", style="", justify="center")
    table.add_column("Expense", style="", justify="right")

    total_expense: float = 0.0  # Initialize with correct type

    for record in records:
        table.add_row(str(record[0]), record[1], record[2], f"₹{record[3]:.2f}")
        total_expense += record[3]

    rprint(table)

    total_cigarettes: int = len(records)
    # Avoid ZeroDivisionError
    average_expense_per_cigarette: float = (
        total_expense / total_cigarettes if total_cigarettes > 0 else 0.0
    )

    rprint(
        f"[bold green]Total Expense: ₹{total_expense:.2f} | "
        f"Total Cigarettes: {total_cigarettes}"
        f"\nAverage Expense per Cigarette: ₹{average_expense_per_cigarette:.2f}\n" #Added average expense per cigarette
    )