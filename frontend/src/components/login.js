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

  function formSubmit(){
      document.body.addEventListener('click', () => {
        window.location.href = '/home';
      }, true);
  }

  useEffect(() => {
    document.body.addEventListener('dblclick', () => {
      fetch("/login").then(
        res => res.json()
        ).then(
            data => {
              setData(data)
              localStorage.setItem('token',data.email);
              console.log(data)
              console.log(data.validity)
              formSubmit();
            }
        )
    }, true);
  }, [])

  const [data, setData] = useState({})

  return (
    <ThemeProvider theme={theme}>
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid item xs={false} sm={4} md={7} sx={{
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
          <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center', }} >
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
                name="email"
                autoComplete="email"
                autoFocus value={data.email}
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                type="password"
                id="password"
                autoComplete="current-password" value={data.password}
              />
              {/* <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              /> */}
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
                  <Link href="/signup" variant="body2"  style={{color: "teal"}}>
                    {"Don't have an account? Sign Up"}
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
}
