import React, {useState, useEffect} from 'react';
import {Avatar, Box, Paper, Stack, styled, Typography, Grid, List, ListItem, ListItemIcon, ListItemText, Button} from '@mui/material';
import FolderIcon from '@mui/icons-material/Folder';
import Navbar from './navbar';


function Sentmails(){
  const [currentUser, setCurrentuser] = useState('');

  const token = localStorage.getItem('token');

  function session(){
    setCurrentuser(token);
  }

  useEffect(() => {
    session();
  }, [])

  document.body.addEventListener('dblclick', formSubmit, true);
  
  function formSubmit(){
    window.location.href = '/home';
  }


  useEffect(() => {
    fetch("/sentmails").then(
            res => res.json()
            ).then(
                data => {
                    console.log(data)

                    if(data.result == 'back')
                      window.location.href = '/home';
                    
                    else if(data.result == "logout"){
                      localStorage.removeItem('token');
                      window.location.href="/";
                    } else{
                      console.log("Invalid choice")
                    }
                }
            )
    }, [])

  function profileBtn(){
    window.location.href = "/profile"; 
  }

  const Item = styled(Paper)(({ theme }) => ({
      backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
      ...theme.typography.body2,
      padding: theme.spacing(1),
      textAlign: 'center',
      color: theme.palette.text.secondary,
      maxWidth: 400,
    }));
    
    function generate(element) {
      return [0, 1, 2].map((value) =>
        React.cloneElement(element, {
          key: value,
        }),
      );
    }
    
    const Demo = styled('div')(({ theme }) => ({
      backgroundColor: theme.palette.background.paper,
    }));

    const [dense, setDense] = React.useState(false);
    const [secondary, setSecondary] = React.useState(false);

    function openMail(id){
      console.log("You opened a mail with id " + id.$oid)
      window.location.href = "/viewmail/?id=" + id.$oid;
    }

    function handlesubmit(){
      window.location.href = "/home"
    }

    function Logout(){
      localStorage.removeItem('token');
      window.location.href="/";
    }

    return (
        <>
            <Navbar/>

            <h1 style={{textAlign: "center", fontSize: "50px"}}>Sent Mails Page</h1>

            <div className="menu">
              <p className="heading">What do you want to do ?</p><br/>
              <ul>
                  <li><Button className="menuBtn Commonbtn" variant="contained">Search</Button></li>
                  <br/>
                  <li><Button className="menuBtn Commonbtn" variant="contained" onClick={handlesubmit}>Menu Page</Button></li>
                  <br/>
                  <li><Button className="menuBtn Commonbtn" variant="contained" onClick={Logout}>Logout</Button></li>
              </ul>
            </div>

        </>
    );
}

export default Sentmails;