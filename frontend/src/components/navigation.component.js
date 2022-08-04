import React from "react";
import { Route, Routes } from 'react-router-dom';
import Home from "../directory/home";
import About from "../directory/about";

const Header = () => {
  return (
    <div>
      Header
      <div>
        Navigation Panel
        <Routes>
        <Route path="/" element={<Home />} />
        <Route path="about" element={<About />} />
        </Routes>
      </div>
    </div>
)
}

export default Header;