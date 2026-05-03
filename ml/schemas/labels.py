"""ClassLabel IntEnum for 9-class meningitis/encephalitis differential diagnosis.

Citations per class:
- PAM: CDC PAM 2017 case definition; MMWR 2025 (PMID 40146665)
- Bacterial: IDSA Tunkel et al. 2004 (doi:10.1086/425368)
- Viral: IDSA Tunkel et al. 2008 (doi:10.1086/589747)
- Tuberculous: Marais et al. Lancet Infect Dis 2010 (doi:10.1016/S1473-3099(10)70138-9)
- Cryptococcal/Fungal: NIH OI guidelines; AMBITION-cm trial
- GAE (Acanthamoeba/Balamuthia): Bravo PMC8760460; Gotuzzo et al. OFID 2026 (doi:10.1093/ofid/ofaf695.345)
- Neurocysticercosis: Del Brutto et al. J Neurol Sci 2017 (PMID 28017213); Allen et al. Pathogens 2023 (doi:10.3390/pathogens12111313)
- Cerebral malaria/severe arboviral: WHO 2023 Malaria Guidelines; Guzman & Martinez Viruses 2024
- Non-infectious mimics: Hinchey NEJM 1996 (PRES original); Graus et al. Lancet Neurol 2016 (NMDAR)
"""
from __future__ import annotations
from enum import IntEnum


class ClassLabel(IntEnum):
    """9-class differential diagnosis ground-truth labels.

    Class assignments are mutually exclusive at the per-vignette level.
    See SCHEMA_README.md for full diagnostic criteria mapping.
    """
    PAM = 1
    BACTERIAL = 2
    VIRAL = 3
    TUBERCULOUS = 4
    CRYPTOCOCCAL_FUNGAL = 5
    GAE = 6
    NEUROCYSTICERCOSIS = 7
    CEREBRAL_MALARIA_OR_SEVERE_ARBO = 8
    NON_INFECTIOUS_MIMIC = 9


__all__ = ["ClassLabel"]
