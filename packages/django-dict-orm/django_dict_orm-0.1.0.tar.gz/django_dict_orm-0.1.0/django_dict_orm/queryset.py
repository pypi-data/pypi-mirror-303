import json



class QuerySet:
    def __init__(self, model):
        self.model = model
        self.filters = []
        self.file_path = f"data/{self.__class__.__name__.lower()}.json"

    def filter(self, **kwargs):
        self.filters.append(('filter', kwargs))
        return self

    def exclude(self, **kwargs):
        self.filters.append(('exclude', kwargs))
        return self

    def all(self):
        with open(self.file_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []

        for operation, kwargs in self.filters:
            if operation == 'filter':
                data = [record for record in data if all(record.get(key) == value for key, value in kwargs.items())]
            elif operation == 'exclude':
                data = [record for record in data if not all(record.get(key) == value for key, value in kwargs.items())]

        return data

    def first(self):
        all_records = self.all()
        return all_records[0] if all_records else None

    def delete(self):
        records_to_keep = []
        with open(self.file_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return 0

        for record in data:
            if not any(all(record.get(key) == value for key, value in filter_kwargs.items()) for _, filter_kwargs in
                       self.filters):
                records_to_keep.append(record)

        with open(self.file_path, "w") as file:
            json.dump(records_to_keep, file, indent=4)

        return len(data) - len(records_to_keep)
