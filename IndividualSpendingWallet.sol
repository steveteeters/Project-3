pragma solidity ^0.5.0;

contract IndividualWallet {
    address payable accountOne = 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2;
    address payable accountTwo = 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db;
    address public lastToWithdraw;
    uint public lastWithdrawlAmount;
    uint public contractBalance;

    function withdraw(uint amount, address payable recipient) public {
        require(recipient == accountOne || recipient == accountTwo, "You don't own this account!");
        require(contractBalance >= lastWithdrawlAmount, "Inufficient Funds!");
        if (lastToWithdraw != recipient) {
            lastToWithdraw = recipient;
        }

        recipient.transfer(amount);
        lastWithdrawlAmount = amount;
        contractBalance = address(this).balance;
    }

    function deposit() public payable {
        contractBalance = address(this).balance;    
    }

    function setAccounts(address payable account1, address payable account2) public{

        accountOne = account1;
        accountTwo = account2;
    }

    function() external payable {}

}   