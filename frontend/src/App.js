import React from 'react';
import { Route,BrowserRouter as Router, Routes } from 'react-router-dom';
import Login  from './components/login';
import Home from './components/home';
import Inbox from './components/inbox';
import Profile from './components/profile';
import Signup from './components/sign';
import './App.css';
import Compose from './components/compose';
import Viewmail from './components/viewMail';
import Sentmails from './components/sentmails';
import Trash from './components/trash';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/home" element={<Home/>} />
          <Route path="/" element={<Login/>} />
          <Route path="/inbox" element={<Inbox/>} /> 
          <Route path="/profile" element={<Profile/>} /> 
          <Route path="/signup" element={<Signup/>} />
          <Route path="/compose" element={<Compose/>} />
          <Route path="/viewmail" element={<Viewmail/>} />
          <Route path="/viewsentmail" element={<Sentmails/>} />
          <Route path="/viewtrash" element={<Trash/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
