import React, {useState, useEffect} from "react";

function Login () {

    document.body.addEventListener('click', formSubmit, true);

    function formSubmit(){
        window.location.href = '/home';
    }

    const [data, setData] = useState({})

    useEffect(() => {
        fetch("/login").then(
            res => res.json()
            ).then(
                data => {
                    setData(data)
                    console.log(data)
                }
            )
    }, [])

    return(
        <>
        <div class="form">
           <h1 id="h2"><span id="logo">V</span>mail</h1>
           <div class="mb-3">
               <label for="exampleFormControlInput1" class="form-label">Email ID</label><br/>
               <input type="email" class="form-control inputs" id="exampleFormControlInput1" placeholder="name@example.com" value={data.email}/>
           </div>
           <div class="mb-3">
               <label for="exampleFormControlInput1" class="form-label">Password</label><br/>
               <input type="password" class="form-control inputs" id="exampleFormControlInput1" placeholder="" value={data.password}/>
           </div>
           <button type="submit" className="button" onClick={formSubmit}>Submit</button>
         </div> 
          
        </>
    );
}

export default Login;
