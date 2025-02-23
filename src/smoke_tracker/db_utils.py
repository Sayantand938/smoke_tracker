# src/smoke_tracker/db_utils.py

import sqlite3
import os
from datetime import date, timedelta, datetime
from typing import List, Tuple, Union

# Type alias for a record from get_records_by_date
Record = Tuple[int, str, str, float]
# Type alias for aggregated record from get_records_by_month
AggregatedRecord = Tuple[int, str, float]


def get_db_path() -> str:
    """Gets the absolute path to the database file in the user's home directory."""
    home_dir = os.path.expanduser("~")
    db_dir = os.path.join(home_dir, ".smoked-tracker")  # Hidden directory
    db_path = os.path.join(db_dir, "smoke_tracker.db")
    os.makedirs(db_dir, exist_ok=True)  # Create the directory if it doesn't exist
    return db_path

def initialize_database() -> None:
    """Initializes the database and creates the table if it doesn't exist."""
    db_path: str = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS smoking_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            smoked_at TEXT NOT NULL,
            brand TEXT NOT NULL,
            expense REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_smoking_record_db(smoked_at: str, brand: str, expense: float) -> None:
    """Adds a smoking record to the database."""
    db_path: str = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO smoking_details (smoked_at, brand, expense)
        VALUES (?, ?, ?)
    ''', (smoked_at, brand, expense))

    conn.commit()
    conn.close()

def get_records_by_date(date_str: str) -> List[Record]:
    """Fetches smoking records for a given date from the database.

    Args:
        date_str: The date (YYYY-MM-DD), 'today', or 'yesterday'.

    Returns:
        A list of tuples, where each tuple represents a record.
        Returns an empty list if no records are found or if the date is invalid.
    """
    db_path: str = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if date_str.lower() == 'today':
        date_to_query: str = date.today().strftime('%Y-%m-%d')
    elif date_str.lower() == 'yesterday':
        date_to_query: str = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            date_to_query: str = date_str
        except ValueError:
            return []

    cursor.execute('SELECT * FROM smoking_details WHERE smoked_at = ?', (date_to_query,))
    records: List[Record] = cursor.fetchall()
    conn.close()
    return records

def get_records_by_month(month: str) -> List[AggregatedRecord]:
    """Fetches smoking records for a given month from the database.

    Args:
        month: The month (YYYY-MM).

    Returns:
        A list of tuples, where each tuple represents aggregated data
        (total_smoked, brand, total_expense).  Returns an empty list if
        no records are found.
    """
    db_path: str = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT
            COUNT(*) AS total_smoked,
            brand,
            SUM(expense) AS total_expense
        FROM smoking_details
        WHERE strftime("%Y-%m", smoked_at) = ?
        GROUP BY brand
        ORDER BY total_smoked DESC
    ''', (month,))
    records: List[AggregatedRecord] = cursor.fetchall()
    conn.close()
    return records

initialize_database()