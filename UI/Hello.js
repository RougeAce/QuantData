var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "My First Dataset",
          data: [65, 59, 80, 81, 56, 55, 40],
          fill: false,
          borderColor: "rgb(75, 192, 192)",
          tension: 0.1,
        },
      ],
    },
    options: {},
  });

var options = ["AAPL", "META", "TSLA", "ALPA", "IGA"];

function showOptions() {
  var input = document.getElementById("searchInput").value;
  var optionsDiv = document.getElementById("optionsDiv");
  optionsDiv.innerHTML = "";

  for (var i = 0; i < options.length; i++) {
    var option = options[i];
    if (option.toLowerCase().indexOf(input.toLowerCase()) !== -1) {
      var optionDiv = document.createElement("div");
      optionDiv.innerHTML = option;
      optionsDiv.appendChild(optionDiv);
    }
  }
}
