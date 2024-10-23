# coding: utf-8

import numpy as np
from chempy.util.parsing import formula_to_composition

from alloys_props.mendeleev_gw import database


__all__ = [
    'vec',
    'delta',
    'pauling_negativities',
    'entropy_of_mixing',
    'atomic_radius',
    'enthalpy_of_mixing',
]


def _total_moles(composition: dict) -> float:
    """
    composition: dict where the keys are atomic
    numbers of atoms in composition and the
    values are their respective concentrations
    """
    return np.sum([composition[z] for z in composition])


def vec(formula: str) -> float:
    """
    VEC is the valence electron concentration
    z: atomic number
    composition[z]: concentration of atom with z atomic number
    """
    composition = formula_to_composition(formula)
    total_moles = _total_moles(composition)
    return np.sum([composition[z] / total_moles * database[z]['vec'] for z in composition])


def delta(formula: str) -> float:
    """
    δ, parameter describing the atomic size mismatch
    or difference in a multi-component alloy system
    z: atomic number
    composition[z]: concentration of atom with z atomic number
    """
    composition = formula_to_composition(formula)
    total_moles = _total_moles(composition)
    raduis_avg = np.sum([composition[k] / total_moles * database[k]['atomic_radius'] for k in composition])
    return np.sqrt(np.sum([composition[z] / total_moles * (1 - database[z]['atomic_radius'] / raduis_avg)**2 for z in composition]))


def pauling_negativities(formula: str) -> float:
    """
    ΔX, Pauling negativities mismatch for multi-component alloy system
    z: atomic number
    composition[z]: concentration of atom with z atomic number
    """
    composition = formula_to_composition(formula)
    total_moles = _total_moles(composition)
    pauling_avg = np.sum([composition[k] / total_moles * database[k]['electronegativity'] for k in composition])
    return np.sqrt(np.sum([composition[k] / total_moles * (database[k]['electronegativity'] - pauling_avg)**2 for k in composition]))


def entropy_of_mixing(formula: str) -> float:
    """
    ΔSmix, The entropy of mixing of a multi-component
    alloy system calculated as follows
    R (= 8.314 JK−1mol−1) is the universal gas constant
    z: atomic number
    composition[z]: concentration of atom with z atomic number
    """
    R = 8.314
    composition = formula_to_composition(formula)
    total_moles = _total_moles(composition)
    return - R * np.sum([composition[z] / total_moles * np.log(composition[z] / total_moles) for z in composition])


def atomic_radius(formula: str) -> float:
    """
    r, the atomic radius of alloy
    z: atomic number
    composition[z]: concentration of atom with z atomic numbe
    """
    composition = formula_to_composition(formula)
    total_moles = _total_moles(composition)
    return np.sum([composition[z] / total_moles * database['atomic_radius'] for z in composition])


def enthalpy_of_mixing(formula: str) -> float:
    """
    ΔHmix, Enthalpy of mixing for a
    multi-component alloy system
    z: atomic number
    composition[z]: concentration of atom with z atomic number
    """
    return 0.0
