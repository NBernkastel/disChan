import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import "./chat.css";

interface ChatProps {
  username: string;
  lastMessage: string;
  onChatClick: () => void;
}

const Chat: React.FC<ChatProps> = ({ username, lastMessage, onChatClick }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen(!isOpen);
    onChatClick();
  };

  return (
    <div className={`chat ${isOpen ? "open" : ""}`} onClick={handleClick}>
      <div className="user-icon">
        <FontAwesomeIcon icon={faUser} />
      </div>
      <div className="chat-details">
        <div style={{color: 'rgb(10,219,238)'}} className="username">{username}</div>
        <div className="last-message">{lastMessage}</div>
      </div>
    </div>
  );
};

export default Chat;