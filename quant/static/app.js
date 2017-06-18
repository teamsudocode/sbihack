var ctx = document.getElementById("expenses").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["1 June","5 June","10 June", "15 June", "20 June"],
        datasets: [{
            data: [3500, 4500, 2500, 5000, 1200],
            backgroundColor: [
                'rgba(0, 168, 226, 0.2)'
            ],
            borderColor: [
                'rgba(0, 168, 226,1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        },
        responsive: true, maintainAspectRatio: false,legend:{
            display:false
        }
    }
});