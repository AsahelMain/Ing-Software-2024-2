import React from "react";
import classes from './UsuarioConsulta.module.css'

function UsuarioConsulta({ usuarios }) {
    return (
        <div>
            <div className={classes.header}>
                <h1>Consulta de usuarios</h1>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Apellido Paterno</th>
                        <th>Apellido Materno</th>
                        <th>Correo</th>
                    </tr>
                </thead>
                <tbody>
                    {usuarios.map((usuario) => (
                        <tr key={usuario.idUsuario}>
                            <td>{usuario.idUsuario}</td>
                            <td>{usuario.nombre}</td>
                            <td>{usuario.apPat}</td>
                            <td>{usuario.apMat || ""}</td>
                            <td>{usuario.email || ""}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default UsuarioConsulta;


/**
 * 
 * return (
        <div>
            <h2>Lista de Usuarios</h2>
            <ul>
                {usuarios.map(usuario => (
                    <li key={usuario.idUsuario}>
                        {usuario.nombre} {usuario.apPat} {usuario.apMat}
                    </li>
                ))}
            </ul>
        </div>
    );
 */