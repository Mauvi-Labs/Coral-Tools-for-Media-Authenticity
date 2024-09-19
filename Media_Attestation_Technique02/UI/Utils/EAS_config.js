import { EAS } from "@ethereum-attestation-service/eas-sdk";
import { ethers } from "ethers";

const EASContractAddress = '0xYourEASContractAddress';

export const easConfig = async () => {
  const provider = new ethers.providers.Web3Provider(window.ethereum);
  const eas = new EAS(EASContractAddress);
  eas.connect(provider);

  return eas;
};
