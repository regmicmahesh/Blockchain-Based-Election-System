const fs = require("fs");
const Web3 = require("web3");

let web3 = new Web3("http://localhost:7545");

let accounts = [];

let majorAuthority, subAuthority;


class Manager{
    constructor(accountAddr, contract){
        this.accountAddr = accountAddr;
        this.contract = contract;
    }
}


async function initContract(jsonfile, accountAddr){

    let rawData = fs.readFileSync(jsonfile);
    let contractData = JSON.parse(rawData);
    const contractABI = contractData.abi;
    const contractBC = contractData.bytecode;
    let contract = new web3.eth.Contract(contractABI);
    contract = await contract.deploy({ data: contractBC }).send({ from: accountAddr ,  gas: 1500000, gasPrice: '30'});
    return contract;
}

async function getBalance(contract){
    balance = await contract.methods.GetBalance().call();
    return balance;
}

const towei = web3.utils.toWei;

async function distributeBalance(contractManager, value, unit="ether"){

    if(unit !== "wei"){
            value = towei(value.toString())
    }
    await contractManager.contract.methods.Distribute(value.toString()).send({from: contractManager.accountAddr});

}

async function sendBalance(from , to, value, unit="ether"){

    if(unit !== "wei"){
        value = towei(value.toString())
    }
    await web3.eth.sendTransaction({from: from, to: to, value: value});
}

async function registerBranch(contractManager, branchAddr){
    await contractManager.contract.methods.RegisterInbranches(branchAddr).send({from: contractManager.accountAddr});
}

async function getBranch(contract, idx){
    return (await contract.methods.branches(idx).call())
}

let majorAuthorityManager;
let subAuthorityManager;

async function init(){

    accounts = await web3.eth.getAccounts();

    

    majorAuthority = await initContract("majorAuthority.json", accounts[0]);
    subAuthority = await initContract("subAuthority.json", accounts[1]);    
    //TODO: Make multiple regions <- subauthority

   majorAuthorityManager = new Manager(accounts[0], majorAuthority);
   subAuthorityManager = new Manager(accounts[1], subAuthority);

}



init();