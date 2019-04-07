pragma solidity >=0.4.22 <0.6.0;


contract Spot {

    enum spotType { box, road }

    struct location {
        int latitude;
        int longitue;
    }

    location spot_location;

}
