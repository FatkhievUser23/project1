def fio(person_info):
    f_name = person_info.get('Имя', '')
    l_name = person_info.get('Фамилия', '')
    m_name = person_info.get('Отчество', '')

    if l_name and f_name and m_name:
        return f"{l_name} {f_name} {m_name}"
    elif l_name and f_name:
        return f"{l_name} {f_name}"
    elif l_name and m_name:
        return f"{l_name} {m_name}"
    elif l_name and f_name:
        return f"{l_name} {f_name}"
    elif f_name and m_name:
        return f"{f_name} {m_name}"
    elif l_name:
        return f"{l_name}"
    elif f_name:
        return f"{f_name}"
    elif m_name:
        return f"{m_name}"
    else:
        'Нет информаций'


fioo = {'f_name': 'Динар'}
r = fio(fioo)
print(r)