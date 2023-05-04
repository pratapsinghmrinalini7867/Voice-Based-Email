import React, { useEffect, useState } from "react";
import {Button} from '@mui/material';
import Navbar from './navbar';

function Home () {
    const [data, setData] = useState({})

    useEffect(() => {
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
                else
                    window.location.href = "/inbox";
            }
        )
    }, [])

    function inboxBtn(){
        window.location.href = "/inbox"; 
    }

    function mailBtn(){
        window.location.href = "/compose"; 
    }

    function sentBtn(){
        window.location.href = "/inbox"; 
    }

    function profileBtn(){
        window.location.href = "/profile"; 
    }

    return(
        <>     
        <Navbar/>
         <div className="menu">
            <p className="heading">What do you want to do ?</p><br/>
            <ul>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={inboxBtn}>Check Inbox</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={mailBtn}>Compose a Mail</Button></li>
                <br/>
                <li><Button className="menuBtn Commonbtn" variant="contained" onClick={sentBtn}>Sent Mails</Button></li>
            </ul>
         </div>
          
        </>
    );
}

export default Home;