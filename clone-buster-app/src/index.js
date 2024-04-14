import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';

import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import UsuarioConsulta from './components/Usuario/UsuarioConsulta';
import UsuarioAgrega from './components/Usuario/UsuarioAgrega';
import UsuarioBorra from './components/Usuario/UsuarioBorra';
import UsuarioActualiza from './components/Usuario/UsuarioActualiza';
import PeliculaConsulta from './components/Pelicula/PeliculaConsulta';
import PeliculaAgrega from './components/Pelicula/PeliculaAgrega';
import PeliculaBorra from './components/Pelicula/PeliculaBorra';
import PeliculaActualiza from './components/Pelicula/PeliculaActualiza';
import RentaConsulta from './components/Renta/RentaConsulta';
import RentaAgrega from './components/Renta/RentaAgrega';
import RentaActualiza from './components/Renta/RentaActualiza';

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

  const [idUsuario, setIdUsuario] = useState(7);


  const [peliculas, setPeliculas] = useState([
    {
      "idPelicula": 1,
      "nombre": "The Shining",
      "genero": "Terror",
      "duracion": "120",
      "inventario": "3"
    },
    {
      "idPelicula": 2,
      "nombre": "Inception",
      "genero": "Sci-Fi",
      "duracion": "148",
      "inventario": "5"
    },
    {
      "idPelicula": 3,
      "nombre": "The Godfather",
      "genero": "Drama",
      "duracion": "175",
      "inventario": "2"
    },
    {
      "idPelicula": 4,
      "nombre": "The Shawshank Redemption",
      "genero": "Drama",
      "duracion": "142",
      "inventario": "4"
    },
    {
      "idPelicula": 5,
      "nombre": "Jurassic Park",
      "genero": "Adventure",
      "duracion": "127",
      "inventario": "6"
    },
    {
      "idPelicula": 6,
      "nombre": "Forrest Gump",
      "genero": "Drama",
      "duracion": "142",
      "inventario": "7"
    }
  ]);

  const [idPelicula, setIdPelicula] = useState(7);

  const [rentas, setRentas] = useState([
    {
      "idRentar": 1,
      "idUsuario": 1,
      "idPelicula": 1,
      "fecha_renta": "2024-02-16",
      "dias_de_renta": 20,
      "estatus": 0
    },
    {
      "idRentar": 2,
      "idUsuario": 2,
      "idPelicula": 2,
      "fecha_renta": "2024-03-10",
      "dias_de_renta": 15,
      "estatus": 1
    },
    {
      "idRentar": 3,
      "idUsuario": 3,
      "idPelicula": 3,
      "fecha_renta": "2024-04-01",
      "dias_de_renta": 25,
      "estatus": 0
    },
    {
      "idRentar": 4,
      "idUsuario": 4,
      "idPelicula": 4,
      "fecha_renta": "2024-04-05",
      "dias_de_renta": 10,
      "estatus": 1
    },
    {
      "idRentar": 5,
      "idUsuario": 5,
      "idPelicula": 5,
      "fecha_renta": "2024-04-10",
      "dias_de_renta": 30,
      "estatus": 0
    },
    {
      "idRentar": 6,
      "idUsuario": 6,
      "idPelicula": 6,
      "fecha_renta": "2024-04-14",
      "dias_de_renta": 5,
      "estatus": 1
    }
  ]);

  const [idRenta, setIdRenta] = useState(7);

  function incrementaIdUsuario() {
      const nuevoId = idUsuario + 1;
      setIdUsuario(nuevoId);
  }

  function incrementaIdPelicula() {
      const nuevoId = idPelicula + 1;
      setIdPelicula(nuevoId);
  }

  function incrementaIdRenta() {
      const nuevoId = idRenta + 1;
      setIdRenta(nuevoId);
  }

  function agregarUsuario(nuevoUsuario) {
     setUsuarios((usuarios) => [...usuarios, nuevoUsuario]);
  }

  function agregarPelicula(nuevaPelicula) {
     setPeliculas((peliculas) => [...peliculas, nuevaPelicula]);
  }

  function agregarRenta(nuevaRenta) {
     setRentas((rentas) => [...rentas, nuevaRenta]);
 }

  function eliminaUsuario(idUsuario) {
    setUsuarios((usuarios) => usuarios.filter((usuario) => usuario.idUsuario !== parseInt(idUsuario)));
  }

  function eliminaPelicula(idPelicula) {
    setPeliculas((peliculas) => peliculas.filter((pelicula) => pelicula.idPelicula !== parseInt(idPelicula)));
  }

  function actualizaUsuario(usuarioActualizado) {
    setUsuarios((usuarios) =>
        usuarios.map((usuario) =>
            usuario.idUsuario === usuarioActualizado.idUsuario ? { ...usuario, ...usuarioActualizado } : usuario
        )
    );
  }

  function actualizaPelicula(peliculaActualizada) {
    setPeliculas((peliculas) =>
      peliculas.map((pelicula) =>
          pelicula.idPelicula === peliculaActualizada.idPelicula ? { ...pelicula, ...peliculaActualizada } : pelicula
      )
    );
  }

  function actualizaRenta(rentaActualizada) {
    setRentas((rentas) =>
      rentas.map((renta) =>
          renta.idRentar === rentaActualizada.idRentar ? { ...renta, ...rentaActualizada } : renta
      )
    );
  }

  const router = createBrowserRouter([

      {path: '/', element: <App />},
      {path: '/usuario-consultar', element: <UsuarioConsulta usuarios={usuarios} />},
      {path: '/usuario-agregar', element: <UsuarioAgrega onAgregarUsuario={agregarUsuario} onIncrementaIdUsuario={incrementaIdUsuario} id={idUsuario}/>},
      {path: '/usuario-borrar', element: <UsuarioBorra onEliminarUsuario={eliminaUsuario} />},
      {path: '/usuario-actualizar', element: <UsuarioActualiza usuarios={usuarios} onActualizarUsuario={actualizaUsuario}/>},

      {path: '/pelicula-consultar', element: <PeliculaConsulta peliculas={peliculas}/>},
      {path: '/pelicula-agregar', element: <PeliculaAgrega onAgregarPelicula={agregarPelicula} onIncrementaIdPelicula={incrementaIdPelicula} id={idPelicula}/>},
      {path: '/pelicula-borrar', element: <PeliculaBorra onEliminarPelicula={eliminaPelicula} />},
      {path: '/pelicula-actualizar', element: <PeliculaActualiza peliculas={peliculas} onActualizarPelicula={actualizaPelicula}/>},


      {path: '/renta-consultar', element: <RentaConsulta rentas={rentas}/>},
      {path: '/renta-agregar', element: <RentaAgrega onAgregarRenta={agregarRenta} onIncrementaIdRenta={incrementaIdRenta} id={idRenta}/>},
      {path: '/renta-actualizar', element: <RentaActualiza rentas={rentas} onActualizarRenta={actualizaRenta}/>}
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