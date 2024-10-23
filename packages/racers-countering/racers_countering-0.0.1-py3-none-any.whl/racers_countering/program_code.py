import re
import pathlib
from datetime import datetime, timedelta
from typing import Sequence, Optional
import pprint


class Record:
    abbr_pattern = re.compile(r"(^[A-Z]{3})_([\w ]+)_([A-Z ]+)$", re.UNICODE)
    start_pattern = re.compile(
        r"^([A-Z]{3})(\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.\d{3}$)"
    )
    stop_pattern = re.compile(
        r"^([A-Z]{3})(\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.\d{3}$)"
    )

    def __init__(
        self,
        driver: Optional[str] = None,
        team: Optional[str] = None,
        abbr: Optional[str] = None,
        start: Optional[datetime] = None,
        stop: Optional[datetime] = None,
    ):
        self._start = None
        self._stop = None
        self.driver = driver
        self.team = team
        self.abbr = abbr
        self.start = start
        self.stop = stop
        self.errors = []

    def __repr__(self):
        return f"Record {self.abbr} laptime {self.duration}"

    endlog_file_name = "end.log"

    @classmethod
    def read_abbreviations(
        cls,
        folder_path: pathlib.Path = pathlib.Path.cwd() / "additional",
        abbr_file_name: str = "abbreviations.txt",
    ) -> dict[str, "Record"]:
        if not folder_path.exists():
            raise FileNotFoundError(f"Folder: {folder_path} does not exist")
        if not (folder_path / abbr_file_name).exists():
            raise FileNotFoundError(
                f"File: {folder_path / abbr_file_name} does not exist"
            )
        result = {}
        with open(folder_path / abbr_file_name, "r", encoding="utf8") as f:
            for num_line, line in enumerate(f):
                #  перевірити формат рядка
                if m := re.match(cls.abbr_pattern, line):
                    result[m.group(1)] = cls(
                        abbr=m.group(1), driver=m.group(2), team=m.group(3)
                    )
                else:
                    record = cls()
                    record.errors.append(
                        f"Invalid format: {abbr_file_name} line: {num_line}: {line}"
                    )
                    result[
                        f"There is an error in line: [{str(num_line)}] in file: {abbr_file_name}"
                    ] = record
        return result

    @classmethod
    def read_start(
        cls,
        result: dict[str, "Record"],
        folder_path: pathlib.Path = pathlib.Path.cwd() / "additional",
        startlog_file_name: str = "start.log",
    ):
        if not (folder_path / startlog_file_name).exists():
            raise FileNotFoundError(
                f"File: {folder_path / startlog_file_name} does not exist"
            )
        with open(folder_path / startlog_file_name, "r", encoding="utf8") as f:

            for num_line, line in enumerate(f):
                #  checking line format
                try:
                    if m := re.match(cls.start_pattern, line):
                        result[m.group(1)].start = datetime.fromisoformat(m.group(2))
                    else:
                        record = cls()
                        record.errors.append(
                            f"Invalid format: {startlog_file_name} line: {num_line}: {line}"
                        )
                        result[str(num_line) + startlog_file_name] = record
                except SyntaxError as e:
                    record = cls()
                    record.errors.append(
                        f"{str(e)} During preparing {line} in {startlog_file_name} "
                    )
                except KeyError as e:
                    record = cls()
                    record.errors.append(
                        f"There is no this abbreviation in {str(e)} {startlog_file_name}"
                    )
        return result

    @classmethod
    def read_stop(
        cls,
        result: dict[str, "Record"],
        folder_path: pathlib.Path = pathlib.Path.cwd() / "additional",
        stoplog_file_name: str = "end.log",
    ):
        if not (folder_path / stoplog_file_name).exists():
            raise FileNotFoundError(
                f"File: {folder_path / stoplog_file_name} does not exist"
            )
        with open(folder_path / stoplog_file_name, "r", encoding="utf8") as f:
            for num_line, line in enumerate(f):
                #  checking line format
                try:
                    if m := re.match(cls.start_pattern, line):
                        result[m.group(1)].stop = datetime.fromisoformat(m.group(2))
                    else:
                        record = cls()
                        record.errors.append(
                            f"Invalid format: {stoplog_file_name} line: {num_line}: {line}"
                        )
                        result[str(num_line) + stoplog_file_name] = record
                except SyntaxError as e:
                    record = cls()
                    record.errors.append(
                        f"{str(e)} During preparing {line} in {stoplog_file_name} "
                    )
                except KeyError as e:
                    record = cls()
                    record.errors.append(
                        f"There is no this abbreviation in {str(e)} {stoplog_file_name}"
                    )
        return result

    @property
    def duration(self) -> timedelta | None:
        if not (self._start is None or self._stop is None):
            return self.stop - self.start

    @property
    def start(self) -> datetime:
        return self._start

    @start.setter
    def start(self, value: datetime):
        if self.stop is None or value < self.stop:
            self._start = value
        else:
            self.errors.append(f"Start time is equal or bigger than stop time: {value}")

    @property
    def stop(self) -> datetime:
        return self._stop

    @stop.setter
    def stop(self, value: datetime):
        if self.start is None or value > self.start:
            self._stop = value
        else:
            self.errors.append(
                f"Stop time is equal or smaller than start time: {value}"
            )

    @classmethod
    def build_report(
        cls,
        folder_path: pathlib.Path = pathlib.Path.cwd() / "additional",
        abbr_file_name: str = "abbreviations.txt",
        startlog_file_name: str = "start.log",
        stoplog_file_name: str = "end.log",
        reverse: bool = False,
    ) -> tuple[list["Record"], list["Record"]]:
        dict_records = cls.read_abbreviations(
            folder_path=folder_path, abbr_file_name=abbr_file_name
        )
        dict_records = cls.read_start(dict_records, folder_path, startlog_file_name)
        dict_records = cls.read_stop(dict_records, folder_path, stoplog_file_name)
        good_records = []
        bad_records = []
        for record in dict_records.values():
            if record.errors:
                bad_records.append(record)
            else:
                good_records.append(record)
        good_records.sort(key=lambda x: x.duration, reverse=reverse)
        return good_records, bad_records

    @staticmethod
    def print_report(
        good_records: list["Record"],
        bad_records: list["Record"],
        under_number: int = 15,
    ):

        top_racers = good_records[:under_number]
        remaining_racers = good_records[under_number:]
        res = ""
        res += "Top 15 Racers:\n"
        # print("Top 15 Racers:")
        for index, record in enumerate(top_racers, start=1):
            res += (
                f"{index}. {record.driver} ({record.team}) - Time: {record.duration}\n"
            )

        if remaining_racers:
            res += "\n" + "-" * 87 + "\n" + "\n"
            res += "Remaining Racers:\n"
            for index, record in enumerate(remaining_racers, start=under_number + 1):
                res += f"{index}. {record.driver} ({record.team}) - Time: {record.duration}\n"

        if bad_records:
            res += "\n" + "-" * 87 + "\n" + "\n"
            res += "Records with Errors:\n"
            for record in bad_records:
                res += f"{record.abbr} - Errors: {', '.join(record.errors)}\n"
        return res


if __name__ == "__main__":
    good_records, bad_records = Record.build_report()
    print(Record.print_report(good_records, bad_records, under_number=5))
