#! usr/bin/env python

"""reporting handles all aspects of the various reports
that Table Differ runs both on the 'diff_table' but also
on the two tables being compared. Due to the potential size
of the two tables, reports done on those are kept to a minimum.
"""

import os

import logging
from rich.console import Console
from rich.table import Table
from rich import print as rprint


class BasicReport:
    """Types of simple reporting this needs to return:
    - counts of rows in origin, comp, and diff, tables
    - counts of identical rows
    - counts of modified rows
    """

    def __init__(
        self,
        conn,
        db_type: str,
        schema_name: str,
        table_initial: str,
        table_secondary: str,
        table_diff: str,
        compare_cols: list[str],
        ignore_cols: list[str],
    ):
        self.conn = conn
        self.cur = conn.cursor()
        self.db_type = db_type
        self.schema_name = schema_name + "."
        self.table_initial = table_initial
        self.table_secondary = table_secondary
        self.table_diff = table_diff
        self.compare_cols = compare_cols
        self.ignore_cols = ignore_cols

    def generate_report(self):
        self.get_counts()
        self.get_percentages()
        self.write_report()


    def get_percentages(self):
        def get_field_percentage():
            dct = {}
            total = 0
            for col in self.compare_cols:
                query = f"""
                    SELECT {col}
                    FROM {self.table_initial}
                EXCEPT
                    SELECT {col}
                    FROM {self.table_secondary}
                UNION ALL
                    SELECT {col}
                    FROM {self.table_secondary}
                EXCEPT
                    SELECT {col}
                    FROM {self.table_initial}
                """
                result = self.conn.sql(query).fetchall()
                dct[col] = round(len(result) / self.row_diff_cnt * 100, 2)
                total = total + len(result)
            return dct

        self.field_percentages = get_field_percentage()

    def get_counts(self):
        def count_rows():
            query = f"""SELECT COUNT(*) FROM {self.schema_name}{self.table_initial}"""
            logging.debug(query)
            if self.db_type == "duckdb":
                self.initial_table_row_cnt = self.conn.sql(query).fetchall()[0][0]
            else:
                self.cur.execute(query)
                self.initial_table_row_cnt = cur.fetchall()[0][0]

        def count_same_rows():
            comp_string = ""
            for num, col in enumerate(self.compare_cols):
                if num == 0:
                    comp_string += f"A.{col} = B.{col}"
                else:
                    comp_string += f" AND A.{col} = B.{col}"

            query = f""" SELECT COUNT(*)
                         FROM (SELECT *
                            FROM {self.schema_name}{self.table_initial} A
                           INNER JOIN {self.schema_name}{self.table_secondary} B
                              ON {comp_string})
                          """
            logging.debug(query)
            if self.db_type == "duckdb":
                self.row_match_cnt = self.conn.sql(query).fetchall()[0][0]
            else:
                self.cur.execute(query)
                self.row_match_cnt = cur.fetchall()[0][0]

        def count_modified_rows():
            query = f""" SELECT COUNT(*)
                         FROM (SELECT *
                                FROM {self.schema_name}{self.table_initial}
                                EXCEPT
                                SELECT *
                                    FROM {self.schema_name}{self.table_secondary})
                        """
            logging.debug(query)
            if self.db_type == "duckdb":
                self.row_diff_cnt = self.conn.sql(query).fetchall()[0][0]
            else:
                self.cur.execute(query)
                self.row_diff_cnt = cur.fetchall()[0][0]

        count_rows()
        count_same_rows()
        count_modified_rows()
        self.conn.commit()

    def write_report(self):
        report_table = Table(title="Basic Report")
        report_table.add_column("report", style="red", no_wrap=True)
        report_table.add_column("measure", style="magenta", no_wrap=True)
        report_table.add_column("result", style="cyan", no_wrap=True)
        report_table.add_row(
            "Diff Table Build",
            "initial table row count",
            str(self.initial_table_row_cnt),
        )
        report_table.add_row(
            "Diff Table Build", "row match count", str(self.row_match_cnt)
        )
        report_table.add_row(
            "Diff Table Build", "row diff count", str(self.row_diff_cnt)
        )
        for col in self.compare_cols:
            report_table.add_row(
                    "Field Percentages", f"field: {col}", str(self.field_percentages[col]) + " %"
                    )

        console = Console()
        console.print(report_table)


class PagerReport:
    def __init__(
        self,
        conn,
        db_type: str,
        schema_name: str,
        table_initial: str,
        table_secondary: str,
        table_diff: str,
        compare_cols: list[str],
        ignore_cols: list[str],
    ):
        self.conn = conn
        self.cur = conn.cursor()
        self.db_type = db_type
        self.schema_name = schema_name + "."
        self.table_initial = table_initial
        self.table_secondary = table_secondary
        self.table_diff = table_diff
        self.compare_cols = compare_cols
        self.ignore_cols = ignore_cols

    def generate_report(self):
        self.cli_control()

    def _get_diff_dict(self) -> dict:
        def get_keys():
            keys = []
            if self.db_type == "duckdb":
                results = self.conn.sql(
                    f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_diff}'"
                ).fetchall()
            else:
                print("not yet supported in PagerReport")
            for result in results:
                keys.append(result[0])
            return keys

        def get_values():
            query = f"SELECT * FROM {self.table_diff}"

            if self.db_type == "duckdb":
                results = self.conn.sql(query).fetchall()
            else:
                print("note yet supported in PagerReport")

            return results

        values = get_values()

        dct = {}
        for i, value in enumerate(values):
            dct[i] = dict((zip(get_keys(), value)))
        return dct

    def cli_control(self):
        rprint("\n[bold red] Welcome to Pager Report")
        diff_dict = self._get_diff_dict()
        try:
            while True:
                index = 0
                while index < len(diff_dict):
                    if index < 0:
                        index = len(diff_dict) - 1
                    if index > len(diff_dict):
                        index = 0
                    rprint(diff_dict[index])

                    user_input = input(
                        "press N to see next row (Ctrl+C to quit pager report)\n"
                    )
                    if user_input.lower() == "p":
                        index += -1
                    elif user_input.lower() == "n":
                        index += 1
                    os.system("clear")
        except KeyboardInterrupt:
            rprint("\n[bold red]Ending...")
