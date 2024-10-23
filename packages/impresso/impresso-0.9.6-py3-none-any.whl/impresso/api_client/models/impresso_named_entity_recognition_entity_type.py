from enum import Enum
from typing import Literal


class ImpressoNamedEntityRecognitionEntityType(str, Enum):
    COMP_DEMONYM = "comp.demonym"
    COMP_FUNCTION = "comp.function"
    COMP_NAME = "comp.name"
    COMP_QUALIFIER = "comp.qualifier"
    COMP_TITLE = "comp.title"
    LOC = "loc"
    LOC_ADD_ELEC = "loc.add.elec"
    LOC_ADD_PHYS = "loc.add.phys"
    LOC_ADM_NAT = "loc.adm.nat"
    LOC_ADM_REG = "loc.adm.reg"
    LOC_ADM_SUP = "loc.adm.sup"
    LOC_ADM_TOWN = "loc.adm.town"
    LOC_FAC = "loc.fac"
    LOC_ORO = "loc.oro"
    LOC_PHYS_ASTRO = "loc.phys.astro"
    LOC_PHYS_GEO = "loc.phys.geo"
    LOC_PHYS_HYDRO = "loc.phys.hydro"
    LOC_UNK = "loc.unk"
    ORG = "org"
    ORG_ADM = "org.adm"
    ORG_ENT = "org.ent"
    ORG_ENT_PRESSAGENCY = "org.ent.pressagency"
    PERS = "pers"
    PERS_COLL = "pers.coll"
    PERS_IND = "pers.ind"
    PERS_IND_ARTICLEAUTHOR = "pers.ind.articleauthor"
    PROD = "prod"
    PROD_DOCTR = "prod.doctr"
    PROD_MEDIA = "prod.media"
    TIME = "time"
    TIME_DATE_ABS = "time.date.abs"
    TIME_HOUR_ABS = "time.hour.abs"

    def __str__(self) -> str:
        return str(self.value)


ImpressoNamedEntityRecognitionEntityTypeLiteral = Literal[
    "comp.demonym",
    "comp.function",
    "comp.name",
    "comp.qualifier",
    "comp.title",
    "loc",
    "loc.add.elec",
    "loc.add.phys",
    "loc.adm.nat",
    "loc.adm.reg",
    "loc.adm.sup",
    "loc.adm.town",
    "loc.fac",
    "loc.oro",
    "loc.phys.astro",
    "loc.phys.geo",
    "loc.phys.hydro",
    "loc.unk",
    "org",
    "org.adm",
    "org.ent",
    "org.ent.pressagency",
    "pers",
    "pers.coll",
    "pers.ind",
    "pers.ind.articleauthor",
    "prod",
    "prod.doctr",
    "prod.media",
    "time",
    "time.date.abs",
    "time.hour.abs",
]
