pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RoyaltyDistribution is ERC721 {
    using SafeMath for uint256;

    struct Distribution {
        address payable[] recipients;
        uint256[] percentages;
    }

    mapping(uint256 => Distribution) public distributions;
    mapping(uint256 => address) public assetOwners;

    constructor() ERC721("Royalty Distribution", "RD") {}

    function setDistribution(
        uint256 tokenId,
        address payable[] calldata recipients,
        uint256[] calldata percentages
    ) external {
        require(msg.sender == ownerOf(tokenId), "Only owner can set distribution");
        require(
            recipients.length == percentages.length,
            "Recipients and percentages arrays must have the same length"
        );
        uint256 total = 0;
        for (uint256 i = 0; i < percentages.length; i++) {
            total = total.add(percentages[i]);
        }
        require(total == 100, "Percentages must add up to 100");

        Distribution storage distribution = distributions[tokenId];
        distribution.recipients = recipients;
        distribution.percentages = percentages;
    }

    function distributeFunds(uint256 tokenId) external payable {
        Distribution storage distribution = distributions[tokenId];
        require(
            distribution.recipients.length > 0,
            "Distribution for this token is not set"
        );
        for (uint256 i = 0; i < distribution.recipients.length; i++) {
            uint256 amount = msg.value.mul(distribution.percentages[i]).div(100);
            distribution.recipients[i].transfer(amount);
        }
    }

    function safeTransfer(uint256 tokenId, address to) external {
        require(msg.sender == ownerOf(tokenId), "Only owner can transfer the token");
        _safeTransfer(msg.sender, to, tokenId, "");
    }

    function mint(address to, uint256 tokenId) public {
        _mint(to, tokenId);
    }
}
