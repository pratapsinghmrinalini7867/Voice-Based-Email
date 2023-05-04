import React, {useState, useEffect} from "react";

function Profile(){

    const [data, setData] = useState([{}]);

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

    return (
        <>
            <h1 className="profile"><span>M</span></h1>
            <h3 className="usname">USERNAME</h3>

            <div className="details">
                {
                    <p>Email ID<span>{data.member}</span></p>
                }
                <hr/>
                <p>Phone Number<span></span></p>
            </div>
        </>
    );
}

export default Profile;