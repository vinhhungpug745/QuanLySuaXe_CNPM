function drawChart(lables, data, tilte, type){
   const ctx = document.getElementById('myChart');

    new Chart(ctx, {
    type: type,
    data: {
      labels: lables,
      datasets: [{
        label: tilte,
        data: data,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
   });
}