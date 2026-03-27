// Select the element with id 'update_header'
const updateHeaderDiv = document.querySelector('#update_header');
// Select the header element
const headerElement = document.querySelector('header');

// Add a click event listener to the updateHeaderDiv
updateHeaderDiv.addEventListener('click', () => {
  // Update the text content of the header element
  headerElement.textContent = 'New Header!!!';
});
