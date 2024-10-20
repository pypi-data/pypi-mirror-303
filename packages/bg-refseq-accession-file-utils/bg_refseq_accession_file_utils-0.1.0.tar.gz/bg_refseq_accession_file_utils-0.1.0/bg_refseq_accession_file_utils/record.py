from pydantic import BaseModel, Field, field_validator

from typing import List, Optional


class Record(BaseModel):

    # Field/column number 1
    gene_symbol: Optional[str] = Field(None, title="Gene symbol")

    # Field/column number 2
    refseq_accession: Optional[str] = Field(None, title="RefSeq accession")

    # Field/column number 3
    alternative_accession: Optional[List[str]] = Field(None, title="Alternative accessions")

