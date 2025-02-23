# src/smoke_tracker/monthwise_details.py

from rich import print as rprint
from rich.table import Table
from .db_utils import get_records_by_month  # Corrected import
from typing import List, Tuple  # Import for type hinting

# Type alias for aggregated record (same as in db_utils)
AggregatedRecord = Tuple[int, str, float]


def view_records_by_month(month: str) -> None: #return type
    """View smoking records for a specific month.

    Args:
        month: The month for which to view records (YYYY-MM).
    """
    records: List[AggregatedRecord] = get_records_by_month(month)

    if not records:
        rprint(f"\n[bold red]No records found for {month}.[/bold red]\n")
        return

    total_smoked: int = sum(record[0] for record in records)
    most_smoked_brand: str = records[0][1] if records else "" # Handle empty records
    total_expense: float = sum(record[2] for record in records)

    table = Table(title=f"\n[bold]Smoking Records for {month}[/bold]", show_lines=True)
    table.add_column("Month", style="", justify="center") # Changed column name
    table.add_column("Total Smoked", style="", justify="center")
    table.add_column("Most Smoked Brand", style="", justify="center") # Changed column name
    table.add_column("Total Expense", style="", justify="right")

    table.add_row(month, str(total_smoked), most_smoked_brand, f"₹{total_expense:.2f}")
    rprint(table)
    rprint()