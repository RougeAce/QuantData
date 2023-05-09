document.addEventListener("DOMContentLoaded", function() {
    // get a reference to the stock price element in the HTML
    const stockPriceElement = document.getElementById('stock-price');

    // define a function to fetch data from the API and update the stock price element
    function updateStockPrice(query) {
      fetch(`/api/${query}`)
        .then(response => response.text())
        .then(data => {
          // update the stock price element with the retrieved data
          stockPriceElement.textContent = data;
          console.log(data);
        })
        .catch(error => console.error(error));
    }

    // call the updateStockPrice function initially to set the initial value
    updateStockPrice('AAPL'); // replace 'AAPL' with your desired query parameter

    // call the updateStockPrice function every second using setInterval()
    setInterval(() => {
      updateStockPrice('AAPL'); // replace 'AAPL' with your desired query parameter
    }, 1000); // repeat every 1000 milliseconds (1 second) 
  });