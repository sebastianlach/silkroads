from unittest import TestCase

from web3 import Web3

from etherntities.services.etherum import EtherumService
from etherntities.solidity import SolidityContracts


class EtherumServiceTests(TestCase):

    def setUp(self):
        self.contracts = SolidityContracts('contracts/**/*.sol')
        self.w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        self.service = EtherumService(self.w3)

    def test_can_deploy_contract(self):
        contract = self.contracts.get('Entity')
        address = self.service.deploy_contract(contract, "my_key")
        self.assertEqual(len(address), 42)

    def test_can_get_contract(self):
        contract = self.contracts.get('Entity')
        address = self.service.deploy_contract(contract, "entity_key")
        entity = self.service.get_contract(contract, address)
        key = entity.functions.getPublicKey().call()
        self.assertEqual(key, "entity_key")

    def test_can_deploy_directory_contract(self):
        contract = self.contracts.get("Directory")
        address = self.service.deploy_contract(contract)
        directory = self.service.get_contract(contract, address)

    def test_can_increment_user_counter(self):
        contract = self.contracts.get("User")
        address = self.service.deploy_contract(contract, "user_key")
        user = self.service.get_contract(contract, address)
        key = user.functions.getPublicKey().call()
        self.assertEqual(key, "user_key")
        user.functions.incrementCounter().transact(
            transaction={'from': self.w3.eth.accounts[1]}
        )
        count = user.functions.getCount().call()
        self.assertEqual(count, 1)
