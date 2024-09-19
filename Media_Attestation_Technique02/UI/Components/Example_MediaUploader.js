import { useState } from 'react';
import crypto from 'crypto';

export default function MediaUploader({ onUpload }) {
  const [file, setFile] = useState(null);
  const [fileHash, setFileHash] = useState('');

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    setFile(uploadedFile);

    const reader = new FileReader();
    reader.onloadend = () => {
      const arrayBuffer = reader.result;
      const hash = crypto.createHash('sha256').update(arrayBuffer).digest('hex');
      setFileHash(hash);
      onUpload(hash, uploadedFile);  // Pass hash and file to parent component
    };
    reader.readAsArrayBuffer(uploadedFile);
  };

  return (
    <div className="media-uploader p-4 bg-gray-800 rounded-md">
      <input 
        type="file" 
        onChange={handleFileChange} 
        accept="image/*,video/*" 
        className="text-white bg-gray-700 rounded-md p-2"
      />
      {file && <p className="text-white mt-2">File: {file.name}</p>}
      {fileHash && <p className="text-white mt-2">File Hash: {fileHash}</p>}
    </div>
  );
}