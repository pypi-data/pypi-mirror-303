from datetime import UTC
from datetime import date
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QWidget

from movsviewer.reader import read

if TYPE_CHECKING:
    from movslib.model import KV
    from movslib.model import Rows

    from movsviewer.settings import Settings


def validate_saldo(kv: 'KV', csv: 'Rows', messages: list[str]) -> bool:
    messages.append(f'bpol.saldo_al:                      {kv.saldo_al}')
    if kv.saldo_al:
        ultimo_update = (datetime.now(tz=UTC).date() - kv.saldo_al).days
        messages.append(
            f'ultimo update:                      {ultimo_update} giorni fa'
        )
    messages.append(
        f'bpol.saldo_contabile:               {float(kv.saldo_contabile):_}'
    )
    messages.append(
        f'bpol.saldo_disponibile:             {float(kv.saldo_disponibile):_}'
    )

    s = sum(item.money for item in csv)
    messages.append(f'Σ (item.accredito - item.addebito): {float(s):_}')
    ret = kv.saldo_contabile == s == kv.saldo_disponibile
    if not ret:
        delta = max(
            [abs(kv.saldo_contabile - s), abs(s - kv.saldo_disponibile)]
        )
        messages.append(f'Δ:                                  {float(delta):_}')
    return ret


def validate_dates(csv: 'Rows', messages: list[str]) -> bool:
    data_contabile: date | None = None
    for row in csv:
        if data_contabile is not None and data_contabile < row.data_contabile:
            messages.append(f'{data_contabile} < {row.data_contabile}!')
            return False
    return True


def validate(fn: str, messages: list[str]) -> bool:
    messages.append(fn)
    kv, csv = read(fn, Path(fn).stem)
    return all(
        [validate_saldo(kv, csv, messages), validate_dates(csv, messages)]
    )


class Validator:
    def __init__(self, parent: QWidget, settings: 'Settings') -> None:
        self.parent = parent
        self.settings = settings

    def validate(self) -> bool:
        for fn in self.settings.data_paths:
            messages: list[str] = []
            if not validate(fn, messages):
                button = QMessageBox.warning(
                    self.parent,
                    f'{fn} seems has some problems!',
                    '\n'.join(messages),
                    QMessageBox.StandardButton.Yes
                    | QMessageBox.StandardButton.No,
                )
                return button is QMessageBox.StandardButton.Yes
        return True
