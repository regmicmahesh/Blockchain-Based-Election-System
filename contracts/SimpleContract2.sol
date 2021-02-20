// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

abstract contract Root {
    address public self; // address of self

    //address public upper; // address of upperbranches

    function GetBalance() public virtual returns (uint256, uint256);
}

abstract contract Authority {
    address[] public branches; // addresses of branches

    // add a child to branches
    function RegisterInbranches(address newAddress) public virtual;

    // triggered on successful addition to branches
    event Register(address whom, address who, string Id);

    // triggered when distributing 
    event Distribution(uint ammount, uint total, address by);

    // this function will distribute ethers
    function Distribute(uint256 value) public {
        require(
            value * branches.length <= address(self).balance,
            "Insufficient balance"
        );

        for (uint256 i = 0; i < branches.length; ++i) {
            payable(branches[i]).transfer(value);
        }
        emit Distribution(value, value * branches.length, address(self));
    }

    // this function returs the balance of contract as well as the total balance of its branches
    function GetBalance()
        public
        view
        override
        returns (uint256 selfBalance, uint256 branchBalance)
    {
        uint256 total;
        for (uint256 i = 0; i < branches.length; ++i) {
            total += branches[i].balance;
        }
        return (address(this).balance, total);
    }

    // fuctions to allow contract to hold credits
    fallback() external payable {}

    receive() external payable {}
}

contract majorAuthority is Root, Authority {
    constructor() {
        self = msg.sender; // the person who deploys contract is the authority
    }

    function RegisterInbranches(address newAddress) public override {
        branches.push(newAddress);
        emit Register(newAddress, self, "E_authority");
    }
}

contract subAuthority is Root, Authority {
    constructor() public {
        self = address(this);
    }

    function RegisterInbranches(address newAddress) public override {
        branches.push(newAddress);
        emit Register(newAddress, self, "R_authority");
    }

}
