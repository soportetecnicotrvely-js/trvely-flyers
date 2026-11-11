# Generador de flyers Trvely

Aplicación web para crear flyers de ofertas de viaje de forma dinámica (plantilla de oferta vertical 9:16), con vista previa en vivo y descarga en PNG.

## Qué hace hoy
- Destino, hotel (filtrado por destino), precio, noches, frase y etiqueta "Solo por hoy".
- Casillas de "qué incluye" (vuelos, traslados, estadía, etc.).
- Banco de 51 fotos únicas por destino, o subir una foto propia.
- 51 logos de hoteles que se cargan solos al elegir el hotel.
- Selector de tipografía (Montserrat de la guía de marca y las de los flyers actuales) y de color.
- Importar lista de hoteles en CSV (`destino;hotel`) y subir logo por hotel (se guarda en el navegador).

## Estructura
```
index.html            la app lista para abrir (generada, no se edita a mano)
src/template.html     código fuente de la app (aquí se hacen los cambios)
data/assets.json      logo Trvely y fotos del banco (en base64)
data/hoteles.json     hoteles con su logo (en base64)
data/*.csv, *.sqlite  catálogo de los 87 flyers analizados y volumen por día
assets-fuente/        logos de hoteles y fotos recortadas como archivos sueltos
tools/build.py        reconstruye index.html
```

## Usarla en local
Abrir `index.html` en el navegador (necesita internet para cargar las tipografías de Google Fonts).

## Modificar y reconstruir
1. Editar `src/template.html` o los JSON de `data/`.
2. Ejecutar `python tools/build.py` (requiere Python 3).
3. Subir los cambios con Git (ver abajo).

## Subir a GitHub (paso a paso)

### 1. Preparar
1. Crear una cuenta en https://github.com (o usar la de la empresa).
2. Instalar Git: https://git-scm.com/downloads (o **GitHub Desktop**: https://desktop.github.com, más fácil si no usa la terminal).
3. Descomprimir este proyecto en una carpeta.

### 2. Crear el repositorio en GitHub
1. En GitHub: botón **New** (o **+ → New repository**).
2. Nombre sugerido: `trvely-flyers`.
3. Marcarlo como **Private** (contiene logos y material de la marca).
4. **No** marcar "Add a README" ni ".gitignore" (ya vienen incluidos).
5. **Create repository**.

### 3. Subir con la terminal
Dentro de la carpeta del proyecto:
```bash
git init
git add .
git commit -m "Primera versión del generador de flyers"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/trvely-flyers.git
git push -u origin main
```
(Reemplace `TU-USUARIO`. GitHub pedirá iniciar sesión; si pide contraseña, use un *Personal Access Token*: Settings → Developer settings → Personal access tokens.)

### 3 (alternativa). Con GitHub Desktop
1. **File → Add local repository** y elegir la carpeta (si lo pide, "create a repository").
2. Escribir un mensaje del commit y pulsar **Commit to main**.
3. **Publish repository**, dejar marcado **Keep this code private**.

### 3 (alternativa). Desde el navegador
El navegador acepta hasta 100 archivos por carga. Este proyecto tiene unos 130, así que súbalo en dos tandas: primero `index.html`, `README.md`, `src/`, `tools/` y `data/`; luego `assets-fuente/`. En el repositorio: **Add file → Upload files**.

### 4. Publicar la app en internet (opcional)
- **GitHub Pages:** Settings → Pages → Source: *Deploy from a branch* → rama `main`, carpeta `/ (root)`. La app queda en `https://TU-USUARIO.github.io/trvely-flyers/`. Ojo: en repositorios privados, Pages requiere un plan de pago de GitHub; con cuenta gratuita el repositorio tendría que ser público.
- **Alternativa con repo privado y gratis:** Cloudflare Pages o Netlify (conectan el repositorio y lo publican solos).

## Antes de compartir el repositorio
- No suba el chat de WhatsApp ni los flyers originales (el `.gitignore` ya los excluye).
- Los hoteles y logos que cada persona importa o sube se guardan solo en su navegador; para que todos los vean, deben agregarse a `data/hoteles.json` y reconstruir.

## Pendiente
- Cargar la lista oficial de hoteles y asociar cada logo.
- Mascotas por destino y los íconos de la marca (faltan los archivos originales).
- Fotos originales de las galerías de hoteles (las actuales son recortes de baja resolución).
- Plantillas 4:5, 2x1 y pasadías.
