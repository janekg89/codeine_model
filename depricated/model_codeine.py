from collections import namedtuple
from pint import UnitRegistry
ureg = UnitRegistry()


#####################################################################################
# hepatic CYP enzyme abundance [pmol/mg]
# hepatic CYP abundance is from Achour et al., 2014
V = namedtuple("Value","mean cv min max unit")
protein_expression = {
    "CYP2D6": V(mean=12.6, cv=74.4, min=0.4, max=38, unit="pmol/mg"), # "amount of cyp2d6 per mg of liver tissue"
    "CYP3A4": V(mean=93, cv=81, min=18.6, max=601, unit ="pmol/mg"),
}

whole_liver_amount_cyp2d6 = ureg("1.5kg")*0.7*protein_expression["CYP2D6"].mean* ureg(protein_expression["CYP2D6"].unit) # 0.7 because 70% of the tissue in the liver a hepatocytes (not sue if correct cause probe might not only contain hepatocytes)

codeine_to_c6g = {
    # this reaction is
    "KM":  V(mean=2.21, cv="na", min="na", max="na", unit="mM"), # "millimol/liter"
    "Vmax":V(mean=0.54, cv="na", min="na", max="na", unit="nmol/mg/min"),

}
codeine_to_c6g["Vmax"].mean*ureg(codeine_to_c6g["Vmax"].unit)
norcodeine = {}
c6g = {}
morphine = {}
normorphine = {}
m3g = {}
m6g = {}
