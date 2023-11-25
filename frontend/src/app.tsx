import React from "react";
import { BrowserRouter, Routes, Route} from "react-router-dom";

// @ts-ignore
import Logo from "./icons/logo-min.png";
import LoginForm from "./pages/sign_in";
import Sign from "./pages/sign_up";
import HomePage from "./pages/home_page";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <div className="d-flex flex-column align-items-center">
          <img src={Logo} alt="Logo" />
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/signup" element={<Sign />} />
        <Route path="/signin" element={<LoginForm />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;