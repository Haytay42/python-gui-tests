import random


def test_add_group(app):
    old_list = app.groups.get_group_list()
    list = app.groups.data_from_excel_file()
    random_group = random.choice(list)
    app.groups.add_new_group(random_group)
    new_list = app.groups.get_group_list()
    old_list.append(random_group)
    assert sorted(old_list) == sorted(new_list)