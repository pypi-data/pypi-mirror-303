import gpolyencode


def encode(limits):
    """
    >>> import gpolyencode
    >>> encoder = gpolyencode.GPolyEncoder()
    >>> points = ((8.94328,52.29834), (8.93614,52.29767), (8.93301,52.29322), (8.93036,52.28938), (8.97475,52.27014),)
    >>> encoder.encode(points)
    {'points':'soe~Hovqu@dCrk@xZpR~VpOfwBmtG', 'levels':'PG@IP', 'zoomFactor':2, 'numLevels':18}
    """
    encoder = gpolyencode.GPolyEncoder()
    points = tuple([tuple([float(b) for b in a.split(',')]) for a in limits.split(' ')])
    return encoder.encode(points)


def encode_limits(sender, instance, **kwargs):
    encoded = encode(instance.limits)
    instance.encode_points = encoded['points']
    instance.encode_levels = encoded['levels']
    instance.encode_zoomfactor = encoded['zoomFactor']
    instance.encode_numlevels = encoded['numLevels']
    return 1
