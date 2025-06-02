/**
 * Envía la ruta de carpeta escrita manualmente al backend
 */
async function seleccionarCarpeta() {
  const carpeta = document.getElementById("carpeta").value;

  if (!carpeta) {
    alert("Ingresa la ruta de la carpeta");
    return;
  }

  try {
    const respuesta = await window.pywebview.api.seleccionar_carpeta(carpeta);
    console.log("Respuesta del backend (manual):", respuesta);
  } catch (error) {
    console.error("Error al enviar carpeta:", error);
  }
}

/**
 * Inicia el proceso de renombrado de PDFs
 */
async function renombrar() {
  const carpeta = document.getElementById("carpeta").value;
  const clave = document.getElementById("clave").value;
  const prefijo = document.getElementById("prefijo").value;
  const sufijo = document.getElementById("sufijo").value;

  if (!carpeta || !clave) {
    alert("Carpeta y clave son obligatorias");
    return;
  }

  try {
    await window.pywebview.api.seleccionar_carpeta(carpeta);

    const resultado = await window.pywebview.api.renombrar_pdfs(prefijo, sufijo, clave);

    const salida = document.getElementById("resultado");
    if (resultado.error) {
      salida.textContent = "❌ " + resultado.error;
    } else {
      salida.textContent = `✅ ${resultado.renombrados} archivos renombrados correctamente`;
    }
  } catch (error) {
    document.getElementById("resultado").textContent = "❌ Error inesperado: " + error.message;
    console.error("Error en renombrado:", error);
  }
}

/**
 * Abre el diálogo nativo para seleccionar carpeta
 */
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btnSeleccionar").addEventListener("click", async () => {
    try {
      const ruta = await window.pywebview.api.abrir_dialogo_carpeta();
      if (ruta) {
        document.getElementById("carpeta").value = ruta;
      }
    } catch (error) {
      console.error("Error al abrir diálogo:", error);
    }
  });
});
