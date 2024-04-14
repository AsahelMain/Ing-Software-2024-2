import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import classes from './RentaAgrega.module.css';

function RentaAgrega({ onAgregarRenta, onIncrementaIdRenta, id }) {
    const navigate = useNavigate('');

    const [usuarioId, setUsuarioId] = useState('');
    const [peliculaId, setPeliculaId] = useState('');
    const [fechaRenta, setFechaRenta] = useState('');
    const [diasRenta, setDiasRenta] = useState('');
    const [estatus, setEstatus] = useState(false);

    function usuarioIdHandler(event) {
        setUsuarioId(event.target.value);
    }

    function peliculaIdHandler(event) {
        setPeliculaId(event.target.value);
    }

    function fechaRentaHandler(event) {
        setFechaRenta(event.target.value);
    }

    function diasRentaHandler(event) {
        setDiasRenta(event.target.value);
    }

    function estatusHandler(event) {
        setEstatus(event.target.value === "true");
    }

    function submitHandler(event) {
        event.preventDefault();

        onIncrementaIdRenta();

        const postData = {
            idRentar: id,
            idUsuario: parseInt(usuarioId),
            idPelicula: parseInt(peliculaId),
            fecha_renta: fechaRenta,
            dias_de_renta: parseInt(diasRenta),
            estatus: estatus
        };

        onAgregarRenta(postData);
        navigate('/');
    }

    return (
        <div>
            <h1 className={classes.header}>Rentar película</h1>
            <form onSubmit={submitHandler}>
                <label htmlFor="user_id">ID Usuario:</label>
                <input 
                  type="text" 
                  name="user_id" 
                  id="user_id" 
                  required 
                  value={usuarioId}
                  onChange={usuarioIdHandler} />
                <br />
                <label htmlFor="movie_id">ID Película:</label>
                <input 
                  type="text" 
                  name="movie_id" 
                  id="movie_id" 
                  required 
                  value={peliculaId}
                  onChange={peliculaIdHandler} />
                <br />
                <label htmlFor="rent_date">Fecha de renta YYYY-MM-DD:</label>
                <input 
                  type="text" 
                  name="rent_date" 
                  id="rent_date" 
                  pattern="\d{4}-\d{2}-\d{2}" 
                  placeholder="YYYY-MM-DD" 
                  required 
                  value={fechaRenta}
                  onChange={fechaRentaHandler} />
                <br />
                <label htmlFor="rent_days">Días de renta:</label>
                <input 
                  type="number" 
                  name="rent_days" 
                  id="rent_days" 
                  value={diasRenta}
                  onChange={diasRentaHandler} />
                <br />
                <label htmlFor="status">Estatus:</label>
                <select name="status" id="status" value={estatus} onChange={estatusHandler}>
                    <option value="false">No devuelta</option>
                    <option value="true">Devuelta</option>
                </select>
                <br />
                <button type="submit">Agregar renta</button>
            </form>
        </div>
    );
}

export default RentaAgrega;
