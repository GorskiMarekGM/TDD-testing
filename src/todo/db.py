class BasicDB:
    def __init__(self, path, _fileopener=open):
        self._path = path
        self._fileopener = _fileopener

    def load(self):
        with self._fileopener(self._path, "r", encoding="utf-8") as f:
            txt = f.read()
        return eval(txt)