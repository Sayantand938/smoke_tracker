# Smoked Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Smoked Tracker is a simple command-line interface (CLI) tool built with Python to help you track your smoking habits. It allows you to record details about each cigarette you smoke, view records by date and month, and analyze your spending.

## Features

- **Add Smoking Records:** Easily add records for each cigarette, including the brand and expense.
- **View Records by Date:** See a detailed breakdown of your smoking history for a specific date, including total cigarettes smoked and total expense.
- **View Records by Month:** Get a monthly summary of your smoking habits, including the total number of cigarettes, the most smoked brand, and the total expense.
- **Data Persistence:** Your data is stored securely in a local SQLite database.
- **Easy to Use:** Simple and intuitive command-line interface.
- **Isolated Environment:** Works seamlessly with `pipx` to ensure a clean and isolated installation.

## Installation

It is recommended to use `pipx` to install `smoked-tracker`. This ensures that the application and its dependencies are installed in an isolated environment, preventing conflicts with other Python packages.

1.  **Install `pipx` (if you don't have it):**

    ```bash
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    ```

    You may need to restart your shell after running `ensurepath`.

2.  **Install `smoked-tracker`:**

    ```bash
    pipx install smoked-tracker
    ```

    _Replace `smoked-tracker` by the actual name of your pypi package._

## Usage

The `smoked-tracker` CLI provides the following commands:

- **`smoked-tracker add`:** Add a new smoking record. You'll be prompted for the date, number of cigarettes, brand, and expense for each cigarette.

  ```bash
  smoked-tracker add
  ```

- **`smoked-tracker date <date>`:** View smoking records for a specific date. The date can be in `YYYY-MM-DD` format, or you can use the keywords `today` or `yesterday`.

  ```bash
  smoked-tracker date 2023-10-27
  smoked-tracker date today
  smoked-tracker date yesterday
  ```

- **`smoked-tracker month <month>`:** View smoking records for a specific month. The month should be in `YYYY-MM` format.

  ```bash
  smoked-tracker month 2023-10
  ```

- **`smoked-tracker --help`** View the help file

  ```bash
  smoked-tracker --help
  ```

## Examples

1.  **Adding a record:**

    ```bash
    smoked-tracker add
    ```

    You'll then be guided through prompts to enter details about the cigarette(s) you smoked.

2.  **Viewing records for today:**

    ```bash
    smoked-tracker date today
    ```

3.  **Viewing records for October 2023:**

    ```bash
    smoked-tracker month 2023-10
    ```

## Dependencies

- [typer](https://typer.tiangolo.com/)
- [rich](https://rich.readthedocs.io/en/latest/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) (Included in the Python standard library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the project's repository.

## Author

Your Name (your.email@example.com) _Replace with your name and email._
