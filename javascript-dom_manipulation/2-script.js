// Select the element with id 'red_header'
const redHeaderDiv = document.querySelector('#red_header');
// Select the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the redHeaderDiv
redHeaderDiv.addEventListener('click', () => {
  // Add the class 'red' to the header element
  headerElement.classList.add('red');
});
