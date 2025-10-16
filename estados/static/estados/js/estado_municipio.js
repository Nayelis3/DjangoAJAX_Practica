function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {
  const estadoSelect = document.getElementById("estado");
  const municipiosTable = document.getElementById("municipios-table");
  const tbody = municipiosTable.querySelector("tbody");
  const mensaje = document.getElementById("mensaje");

  estadoSelect.addEventListener("change", () => {
    const estadoId = estadoSelect.value;
    mensaje.textContent = "Cargando municipios...";
    municipiosTable.classList.add("hidden");
    tbody.innerHTML = "";

    if (!estadoId) {
      mensaje.textContent = "Selecciona un estado para ver sus municipios.";
      return;
    }

    fetch(`/ajax/municipios/?estado_id=${estadoId}`, {
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => {
        if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
        return response.json();
      })
      .then((data) => {
        if (!data.municipios || data.municipios.length === 0) {
          mensaje.textContent = "No hay municipios disponibles para este estado.";
          municipiosTable.classList.add("hidden");
          return;
        }

        mensaje.textContent = "";
        municipiosTable.classList.remove("hidden");

        data.municipios.forEach((m, i) => {
          const row = document.createElement("tr");
          row.innerHTML = `<td>${i + 1}</td><td>${m.nombre}</td>`;
          tbody.appendChild(row);
        });
      })
      .catch((error) => {
        mensaje.textContent = "Error al cargar municipios. Inténtalo de nuevo.";
        municipiosTable.classList.add("hidden");
        console.error(error);
      });
  });
});
