//line
var ctxL = document.getElementById("lineChart").getContext('2d');
var myLineChart = new Chart(ctxL, {
  type: 'line',
  data: {
    labels: ["Oct-17", "Nov-17", "Dec-18", "Jan-18", "Feb-18", "Mar-18", "Apr-18", "May-18", "Jun-18", "Jul-18", "Aug-18", "Sep-18", "Oct-18", "Nov-18", "Dec-18"],
    datasets: [{
        label: "negative",
        // data: [45, 59, 80, 81, 56, 55, 40, 78, 29, 89, 58, 38],
        data: neg,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
        ],
        borderColor: [
          'rgba(255,99,132,1)',
        ],
        borderWidth: 2
      },
      {
        label: "positive",
        // data: [28, 48, 40, 19, 86, 27, 90, 65, 59, 80, 81, 56],
          data: pos,
        backgroundColor: [
          'rgba(54, 162, 235, 0.2)',
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
        ],
        borderWidth: 2
      },
        {
        label: "neutrual",
        // data: [10, 20, 30, 40, 50, 55, 40, 19, 86, 27, 90, 65],
            data: neu,
        backgroundColor: [
          'rgba(255, 206, 86, 0.2)',
        ],
        borderColor: [
          'rgba(255, 206, 86, 1)',
        ],
        borderWidth: 2
      },

    ]
  },

  options: {
    responsive: true,
    // tooltipTemplate: "<%= value %>%",
    //   showTooltips: true,
  }
});