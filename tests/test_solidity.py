from unittest import TestCase

from etherntities.solidity import SolidityContracts


class SolidityContractsTests(TestCase):

    def test_can_compile_contracts(self):
        contracts = SolidityContracts('contracts/**/*.sol')
        contract = contracts.get('Entity')
        self.assertIn('abi', contract)
        self.assertIn('bin', contract)
