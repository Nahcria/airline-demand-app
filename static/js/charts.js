// Fetch the API data and render a chart
fetch("/api/data")
  .then((response) => response.json())
  .then((data) => {
    const routeLabels = data.map((d) => `${d.origin} → ${d.destination}`);
    const prices = data.map((d) => d.price);

    const ctx = document.getElementById("priceChart").getContext("2d");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: routeLabels,
        datasets: [
          {
            label: "Flight Prices ($)",
            data: prices,
            backgroundColor: "rgba(54, 162, 235, 0.7)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
          },
          title: {
            display: true,
            text: "Price by Route",
          },
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  });
