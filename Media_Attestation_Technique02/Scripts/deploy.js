const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const MediaAttestation = await hre.ethers.getContractFactory("MediaAttestation");
  const mediaAttestation = await MediaAttestation.deploy("0xEASContractAddress");

  console.log("MediaAttestation contract deployed to:", mediaAttestation.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });