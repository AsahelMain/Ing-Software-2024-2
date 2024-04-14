import React from "react";
import { Link } from 'react-router-dom';

import './Button.css';

function Button({ reference, message}) {
    const classes = 'button'; 

    return (
        <Link to={reference} className={classes}>{message}</Link>
    )
}

export default Button;