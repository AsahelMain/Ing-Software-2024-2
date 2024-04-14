import React from 'react';
import Header from './components/Header/Header';
import CrudPelicula from './components/CrudSection/CrudPelicula';
import CrudRenta from './components/CrudSection/CrudRenta';
import CrudUsuario from './components/CrudSection/CrudUsuario';

function App() {
  return (
    <div>
      <Header />
      <div className='crud-section'>
          <CrudUsuario />
          <CrudPelicula />
          <CrudRenta />
      </div>
    </div>  
  );
}

export default App;