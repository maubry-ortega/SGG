// JS para búsqueda y paginación de tabla de guías

document.addEventListener("DOMContentLoaded", () => {
  const rowsPerPage = 5;
  const table = document.getElementById("guiasTable");
  const tbody = table.querySelector("tbody");
  const rows = Array.from(tbody.querySelectorAll("tr"));
  const pagination = document.getElementById("pagination");
  const searchInput = document.getElementById("searchInput");

  let currentPage = 1;

  function filterRows(query) {
    return rows.filter(row =>
      row.textContent.toLowerCase().includes(query.toLowerCase())
    );
  }

  function renderTable(page = 1) {
    const filteredRows = filterRows(searchInput.value);
    const totalPages = Math.ceil(filteredRows.length / rowsPerPage);

    tbody.innerHTML = "";
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    filteredRows.slice(start, end).forEach(row => tbody.appendChild(row));

    renderPagination(totalPages, page);
  }

  function renderPagination(totalPages, current) {
    pagination.innerHTML = "";
    for (let i = 1; i <= totalPages; i++) {
      const btn = document.createElement("button");
      btn.textContent = i;
      btn.className = i === current ? "btn btn-primary disabled" : "btn btn-primary";
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

  renderTable(currentPage);
});
