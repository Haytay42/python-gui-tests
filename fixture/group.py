import openpyxl


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def open_delete_group_form(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group_form = self.app.application.window(title="Delete group")
        self.delete_group_form.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def del_group(self, name):
        self.open_group_editor()
        tree = self.group_editor['TreeView']
        tree.GetItem([u'Contact groups', u'%s' % name]).Click()
        self.open_delete_group_form()
        self.delete_group_form.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def data_from_excel_file(self):
        book = openpyxl.open("C:\\Users\\Haytay\\PycharmProjects\\python-gui-tests\\groups.xlsx", read_only=True)
        sheet = book.active
        list = []
        for row in range(1, 11):
            group = sheet[row][0].value
            list.append(group)
        return list



