from copy import deepcopy
from sbmlutils.modelcreator import creator
from models.utils.templates import MODEL_UNITS, UNITS
from models.utils.utils import read_data, create_compartment, create_species, create_reaction

data = read_data("kidney/data.xlsx")
mid = data["info"]["mid"][0]
model_units = deepcopy(MODEL_UNITS)
units = deepcopy(UNITS)

compartments = [create_compartment(instance) for _,instance in data["compartment"].iterrows()]
species = [create_species(instance) for _,instance in data["specie"].iterrows()]
reactions = [create_reaction(instance, data["parameter"]) for _, instance in data["reaction"].iterrows()]

ports = []


def create_model(target_dir):
    return creator.create_model(
        modules=['models.kidney.model_kidney'],
        target_dir=target_dir,
        create_report=True
    )

