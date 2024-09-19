export default function AttestationBadge({ isVerified }) {
  return (
    <div className="attestation-badge bg-gray-900 p-2 rounded-md">
      {isVerified && (
        <span className="text-white text-xl">OG 🖌️</span>
      )}
    </div>
  );
}