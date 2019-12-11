from sbmlutils.units import *

UNIT_DICT = {
    'kg': UNIT_kg,
    'm': UNIT_m,
    'm2': UNIT_m2,
    'm3': UNIT_m3,
    'mmol/l': UNIT_mM,
    'mmol': UNIT_mmole,
    'mol/min': UNIT_mole_per_min,
    'mmol/min': UNIT_mmole_per_min,
    'l': UNIT_KIND_LITRE

}

"""
  UNIT_mmole_per_s = Unit('mmole_per_s', [(UNIT_KIND_MOLE, 1, -3, 1.0), (UNIT_KIND_SECOND, -1.0)], port=True)
    UNIT_mole_per_s = Unit('mole_per_s', [(UNIT_KIND_MOLE, 1.0), (UNIT_KIND_SECOND, -1.0)], port=True)
    
    UNIT_s = Unit('s', [(UNIT_KIND_SECOND, 1.0)], port=True)
    UNIT_min = Unit('min', [(UNIT_KIND_SECOND, 1.0, 0, 60)], port=True)
    UNIT_hr = Unit('hr', [(UNIT_KIND_SECOND, 1.0, 0, 3600)], port=True)
    
    UNIT_per_s = Unit('per_s', [(UNIT_KIND_SECOND, -1.0)], port=True)
    UNIT_per_min = Unit('per_min', [(UNIT_KIND_SECOND, -1.0, 0, 60)], port=True)
    UNIT_per_hr = Unit('per_hr', [(UNIT_KIND_SECOND, -1.0, 0, 3600)], port=True)
    
    UNIT_mg = Unit('mg', [(UNIT_KIND_GRAM, 1.0, -3, 1.0)], port=True)
    UNIT_mg_per_hr = Unit('mg_per_hr', [(UNIT_KIND_GRAM, 1.0, -3, 1.0), (UNIT_KIND_SECOND, -1.0, 0, 3600)], port=True)
    
    UNIT_ml = Unit('ml', [(UNIT_KIND_LITRE, 1.0, -3, 1.0)], metaId='meta_ml', port=True)

"""
