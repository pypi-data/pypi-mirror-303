import os
import json
from . import models


def export(model, *args, **kwargs):
    """
    Export `model` as an atooms.f90.Interaction object, passing the
    remaining arguments to the Interaction constructor
    """
    try:
        from atooms.backends.f90 import Interaction
    except ImportError:
        print('atooms is not installed')
        raise

    if not hasattr(model, 'get'):
        if os.path.isfile(model) and model.endswith('json'):
            # This is a json file, we read it
            with open(model) as fh:
                model = json.load(fh)
        else:
            # This may be a string, so we look for the model in the
            # database and replace the string with the dictionary
            model = models.get(model)

    return Interaction(model, *args, **kwargs)


Interaction = export
