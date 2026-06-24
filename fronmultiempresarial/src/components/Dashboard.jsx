import { useState } from "react";
import { LineChart } from "lucide-react";

/*
  ============================================================================
  DASHBOARD DE GRAFICAS
  ============================================================================
  Aqui los estudiantes muestran las graficas que generaron con Python.

  PASOS:
  1. Corran la rutina de Python (main.py). Eso crea las imagenes .png
     dentro de:  analiticamultiempresarial/graficas/
  2. COPIEN esas imagenes .png a la carpeta:  fronmultiempresarial/public/graficas/
  3. En la lista "GRAFICAS" de abajo, escriban el TITULO y la URL de cada imagen.
       - La URL empieza con "/graficas/"  (porque esta en la carpeta public)
       - Ejemplo:  url: "/graficas/1_usuarios_adultos_por_nombre.png"

  Si la imagen todavia no existe (no han corrido Python o no la han copiado),
  la tarjeta mostrara el mensaje "Imagen no disponible".
  ============================================================================
*/

//  <-- EDITEN ESTA LISTA: agreguen un objeto por cada grafica que quieran mostrar.
//      Formato de cada objeto:  { titulo: "Mi grafica", url: "/graficas/mi_imagen.png" }
//      Empieza vacia a proposito: aqui NO hay ninguna grafica precargada.
const GRAFICAS = [
  { titulo: "Grafica 1 - Cantidad de usuarios por nombre", url: "/graficas/grafica1.png" },
  { titulo: "Grafica 2 - Edad promedio por correo", url: "/graficas/grafica2.png" },
  { titulo: "Grafica 3 - Suma de edades de usuarios jovenes por nombre", url: "/graficas/grafica3.png" },
  { titulo: "Grafica 4 - Cantidad de usuarios por edad", url: "/graficas/grafica4.png" },
  { titulo: "Grafica 5 - Resumen por nombre", url: "/graficas/grafica5.png" },
  { titulo: "Grafica 6 - Total gastado por descripcion", url: "/graficas/grafica6.png" },
  { titulo: "Grafica 7 - Promedio de gasto por descripcion", url: "/graficas/grafica7.png" },
  { titulo: "Grafica 8 - Cantidad de gastos por usuario", url: "/graficas/grafica8.png" },
  { titulo: "Grafica 9 - Gastos grandes por descripcion", url: "/graficas/grafica9.png" },
  { titulo: "Grafica 10 - Resumen por descripcion", url: "/graficas/grafica10.png" },
];


//Tarjeta de UNA grafica. Si la imagen no carga, muestra un aviso.
function TarjetaGrafica({ titulo, url }) {
  const [error, setError] = useState(false);

  return (
    <div className="glass overflow-hidden rounded-2xl">
      <div className="border-b border-white/10 px-5 py-3">
        <h3 className="font-medium text-slate-100">{titulo}</h3>
      </div>

      {error ? (
        //La imagen no existe todavia -> aviso
        <div className="flex h-64 flex-col items-center justify-center gap-2 px-6 text-center">
          <LineChart className="h-10 w-10 text-purple-400/60" />
          <p className="font-medium text-slate-200">Imagen no disponible</p>
          <p className="text-sm text-slate-400">
            Ejecuta <code className="rounded bg-white/10 px-1.5 py-0.5 text-fuchsia-200">main.py</code> en Python
            y copia la imagen a <code className="rounded bg-white/10 px-1.5 py-0.5 text-fuchsia-200">public/graficas/</code>
          </p>
        </div>
      ) : (
        //La imagen existe -> se muestra
        <img
          src={url}
          alt={titulo}
          className="w-full bg-white"
          onError={() => setError(true)}
        />
      )}
    </div>
  );
}


export default function Dashboard() {
  return (
    <section id="dashboard" className="relative py-24">
      {/* difuminado morado de fondo */}
      <div className="pointer-events-none absolute left-1/2 top-20 -z-10 h-80 w-[40rem] -translate-x-1/2 rounded-full bg-fuchsia-700/20 blur-3xl" />

      <div className="mx-auto max-w-6xl px-6">
        <div className="text-center">
          <h2 className="font-display text-4xl font-bold tracking-tight">
            Dashboard de <span className="text-degradado">gráficas</span>
          </h2>
          <p className="mt-3 text-slate-300">
            Visualiza las gráficas generadas con Python. Copia tus imágenes a{" "}
            <code className="rounded bg-white/10 px-2 py-0.5 text-fuchsia-200">public/graficas/</code>
          </p>
        </div>

        {/* Cuadricula de graficas */}
        {GRAFICAS.length === 0 ? (
          //Lista vacia -> aviso para que agreguen sus graficas
          <div className="mt-12 glass rounded-2xl px-6 py-16 text-center">
            <LineChart className="mx-auto h-12 w-12 text-purple-400/60" />
            <p className="mt-4 font-medium text-slate-200">Aún no hay gráficas</p>
            <p className="mt-1 text-sm text-slate-400">
              Agrega tus gráficas en la lista{" "}
              <code className="rounded bg-white/10 px-1.5 py-0.5 text-fuchsia-200">GRAFICAS</code>{" "}
              dentro de <code className="rounded bg-white/10 px-1.5 py-0.5 text-fuchsia-200">Dashboard.jsx</code>
            </p>
          </div>
        ) : (
          <div className="mt-12 grid gap-6 md:grid-cols-2">
            {GRAFICAS.map((g) => (
              <TarjetaGrafica key={g.url} titulo={g.titulo} url={g.url} />
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
