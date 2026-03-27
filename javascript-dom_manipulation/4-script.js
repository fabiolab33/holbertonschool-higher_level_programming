// Select the element with id 'add_item'
const addItemDiv = document.querySelector('#add_item');
// Select the ul element with class 'my_list'
const myListUl = document.querySelector('.my_list');

// Add a click event listener to the addItemDiv
addItemDiv.addEventListener('click', () => {
  // Create a new li element
  const newLi = document.createElement('li');
  // Set the text content of the new li element
  newLi.textContent = 'Item';
  // Append the new li element to the ul list
  myListUl.appendChild(newLi);
});
