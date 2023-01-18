def sort_full_names(*args):
    sorted_dict = {}
    for item in args:
        _sub_dict = {}
        _spit_name = item.split()
        key = _spit_name[1][0]
        _sub_dict = sorted_dict.setdefault(key, _sub_dict)
        sub_dict_val = []
        sub_key = _spit_name[0][0]
        _sub_dict.setdefault(sub_key, sub_dict_val)
        if _spit_name[0][0] in _sub_dict.keys():
            _sub_dict[_spit_name[0][0]].append(item)

    return sorted_dict

a = sort_full_names('Иван Сергеев', 'Елена Авралинина', 'Ирина Крупина', 'Анна Рогова', 'Александр Каскин', 'Максим Савин')

sorted_tuple = sorted(a.items())

b = dict(sorted_tuple)

print(b)