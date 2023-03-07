import React, {useState, useEffect} from 'react';

function Inbox(){

    const [data, setData] = useState({})

    useEffect(() => {
        fetch("/members").then(
            res => res.json()
            ).then(
                data => {
                    setData(data)
                    console.log(data)
                }
            )
    }, [])

    function profileBtn(){
        window.location.href = "/profile"; 
    }

    return (
        <>
            <nav class="navbar bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <h3 id="h2 navhead"><span id="logo">V</span>mail</h3>
                </a>
                <button className="idlog" onClick={profileBtn}><span class="icon">M</span>Signed In</button>
            </div>
            </nav>

            <h1>Inbox Page</h1>
            <div>
                {data.Data}{data.People}
                {data.array}
            </div>
        </>
    );
}

export default Inbox;