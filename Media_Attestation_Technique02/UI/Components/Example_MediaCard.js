import AttestationBadge from './AttestationBadge';

export default function MediaCard({ mediaUrl, isVerified }) {
  return (
    <div className="media-card p-4 bg-gray-800 border border-gray-700 rounded-lg shadow-md">
      <img src={mediaUrl} alt="Media" className="rounded-md w-full" />
      <div className="mt-2 flex justify-between items-center">
        <p className="text-white">Media URL: {mediaUrl}</p>
        <AttestationBadge isVerified={isVerified} />
      </div>
    </div>
  );
}