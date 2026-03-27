# JavaScript - DOM Manipulation

## Description
This project focuses on learning how to manipulate the DOM (Document Object Model) using JavaScript. It covers selecting elements, modifying styles and content, handling user events (like clicks), and performing asynchronous data fetching using the Fetch API.

## Learning Objectives
At the end of this project, I am able to:
* Select HTML elements using JavaScript selectors.
* Understand the differences between ID, class, and tag name selectors.
* Modify HTML element styles and content dynamically.
* Add and remove elements from the DOM.
* Handle user events (click, DOMContentLoaded).
* Make network requests using the Fetch API.

## Requirements
* All files are interpreted on Chrome browser (version 57.0 or later).
* All files end with a new line.
* The code is **semistandard** compliant.
* No `var` is used; only `const` and `let`.
* HTML does not reload for each action.

## Tasks


| Task | File | Description |
| --- | --- | --- |
| **0. Color Me** | `0-script.js` | Updates the text color of the `<header>` element to red (#FF0000) using `document.querySelector`. |
| **1. Click and turn red** | `1-script.js` | Updates the header color to red only when the user clicks on the element with ID `red_header`. |
| **2. Add .red class** | `2-script.js` | Adds the CSS class `red` to the `<header>` element when the element with ID `red_header` is clicked. |
| **3. Toggle classes** | `3-script.js` | Toggles the class of the `<header>` between `red` and `green` when the element with ID `toggle_header` is clicked. |
| **4. List of elements** | `4-script.js` | Adds a new `<li>Item</li>` to a `<ul>` with class `my_list` every time the element with ID `add_item` is clicked. |
| **5. Change the text** | `5-script.js` | Updates the text of the `<header>` to "New Header!!!" when the element with ID `update_header` is clicked. |
| **6. Star wars character** | `6-script.js` | Fetches a Star Wars character name from an API and displays it in the element with ID `character`. |
| **7. Star Wars movies** | `7-script.js` | Fetches all Star Wars movie titles from an API and lists them in the `<ul>` with ID `list_movies`. |
| **8. Say Hello!** | `8-script.js` | Fetches a greeting in French and displays it. The script works even when imported in the `<head>` by using the `DOMContentLoaded` event. |
