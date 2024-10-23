try:
    import rumd

except ImportError:
    # Dummy classes for testing
    class _Potential:
        def __init__(self, cutoff_method, **kwargs):
            self.cutoff_method = cutoff_method
            self.__dict__.update(kwargs)
            self.params = {}

        def SetParams(self, i, j, **params):
            self.params[(i, j)] = params

    class _Cutoff:
        def __init__(self, cutoff):
            self.cutoff = cutoff

    class rumd:
        ShiftedForce = _Cutoff
        ShiftedPotential = _Cutoff
        Pot_LJ_12_6 = _Potential
        Pot_IPL_12 = _Potential
        Pot_IPL_n = _Potential
        Pot_Gauss = _Potential


_extra = {'inverse_power': {'n': 'exponent'}}

# TODO: better cut_shift_linear (ad alias)
_map = {
    'cut_shift': rumd.ShiftedPotential,
    'cubic_spline': rumd.ShiftedForce,  # raise WARNING
    'linear_cut_shift': rumd.ShiftedForce,
    'quadratic_cut_shift': rumd.ShiftedForce,  # raise WARNING
    'gaussian': rumd.Pot_Gauss,
    'lennard_jones': rumd.Pot_LJ_12_6,
    # 'inverse_power': rumd.Pot_IPL_12,  # only if exponent 12
    'inverse_power': rumd.Pot_IPL_n
}

_warn = ['cubic_spline', 'quadratic_cut_shift']

# def potential(model):
def export(model):
    """Export model as an array of RUMD potentials"""
    from . import models
    if not hasattr(model, 'get'):
        # This may be a string, so we look for the model in the
        # models database and replace the string with the dictionary
        model = models.get(model, schema_version=2)
    if models.schema_version(model) == 2:
        return _potential_v2(model)
    else:
        raise ValueError('unsupported schema for model')

def _potential_v1(model):
    # At this stage we expect a model dictionary
    assert len(model.get('potential')) == 1
    assert len(model.get('cutoff')) == 1

    n_potentials = len(model.get('potential'))
    potentials = []
    for i in range(n_potentials):
        potential = model.get('potential')[i].get('type')
        potential_parameters = model.get('potential')[i].get('parameters')
        cutoff = model.get('cutoff')[i].get('type')
        cutoff_parameters = model.get('cutoff')[i].get('parameters')

        if potential not in _map:
            raise ValueError('not available {}'.format(potential))
        if cutoff not in _map:
            raise ValueError('not available {}'.format(cutoff))
        if cutoff in _warn:
            import warnings
            warnings.warn("WARNING: incompatible cutoff {} replaced with RUMD cutoff 2 {}".format(cutoff, _map[cutoff]))

        # Some parameters go in the potential constructor
        params = {}
        params['cutoff_method'] = _map[cutoff]
        if potential in _extra:
            for entry in _extra[potential]:
                name = _extra[potential][entry]
                params[entry] = potential_parameters[name]
        pot = _map[potential](**params)

        # To guess the number of species,
        # find the first key that has a list of parameters
        for key in potential_parameters:
            try:
                nsp = len(potential_parameters[key])
                break
            except TypeError:
                continue

        # Loop over species pairs
        for i in range(nsp):
            for j in range(nsp):
                params = {}
                for entry in potential_parameters:
                    Entry = entry.capitalize()
                    # Ignore parameters that entered in the constructor
                    if potential in _extra and entry in _extra[potential].values():
                        continue
                    params[Entry] = potential_parameters[entry][i][j]
                # The input cutoff distance must be divided by sigma for most RUMD potentials
                if 'rcut' in cutoff_parameters:
                    params['Rcut'] = cutoff_parameters["rcut"][i][j] / cutoff_parameters["sigma"][i][j]
                else:
                    # cubic spline has rspl
                    params['Rcut'] = cutoff_parameters["rspl"][i][j] / cutoff_parameters["sigma"][i][j]
                pot.SetParams(i, j, **params)
        potentials.append(pot)

    return potentials

def _potential_v2(model):
    n_potentials = len(model.get('potential'))
    potentials = []
    for i in range(n_potentials):
        potential = model.get('potential')[i].get('type')
        potential_parameters = model.get('potential')[i].get('parameters')
        cutoff = model.get('potential')[i].get('cutoff').get('type')
        cutoff_parameters = model.get('potential')[i].get('cutoff').get('parameters')

        # TODO: refactor
        if potential not in _map:
            raise ValueError('not available {}'.format(potential))
        if cutoff not in _map:
            raise ValueError('not available {}'.format(cutoff))
        if cutoff in _warn:
            import warnings
            warnings.warn("WARNING: incompatible cutoff {} replaced with RUMD cutoff 2 {}".format(cutoff, _map[cutoff]))

        species = []
        first_pair = None
        for pair in potential_parameters:
            if first_pair is None:
                first_pair = pair
            species.append(pair.split('-')[0])
            species.append(pair.split('-')[1])
        species = sorted(set(species))
        nsp = len(species)

        # Some parameters go in the potential constructor
        params = {}
        params['cutoff_method'] = _map[cutoff]
        if potential in _extra:
            for entry in _extra[potential]:
                name = _extra[potential][entry]
                params[entry] = potential_parameters[first_pair][name]
        pot = _map[potential](**params)

        # Loop over species pairs
        for pair in potential_parameters:
            a, b = pair.split('-')
            i, j = species.index(a), species.index(b)
            params = {}
            for entry in potential_parameters[pair]:
                Entry = entry.capitalize()
                # Ignore parameters that entered in the constructor
                if potential in _extra and entry in _extra[potential].values():
                    continue
                params[Entry] = potential_parameters[pair][entry]
            # cubic spline has rspl
            params['Rcut'] = cutoff_parameters[pair]["rcut"] / potential_parameters[pair]["sigma"]
            pot.SetParams(i, j, **params)
        potentials.append(pot)
    return potentials
