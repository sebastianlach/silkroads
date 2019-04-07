pragma solidity >=0.4.22 <0.6.0;
import "./Entity.sol";


contract User is Entity {

    event CounterIncrementedEvent(int count);
    event CounterDecrementedEvent(int count);

    int private count = 0;


    // this runs when the contract is executed
    constructor(string memory _pgp) Entity(_pgp) public {
        count = 0;
    }


    function incrementCounter() public {
        count += 1;
        emit CounterIncrementedEvent(count);
    }


    function decrementCounter() public {
        count -= 1;
        emit CounterDecrementedEvent(count);
    }


    function getCount() public view returns (int) {
        return count;
    }

}
