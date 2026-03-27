// Select the element with id 'toggle_header'
const toggleHeaderDiv = document.querySelector('#toggle_header');
// Select the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the toggleHeaderDiv
toggleHeaderDiv.addEventListener('click', () => {
  // Check if the current class is 'red'
  if (headerElement.classList.contains('red')) {
    // If it is red, remove it and add green
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    // If it is not red (meaning it is green), remove green and add red
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
