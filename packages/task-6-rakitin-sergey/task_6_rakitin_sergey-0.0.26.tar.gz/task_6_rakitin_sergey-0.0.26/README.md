# F1 Racing Report Package

This Python package generates and prints a report for Formula 1 racing, based on logs of start and end times of racers. The package also provides a command-line interface (CLI) to interact with the report generation and allows flexible configuration options.

## Features

- **Report Generation**: Generate a sorted list of F1 racers by lap times.
- **CLI Interface**: Process files from a specified folder and print reports or errors.
- **Error Handling**: Provides detailed error messages for problematic records (e.g., invalid times).
- **Custom Report Options**: Includes optional sorting and underline settings.

## Installation

Install the package using PIP:

```bash
    pip install task_6_rakitin_sergey
```
# Usage

Enter the following commands via CMD.

## Below are some examples of how to use the CLI.

Basic Report generation (with ascending order by default):

```bash
    python -m task_6_rakitin_sergey.f1_report
```

Generate report with sorting order descending:

```bash
  python -m task_6_rakitin_sergey.f1_report --order desc
```

Print report with custom underline after a specific line (for example, 3):

```bash
    python -m task_6_rakitin_sergey.f1_report --underline_after 3
```

Show only errors:

```bash
    python -m task_6_rakitin_sergey.f1_report --errors_only
```

Show report for a specific driver:

```bash
    python -m task_6_rakitin_sergey.f1_report --driver "Sebastian Vettel"
```

Use an own path to .log and .txt files:

```bash
    python -m task_6_rakitin_sergey.f1_report --files <folder_path>
```

List of commands:

```bash
    python -m task_6_rakitin_sergey.f1_report --help
```

Import package to your project and call:

```bash
  from task_6_rakitin_sergey import f1_report

  if __name__ == "__main__":
      f1_report.command_line_input()
```

## Link to package page 

```Bash
    https://pypi.org/project/task-6-rakitin-sergey/
```



