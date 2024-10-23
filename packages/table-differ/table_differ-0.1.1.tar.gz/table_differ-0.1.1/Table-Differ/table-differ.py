#! /usr/bin/env python3

# long-help
""" Table Differ: Table comparison utility to be used within a SQLite, PostgreSQL, MySQL, or DuckDB database.
    Table comparison is achieved by creating a 'diff_table' out of changes between two
    different related tables based on given keys and what columns to focus on.
    Table Differ then conducts various reports on the contents of the 'diff_table'
    and prints them to the CLI.

    Table Differ picks up changes between the two tables as:
        - any row that has changed values within selected columns
        - any row that is missing information that exists in the other table
        - any row that exists within one table but not within the other

    Arguments that Table-Differ accepts:
    # REQUIRED ARGUMENTS

        -k --key_cols               specifies the name or names of key columns used
                                    to connect the two tables by

    # OPTIONAL ARGUMENTS

        -c --compare_cols           specified columns to focus on
        -i --ignore_cols            specified columns to ignore

    | 
    | Note that while both -c and -i can accept n number of values,
    |   only one of the two can be used on any single run.
    |

        --config-file               sources arguments from specified file

        -d --db_type                specifies what type of database to connect to

        -k --key_columns            specifies the name or names of key columns used
                                    to connect the two tables by

        -e --except_rows            signals Table Differ to ignore specific rows within
                                    each table based on the value of their key column(s)

        -l --logging_level          sets the logging level of Table Differ (default CRITICAL)

        -p --print_tables           attempts to print both of the tables used in the comparison
                                    to the CLI. This should only be used with small tables and will
                                    certainly cause issues when applied to very large tables

        --local-db                  specifies that the db path is local to run machine

        --report-mode               flag to only run reports on latest _diff_table__ found


    |
    | It is important to note that while --configs and -c/-i are optional arguments, one MUST be present
    |   at run time.
    |

example run
poetry run python3 table-differ.py -l info --config-file test_config.yaml -p

"""

# BUILT-INS
import logging
import sys
from os.path import expanduser

# THIRD PARTY
#import psycopg2 # psycopg2 encountering wheel build error and currently disabled
import duckdb
from rich import print as rprint

# PERSONAL
from modules import get_config
from modules.create_diff_table import DiffWriter
from modules.reporting import BasicReport, PagerReport


def main():
    args = get_config.get_config()
    db = args["database"]["db_type"]
    conn = create_connection(args, db)

    def report():
        basic_report = BasicReport(conn,
                                   args['database']['db_type'],
                                    args['table_info']['schema_name'],
                                    args['table_info']['table_initial'],
                                    args['table_info']['table_secondary'],
                                    args['table_info']['table_diff'],
                                    args['table_info']['comp_cols'],
                                    args['table_info']['ignore_cols'])
        basic_report.generate_report()

        pager_report = PagerReport(conn,
                                   args['database']['db_type'],
                                    args['table_info']['schema_name'],
                                    args['table_info']['table_initial'],
                                    args['table_info']['table_secondary'],
                                    args['table_info']['table_diff'],
                                    args['table_info']['comp_cols'],
                                    args['table_info']['ignore_cols'])
        pager_report.generate_report()

    if args["system"]["report_mode"]:
        report()
        sys.exit("Quiting Report Mode")

    tables = DiffWriter(args, conn)
    tables.create_diff_table()
    report()


def create_connection(args, db: str):
    """Attempts to connect to database pieced together from components in config.yaml
    """
    try:
        if db == "postgres":
            conn = psycopg2.connect(
                host=args["database"]["db_host"],
                database=args["database"]["db_name"],
                user=args["database"]["db_user"],
                port=args["database"]["db_port"],
            )
        elif db == "sqlite":
            assert args["database"]["db_path"]
            conn = sqlite3.connect(args["database"]["db_path"])
        elif db == "duckdb":
            assert args["database"]["db_path"]
            conn = duckdb.connect(args["database"]["db_path"])
        else:
            raise ValueError(f'Invalid db value: {db}')
        logging.info(f"[bold red]CURRENT CONNECTION:[/]  {conn}")
    except IOError as e:
        rprint(f"[bold red] IO Error:[/bold red] {str(e)}")
    except Exception as e:
        rprint(f"[bold red]UNRECOGNIZED ERROR:[/bold red] {str(e)}")
    finally:
        return conn


if __name__ == "__main__":
    main()
    
