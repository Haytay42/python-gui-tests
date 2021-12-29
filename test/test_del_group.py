
def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    app.groups.del_group()
    new_list = app.groups.get_group_list()
    old_list.remove("my group")
    assert sorted(old_list) == sorted(new_list)