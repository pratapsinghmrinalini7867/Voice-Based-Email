// import React, {useState, useEffect} from "react";

// function Login () {

//     document.body.addEventListener('click', formSubmit, true);

//     function formSubmit(){
//         window.location.href = '/home';
//     }

//     const [data, setData] = useState({})

//     useEffect(() => {
//         fetch("/login").then(
//             res => res.json()
//             ).then(
//                 data => {
//                     setData(data)
//                     console.log(data)
//                 }
//             )
//     }, [])

//     // useEffect(() => {
//     //     fetch("/confirmation").then(
//     //         data => {
//     //             if(data.answer == "yes")
//     //                 window.location.href = "/home";
//     //             else
//     //                 window.location.href = "/"
//     //         }
//     //     )
//     // })

//     return(
//         <>
//         <div class="form">
//            <h1 id="h2"><span id="logo">V</span>mail</h1>
//            <div class="mb-3">
//                <label for="exampleFormControlInput1" class="form-label">Email ID</label><br/>
//                <input type="email" class="form-control inputs" id="exampleFormControlInput1" placeholder="name@example.com" value={data.email}/>
//            </div>
//            <div class="mb-3">
//                <label for="exampleFormControlInput1" class="form-label">Password</label><br/>
//                <input type="password" class="form-control inputs" id="exampleFormControlInput1" placeholder="" value={data.password}/>
//            </div>
//            <button type="submit" className="button btn btn-lg" onClick={formSubmit}>Submit</button>
//          </div> 
          
//         </>
//     );
// }

// export default Login;

import React, {useState, useEffect} from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import SignIcon from '../images/login.png';

const theme = createTheme();

export default function Login() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };

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
                    console.log(data.validity)
                    if(data.validity == true)
                      window.location.href = "/home";
                }
            )
    }, [])

  return (
    <ThemeProvider theme={theme}>
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage: 'url()',
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}>
            <img src={SignIcon} style={{width: "300px", margin: "13% 30%", height: "300px"}}></img>
        </Grid>
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: 'teal' }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
              />
              <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              />
              <Button className="Commonbtn"
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign In
              </Button>
              <Grid container>
                <Grid item xs>
                  <Link href="#" variant="body2" style={{color: "teal"}}>
                    Forgot password?
                  </Link>
                </Grid>
                <Grid item>
                  <Link href="#" variant="body2"  style={{color: "teal"}}>
                    {"Don't have an account? Sign Up"}
                  </Link>
                  {/* <img src={SignIcon}></img> */}
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}
