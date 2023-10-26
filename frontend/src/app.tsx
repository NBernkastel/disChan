import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

// @ts-ignore
import logo from "./icons/logo-min.png";
import LoginForm from "./pages/sign_in";
import Sign from "./pages/sign_up";
import Home_page from "./pages/home_page";

function App() {
  return (
    <BrowserRouter>
      {/* Navigation bar */}
      <nav>
        {/* Application logo */}
        <div className="d-flex flex-column align-items-center">
          <img src={logo} alt="Logo" />
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Home_page />} />
        <Route path="/Sign Up" element={<Sign />} />
        <Route path="/Sign In" element={<LoginForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;