document.addEventListener("DOMContentLoaded", () => {
  const rowsPerPage = 5;
  let currentPage = 1;
  let guias = [];

  const tbody = document.getElementById("guiasBody");
  const searchInput = document.getElementById("searchInput");
  const pagination = document.getElementById("pagination");

  async function cargarGuias() {
    try {
      const res = await fetch("http://127.0.0.1:5000/api/guias/");
      const data = await res.json();
      guias = data;
      renderTable(currentPage);
    } catch (error) {
      console.error("Error al obtener las guías:", error);
    }
  }

  function filtrarGuias(query) {
    return guias.filter(g =>
      JSON.stringify(g).toLowerCase().includes(query.toLowerCase())
    );
  }

  function renderTable(page = 1) {
    const filtradas = filtrarGuias(searchInput.value);
    const totalPages = Math.ceil(filtradas.length / rowsPerPage);

    tbody.innerHTML = "";
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    filtradas.slice(start, end).forEach(guia => {
      const fila = document.createElement("tr");

      fila.innerHTML = `
        <td>${guia.full_name}</td>
        <td>${guia.description}</td>
        <td>${guia.program.name}</td>
        <td>${guia.instructor.full_name}</td>
        <td>${guia.instructor.region}</td>
        <td>${new Date(guia.date).toLocaleDateString()}</td>
        <td><a href="/${guia.pdf_file}" target="_blank" class="btn btn-link">Ver</a></td>
      `;

      tbody.appendChild(fila);
    });

    renderPagination(totalPages, page);
  }

  function renderPagination(totalPages, current) {
    pagination.innerHTML = "";

    for (let i = 1; i <= totalPages; i++) {
      const btn = document.createElement("button");
      btn.textContent = i;
      btn.className = i === current ? "btn btn-primary disabled" : "btn btn-primary mx-1";
      if (i !== current) {
        btn.addEventListener("click", () => {
          currentPage = i;
          renderTable(currentPage);
        });
      }
      pagination.appendChild(btn);
    }
  }

  searchInput.addEventListener("input", () => {
    currentPage = 1;
    renderTable(currentPage);
  });

  cargarGuias();
});
