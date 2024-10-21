from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List
import re, argparse


class Record:
    """
    The class will collect data about each racer and lap. Data includes: abbreviation,
    racer name, team, start and end time, calculated lap time
    """

    # Regular expression pattern for validation and capturing abbreviation and start or end time
    line_pattern = re.compile(r"^(?P<abbreviation>[A-Z]{3})(?P<time>\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}\.\d{3})$")

    def __init__(
        self,
        abbreviation: Optional[str] = None,
        racer_name: Optional[str] = None,
        team: Optional[str] = None,
    ) -> None:

        self.abbreviation = abbreviation  # Abbreviation of team
        self.racer_name = racer_name  # Racer name
        self.team = team  # Team
        self._start_time: Optional[datetime] = None  # Time of start
        self._end_time: Optional[datetime] = None  # Time of the end
        self._lap_time: Optional[timedelta] = None  # Calculated lap time
        self.errors: list[str] = []  # List for errors

    # Getter for start_time
    @property
    def start_time(self) -> Optional[datetime]:
        return self._start_time

    # Setter for start_time
    @start_time.setter
    def start_time(self,  value: Optional[str] = None) -> None:
        """
        Setting the start time attribute.
        Validates the start time format and logs errors if the format incorrect or empty.
        Arguments:
            param str -- The start time format "%Y-%m-%d_%H:%M:%S.%f"
        """

        if value is None:  # Intercepting None case
            self._start_time = None
            pass
        else:
            try:
                self._start_time = datetime.strptime(value, "%Y-%m-%d_%H:%M:%S.%f")
            except ValueError:
                self.errors.append("Start_time: Invalid start time format.")
                pass  # Skip further processing for this record

    # Getter for end_time
    @property
    def end_time(self) -> Optional[datetime]:
        return self._end_time

    # Setter for end_time
    @end_time.setter
    def end_time(self, value: Optional[str] = None) -> None:
        """
        Setting the end time attribute.
        Validates the end time format and logs errors if the format incorrect or empty.
        Arguments:
            param str -- The end time format "%Y-%m-%d_%H:%M:%S.%f"
        """

        if value is None:              # Intercepting None case
            self._end_time = None
            pass
        else:
            try:
                self._end_time = datetime.strptime(value, "%Y-%m-%d_%H:%M:%S.%f")
            except ValueError:
                self.errors.append("End_time: Invalid end time format.")
                pass     # Skip further processing for this record

    @property
    def calculated_lap_time(self) -> timedelta:
        """
        Method will calculate lap time from start and end time.
        In case of logical errors they will be logged.
        Returns:
            timedelta: difference between start and end time
        """

        if self._start_time is None or self._end_time is None:
            self.errors.append("Logical error: Start or End time is empty")
            pass        # Skip further processing for this record
        elif self._start_time == self._end_time:
            self.errors.append("Logical error: Start time and end time are equal")
            pass        # Skip further processing for this record
        elif self._start_time > self._end_time:
            self.errors.append("Logical error: Start time cannot be greater than end time")
            pass        # Skip further processing for this record
        else:
            self._lap_time = self._end_time - self._start_time
        return self._lap_time or timedelta(0)

    @classmethod
    def get_record_dict(cls, folder: Path = Path(__file__).resolve().parent.parent / "data",
                       file: str = "abbreviations.txt") -> dict[str, "Record"]:
        """
        Method reads abbreviation file and creates a dictionary of abbreviations
        names and teams of each racer.
        Each line in the file should follow the format:
        abbreviation_racer_name_team

        If the line is missing any of these parts (i.e., abbreviation, racer name, or team),
        an error entry will be created with None values for the racer and team, and the
        specific error will be logged under the 'errors' attribute.
        Arguments:
            folder {Path} -- The folder containing the abbreviation
            file {str} -- The abbreviation file name
            default {Path.cwd}\data\abbreviations.txt
        Returns:
            dict[str, "Record"] -- Dictionary where keys are abbreviations and values
            are instances of Record class.
        Raises:
        FileNotFoundError -- If the specified file is not found in the provided folder.
        """


        records = {}               # Dictionary to store the parsed records
        file_path = folder / file  # Combine folder and file to create full path

        try:
            # Open the file for reading
            with open(file_path, 'r', encoding="UTF-8") as f:
                # Iterate each line in the file
                for line_num, line in enumerate(f, start=1):

                    # Split the line by underscores (up to 3 parts: abbreviation, racer name, and team)
                    parts  = line.strip().split("_", 2)

                    # Check if the line has fewer than 3 parts or contains empty elements
                    if len(parts) != 3 or any(not part.strip() for part in parts):
                        # Handle incorrect format
                        error_record = cls(None, None, None)  # Create an error record
                        error_record.errors.append(f"Line {line_num}: Invalid format in line: {line.strip()}")
                        records[f"{folder.name}_{line_num}"] = error_record
                        continue


                    try:
                    # Parse the line into abbreviation, name and team
                        abbreviation, racer_name, team = line.strip().split('_', 2)
                        # Create a Record object and store it in the dictionary
                        record = cls(abbreviation, racer_name, team)
                        records[abbreviation] = record
                    except ValueError:
                        # Handle format error in the line
                        error_record = cls(None, None, None)
                        error_record.errors.append(f"Line {line_num}: Invalid format in line: {line.strip()}")


        # Handle  file not exist error
        except FileNotFoundError:
            raise FileNotFoundError(f"The file abbreviations.txt in {folder} was not found.")

        return records

    @classmethod
    def add_start_time(cls, records: dict[str, "Record"],
                       folder: Path = Path(__file__).resolve().parent.parent / "data",
                       file: str = "start.log") -> dict[str, "Record"]:
        """
        Reads the corresponding start time file and updates records in the dictionary.

        Possible errors:
        - File not found (raise FileNotFoundError)
        - Line does not match the expected format (creates a new record with null fields and logs the error)
        - Correct format, but the key is not in the dictionary (creates a new record with an error description)

        Arguments:
        - records {dict}: Dictionary with existing racer records.
        - folder {Path}: Path to the folder containing the file.
        - File {str}: File name for reading the start times.

        Returns:
        - dict: Updated dictionary with records and errors where applicable.
        """

        file_path = folder / file  # Combine folder and file to create a full path

        # Check if the file exists before opening it
        if not file_path.exists():
            raise FileNotFoundError(f"The file {file} in {folder} was not found.")

        # Open and process the file
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                # Skip empty lines
                if not line.strip():
                    continue

                # Use the regular expression to validate and capture abbreviation and time
                match = cls.line_pattern.match(line.strip())

                if not match:

                    # Log an error if the line does not match the expected pattern
                    error_record = cls(None, None, None)
                    error_record.errors.append(f"Line {line_num}: Invalid format in line: {line.strip()}")
                    records[f"{file}_{line_num}"] = error_record

                else:
                    # Extract abbreviation and start time from the matched groups
                    abbreviation = match.group("abbreviation")
                    start_time_str = match.group("time")

                    # Check if abbreviation exists in records
                    if abbreviation in records:
                        try:
                            # Use setter to set the start time
                            records[abbreviation].start_time = start_time_str

                        except ValueError as e:
                            error_record = records[abbreviation]
                            error_record.errors.append(f"Line {line_num}: Error setting start time: {str(e)}")
                            records[abbreviation] = error_record

                    else:
                        error_record = cls(abbreviation, None, None)
                        error_record.errors.append(f"Line {line_num}: Abbreviation not found in records")
                        records[f"{file}_{line_num}"] = error_record

        return records

    @classmethod
    def add_end_time(cls, records: dict[str, "Record"],
                     folder: Path = Path(__file__).resolve().parent.parent / "data",
                     file: str = "end.log") -> dict[str, "Record"]:
        """
        Reads the corresponding end time file and updates records in the dictionary.

        Possible errors:
        - File not found (raise FileNotFoundError)
        - Line does not match the expected format (creates a new record with null fields and logs the error)
        - Correct format, but the key is not in the dictionary (creates a new record with an error description)

        Arguments:
        - records {dict}: Dictionary with existing racer records.
        - folder {Path}: Path to the folder containing the file.
        - File {str}: File name for reading the end times (default: "end.log").

        Returns:
        - dict: Updated dictionary with records and errors where applicable.
        """

        file_path = folder / file  # Combine folder and file to create a full path

        # Check if the file exists before opening it
        if not file_path.exists():
            raise FileNotFoundError(f"The file {file} in {folder} was not found.")

        # Open and process the file
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                # Skip empty lines
                if not line.strip():
                    continue

                # Use the regular expression to validate and capture abbreviation and time
                match = cls.line_pattern.match(line.strip())

                if not match:
                    # Log an error if the line does not match the expected pattern
                    error_record = cls(None, None, None)
                    error_record.errors.append(f"Line {line_num}: Invalid format in line: {line.strip()}")
                    records[f"{file}_{line_num}"] = error_record
                    continue  # Skip to the next line
                else:
                    # Extract abbreviation and end time from the matched groups
                    abbreviation = match.group("abbreviation")
                    end_time_str = match.group("time")

                    # Check if abbreviation exists in records
                    if abbreviation in records:
                        try:
                            # Use setter to set the end time
                            records[abbreviation].end_time = end_time_str

                        except ValueError as e:
                            error_record = records[abbreviation]
                            error_record.errors.append(f"Line {line_num}: Error setting end time: {str(e)}")
                            records[abbreviation] = error_record

                    # If the abbreviation is not found, log an error under that abbreviation
                    else:
                        error_record = cls(abbreviation, None, None)
                        error_record.errors.append(f"Line {line_num}: Abbreviation not found in records")
                        records[f"{file}_{line_num}"] = error_record

        return records

    @property
    def lap_time(self):
        return self._lap_time


def build_report(records: dict[str, Record]) -> tuple[list[Record], dict[str, list[str]]]:
    """
    Builds a list of valid racer records sorted by lap time and collects errors.
    The function filters out racers with any recorded errors, sorts the remaining records
    based on lap time, and returns both a list of valid records and a dictionary of errors.

    Args:
        records (dict[str, Record]): A dictionary where the key is the abbreviation
                                     and the value is a Record object containing the racer's details.

    Returns:
        tuple: A tuple containing:
            - list[Record]: A list of valid Record objects sorted by their lap times.
            - dict[str, list[str]]: A dictionary with abbreviations as keys and lists of errors as values.
    """

    # Filter records that have no errors and sort them by lap time
    valid_records = [
        record for record in records.values()
        if not record.errors and record.calculated_lap_time > timedelta(0)
    ]

    # Sort the filtered records by lap time (ascending)
    sorted_records = sorted(valid_records, key=lambda r: r.calculated_lap_time)

    # Collect errors in a dictionary where keys are abbreviations and values are lists of errors
    error_dict = {
        record.abbreviation: record.errors
        for record in records.values() if record.errors
    }

    return sorted_records, error_dict


def print_report(
        valid_records: list[Record],
        errors: dict[str, list[str]] = None,
        underline_after: int = 15) -> None:
    """
    Prints the race report with valid lap records and error report.

    The report is generated using the build_report function.

    Underline_after (int): The row after which to print a separator line. Default is 15.
    """

    # Printing report
    print("Generated Report:")
    for i, record in enumerate(valid_records, start=1):

        # Format class Records objects to strings and print
        print(f"{i}. {record.racer_name:<20} | {record.team:<40} | {str(record.calculated_lap_time)[2:]}")

        # Add a separator after line 15
        if i == underline_after:
            print("-" * 72)

    # Continue processing after separator line
    for i, record in enumerate(valid_records[15:], start=16):
        print(f"{i}. {record.racer_name:<20} | {record.team:<40} | {str(record.calculated_lap_time)[2:]}")

    # Printing errors if any
    if errors:
        print("\nErrors:")
        print("-" * 72)
        for abbreviation, error_list in errors.items():
            for error in error_list:
                print(f"{abbreviation}: {', '.join(error_list)}")


def command_line_input() -> None:
    """
    Main function for handling command-line interface (CLI).

    It parses the command-line arguments, processes the input files (if provided),
    generates a report, and prints it using the `print_report` function.

        Command-line options:
        - --files <folder_path>: Specifies the folder containing the data files.
        - --order {asc, desc}: Optional sorting order for the report (default is ascending).
        - --driver "Name": Prints statistics for a specific driver.
        - --errors_only: Prints only the errors in the report.
        - --underline_after <number>: Customizes the row after which the separator line is printed.

    This function uses the `print_report` function to display the race report and errors.
    """

    # Parse CLI options
    parser = argparse.ArgumentParser(description="Generate F1 race report")

    parser.add_argument('--files', type=str, help="Path to the folder with log files",
                        default=str(Path(__file__).resolve().parent.parent / "data"))

    parser.add_argument('--order', choices=['asc', 'desc'], default='asc',
                        help="Order of the report (asc or desc)")

    parser.add_argument('--underline_after', type=int, default=15,
                        help="Row after which to print a separator line (default: 15)")

    parser.add_argument('--driver', type=str, help="Show statistics for a specific driver")

    parser.add_argument('--errors_only', action='store_true', help="Show only the error report")

    args = parser.parse_args()

    # Path to the users folder if provided
    folder = Path(args.files)

    # Check if the folder exists
    if not folder.exists():
        raise FileNotFoundError(f"The folder {folder} was not found.")

    # Reading data
    records = Record.get_record_dict(folder=folder)
    records = Record.add_start_time(records, folder=folder)
    records = Record.add_end_time(records, folder=folder)

    # Build a report (valid records and errors)
    valid_records, errors = build_report(records)

    # Handling CLI arguments and print report
    # If a specific driver is requested
    if args.driver:
        driver_record = next((rec for rec in valid_records if rec.racer_name == args.driver), None)
        if driver_record:
            print(
                f"{driver_record.racer_name:<20} | {driver_record.team:<40} | {str(driver_record.calculated_lap_time)[2:]}")
        else:
            print(f"No data found for driver: {args.driver}")
        return

    # If errors only are requested
    if args.errors_only:
        if errors:
            print("Errors:")
            for abbreviation, error_list in errors.items():
                for error in error_list:
                    print(f"{abbreviation}: {error}")
        else:
            print("No errors found.")
        return

    # Print the report in the requested order "--desc"
    if args.order == 'desc':
        valid_records = valid_records[::-1]  # Reverse the order for descending

    # Call print_report to display the sorted records and errors (if any) by default
    print_report(valid_records, errors, underline_after=args.underline_after)


if __name__ == "__main__":
    command_line_input()
