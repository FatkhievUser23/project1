def u_n(*args):
    u_set = set()

    for arg in args:
        if isinstance(arg, (int, float)):
            u_set.add(arg)

    return sorted(list(u_set))

in_arg = [1, '2', 'text', 42, None, None,None, 15, True, 1, 1.0]
r = u_n(*in_arg)
print(r)