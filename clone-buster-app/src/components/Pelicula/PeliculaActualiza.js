import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './PeliculaActualiza.module.css';

function PeliculaActualiza({ onActualizarPelicula, peliculas }) {
    const navigate = useNavigate('');

    const [targetId, setTargetId] = useState('');
    const [nuevoNombre, setNuevoNombre] = useState('');
    const [nuevoGenero, setNuevoGenero] = useState('');
    const [nuevaDuracion, setNuevaDuracion] = useState('');
    const [nuevoInventario, setNuevoInventario] = useState('');

    function idHandler(event) {
        setTargetId(event.target.value);
    }

    function nombreHandler(event) {
        setNuevoNombre(event.target.value);
    }

    function generoHandler(event) {
        setNuevoGenero(event.target.value);
    }

    function duracionHandler(event) {
        setNuevaDuracion(event.target.value);
    }

    function inventarioHandler(event) {
        setNuevoInventario(event.target.value);
    }

    function obtenerPeliculaPorId(id) {
        const pelicula = peliculas.find(pelicula => pelicula.idPelicula === parseInt(id));
        return pelicula || null;
    }

    function submitHandler(event) {
        event.preventDefault();

        const peliculaTarget = obtenerPeliculaPorId(targetId);

        if (peliculaTarget) {
            const postData = {
                idPelicula: parseInt(targetId),
                nombre: nuevoNombre || peliculaTarget.nombre,
                genero: nuevoGenero || peliculaTarget.genero,
                duracion: nuevaDuracion || peliculaTarget.duracion,
                inventario: nuevoInventario || peliculaTarget.inventario
            };

            onActualizarPelicula(postData);
        } else {
            console.log("Película no encontrada");
        }

        navigate('/');
    }

    return (
        <div>
            <h1 className={classes.header}>Actualizar película</h1>
            <form onSubmit={submitHandler}>
                <label htmlFor="id">Ingrese el ID de la película a actualizar:</label>
                <input type="text" name="id" id="id" value={targetId} onChange={idHandler} required />
                <br />
                <label htmlFor="name">Ingrese el nuevo nombre:</label>
                <input type="text" name="name" id="name" value={nuevoNombre} onChange={nombreHandler} />
                <br />
                <label htmlFor="genre">Ingrese el nuevo género:</label>
                <input type="text" name="genre" id="genre" value={nuevoGenero} onChange={generoHandler} />
                <br />
                <label htmlFor="length">Ingrese la nueva duración:</label>
                <input type="number" name="length" id="length" value={nuevaDuracion} onChange={duracionHandler} />
                <br />
                <label htmlFor="stock">Ingrese un número representando el inventario:</label>
                <input type="number" name="stock" id="stock" value={nuevoInventario} onChange={inventarioHandler} />
                <br />
                <button type="submit">Actualizar película</button>
            </form>
        </div>
    );
}

export default PeliculaActualiza;
