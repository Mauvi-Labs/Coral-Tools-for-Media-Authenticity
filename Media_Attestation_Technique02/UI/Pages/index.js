import { useState } from 'react';
import MediaUploader from '../components/MediaUploader';
import MediaCard from '../components/MediaCard';
import { ethers } from 'ethers';
import { EAS } from '@ethereum-attestation-service/eas-sdk';

const EASContractAddress = '0xYourEASContractAddress';

export default function Home() {
  const [mediaHash, setMediaHash] = useState('');
  const [attestation, setAttestation] = useState(null);
  const [verificationResult, setVerificationResult] = useState(null);
  const [mediaUrl, setMediaUrl] = useState('');
  const [badge, setBadge] = useState(null);

  // Handle media file upload
  const handleUpload = (hash, file) => {
    setMediaHash(hash);
    setMediaUrl(URL.createObjectURL(file));  // Create a URL to preview the uploaded media
  };

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
      setBadge(isVerified ? 'OG 🖌️' : '');
    } catch (err) {
      console.error("Error verifying media: ", err);
    }
  };

  return (
    <div className="container mx-auto p-4 bg-gray-900 min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-6">Media Attestation with EAS</h1>

      {/* MediaUploader component */}
      <MediaUploader onUpload={handleUpload} />

      {/* Attest and Verify Buttons */}
      <div className="my-6">
        <button 
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded mr-4"
          onClick={handleAttestMedia}
        >
          Attest Media
        </button>
        <button 
          className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
          onClick={handleVerifyMedia}
        >
          Verify Media
        </button>
      </div>

      {/* Attestation Hash */}
      {attestation && <p className="mt-4 text-gray-300">Attestation Hash: {attestation}</p>}

      {/* MediaCard for displaying media and badge */}
      {mediaUrl && (
        <MediaCard mediaUrl={mediaUrl} isVerified={verificationResult} />
      )}
    </div>
  );
}
  