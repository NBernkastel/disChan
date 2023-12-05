import React from "react";
import {Container, Row, Col, Button, Form} from "react-bootstrap";
import Server_link from "../component/server_link";
import Chat from "../component/chat";
import FriendsList from "../component/friendsList";

function MainPage() {
    const handleChatClick = () => {
    // Обработка открытия переписки на текущей странице
    // Например, показать детали переписки или перенаправить на другую страницу
    console.log("Переписка открыта!");
  };
  return (
    <main className="d-flex flex-nowrap">
        <div className="d-flex flex-column flex-shrink-0 p-3 text-bg-dark" style={{width: "100px"}}>
            <a style={{ color: 'rgb(125,7,250)', fontSize: '22px' }} className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-decoration-none">DisChan</a>
            <hr style={{width: "80px"}} />
            <ul className="nav nav-pills flex-column mb-auto">
                <li>
                    <Server_link
                        imageUrl="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"
                        serverName="YouTube"
                    />
                </li>
                <span style={{height: "10px"}}></span>
                <li>
                    <Server_link
                        imageUrl="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"
                        serverName="YouTube"
                    />
                </li>
                <span style={{height: "10px"}}></span>
                <li>
                    <Server_link
                        imageUrl="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg"
                        serverName="YouTube"
                    />
                </li>
            </ul>
        </div>
        <div className="d-flex flex-column flex-shrink-0 p-3 text-bg-dark darker-bg" style={{width: "200px"}}>
            <FriendsList />
            <a style={{ color: 'rgb(125,7,250)', fontSize: '22px' }}>Messages</a>
            <Chat username="Dima" lastMessage="kogda prod?" onChatClick={handleChatClick} />
            <Chat username="Sergay" lastMessage="I GAY" onChatClick={handleChatClick} />
            <Chat username="Denis" lastMessage="che?" onChatClick={handleChatClick} />
        </div>
        <div>

        </div>
    </main>
  );
}

export default MainPage;