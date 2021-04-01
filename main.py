def greaterThan(x, y):
    if abs(x) > abs(y):
        return True
    else:
        return False

print(greaterThan(10, 8))

def lessThan(x, y):
    if abs(x) < abs(y):
        return True
    else:
        return False

print(lessThan(8, 9))

def equalTo(x, y):
    if abs(x) == abs(y):
        return True
    else:
        return False

print(equalTo(6, 7))

def greaterOrEqual(x, y):
    if abs(x) >= abs(y):
        return True
    else:
        return False

print(greaterOrEqual(14, 16))

def lessOrEqual(x, y):
    if abs(x) <= abs(y):
        return True
    else:
        return False

print(lessOrEqual(30, 16))