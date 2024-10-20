import csv
import logging
import os

from singleton_decorator import singleton
from typing import Dict, List, Optional

from . import constants
from .file_utils import check_infile_status
from .record import Record

DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP
)

@singleton
class Parser:
    """Class for parsing tab-delimited review file."""

    def __init__(self, **kwargs):
        """Constructor for class Parser"""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.infile = kwargs.get("infile", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", DEFAULT_OUTDIR)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        self._is_parsed = False
        self._records = []
        self.alternative_accession_to_refseq_accession_lookup = {}
        self.gene_symbol_to_refseq_accession_lookup = {}
        self.refseq_accession_to_gene_symbol_lookup = {}

        logging.info(f"Instantiated Parser in {os.path.abspath(__file__)}")

    def get_records(self, infile: Optional[str]) -> List[Record]:
        """Get the records.

        Args:
            infile (Optional[str]): The path to the file.

        Returns:
            List[Record]: List of records.
        """
        if not self._is_parsed:
            self._parse_file(infile)
        return self._records

    def _parse_file(self, infile: Optional[str]) -> None:
        """Parse the tab-delimited review file.

        Args:
            infile (Optional[str]): The path to the file.
        """
        if infile is None:
            infile = self.infile

        check_infile_status(infile)

        logging.info(f"Will parse the tab-delimited review file '{infile}'")

        with open(infile, mode='r') as f:

            reader = csv.reader(f, delimiter='\t')

            line_ctr = 0

            for row in reader:

                line_ctr += 1

                if line_ctr == 1:
                    continue

                gene_symbol = row[constants.DEFAULT_GENE_SYMBOL_IDX]
                refseq_accession = row[constants.DEFAULT_REFSEQ_ACCESSION_IDX]
                alternative_accessions = row[constants.DEFAULT_ALTERNATIVE_ACCESSIONS_IDX]

                if refseq_accession in self.refseq_accession_to_gene_symbol_lookup:
                    raise Exception(f"RefSeq accession '{refseq_accession}' is already in the lookup with gene symbol '{self.refseq_accession_to_gene_symbol_lookup[refseq_accession]}'")

                self.refseq_accession_to_gene_symbol_lookup[refseq_accession] = gene_symbol


                if gene_symbol in self.gene_symbol_to_refseq_accession_lookup:
                    raise Exception(f"Gene symbol '{gene_symbol}' is already in the lookup with RefSeq accession '{self.gene_symbol_to_refseq_accession_lookup[gene_symbol]}'")

                self.gene_symbol_to_refseq_accession_lookup[gene_symbol] = refseq_accession

                aas = alternative_accessions.split(",")

                for aa in aas:
                    aa = aa.strip()  # Remove leading/trailing whitespace
                    if aa not in self.alternative_accession_to_refseq_accession_lookup:
                        self.alternative_accession_to_refseq_accession_lookup[aa] = refseq_accession

                record = Record(
                    gene_symbol=gene_symbol,
                    refseq_accession=refseq_accession,
                    alternative_accessions=aas,
                )

                self._records.append(record)

        self._is_parsed = True
        logging.info(f"Processed '{line_ctr}' lines in the file '{infile}'")

    def get_gene_symbol_to_refseq_accession_lookup(self) -> Dict[str, str]:
        """Get the gene symbol to RefSeq accession lookup.

        Returns:
            dict: The gene symbol to RefSeq accession lookup.
        """
        return self.gene_symbol_to_refseq_accession_lookup

    def get_refseq_accession_to_gene_symbol_lookup(self) -> Dict[str, str]:
        """Get the RefSeq accession to gene symbol lookup.

        Returns:
            dict: The RefSeq accession to gene symbol lookup.
        """
        return self.refseq_accession_to_gene_symbol_lookup

    def get_alternative_accessions_to_refseq_accession_lookup(self) -> Dict[str, str]:
        """Get the alternative accessions to RefSeq accession lookup.

        Returns:
            dict: The alternative accessions to RefSeq accession lookup.
        """
        return self.alternative_accession_to_refseq_accession_lookup
