import React, { useState } from "react";
import "./server_link.css"; // Подключение файла стилей
import Card from "react-bootstrap/Card";
interface ServerLinkProps {
  imageUrl: string;
  serverName: string;
}

const ServerLink: React.FC<ServerLinkProps> = ({ imageUrl, serverName }) => {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <div
      className={`server-link ${isHovered ? "hovered" : ""}`}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <img className="server-image" src={imageUrl} alt={serverName} />
      {isHovered && <Card style={{ backgroundColor: 'black' }} className="server-name">{serverName}</Card>}
    </div>
  );
};

export default ServerLink;