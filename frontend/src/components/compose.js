import React, { useState, useEffect } from "react";
import Navbar from "./navbar";
import { TextField, Grid, Card, CardContent, Button } from "@mui/material";
    
function Compose(){
    const [data, setData] = useState({})

    function formSubmit(){
        document.body.addEventListener('click', () => {
            window.location.href = '/home';
        }, true);
    }

    useEffect(() => {
        document.body.addEventListener('dblclick', () => {
        fetch("/compose").then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                formSubmit();
            }
        )}, true);
    }, [])

    return (
        <>
            <Navbar/>

            <Grid lg={4}>
            <Card className="compose">
                <h2>Compose a mail</h2>
                <CardContent>
                    <label>To</label>
                    <TextField id="standard-basic" variant="standard" fullWidth value={data.to}/>
                </CardContent>
                <CardContent>
                    <label>Subject</label>
                    <TextField id="standard-basic" variant="standard" fullWidth value={data.sub}/>
                </CardContent>
                <CardContent>
                    <label>Description</label>
                    <TextField multiline rows={5} maxRows={5} fullWidth value={data.desc} style={{marginTop: "20px"}}/>
                </CardContent>
                <CardContent>
                    <Button variant="contained" fullWidth className="Commonbtn" color="primary">Submit</Button>
                </CardContent>
            </Card>
        </Grid>

        </>
    );
}

export default Compose;