#"initial" points out to the initial unit, and "final" points out to the desired unit. "val" is the value without the unit.
def unit_conversion(initial, final, val):
    metric_prefixes = {
        "giga": 10**9,
        "mega": 10**6,
        "kilo": 10**3,
        "mili": 10**-3,
        "micro": 10**-6
    }
    return val