import React, { useState } from "react";
import {Button} from "react-bootstrap";

const FriendsList: React.FC = () => {
  const [isListVisible, setListVisible] = useState(false);

  const toggleListVisible = () => {
    setListVisible(!isListVisible);
  };

  const friends = ["Gondon", "Urod", "Xuesos", "Daun"];

  return (
    <div>
      <Button onClick={toggleListVisible}>Friends</Button>
      {isListVisible && (
        <ul>
          {friends.map((friend) => (
            <li key={friend}>{friend}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default FriendsList;