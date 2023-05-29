import React, { useEffect, useState } from "react";
import {Button, Grid} from '@mui/material';
import { experimentalStyled as styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Navbar from './navbar';

function Home () {
    const [data, setData] = useState({})
    const [currentUser, setCurrentuser] = useState('');

    const token = localStorage.getItem('token');

    function session(){
        setCurrentuser(token);
    }
    useEffect(() => {
        session();
    }, [])

    useEffect(() => {
        document.body.addEventListener('dblclick', () => {
            fetch("/menu").then(
                res => res.json()
            ).then(
                data => {
                    console.log(data)
                    setData(data)
                    if(data.choice == "inbox")
                        window.location.href = "/inbox";
                    else if(data.choice == "compose")
                        window.location.href = "/compose";
                    else if(data.choice == "sent")
                        window.location.href = "/viewsentmail";
                    else if(data.choice == "trash")
                        window.location.href = "/viewtrash";
                    else if(data.choice == "logout"){
                            localStorage.removeItem('token');
                            window.location.href="/";
                    }
                    else{
                        window.location.href = "/home";
                    }
                }
        )}, true);
    }, [])

    function inboxBtn(){
        window.location.href = "/inbox"; 
    }

    function mailBtn(){
        window.location.href = "/compose"; 
    }

    function sentBtn(){
        window.location.href = "/viewsentmail"; 
    }

    function profileBtn(){
        window.location.href = "/profile"; 
    }

    function trashBtn(){
        window.location.href = "/viewtrash"; 
    }

    function Logout(){
        localStorage.removeItem('token');
        window.location.href="/";
    }

    const Item = styled(Paper)(({ theme }) => ({
        backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
        ...theme.typography.body2,
        padding: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.secondary,
    }));


    return(
        <>     
        <Navbar/>

        {/* <Grid container spacing={{ xs: 2, md: 1 }} columns={{ xs: 4, sm: 8, md: 12 }}>
                <Grid item xs={2} sm={4} md={5} >
                <h1 style={{textAlign: "center", fontSize: "50px", margin: "40% 10%"}}>Menu Page</h1>
                </Grid>
                <Grid item xs={2} sm={4} md={7}>
            <div className="othermenu">
            <p className="heading">What do you want to do ?</p><br/>
            <ul>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={mailBtn}>Compose a Mail</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={inboxBtn}>Check Inbox</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={sentBtn}>Sent Mails</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={trashBtn}>Trash</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={Logout}>Logout</Button></li>
            </ul>
         </div>
                </Grid>
        </Grid> */}

        <h1 style={{textAlign: "center", fontSize: "50px"}}>Menu Page</h1>
         <div className="menu">
            <p className="heading">What do you want to do ?</p><br/>
            {/* <p style={{textAlign: "center"}}>Current session: {token}</p> */}
            <ul>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={mailBtn}>Compose a Mail</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={inboxBtn}>Check Inbox</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={sentBtn}>Sent Mails</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={trashBtn}>Trash</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={Logout}>Logout</Button></li>
            </ul>
         </div>
          
        </>
    );
}

export default Home;