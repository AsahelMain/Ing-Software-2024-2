import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './PeliculaAgrega.module.css';

function PeliculaBorra({ onEliminarPelicula }) {
    const navigate = useNavigate('');
    const [peliculaId, setPeliculaId] = useState('');

    function peliculaIdHandler(event) {
        setPeliculaId(event.target.value);
    }

    function submitHandler(event) {
        event.preventDefault();
        console.log(peliculaId);
        onEliminarPelicula(peliculaId);
        navigate('/');
    }

    return (
      <div>
        <h1>Elimina película</h1>
        <form onSubmit={submitHandler}>
            <label htmlFor="movie_id">Ingrese el ID de la película:</label>
            <input
            type="text"
            name="movie_id"
            id="movie_id"
            required
            value={peliculaId}
            onChange={peliculaIdHandler}
            />
            <br />
            <button type="submit">Elimina película</button>
            <label className={classes.disclaimer}>Se borrará permanentemente</label>
        </form>
      </div>
    );
}

export default PeliculaBorra;
