import React from "react";
import classes from './PeliculaConsulta.module.css'

function PeliculaConsulta({ peliculas }) {
    return (
        <div>
            <div className={classes.header}>
                <h1>Consulta de peliculas</h1>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Género</th>
                        <th>Duración</th>
                        <th>Inventario</th>
                    </tr>
                </thead>
                <tbody>
                    {peliculas.map((pelicula) => (
                        <tr key={pelicula.idPelicula}>
                            <td>{pelicula.idPelicula}</td>
                            <td>{pelicula.nombre}</td>
                            <td>{pelicula.genero || ""}</td>
                            <td>{pelicula.duracion || ""}</td>
                            <td>{pelicula.inventario}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default PeliculaConsulta;
