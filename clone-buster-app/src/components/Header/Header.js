import React from "react";
import classes from './Header.module.css'

function Header() {
    return (
        <div className={classes.firstSection}>
            <div className={classes.container}>
                <div className={classes.header}>
                    <div className={`${classes.text} ${classes.main}`}>CLONEBUSTER</div>
                </div>
            </div>
        </div>
    )
}

export default Header;