import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import classes from './PeliculaAgrega.module.css';

function PeliculaAgrega({ onAgregarPelicula, onIncrementaIdPelicula, id}) {
  const navigate = useNavigate('');

  const [nombre, setNombre] = useState('');
  const [genero, setGenero] = useState('');
  const [duracion, setDuracion] = useState('');
  const [inventario, setInventario] = useState('');

  function nombreHandler(event){
    setNombre(event.target.value);
  }
  
  function generoHandler(event){
    setGenero(event.target.value);
  }

  function duracionHandler(event){
    setDuracion(event.target.value);
  }

  function inventarioHandler(event){
    setInventario(event.target.value);
  }

  function submitHandler(event) {
    event.preventDefault();

    onIncrementaIdPelicula();

    const postData = {
        idPelicula: id,
        nombre: nombre,
        genero: genero,
        duracion: duracion,
        inventario: inventario,
    };
    
    onAgregarPelicula(postData); 
    navigate('/');
  }

  return (
    <div>
      <h1 className={classes.header}>Agregar película</h1>
      <form onSubmit={submitHandler}>
        <label htmlFor="name">Ingrese el nombre:</label>
        <input
          type="text"
          name="name"
          id="name"
          required
          value={nombre}
          onChange={nombreHandler}
        />
        <br />
        <label htmlFor="genre">Ingrese el género:</label>
        <input
          type="text"
          name="genre"
          id="genre"
          value={genero}
          onChange={generoHandler}
        />
        <br />
        <label htmlFor="length">Ingrese la duración en minutos:</label>
        <input
          type="number"
          name="length"
          id="length"
          value={duracion}
          onChange={duracionHandler}
        />
        <br />
        <label htmlFor="stock">Ingrese un número representando el inventario:</label>
        <input
          type="number"
          name="stock"
          id="stock"
          required
          value={inventario}
          onChange={inventarioHandler}
        />
        <br />
        <button type="submit">Agregar película</button>
      </form>
    </div>
  );
}

export default PeliculaAgrega;
