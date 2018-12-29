from glob import iglob

from solc import compile_files


class SolidityContracts(object):
    """
    Solidity contracts manager.
    """

    def __init__(self, pattern):
        self._files = iglob(pattern, recursive=True)
        self._contracts = self.compile()

    def compile(self):
        return dict([
            (index.split(':')[1], value)
            for index, value in compile_files(self._files).items()
        ])

    def get(self, name):
        return self._contracts.get(name, None)
