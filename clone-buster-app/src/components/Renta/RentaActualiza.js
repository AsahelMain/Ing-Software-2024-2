import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import classes from './RentaActualiza.module.css';

function RentaActualiza({ onActualizarRenta, rentas }) {
    const navigate = useNavigate('');

    const [rentaId, setRentaId] = useState('');
    const [nuevoEstatus, setNuevoEstatus] = useState(false);

    function rentaIdHandler(event) {
        setRentaId(event.target.value);
    }

    function estatusHandler(event) {
        setNuevoEstatus(event.target.value === "true");
    }

    function obtenerRentaPorId(id) {
        const renta = rentas.find(renta => renta.idRentar === parseInt(id));
        return renta || null;
    }

    function submitHandler(event) {
        event.preventDefault();

        const rentaTarget = obtenerRentaPorId(rentaId);
    
        if (rentaTarget) {
            const postData = {
                idRentar: parseInt(rentaId),
                idUsuario: rentaTarget.idUsuario,
                idPelicula: rentaTarget.idPelicula,
                fecha_renta: rentaTarget.fecha_renta,
                dias_de_renta: rentaTarget.dias_de_renta,
                estatus: nuevoEstatus
            };

            console.log(postData);
            onActualizarRenta(postData);
        } else {
            console.log("Renta no encontrada");
        }

        navigate('/');
    }

    return (
        <div>
            <h1 className={classes.header}>Actualizar renta</h1>
            <form onSubmit={submitHandler}>
                <label htmlFor="rent_id">Ingrese el ID de la renta a actualizar:</label>
                <input type="text" name="rent_id" id="rent_id" value={rentaId} onChange={rentaIdHandler} required />
                <br />
                <label htmlFor="status">Seleccione el nuevo estatus:</label>
                <select name="status" id="status" onChange={estatusHandler}>
                    <option value="false">No devuelta</option>
                    <option value="true">Devuelta</option>
                </select>
                <br />
                <button type="submit">Actualizar renta</button>
            </form>
        </div>
    );
}

export default RentaActualiza;
