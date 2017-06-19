
var ctx2 = document.getElementById('live').getContext('2d');
var myChart2 = new Chart(ctx2,{
    type: 'line',
    data: {
        labels: ["1:15PM","1:30PM","1.45PM", "2.00PM", "2.15PM"],
        datasets: [{
            data: [100,200,300,50,230],
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