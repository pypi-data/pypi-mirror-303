import json
import os


class QuerySet:
    def __init__(self, model):
        self.model = model
        self.filters = []
        self.file_path = f"data/{self.model.__name__.lower()}.json"

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
        return self.all()[0] if self.all() else None

    def count(self):
        return len(self.all())

    def delete(self):
        all_data = self.all()
        with open(self.file_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return 0

        records_to_keep = [record for record in data if record not in all_data]

        with open(self.file_path, "w") as file:
            json.dump(records_to_keep, file, indent=4)

        return len(data) - len(records_to_keep)

    def get_or_create(self, **kwargs):
        instance = self.filter(**kwargs).first()
        if instance:
            return instance, False
        else:
            instance = self.model(**kwargs)
            instance.save()
            return instance, True
