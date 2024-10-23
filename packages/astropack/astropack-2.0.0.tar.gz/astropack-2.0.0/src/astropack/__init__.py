from . import preprocess
from . import tuning
from . import models
from . import evaluation

# Sets of filters and corrections used
FILTERS = {
    "JPLUS": [
        "uJAVA",
        "J0378",
        "J0395",
        "J0410",
        "J0430",
        "gSDSS",
        "J0515",
        "rSDSS",
        "J0660",
        "iSDSS",
        "J0861",
        "zSDSS",
    ],
    "WISE": ["W1", "W2", "J", "H", "K"],
    "GALEX": ["NUVmag"],
    "GAIA": ["G", "BP", "RP"],
}

ERRORS = {"JPLUS": [f"{x}_err" for x in FILTERS["JPLUS"]]}

CORRECTIONS = {"JPLUS": [f"Ax_{x}" for x in FILTERS["JPLUS"]]}
