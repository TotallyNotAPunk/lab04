import lib
def test():
    array = [[0, 1, 3], [3, 4, 6], [5, 6, 7], [7, 8, 9], [1, 2, 9]]
    res = lib.findRepeats(array)
    check = False
    expected = {1, 3, 6, 7, 9}
    if expected == res:
        check = True
    return check