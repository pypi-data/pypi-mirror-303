from . import _schemas

schemas = {1: _schemas.m1, 2: _schemas.m2}

# Model schema helpers

def schema_version(model):
    """
    Return the schema version of the model
    """
    from jsonschema import ValidationError

    # Validate model against either version
    valid = []
    for schema_version in [1, 2]:
        try:
            _validate_model(model, schema_version)
            valid.append(schema_version)
        except ValidationError as e:
            pass
    # Return the schema id
    if len(valid) == 1:
        return valid[0]
    elif len(valid) == 0:
        raise ValidationError(f'invalid model {model}')
    else:
        raise RuntimeError(f'model {model} is valid for multiple schemas, this should not happen')

def _validate_model(model, schema_version=1):
    from jsonschema import validate
    validate(instance=model, schema=schemas[schema_version])

def _convert(model, new_schema_version):
    """
    Convert model to schema `schema_version`. Do nothing is schema version is already the requested one
    """
    if schema_version(model) == new_schema_version:
        return model
    elif schema_version(model) == 1 and new_schema_version == 2:
        return _upgrade_1_to_2(model)
    else:
        raise ValueError('cannot handle this conversion')

def _upgrade_1_to_2(model):
    """Convert from schema version 1 to 2"""
    new_model = {}
    # Optional
    new_model['metadata'] = model['metadata']
    new_model["potential"] = []
    for potential in model["potential"]:
        new_potential = {}
        new_potential["type"] = potential["type"]
        new_potential["parameters"] = {}
        db = {}
        for key in potential["parameters"]:
            db[key] = {}
            nsp = len(potential["parameters"][key])
            for i in range(nsp):
                for j in range(nsp):
                    if j < i:
                        continue
                    pair = f'{i+1}-{j+1}'
                    db[key][pair] = potential["parameters"][key][i][j]
        last_key = key
        for pair in db[last_key].keys():
            new_potential["parameters"][pair] = {key: db[key][pair] for key in db.keys()}
        new_model["potential"].append(new_potential)

    new_cutoffs = []
    for cutoff in model["cutoff"]:
        new_cutoff = {}
        new_cutoff["type"] = cutoff["type"]
        new_cutoff["parameters"] = {}
        db = {}
        for key in cutoff["parameters"]:
            db[key] = {}
            nsp = len(cutoff["parameters"][key])
            for i in range(nsp):
                for j in range(nsp):
                    if j < i:
                        continue
                    pair = f'{i+1}-{j+1}'
                    db[key][pair] = cutoff["parameters"][key][i][j]
        last_key = key
        for pair in db[last_key].keys():
            new_cutoff["parameters"][pair] = {key: db[key][pair] for key in db.keys()}
        new_cutoffs.append(new_cutoff)
    for i, new_cutoff in enumerate(new_cutoffs):
        new_model["potential"][i]["cutoff"] = new_cutoff
    return new_model
