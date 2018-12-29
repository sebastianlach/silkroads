pragma solidity >=0.4.22 <0.5.0;


contract Quorum {

    // events
    event QuorumNotificationEvent(string message);


    function notify() public {
        emit QuorumNotificationEvent("Hello world");
    }

}
