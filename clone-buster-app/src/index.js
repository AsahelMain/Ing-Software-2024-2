import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';

import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import UsuarioConsulta from './components/Usuario/UsuarioConsulta';
import UsuarioAgrega from './components/Usuario/UsuarioAgrega';

const AppWithRouter = () => {
  const [usuarios, setUsuarios] = useState([
    {
      "idUsuario": 1,
      "nombre": "Jorge",
      "apPat": "Perez",
      "apMat": "Lopez",
      "password": "agua",
      "email": "jorgeperez@gmail.com",
      "superUser": 0
    },
    {
      "idUsuario": 2,
      "nombre": "Maria",
      "apPat": "Gonzalez",
      "apMat": "Martinez",
      "password": "verde",
      "email": "mariagonzalez@gmail.com",
      "superUser": 0
    },
    {
      "idUsuario": 3,
      "nombre": "Carlos",
      "apPat": "Garcia",
      "apMat": "Rodriguez",
      "password": "gato",
      "email": "carlosgarcia@gmail.com",
      "superUser": 1
    },
    {
      "idUsuario": 4,
      "nombre": "Laura",
      "apPat": "Lopez",
      "apMat": "Hernandez",
      "password": "jwjue",
      "email": "lauralopez@gmail.com",
      "superUser": 0
    },
    {
      "idUsuario": 5,
      "nombre": "Alejandro",
      "apPat": "Martinez",
      "apMat": "Perez",
      "password": "casa",
      "email": "alejandromartinez@gmail.com",
      "superUser": 1
    },
    {
      "idUsuario": 6,
      "nombre": "Sofia",
      "apPat": "Diaz",
      "apMat": "Gutierrez",
      "password": "maria22",
      "email": "sofiadiaz@gmail.com",
      "superUser": 0
    }
  ]);

  const [id, setId] = useState(7);

  function incrementaId() {
      const nuevoId = id + 1;
      setId(nuevoId);
  }

  function agregarUsuario(nuevoUsuario) {
     setUsuarios((usuarios) => [...usuarios, nuevoUsuario]);
  }

  const router = createBrowserRouter([
      {path: '/', element: <App />},
      {path: '/usuario-consultar', element: <UsuarioConsulta usuarios={usuarios} />},
      {path: '/usuario-agregar', element: <UsuarioAgrega onAgregarUsuario={agregarUsuario} onIncrementaId={incrementaId} id={id}/>}
  ]);

  return (
    <React.StrictMode>
      <RouterProvider router={router}/>
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<AppWithRouter />);

reportWebVitals();