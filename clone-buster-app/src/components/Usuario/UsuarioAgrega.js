import React from "react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import classes from './UsuarioAgrega.module.css';

function UsuarioAgrega({ onAgregarUsuario, onIncrementaIdUsuario, id }) {
  const navigate = useNavigate('');

  const [nombre, setNombre] = useState('');
  const [apPat, setApPat] = useState('');
  const [apMat, setApMat] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [isSuperUser, setIsSuperUser] = useState('');

  function nombreHandler(event) {
    setNombre(event.target.value);
  }

  function apellidoPatHandler(event) {
    setApPat(event.target.value);
  }

  function apellidoMatHandler(event) {
    setApMat(event.target.value);
  }

  function passwordHandler(event) {
    setPassword(event.target.value);
  }

  function emailHandler(event) {
    setEmail(event.target.value);
  }

  function superUserHandler(event) {
    setIsSuperUser(event.target.value);
  }

  function submitHandler(event) {
    event.preventDefault();

    onIncrementaIdUsuario();

    const postData = {
        idUsuario: id,
        nombre: nombre,
        apPat: apPat,
        apMat: apMat,
        password: password,
        email: email,
        superUser: isSuperUser
        };
    
    onAgregarUsuario(postData); 
    navigate('/');
  }

  return (
    <div>
      <h1 className={classes.header}>Agregar usuario</h1>
      <form onSubmit={submitHandler}>
        <label htmlFor="name">Ingrese el nombre:</label>
        <input type="text" name="name" id="name" required onChange={nombreHandler}/>
        <br />
        <label htmlFor="ap_pat">Ingrese el apellido paterno:</label>
        <input type="text" name="ap_pat" id="ap_pat" required onChange={apellidoPatHandler}/>
        <br />
        <label htmlFor="ap_mat">Ingrese el apellido materno:</label>
        <input type="text" name="ap_mat" id="ap_mat" onChange={apellidoMatHandler}/>
        <br />
        <label htmlFor="password">Contraseña:</label>
        <input type="password" name="password" id="password" required onChange={passwordHandler} />
        <br />
        <label htmlFor="email">Correo electrónico:</label>
        <input type="text" name="email" id="email" onChange={emailHandler}/>
        <br />
        <label htmlFor="super_user">¿Es un super usuario?</label>
        <select name="super_user" id="super_user" onChange={superUserHandler}>
          <option value="no">No</option>
          <option value="yes">Sí</option>
        </select>
        <br />
        <button>Crear usuario</button>
      </form>
    </div>
  );
}

export default UsuarioAgrega;