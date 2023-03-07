import React, { useEffect, useState } from "react";

function Home () {
    const [data, setData] = useState({})

    useEffect(() => {
        fetch("/menu").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    })

    if(data == "inbox"){
        window.location.href = "/inbox"; 
    }

    if(data == "compose"){
        window.location.href = "/compose"; 
    }

    if(data == "sent"){
        window.location.href = "/sentmails"; 
    }

    function inboxBtn(){
        window.location.href = "/inbox"; 
    }

    function mailBtn(){
        window.location.href = "/inbox"; 
    }

    function sentBtn(){
        window.location.href = "/inbox"; 
    }

    function profileBtn(){
        window.location.href = "/profile"; 
    }

    return(
        <>
        <nav class="navbar bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <h3 id="h2 navhead"><span id="logo">V</span>mail</h3>
                </a>
                <button className="idlog" onClick={profileBtn}><span class="icon">M</span>Signed In</button>
            </div>
        </nav>

         <div className="menu">
            <p className="heading">What do you want to do ?</p><br/>
            <ul>
                <li><button className="menuBtn" onClick={inboxBtn}>Check Inbox</button></li>
                <br/>
                <li><button className="menuBtn" onClick={mailBtn}>Compose a Mail</button></li>
                <br/>
                <li><button className="menuBtn" onClick={sentBtn}>Sent Mails</button></li>
            </ul>
         </div>
          
        </>
    );
}

export default Home;