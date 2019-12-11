from copy import deepcopy

from sbmlutils.modelcreator import creator
from sbmlutils.factory import *
from sbmlutils.units import *
from sbmlutils.annotation.sbo import *
import pandas as pd
from models.utils.templates import MODEL_UNITS, UNITS

data = pd.read_excel(".data.xlsx", sheet_name=None, skiprows=[0], comment="#")


mid = data["info"]["mid"][0]
model_units = deepcopy(MODEL_UNITS)
units = deepcopy(UNITS)



compartments = [



    Compartment("Vli", 1.5, name="liver", sboTerm=SBO_PHYSICAL_COMPARTMENT,
                unit=UNIT_KIND_LITRE, port=True),
    Compartment("Vext", 1.0, name="extern", sboTerm=SBO_PHYSICAL_COMPARTMENT,
                unit=UNIT_KIND_LITRE, port=True),
]


species = [
    #extern
    Species("cod_ext", initialConcentration=0.0, name="codeine (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("ncod_ext", initialConcentration=0.0, name="norcodeine (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("c6g_ext", initialConcentration=0.0, name="codeine-6-glucuronide (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("mor_ext", initialConcentration=0.0, name="morphine (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("nmor_ext", initialConcentration=0.0, name="normorphine (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("m3g_ext", initialConcentration=0.0, name="morphine-3-glucuronide (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    Species("m6g_ext", initialConcentration=0.0, name="morphine-6-glucuronide (extern)",
            compartment="Vext", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True, port=True),

    #intern
    Species("cod", initialConcentration=0.0, name="codeine",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("mor", initialConcentration=0.0, name="morphine",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("ncod", initialConcentration=0.0, name="norcodeine",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("c6g", initialConcentration=0.0, name="codeine-6-glucuronide",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("nmor", initialConcentration=0.0, name="normorphine",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("m3g", initialConcentration=0.0, name="morphine-3-glucuronide",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),

    Species("m6g", initialConcentration=0.0, name="morphine-6-glucuronide",
            compartment="Vli", substanceUnit=UNIT_mmole, hasOnlySubstanceUnits=True),
]

transport_reactions_in =[
    Reaction(f"CODIM",
             equation=f"cod_ext <-> cod",
             sboTerm=SBO_TRANSPORT_REACTION,
             pars=[
                 Parameter(f"CODIM_Vmax",0.1, unit=UNIT_mmole_per_min),
                 Parameter(f"CODIM_Km", 1, unit=UNIT_mM),
             ],
             formula=(f"CODIM_Vmax*(cod_ext/Vext/(cod_ext/Vext+CODIM_Km))", UNIT_mmole_per_min))
]

transport_reactions_ex = [
        Reaction(f"MOREX",
                 equation=f"mor <-> mor_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"MOREX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"MOREX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"MOREX_Vmax*(mor/Vli/(mor/Vli + MOREX_Km))", UNIT_mmole_per_min)),
        Reaction(f"NCODEX",
                 equation=f"ncod <-> ncod_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"NCODEX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"NCODEX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"NCODEX_Vmax*(ncod/Vli/(ncod/Vli + NCODEX_Km))", UNIT_mmole_per_min)),

        Reaction(f"C6GEX",
                 equation=f"c6g <-> c6g_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"C6GEX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"C6GEX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"C6GEX_Vmax*(c6g/Vli/(c6g/Vli + C6GEX_Km))", UNIT_mmole_per_min)),
        Reaction(f"NMOREX",
                 equation=f"nmor <-> nmor_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"NMOREX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"NMOREX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"NMOREX_Vmax*(nmor/Vli/(nmor/Vli + NMOREX_Km))", UNIT_mmole_per_min)),
        Reaction(f"M3GEX",
                 equation=f"m3g <-> m3g_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"M3GEX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"M3GEX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"M3GEX_Vmax*(m3g/Vli/(m3g/Vli + M3GEX_Km))", UNIT_mmole_per_min)),

        Reaction(f"M6GEX",
                 equation=f"m6g <-> m6g_ext",
                 sboTerm=SBO_TRANSPORT_REACTION,
                 pars=[
                     Parameter(f"M6GEX_Vmax", 0.1,unit=UNIT_mmole_per_min),
                     Parameter(f"M6GEX_Km", 1.0, unit=UNIT_mM),
                 ],
                 formula=(f"M6GEX_Vmax*(m6g/Vli/(m6g/Vli + M6GEX_Km))", UNIT_mmole_per_min)),
]

# relations:
# 2*MOR_VMAX ~ NOCOD_Vmax
# MOR_KM ~ 3*NOCOD_KM
# M3G_VMAX ~ 3*M6G_VMAX
# M3G_VMAX ~ 3*M6G_VMAX

bio_reactions = [
    Reaction("COD_MOR", # O-demethylation
             equation="cod -> mor",
             sboTerm=SBO_BIOCHEMICAL_REACTION,
             pars = [
               Parameter(f"MOR_Vmax", 0.1, unit=UNIT_mmole_per_min), #my guess
               Parameter(f"MOR_Km", 1.079, unit=UNIT_mM), # [(1.079, 1.206, 1470), Shen2007] [(1.459, 3.127, 4.890, 6.165), Yue1997]
             ],
             formula=(f"MOR_Vmax*(cod/Vli/(cod/Vli + MOR_Km))", UNIT_mmole_per_min),
             ),
    Reaction("COD_NCOD", # N-demethylation
                 equation="cod -> ncod",
                 sboTerm=SBO_BIOCHEMICAL_REACTION,
                 pars=[
                     Parameter(f"NCOD_Vmax", 0.3, unit=UNIT_mmole_per_min), #my guess
                     Parameter(f"NCOD_Km", 0.8, unit=UNIT_mM), #[(2.680, 3.268, 0.276, 1.972),Yue1997]
                 ],
                 formula=(f"NCOD_Vmax*(cod/Vli/(cod/Vli + NCOD_Km))", UNIT_mmole_per_min),
                 ),
    Reaction("COD_C6G",
             equation="cod -> c6g",
             sboTerm=SBO_BIOCHEMICAL_REACTION,
             pars=[
                 Parameter(f"C6G_Vmax", 2.0, unit=UNIT_mmole_per_min),#  #my guess
                 Parameter(f"C6G_Km", 1.0, unit=UNIT_mM), # [(), Coffman1997], [(1.54,1.707,1.211,2.149), Ammon2000]
             ],
             formula=(f"C6G_Vmax*(cod/Vli/(cod/Vli + C6G_Km))", UNIT_mmole_per_min),
             ),

    Reaction("MOR_M3G",
             equation="mor -> m3g",
             sboTerm=SBO_BIOCHEMICAL_REACTION,
             pars=[
                 Parameter(f"M3G_Vmax",0.1, unit=UNIT_mmole_per_min), #my guess
                 Parameter(f"M3G_Km", 1.0, unit=UNIT_mM),
             ],
             formula=(f"M3G_Vmax*(mor/Vli/(mor/Vli + M3G_Km))", UNIT_mmole_per_min),
             ),

    Reaction("MOR_M6G",
             equation="mor -> m6g",
             sboTerm=SBO_BIOCHEMICAL_REACTION,
             pars=[
                 Parameter(f"M6G_Vmax", 0.1, unit=UNIT_mmole_per_min), #my guess
                 Parameter(f"M6G_Km", 1.0, unit=UNIT_mM),
             ],
             formula=(f"M6G_Vmax*(mor/Vli/(mor/Vli + M6G_Km))", UNIT_mmole_per_min),
             ),

    Reaction("MOR_NMOR",
             equation="mor -> nmor",
             sboTerm=SBO_BIOCHEMICAL_REACTION,
             pars=[
                 Parameter(f"NMOR_Vmax",0.1, unit=UNIT_mmole_per_min), #my guess
                 Parameter(f"NMOR_Km", 1.0, unit=UNIT_mM),
             ],
             formula=(f"NMOR_Vmax*(mor/Vli/(mor/Vli + NMOR_Km))", UNIT_mmole_per_min),
             ),

]
reactions = bio_reactions + transport_reactions_in + transport_reactions_ex

def create_model(target_dir):
    return creator.create_model(
        modules=['model_codeine'],
        target_dir=target_dir,
        create_report=True
    )

if __name__ == "__main__":
    create_model(target_dir=".")
