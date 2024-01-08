import React, { useState } from 'react';

export const Choice = () => {
  const [roomId, setRoomId] = useState('');

  const handleJoinRoom = () => {
    // Implement logic to handle joining a room with the roomId
    console.log(`Joining room ${roomId}`);
  };

  const handleCreateRoom = () => {
    // Implement logic to handle creating a room
    console.log('Creating a new room');
  };

  return (
    <div style={styles.container}>
      <div style={styles.choiceContainer}>
        <h2>Create a Room</h2>
        <p>Provide a description of what creating a room entails.</p>
        <button style={styles.button} onClick={handleCreateRoom}>
          Create Room
        </button>
      </div>

      <div style={styles.choiceContainer}>
        <h2>Join a Room</h2>
        <p>Provide a description of what joining a room entails.</p>
        <input
          type="text"
          placeholder="Enter Room ID"
          value={roomId}
          onChange={(e) => setRoomId(e.target.value)}
          style={styles.input}
        />
        <button style={styles.button} onClick={handleJoinRoom}>
          Join Room
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    justifyContent: 'space-around',
    alignItems: 'center',
    height: '100vh',
  },
  choiceContainer: {
    textAlign: 'center',
    padding: '20px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    maxWidth: '300px',
  },
  input: {
    margin: '10px 0',
    padding: '5px',
    width: '100%',
  },
  button: {
    padding: '10px',
    backgroundColor: '#007BFF',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
};


export default Choice;