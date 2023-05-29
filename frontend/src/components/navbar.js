import React, {useState, useEffect} from "react";
import {AppBar, Box, Toolbar, Typography, IconButton, Button, MenuItem, Menu} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';

function Navbar(){
  const [auth, setAuth] = React.useState(true);
  const [anchorEl, setAnchorEl] = React.useState(null);

  const [currentUser, setCurrentuser] = useState('');

  const token = localStorage.getItem('token');
  function session(){
      setCurrentuser(token);
  }
  useEffect(() => {
      session();
  }, [])

  const handleChange = (event) => {
    setAuth(event.target.checked);
  };

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  function profileBtn(){
    localStorage.removeItem('token');
    window.location.href="/"; 
  }
  
    return (
        <>
        <Box sx={{ flexGrow: 1 }}>
        
          <AppBar position="static" style={{backgroundColor: "teal"}} >
            <Toolbar>
              <IconButton size="large" edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>                <MenuIcon />
              </IconButton>
              <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                <a href="/" className="l"><h2 className="navhead navLog"><span className="logo">V</span>mail</h2></a>
              </Typography>
              {auth && (
                <div>
                  <IconButton size="large" aria-label="account of current user" aria-controls="menu-appbar" aria-haspopup="true" onClick={handleMenu} color="inherit">
                  
                  {token?
                  // <Button variant="outlined" className='profileBtn'><AccountCircle /><p style={{marginRight: "2px"}}></p>Signed In: {token}</Button>
                  <Button variant="outlined" className='profileBtn'><AccountCircle /><p style={{marginRight: "2px"}}></p>Signed In: 1940036@sliet.ac.in</Button>
                    :
                  <Button variant="outlined" className='profileBtn'><AccountCircle /><p style={{marginRight: "2px"}}></p>Sign UP/ Sign In</Button>
                  }

                   
                  </IconButton>
                  <Menu
                    id="menu-appbar"
                    anchorEl={anchorEl}
                    anchorOrigin={{
                      vertical: 'top',
                      horizontal: 'right',
                    }}
                    keepMounted
                    transformOrigin={{
                      vertical: 'top',
                      horizontal: 'right',
                    }}
                    open={Boolean(anchorEl)}
                    onClose={handleClose}
                  >
                    <MenuItem onClick={handleClose}>Profile</MenuItem>
                    <MenuItem onClick={handleClose}>My account</MenuItem>
                  </Menu>
                </div>
              )}
            </Toolbar>
          </AppBar>
        </Box>
        </>
    )
}

export default Navbar;