// const SimpleContract = artifacts.require("SimpleContract");
// const Authority = artifacts.require("Authority");
const majorAuthority = artifacts.require("majorAuthority");
// const Root = artifacts.require("Root");
const subAuthority = artifacts.require("subAuthority");

module.exports = function (deployer) {
  // deployer.deploy(SimpleContract);
  // deployer.deploy(Authority);
  deployer.deploy(majorAuthority);
  // deployer.deploy(Root);
  deployer.deploy(subAuthority);
};

// "0x93B3715C85A9b5EE87CaD68D0f5d2EdA0b44C101"