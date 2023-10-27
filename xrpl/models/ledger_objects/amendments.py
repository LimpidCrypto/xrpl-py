"""Models for the Ledger Object `Amendments`"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from xrpl.models.ledger_objects.ledger_entry_type import LedgerEntryType
from xrpl.models.ledger_objects.ledger_object import LedgerObject
from xrpl.models.nested_model import NestedModel
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class Amendments(LedgerObject):
    """The model for the `Amendments` Ledger Object"""

    # always 0
    flags: int = REQUIRED  # type: ignore
    amendments: Optional[List[str]] = None
    majorities: Optional[List[Majority]] = None
    ledger_entry_type: LedgerEntryType = field(
        default=LedgerEntryType.AMENDMENTS,
        init=False,
    )


@require_kwargs_on_init
@dataclass(frozen=True)
class MDAmendmentsFields(LedgerObject):
    """
    The model for the `Amendments` Ledger Object when
    represented in a transaction's metadata.
    """

    # always 0
    flags: Optional[int] = None
    amendments: Optional[List[str]] = None
    majorities: Optional[List[Majority]] = None


@require_kwargs_on_init
@dataclass(frozen=True)
class Majority(NestedModel):
    """A model for the `Majority` object"""

    amendment: str = REQUIRED  # type: ignore
    close_time: int = REQUIRED  # type: ignore