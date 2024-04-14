import React from "react";
import Card from "./Card";
import Button from "./Button";
import './CrudSection.css'

function CrudUsuario({usuarios}) {
    return(
        <div className="crud-section">
            <Card>
                    <Button reference="/usuario-agregar" className="create" message="Agregar Usuario"/>
                    <Button reference="/usuario-consultar" className="read" message="Consultar Usuarios"/>
                    <Button reference="/usuario-actualizar" className="update" message="Actualizar Usuario"/>
                    <Button reference="/usuario-borrar" className="delete" message="Borrar Usuarios"/>
            </Card>
        </div>
    )
}

export default CrudUsuario;