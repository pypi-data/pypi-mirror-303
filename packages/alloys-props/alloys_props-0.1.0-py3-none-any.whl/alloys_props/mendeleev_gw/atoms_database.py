# coding: utf-8

from mendeleev import element

from alloys_props.settings import MIN_ATOMIC_NUMBER, MAX_ATOMIC_NUMBER


__all__ = [
    'DB',
]


class DB:
    """
    Build a database with mendeleev elements proporties
    """
    _db: dict

    def __init__(self):
        self._db: dict = {}
        for atomic_number in range(MIN_ATOMIC_NUMBER, MAX_ATOMIC_NUMBER):
            atom = element(atomic_number)
            atom_properties = {
                'symbol': atom.symbol,
                'atomic_radius': atom.atomic_radius,
                'melting_point': atom.melting_point,
                'electronegativity': atom.electronegativity(),
                'vec': atom.nvalence(),
            }
            self._db[atomic_number] = atom_properties

    @property
    def db(self) -> dict:
        return self._db
