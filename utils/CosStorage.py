from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class CosStorage(Storage):
    def __init__(self):
        pass

    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        pass

    def url(self, name):
        pass

    def exists(self, name):
        pass

    def delete(self, name):
        pass

    def listdir(self, path):
        pass

    def size(self, name):
        pass
