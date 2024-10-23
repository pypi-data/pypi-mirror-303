# Racers Counter

Racers Counter is a Python package that processes racing logs, including driver names, teams, 
start times, and stop times. It reads data from log files placed in a folder 'additional', calculates the lap time 
for each racer, and generates a report with the fastest lap times. It also handles errors in the input data 
and provides a detailed list of invalid records.

## Features

- Reads abbreviations, start, and stop logs to process race records
- Calculates lap times for each driver
- Sorts drivers based on their lap times
- Generates a report with top racers and records with errors

## Installation

You can install the package via pip:

pip install racers-countering

## Usage

1. Prepare the following log files in a directory (by default additional folder):

* abbreviations.txt: Contains abbreviations of drivers and teams.
* start.log: Contains the start time of each driver.
* end.log: Contains the stop time of each driver.

2. Import the Record class and call its methods to build and print the report:
from racers_counter.record import Record

good_records, bad_records = Record.build_report(
    folder_path="path_to_your_logs",
    abbr_file_name="abbreviations.txt",
    startlog_file_name="start.log",
    stoplog_file_name="end.log",
    reverse=False
)

print(Record.print_report(good_records, bad_records, under_number=5))

## Methods:

### Record.read_abbreviations()
Read all abbreviations from 'additional\abbreviations.txt'

### Record.build_report()
Builds the race report by reading the abbreviations, start times, and stop times. Returns two lists:

* good_records: List of records that were processed correctly.
* bad_records: List of records with errors.

### Record.print_report()
Generates a formatted report based on the provided records.