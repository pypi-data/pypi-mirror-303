from pickle import dump, load

import nicely


class Dico(dict):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            value = self[item] = Dico()
            return value

    def __getattr__(self, attr):
        if attr.startswith('_'):
            return super().__getattr__(attr)
        else:
            return self[attr]

    def __setattr__(self, attr, val):
        if attr.startswith('_'):
            super().__setattr__(attr, val)
        else:
            if isinstance(val, dict) and not isinstance(val, Dico):
                val = Dico(val)
            self[attr] = val

    def __getstate__(self):
        return dict(self.items())

    def dump(self, path):
        items = dict(self)
        with open(path, 'wb') as out:
            dump(items, out)

    def load(self, path):
        with open(path, 'rb') as inp:
            items = load(inp)
        self.update(items)

    def __str__(self):
        return nicely.format(self)
