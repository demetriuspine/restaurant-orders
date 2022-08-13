def maria(name, order, maria_favorite):
    if name == 'maria':
        if order in maria_favorite:
            maria_favorite[order] += 1
        else:
            maria_favorite[order] = 1


def arnaldo(name, order, burger_orders):
    if name == 'arnaldo' and order == 'hamburguer':
        burger_orders += 1
    return burger_orders


def joao(name, order, day, days, joao_visit, menu, joao_orders):
    menu.add(order)
    days.add(day)
    if name == 'joao':
        joao_orders.add(order)
        joao_visit.add(day)

def analyze_log(path_to_file):
    raise NotImplementedError
