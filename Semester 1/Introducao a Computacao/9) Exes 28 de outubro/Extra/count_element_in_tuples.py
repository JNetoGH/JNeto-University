def elements_int_tuple(t: tuple) -> str:
    tested = []
    msg = ""
    for element in t:
        if element not in tested:
            tested.append(element)
            msg += f"{element}:{t.count(element)}  "
    return msg


print(elements_int_tuple(('A', 'A', 'B', 'C', 'A', 'C')))
