"""
Base types for ERC-7730 descriptors.

Specification: https://github.com/LedgerHQ/clear-signing-erc7730-registry/tree/master/specs
JSON schema: https://github.com/LedgerHQ/clear-signing-erc7730-registry/blob/master/specs/erc7730-v1.schema.json
"""

from typing import Annotated

from pydantic import Field

Id = Annotated[
    str,
    Field(
        title="Id",
        description="An internal identifier that can be used either for clarity specifying what the element is or as a"
        "reference in device specific sections.",
        min_length=1,
    ),
]

Address = Annotated[
    str,
    Field(
        title="Contract Address",
        description="An Ethereum contract address.",
        min_length=42,
        max_length=42,
        pattern=r"^0x[a-zA-Z0-9_\-]+$",
    ),
]

ScalarType = str | int | bool | float
