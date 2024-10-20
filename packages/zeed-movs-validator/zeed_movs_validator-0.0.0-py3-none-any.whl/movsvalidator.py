from datetime import UTC
from datetime import date
from datetime import datetime
from logging import INFO
from logging import basicConfig
from logging import error
from logging import info
from sys import argv
from typing import TYPE_CHECKING

from movslib.movs import read_txt

if TYPE_CHECKING:
    from movslib.model import KV
    from movslib.model import Row


def validate_saldo(kv: 'KV', csv: list['Row']) -> bool:
    info('bpol.saldo_al:                      %s', kv.saldo_al)
    if kv.saldo_al:
        ultimo_update = (datetime.now(UTC).date() - kv.saldo_al).days
        info('ultimo update:                      %s giorni fa', ultimo_update)
    info('bpol.saldo_contabile:               %s', kv.saldo_contabile)
    info('bpol.saldo_disponibile:             %s', kv.saldo_disponibile)

    s = sum(item.money for item in csv)
    info('Σ (item.accredito - item.addebito): %s', s)
    ret = kv.saldo_contabile == s == kv.saldo_disponibile
    if not ret:
        delta = max(
            [abs(kv.saldo_contabile - s), abs(s - kv.saldo_disponibile)]
        )
        info('Δ:                                  %s', delta)
    return ret


def validate_dates(csv: list['Row']) -> bool:
    data_contabile: date | None = None
    for row in csv:
        if data_contabile is not None and data_contabile < row.data_contabile:
            error('%s < %s!', data_contabile, row.data_contabile)
            return False
    return True


def validate(fn: str) -> bool:
    info(fn)
    kv, csv = read_txt(fn)
    return all([validate_saldo(kv, csv), validate_dates(csv)])


def main() -> None:
    basicConfig(level=INFO, format='%(message)s')

    if not argv[1:]:
        error('uso: %s ACCUMULATOR...', argv[0])
        raise SystemExit

    for fn in argv[1:]:
        if not validate(fn):
            error('%s seems has some problems!', fn)
            raise SystemExit
