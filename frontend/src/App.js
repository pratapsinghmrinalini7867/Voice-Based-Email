import React from 'react';
import './App.css';
import { Route,BrowserRouter as Router, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import $ from 'jquery';
import Popper from 'popper.js';
import Login from './components/Login';
import Home from './components/Home';
import Inbox from './components/inbox';
import Profile from './components/profile';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/home" element={<Home/>} />
          <Route path="/" element={<Login/>} />
          <Route path="/inbox" element={<Inbox/>} />
          <Route path="/profile" element={<Profile/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
