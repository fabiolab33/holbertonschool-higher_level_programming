// Select the element with id 'red_header'
const redHeaderDiv = document.querySelector('#red_header');
// Select the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the redHeaderDiv
redHeaderDiv.addEventListener('click', () => {
  // Update the header text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
