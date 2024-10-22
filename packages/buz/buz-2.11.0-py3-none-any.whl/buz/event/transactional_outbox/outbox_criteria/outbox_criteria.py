from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import ClassVar, Union, Tuple

from buz.event.transactional_outbox.outbox_criteria import OutboxSortingCriteria


@dataclass(frozen=True)
class OutboxCriteria:
    UNSET_VALUE: ClassVar[object] = object()

    delivered_at: Union[datetime, None, object] = UNSET_VALUE
    delivered_at_previous_to: Union[datetime, object] = UNSET_VALUE
    delivery_paused: Union[bool, object] = UNSET_VALUE
    order_by: Union[OutboxSortingCriteria, None, object] = UNSET_VALUE
    created_within_timerange: Union[Tuple[Union[timedelta, None], timedelta], object] = UNSET_VALUE
