from json import loads, dumps
from django.db.models import Model, CharField, TextField


class Metric(Model):
    name = CharField(max_length=50, unique=True)
    data_str = TextField()

    def __str__(self):
        return self.name

    @property
    def data(self):
        """
        get `data_str` as py dict
        """
        return loads(self.data_str)

    def set_data(self, data):
        """
        cast python dict `data` in str `data_str`
        """
        self.data_str = dumps(data)
        self.save()
