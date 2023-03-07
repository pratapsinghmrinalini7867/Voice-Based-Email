import React from "react";

function Profile(){
    return (
        <>
            <h1 className="profile"><span>M</span></h1>
            <h3 className="usname">USERNAME</h3>

            <div className="details">
                <p>Email ID<span></span></p>
                <hr/>
                <p>Phone Number<span></span></p>
            </div>
        </>
    );
}

export default Profile;