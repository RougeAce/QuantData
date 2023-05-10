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
