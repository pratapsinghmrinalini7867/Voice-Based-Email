import React, {useState, useEffect} from "react";
import Navbar from "./navbar";
import {Avatar, Box, Paper, styled, Button} from '@mui/material';
import TurnLeftIcon from '@mui/icons-material/TurnLeft';
import TurnRightIcon from '@mui/icons-material/TurnRight';

function Viewmail(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const id = urlParams.get('id');
    console.log(id)

    const [data, setData] = useState([])
    const [avch, setAvch] = useState()
    const [time, setTime] = useState()

    useState(() => {
        fetch("/viewonemail", {
            method: "POST",
            body: JSON.stringify({
                content:id
            })
        }).then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
                setAvch(data.subject.charAt(0))
                setTime(data.date_created.$date)
            }
        )
    })


    const Item = styled(Paper)(({ theme }) => ({
        backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff', ...theme.typography.body2,
        padding: theme.spacing(1),
        textAlign: 'center',
        color: theme.palette.text.secondary,
        maxWidth: 400,
      }));

    
    return (
        <>
            <Navbar/>

            <Box sx={{ flexGrow: 1, overflow: 'hidden', px: 2 }}>
                    {[data].map((item) => (
                    <Item sx={{my: 2, mx: 'auto', py: 2, px: 5, }} className="item" key={item._id}>
                        <h2 className="h2">{item.subject}</h2> 
                        <div className="d">
                        <Avatar className="av">{avch}</Avatar>
                        <p className="addr">{item.from}</p>
                        <p className="time">{time}</p>
                        </div><br/>
                        <div className="msgBox">
                            <div className="mainBox">
                                <p>{item.description}</p>
                            </div>
                            <Button variant="outlined" className="replyBtn"><TurnLeftIcon/>Reply</Button>
                            <Button variant="outlined" className="replyBtn"><TurnRightIcon/>Forward</Button>
                        </div>
                    </Item>                    
                    ))}                
            </Box>
        </>
    );
}

export default Viewmail;