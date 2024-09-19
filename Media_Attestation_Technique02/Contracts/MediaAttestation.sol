// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@ethereum-attestation-service/eas-contracts/contracts/IEAS.sol";

contract MediaAttestation is Ownable {
    IEAS public eas;

    // Store attestations by media hash
    mapping(bytes32 => address) public attestations;

    constructor(address _easAddress) {
        eas = IEAS(_easAddress);
    }

    // Attest a media file (hash of media content)
    function attestMedia(bytes32 mediaHash) external {
        require(attestations[mediaHash] == address(0), "Media already attested");
        attestations[mediaHash] = msg.sender;
        eas.attest(msg.sender, mediaHash);
    }

    // Verify the attestation of a media file
    function verifyMedia(bytes32 mediaHash) external view returns (bool) {
        return eas.verify(attestations[mediaHash], mediaHash);
    }
}