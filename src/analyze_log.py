def maria(name, order, maria_favorite):
    if name == 'maria':
        if order in maria_favorite:
            maria_favorite[order] += 1
        else:
            maria_favorite[order] = 1


def analyze_log(path_to_file):
    raise NotImplementedError
