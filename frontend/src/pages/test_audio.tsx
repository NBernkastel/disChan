import React, { useEffect, useRef } from 'react';

const AudioComponent: React.FC = () => {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const mediaStreamRef = useRef<MediaStream | null>(null);

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/sockets/test');

    // Event handler for when the WebSocket connection is established
    socket.onopen = () => {
      console.log('WebSocket connection established');

      // Start audio stream
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          mediaStreamRef.current = stream;
          if (audioRef.current) {
            audioRef.current.srcObject = stream;
          }

          // Create a new RTCPeerConnection
          const peerConnection = new RTCPeerConnection();

          // Add the audio track to the peer connection
          stream.getTracks().forEach(track => {
            peerConnection.addTrack(track, stream);
          });

          // Create an offer to establish a connection
          peerConnection.createOffer()
            .then(offer => peerConnection.setLocalDescription(offer))
            .then(() => {
              // Send the offer to the server
              socket.send(JSON.stringify(peerConnection.localDescription));
            });

          // Event handler for receiving an answer from the server
          socket.onmessage = async event => {
            const answer = JSON.parse(event.data);

            // Set the remote description of the peer connection
            await peerConnection.setRemoteDescription(answer);

            console.log('Connection established');
          };
        })
        .catch(error => {
          console.error('Error accessing microphone:', error);
        });
    };

    // Event handler for when the WebSocket connection is closed
    socket.onclose = () => {
      console.log('WebSocket connection closed');
    };

    // Clean up the WebSocket connection and media stream on component unmount
    return () => {
      socket.close();
      if (mediaStreamRef.current) {
        mediaStreamRef.current.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  return (
    <div>
      <div>Audio Component</div>
      <audio ref={audioRef} controls />
    </div>
  );
};

export default AudioComponent;