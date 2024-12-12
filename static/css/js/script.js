let chart;
function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            // Update stats
            document.getElementById('pm25').innerText = `PM2.5: ${data['PM2.5']}`;
            document.getElementById('pm10').innerText = `PM10: ${data['PM10']}`;
            document.getElementById('co2').innerText = `CO2: ${data['CO2']}`;

            // Update chart
            updateChart(data);
        });
}

function updateChart(data) {
    const now = data.timestamp;
    chart.data.labels.push(now);
    chart.data.datasets[0].data.push(data['PM2.5']);
    chart.data.datasets[1].data.push(data['PM10']);
    chart.data.datasets[2].data.push(data['CO2']);
    chart.update();
}

// Initialize chart
function initializeChart() {
    const ctx = document.getElementById('lineChart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                { label: 'PM2.5', borderColor: 'red', data: [] },
                { label: 'PM10', borderColor: 'blue', data: [] },
                { label: 'CO2', borderColor: 'green', data: [] }
            ]
        },
        options: {
            responsive: true,
            scales: { y: { beginAtZero: true } }
        }
    });
}

// Start fetching data
initializeChart();
setInterval(fetchData, 5000);