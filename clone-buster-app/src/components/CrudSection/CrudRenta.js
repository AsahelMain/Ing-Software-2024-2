import React from "react";
import Card from "./Card";
import Button from "./Button";
import './CrudSection.css'

function CrudRenta() {
    return(
        <div className="crud-section">
            <Card>
                    <Button reference="/renta-agregar" className="create" message="Agregar rentas"/>
                    <Button reference="/renta-consultar" message="Consultar renta"/>
                    <Button reference="/renta-actualizar" message="Actualizar renta"/>
            </Card>
        </div>
    )
}

export default CrudRenta;