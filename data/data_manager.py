class Dataset:

    def __init__(self):
        self.data_dict = {}

    def _create_id(self):
        return len(self.data_dict)

    def set_data_list(self, data_list):
        for data in data_list:
            id = self._create_id()
            self.data_dict[id] = data

    def get_data_dict(self):
        return self.data_dict

    def get_data(self, id):
        return self.data_dict[int(id)]