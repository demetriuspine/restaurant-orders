import csv


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
    if 'csv' in path_to_file:
        burger_orders = 0
        maria_favorite = dict()
        joao_visit = set()
        joao_orders = set()
        days = set()
        menu = set()

        try:
            with open(path_to_file) as file:
                file = csv.reader(file, delimiter=",")
                for name, order, day in file:
                    maria(name, order, maria_favorite)
                    joao(name, order, day, days, joao_visit, menu, joao_orders)
                    burger_orders = arnaldo(name, order, burger_orders)

            with open('data/mkt_campaign.txt', 'w') as file:
                file.writelines([
                    f"{max(maria_favorite, key=maria_favorite.get)}\n",
                    f"{burger_orders}\n",
                    f"{menu - joao_orders}\n",
                    f"{days - joao_visit}",
                ])

        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
