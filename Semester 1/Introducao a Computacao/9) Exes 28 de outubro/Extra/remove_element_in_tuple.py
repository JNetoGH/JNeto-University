def remove_element(t: tuple, remove: str) -> tuple:
    lista = []
    for element in t:
        if element != remove:
            lista.append(element)
    return tuple(lista)


print(remove_element(('A', 'A', 'B', 'C', 'A', 'C'), "A"))
