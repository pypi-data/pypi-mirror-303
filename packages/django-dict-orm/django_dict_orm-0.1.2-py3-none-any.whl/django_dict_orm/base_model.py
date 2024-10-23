import json
import os
from django_dict_orm.fields import Field
from django_dict_orm.queryset import QuerySet


class DjangoDictMeta(type):
    def __new__(mcs, name, bases, attrs):
        fields = {key: value for key, value in attrs.items() if isinstance(value, Field)}
        cls = super().__new__(mcs, name, bases, attrs)
        cls._fields = fields
        return cls


class DjangoDict(metaclass=DjangoDictMeta):
    def __init__(self, **kwargs):
        self.pk = kwargs.get("id", None)  # Primary Key management
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name, field.get_default())
            field.validate(value)
            setattr(self, field_name, value)

    def save(self):
        file_path = f"data/{self.__class__.__name__.lower()}.json"
        directory = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        data = self.to_dict()

        # Load existing data from JSON
        existing_data = []  # Initialize existing_data here
        try:
            with open(file_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []  # Reset to empty list on JSON error
        except FileNotFoundError:
            existing_data = []  # Reset to empty list if file not found

        # Manage the primary key (pk)
        if self.pk is None:  # If no pk, assign a new one
            self.pk = max([obj['id'] for obj in existing_data], default=0) + 1
            data['id'] = self.pk
            existing_data.append(data)
        else:
            for i, record in enumerate(existing_data):
                if record['id'] == self.pk:
                    existing_data[i] = data  # Update existing record
                    break
            else:
                existing_data.append(data)  # Add new record if pk not found

        # Write back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)

    def to_dict(self):
        return {field_name: getattr(self, field_name) for field_name in self._fields}

    @classmethod
    def objects(cls):
        return QuerySet(cls)
