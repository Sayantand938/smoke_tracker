# src/smoke_tracker/monthwise_details.py

import logging
from rich.console import Console
from rich.table import Table
from .db_utils import get_records_by_month
from typing import List, Tuple
from rich import print as rprint

logger = logging.getLogger(__name__)

# Type alias for aggregated record (same as in db_utils)
AggregatedRecord = Tuple[int, str, float]

def view_records_by_month(month: str) -> None:
    """View smoking records for a specific month.

    Args:
        month (str): The month for which to view records (YYYY-MM).
    """
    try:
        records: List[AggregatedRecord] = get_records_by_month(month)

        if not records:
            rprint(f"[yellow]No records found for {month}.[/yellow]")
            return

        total_smoked: int = sum(record[0] for record in records)
        most_smoked_brand: str = records[0][1] if records else ""
        total_expense: float = sum(record[2] for record in records)

        table = Table(title=f"Smoking Records for {month}", show_lines=True)
        table.add_column("Month", justify="center")
        table.add_column("Total Smoked", justify="center")
        table.add_column("Most Smoked Brand", justify="center")
        table.add_column("Total Expense", justify="right")

        table.add_row(month, str(total_smoked), most_smoked_brand, f"₹{total_expense:.2f}")

        console = Console()
        console.print(table)

    except Exception as e:
        rprint(f"[red]An error occurred while fetching records for {month}. Please try again.[/red]")
        logger.error(f"Error in view_records_by_month: {e}")