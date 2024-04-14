import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './UsuarioAgrega.module.css';

function UsuarioBorra({ onEliminarUsuario }) {
    const navigate = useNavigate('');
    const [userId, setUserId] = useState('');

    function userIdHandler(event) {
        setUserId(event.target.value);
    }

    function submitHandler(event) {
        event.preventDefault();
        console.log(userId);
        onEliminarUsuario(userId);
        navigate('/');
    }

    return (
        <div>
            <h1>Elimina usuario</h1>
            <form onSubmit={submitHandler}>
                <label htmlFor="user_id">Ingrese el ID del usuario:</label>
                <input type="text" name="user_id" id="user_id" value={userId} onChange={userIdHandler} required />
                <br />
                <button>Eliminar usuario</button>
                <label className={classes.disclaimer}>Se borrarán todas las rentas asociadas</label>
            </form>
        </div>
    );
}

export default UsuarioBorra;
