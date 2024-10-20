import logging
import os
from datetime import datetime

from singleton_decorator import singleton
from typing import List, Optional

from . import constants
from .record import Record


@singleton
class Writer:
    """Class for writing tab-delimited RefSeq accession file."""

    def __init__(self, **kwargs):
        """Constructor for class Writer."""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.outfile = kwargs.get("outfile", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", constants.DEFAULT_OUTDIR)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        logging.info(f"Instantiated Writer in {os.path.abspath(__file__)}")

    def write_file(self, records: List[Record], outfile: Optional[str]) -> None:
        """Write the records to the output tab-delimited RefSeq accession file.

        Args:
            records: List of records.
            outfile (Optional[str]): The path to the output file.
        """
        with open(outfile, 'w') as of:
            of.write(f"## method-created: {os.path.abspath(__file__)}\n")
            of.write(f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n")
            of.write(f"## created-by: {os.environ.get('USER')}\n")
            of.write(f"## logfile: {self.logfile}\n")

            header_line = "\t".join(self.config.get("column_headers"))

            of.write(f"#{header_line}\n")

            for record in records:

                aas = record.alternative_accessions

                line = record.gene_symbol + "\t" + \
                    record.refseq_accession + "\t" + \
                    ",".join(aas)

                of.write(f"{line}\n")

        logging.info(f"Wrote tab-delimited RefSeq accession file '{outfile}'")

        if self.verbose:
            print(f"Wrote tab-delimited RefSeq accession file '{outfile}'")

