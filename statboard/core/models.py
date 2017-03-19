from json import loads, dumps
from django.db.models import Model, CharField, TextField


class Metric(Model):
    name = CharField(max_length=50, unique=True)
    data = TextField()

    def __str__(self):
        return self.name

    @property
    def data_dict(self):
        """
        docstring for json_data
        """
        return loads(self.data)

    def set_data(self, data_dict):
        """docstring for set_data"""
        self.data = dumps(data_dict)
        self.save()
