import React, { useState, useEffect } from 'react';

const AudioRecorder = () => {
  const [audioStream, setAudioStream] = useState<MediaStream | null>(null);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const [audioChunks, setAudioChunks] = useState<Blob[]>([]);
  const [recording, setRecording] = useState(false);

  useEffect(() => {
    async function startRecording() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        setAudioStream(stream);
        const mediaRecorder = new MediaRecorder(stream);
        setMediaRecorder(mediaRecorder);

        mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0) {
            setAudioChunks((prevChunks) => [...prevChunks, event.data]);
          }
        };
      } catch (error) {
        console.error('Error accessing microphone:', error);
      }
    }

    if (recording) {
      startRecording();
    } else {
      if (audioStream) {
        audioStream.getTracks().forEach((track) => track.stop());
      }
      if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
      }
    }
  }, [recording]);

  const handleStartRecording = () => {
    setRecording(true);
  };

  const handleStopRecording = () => {
    setRecording(false);
  };

  const handleSendDataToServer = () => {
    // Объедините все audioChunks в один байтовый массив и конвертируйте его в Uint8Array.
    const blob = new Blob(audioChunks, { type: 'audio/wav' });

    const reader = new FileReader();
    reader.onload = (event) => {
      if (event.target?.result) {
        const audioData = new Uint8Array(event.target.result as ArrayBuffer);

        // Отправьте данные на сервер по WebSocket.
        const ws = new WebSocket('ws://localhost:8000/sockets/test');
        ws.binaryType = 'arraybuffer';
        ws.onopen = () => {
          ws.send(audioData.buffer);
          ws.close();
        };
      }
    };
    reader.readAsArrayBuffer(blob);
  };

  return (
    <div>
      <button onClick={handleStartRecording}>Start Recording</button>
      <button onClick={handleStopRecording}>Stop Recording</button>
      <button onClick={handleSendDataToServer}>Send Audio to Server</button>
    </div>
  );
};

export default AudioRecorder;
