class Mapper:
    def __init__(self, path_map: dict):
        self.path_map = path_map

    def get_xpath(self, key):
        if key in self.path_map:
            return self.path_map[key]
        else:
            print(f'Xpath for key "{key}" was not found.')
