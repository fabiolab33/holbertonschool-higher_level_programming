// Define the API URL
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
// Select the UL element where movies will be listed
const listMoviesUl = document.querySelector('#list_movies');

// Fetch the data from the API
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Iterate through each movie in the results array
    data.results.forEach(movie => {
      // Create a new li element
      const newLi = document.createElement('li');
      // Set the text content to the movie title
      newLi.textContent = movie.title;
      // Append the li to the ul
      listMoviesUl.appendChild(newLi);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
