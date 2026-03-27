// URL to fetch the character data
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
// Select the element with id 'character'
const characterDiv = document.querySelector('#character');

// Use Fetch API to get the data
fetch(url)
  .then(response => {
    // Convert the response to JSON format
    return response.json();
  })
  .then(data => {
    // Extract the name from the data and update the characterDiv
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    // Log any errors to the console
    console.error('Error:', error);
  });
