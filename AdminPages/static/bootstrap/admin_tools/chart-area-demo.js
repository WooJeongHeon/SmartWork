// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily =
    '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById('myAreaChart');
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            '10월 22일',
            '10월 23일',
            '10월 24일',
            '10월 25일',
            '10월 26일',
            '10월 27일',
            '10월 28일',
            '10월 29일',
            '10월 30일',
            '10월 31일',
            '11월 1일',
            '11월 2일',
            '11월 3일'
        ],
        datasets: [
            {
                label: '출타 인원',
                lineTension: 0.3,
                backgroundColor: 'rgba(2,117,216,0.2)',
                borderColor: 'rgba(2,117,216,1)',
                pointRadius: 5,
                pointBackgroundColor: 'rgba(2,117,216,1)',
                pointBorderColor: 'rgba(255,255,255,0.8)',
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(2,117,216,1)',
                pointHitRadius: 50,
                pointBorderWidth: 2,
                data: [5, 4, 4, 3, 2, 4, 5, 5, 6, 4, 3, 3, 2]
            }
        ]
    },
    options: {
        scales: {
            xAxes: [
                {
                    time: {
                        unit: 'date'
                    },
                    gridLines: {
                        display: false
                    },
                    ticks: {
                        maxTicksLimit: 7
                    }
                }
            ],
            yAxes: [
                {
                    ticks: {
                        min: 0,
                        max: 20,
                        maxTicksLimit: 5
                    },
                    gridLines: {
                        color: 'rgba(0, 0, 0, .125)'
                    }
                }
            ]
        },
        legend: {
            display: false
        }
    }
});