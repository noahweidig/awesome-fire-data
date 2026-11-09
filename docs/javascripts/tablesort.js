document$.subscribe(function () {
  var sorters = [];
  document.querySelectorAll("article .sortable table").forEach(function (table) {
    sorters.push(new Tablesort(table));
  });
  var input = document.getElementById("dataset-filter");
  if (!input) return;
  input.addEventListener("input", function () {
    var q = input.value.toLowerCase();
    document.querySelectorAll("article .sortable tbody tr").forEach(function (row) {
      row.hidden = q && row.textContent.toLowerCase().indexOf(q) === -1;
    });
  });
});
