"""Models for the Ledger Object `Escrow`"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from xrpl.models.ledger_objects.ledger_entry_type import LedgerEntryType
from xrpl.models.ledger_objects.ledger_object import LedgerObject
from xrpl.models.required import REQUIRED
from xrpl.models.utils import require_kwargs_on_init


@require_kwargs_on_init
@dataclass(frozen=True)
class Escrow(LedgerObject):
    """The model for the `Escrow` Ledger Object"""

    account: str = REQUIRED  # type: ignore
    amount: str = REQUIRED  # type: ignore
    destination: str = REQUIRED  # type: ignore
    # always 0
    flags: int = REQUIRED  # type: ignore
    owner_node: str = REQUIRED  # type: ignore
    previous_txn_id: str = REQUIRED  # type: ignore
    previous_txn_lgr_seq: int = REQUIRED  # type: ignore
    condition: Optional[str] = None
    cancel_after: Optional[int] = None
    destination_node: Optional[str] = None
    destination_tag: Optional[int] = None
    finish_after: Optional[int] = None
    source_tag: Optional[int] = None
    ledger_entry_type: LedgerEntryType = field(
        default=LedgerEntryType.ESCROW, init=False
    )


@require_kwargs_on_init
@dataclass(frozen=True)
class MDEscrowFields(LedgerObject):
    """
    The model for the `Escrow` Ledger Object when
    represented in a transaction's metadata.
    """

    account: Optional[str] = None
    amount: Optional[str] = None
    destination: Optional[str] = None
    # always 0
    flags: Optional[int] = None
    owner_node: Optional[str] = None
    previous_txn_id: Optional[str] = None
    previous_txn_lgr_seq: Optional[int] = None
    condition: Optional[str] = None
    cancel_after: Optional[int] = None
    destination_node: Optional[str] = None
    destination_tag: Optional[int] = None
    finish_after: Optional[int] = None
    source_tag: Optional[int] = None