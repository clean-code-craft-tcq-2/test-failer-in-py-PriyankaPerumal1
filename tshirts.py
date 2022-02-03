
def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    else:
        return 'L'

def test_tshirt_size():
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size(38) == 'M')


test_tshirt_size()
print("All is well\n")
