import React from "react";
import Card from "./Card";
import Button from "./Button";
import './CrudSection.css'

function CrudPelicula() {
    return(
        <div className="crud-section">
            <Card>
                    <Button reference="/pelicula-agregar" className="create" message="Agregar película"/>
                    <Button reference="/pelicula-consultar" message="Consultar películas"/>
                    <Button reference="/pelicula-actualizar" message="Actualizar película"/>
                    <Button reference="/pelicula-borrar" message="Borrar película"/>
            </Card>
        </div>
    )
}

export default CrudPelicula;