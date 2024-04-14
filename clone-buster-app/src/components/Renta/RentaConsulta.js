import React from "react";
import classes from './RentaConsulta.module.css';

function RentaConsulta({ rentas, fecha_actual }) {
    return (
        <div>
            <div className={classes.header}>
                <h1>Consulta de rentas</h1>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>ID renta</th>
                        <th>ID usuario</th>
                        <th>ID película</th>
                        <th>Fecha de renta</th>
                        <th>Días de renta</th>
                        <th>Estatus</th>
                    </tr>
                </thead>
                <tbody>
                    {rentas.map((renta) => {
                        const fecha_renta = new Date(renta.fecha_renta);
                        const dias_de_renta = renta.dias_de_renta;
                        const dias_transcurridos = Math.floor((fecha_actual - fecha_renta) / (1000 * 60 * 60 * 24));
                        const backgroundColor = dias_transcurridos > dias_de_renta ? "#ffcccc" : "transparent";

                        return (
                            <tr key={renta.idRentar} style={{ backgroundColor }}>
                                <td>{renta.idRentar}</td>
                                <td>{renta.idUsuario}</td>
                                <td>{renta.idPelicula}</td>
                                <td>{renta.fecha_renta}</td>
                                <td>{renta.dias_de_renta}</td>
                                <td>{renta.estatus ? "Devuelta" : "No devuelta"}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default RentaConsulta;
