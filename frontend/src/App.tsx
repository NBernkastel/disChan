import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Link } from "react-router-dom";

import Sign from "./pages/Sign_Up";
// @ts-ignore
import logo from "./icons/logo-min.png";
import LoginForm from "./pages/Sign_In"; // Замените "path/to/your/animated.gif" на путь к вашему анимированному GIF

function App() {
  return (
    <BrowserRouter>
      {/* Navigation bar */}
      <nav>
        {/* Application logo */}
        <img src={logo} alt="Logo" />
        {/* Link to sign in or sign up */}
        {/* <Link to="/">Sign In/Sign Up</Link> */}
      </nav>
      <Routes>
        <Route path="/Sign Up" element={<Sign />} />
        <Route path="/Sign In" element={<LoginForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;