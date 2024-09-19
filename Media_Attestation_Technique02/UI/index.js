import { useState } from 'react';
import { ethers } from 'ethers';
import { EAS } from '@ethereum-attestation-service/eas-sdk';

const EASContractAddress = '0xYourEASContractAddress';

export default function Home() {
  const [mediaHash, setMediaHash] = useState('');
  const [attestation, setAttestation] = useState(null);
  const [verificationResult, setVerificationResult] = useState(null);
  const [mediaUrl, setMediaUrl] = useState('');
  const [badge, setBadge] = useState(null);

  // Connect to EAS and submit attestation
  const handleAttestMedia = async () => {
    try {
      const eas = new EAS(EASContractAddress);
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      eas.connect(provider);

      const signer = provider.getSigner();
      const tx = await eas.attest(signer.getAddress(), mediaHash);
      setAttestation(tx.hash); // tx.hash is the attestation hash

    } catch (err) {
      console.error("Error attesting media: ", err);
    }
  };

  // Verify media attestation and append badge if valid
  const handleVerifyMedia = async () => {
    try {
      const eas = new EAS(EASContractAddress);
      const isVerified = await eas.verify(mediaHash);

      setVerificationResult(isVerified);
      if (isVerified) {
        setBadge('OG 🖌️');  // Updated badge design
      } else {
        setBadge('❌ Not Verified');
      }
    } catch (err) {
      console.error("Error verifying media: ", err);
    }
  };

  return (
    <div className="container">
      <h1>Media Attestation with EAS</h1>

      {/* Media Hash Input */}
      <input 
        type="text" 
        value={mediaHash} 
        onChange={(e) => setMediaHash(e.target.value)} 
        placeholder="Enter media hash"
      />

      <button onClick={handleAttestMedia}>Attest Media</button>
      
      {attestation && <p>Attestation Hash: {attestation}</p>}

      {/* Media URL for displaying badge */}
      <input 
        type="text" 
        value={mediaUrl} 
        onChange={(e) => setMediaUrl(e.target.value)} 
        placeholder="Enter media URL"
      />

      <button onClick={handleVerifyMedia}>Verify Media</button>
      
      {verificationResult !== null && (
        <div>
          <p>Verification Result: {verificationResult ? 'Valid' : 'Invalid'}</p>
          {/* Display Badge next to Media */}
          <div>
            <img src={mediaUrl} alt="Verified Media" />
            {badge && <span style={{ marginLeft: '10px', fontSize: '18px', color: 'green' }}>{badge}</span>}  {/* OG badge */}
          </div>
        </div>
      )}
    </div>
  );
}