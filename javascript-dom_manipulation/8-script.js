// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  // Define the API URL
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  // Select the element with id 'hello'
  const helloDiv = document.querySelector('#hello');

  // Fetch the data from the API
  fetch(url)
    .then(response => response.json())
    .then(data => {
      // Update the text content with the 'hello' value from the API
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching greeting:', error);
    });
});
