pragma solidity >=0.4.22 <0.6.0;


contract Entity {

    // define variable owner of the type address
    address owner;

    // entity pgp
    string pgp;


    // executed at initialization, sets the owner of the contract
    constructor(string memory _pgp) public {
        owner = msg.sender;
        pgp = _pgp;
    }


    // get public key of entity
    function getPublicKey() public view returns (string memory) {
        return pgp;
    }


    // to recover the funds on the contract
    function kill() public {
        if (msg.sender == owner) {
            selfdestruct(msg.sender);
        }
    }

}
