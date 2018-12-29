class EtherumService(object):

    def __init__(self, w3):
        self._w3 = w3

    def deploy_contract(self, contract_interface, *args, **kwargs):
        """
        Deploy contracts and return adddress.
        """
        # instantiate and deploy contract
        contract = self._w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']
        )

        # submit the transaction that deploys the contract
        tx_hash = contract.constructor(*args, **kwargs).transact(
            transaction={'from': self._w3.eth.accounts[1]}
        )

        # get tx receipt to get contract address
        tx_receipt = self._w3.eth.getTransactionReceipt(tx_hash)
        return tx_receipt['contractAddress']

    def get_contract(self, contract_interface, address):
        return self._w3.eth.contract(
            address=address,
            abi=contract_interface['abi'],
        )
