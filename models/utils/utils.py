from copy import deepcopy
import pandas as pd
from sbmlutils.factory import Compartment, Species, Reaction, Parameter

from models.utils.units import UNIT_DICT


def read_data(path):
    data_sheets = pd.read_excel(path, sheet_name=None, skiprows=[0], comment="#")
    result = {}
    for key, df in data_sheets.items():
        header = [column for column in df.columns if "Unnamed" not in str(column)]
        result[key] = df[header]
    return result

def _update_dict(d):
    updated_d = deepcopy(d)
    if isinstance(updated_d, pd.Series):
        updated_d = updated_d.to_dict()
    if "unit" in d:
        updated_d["unit"] = UNIT_DICT[d["unit"]]

    if "hasOnlySubstanceUnits" in d:
        updated_d["hasOnlySubstanceUnits"] = bool(d["hasOnlySubstanceUnits"])

    if "port" in d:
        updated_d["port"] = bool(d["port"])

    return updated_d


def create_compartment(data):
    return Compartment(**_update_dict(data))

def create_parameter(data):
    data.pop("reaction")
    return Parameter(**_update_dict(data))

def create_species(data):
    return Species(**_update_dict(data))


def create_reaction(data, parameter):

    data_updated = {k:v for k, v in data.items() if k not in ["formula_unit", "formula"]}
    # add parameters
    this_pars = parameter[parameter["reaction"] == data["sid"]]
    data_updated["pars"] = [create_parameter(par) for _, par in this_pars.iterrows()]
    data_updated["formula"] = (data["formula"], data["formula_unit"])

    return Reaction(**_update_dict(data_updated))
