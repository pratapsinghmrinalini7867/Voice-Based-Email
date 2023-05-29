import React, {useState, useEffect} from 'react';
import {Avatar, Box, Paper, Stack, styled, Typography, Grid, List, ListItem, ListItemIcon, ListItemText, Button} from '@mui/material';
import Navbar from './navbar';


function Inbox(){

    // const [data, setData] = useState([])
    // const [avch, setAvch] = useState()
    // const [time, setTime] = useState()

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
        fetch("/inbox").then(
            res => res.json()
            ).then(
                data => {
                    // setData(data)
                    // setTime(data.date_created.$date)
                    // setAvch(data.subject.charAt(0))
                    console.log(data)

                    if(data.data == 'back')
                      window.location.href = '/home';
                    
                    else if(data.data == 'logout'){
                      localStorage.removeItem('token');
                      window.location.href="/";
                    } else{
                      console.log("Invalid choice")
                    }
                    
                  })
                    
    }, [])

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

      function handleSubmit(){
        window.location.href="/home";
      }

      function Logout(){
        localStorage.removeItem('token');
        window.location.href="/";
      }


    return (
        <>
            <Navbar/>

            <h1 style={{textAlign: "center", fontSize: "50px"}}>Inbox Page</h1>

            <div className="menu">
            <p className="heading">What do you want to do ?</p><br/>
            <ul>
                <li><Button className="menuBtn Commonbtn" variant="contained">Unseen Mails</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained">Search Mail</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained">Menu Page</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={Logout}>Logout</Button></li>
            </ul>
         </div>

            {/* <Box sx={{ flexGrow: 1, overflow: 'hidden', px: 2 }}>
                    {data.map((item) => (
                    <a onClick={() => openMail(item._id)} style={{textDecoration: "none"}}>                    
                    <Item sx={{my: 2, mx: 'auto', py: 2, px: 5, }} style={{maxWidth: "800px", maxHeight: "40px"}} key={item._id}>
                        <Stack className="items" spacing={2} direction="row" alignItems="center">
                        <Avatar style={{backgroundColor: "purple"}}>{item.subject.charAt(0).toUpperCase()}</Avatar>
                        <Typography noWrap style={{maxWidth: "200px", minWidth: "50px"}}>{item.subject}</Typography>
                        <Typography noWrap onClick={() => openMail(item._id)} style={{ textDecoration: "none"}}>{item.description}</Typography>
                        <p style={{textAlign: "right", width: "300px"}}>{item.date_created.$date}</p>
                        </Stack>
                    </Item>
                    </a>
                    ))}                
            </Box> */}



        </>
    );
}

export default Inbox;