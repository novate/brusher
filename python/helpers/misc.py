def eq(p, r):
    '''Check whether the proposed answer p is the same as the real answer.

    p:  proposed answer
    r:  real answer
    '''
    assert p == r, f'Proposed: {p}, Real: {r}.'