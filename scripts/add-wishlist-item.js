const fs = require('fs');
const path = require('path');

const person = process.env.PERSON;
const title = process.env.TITLE;
const description = process.env.DESCRIPTION;
const price = parseInt(process.env.PRICE, 10);
const link = process.env.LINK;
const imageUrl = process.env.IMAGE_URL;

// Validate inputs
if (!person || !title || !description || !price || !link || !imageUrl) {
  console.error('Missing required environment variables');
  process.exit(1);
}

if (!['frans', 'bosse'].includes(person)) {
  console.error('Person must be either "frans" or "bosse"');
  process.exit(1);
}

// Read the data.js file
const dataFilePath = path.join(__dirname, '..', 'data.js');
let dataContent = fs.readFileSync(dataFilePath, 'utf8');

// Create the new item
const newItem = {
  title: title,
  description: description,
  price: price,
  link: link,
  image: imageUrl,
  bought: false
};

// Format the new item as a JavaScript object string
const itemString = `    {
      title: ${JSON.stringify(title)},
      description: ${JSON.stringify(description)},
      price: ${price},
      link: ${JSON.stringify(link)},
      image: ${JSON.stringify(imageUrl)},
      bought: false
    }`;

// Find the position to insert the new item
// We need to find the array for the person and add the item at the end
const personArrayRegex = new RegExp(`(${person}:\\s*\\[)([\\s\\S]*?)(\\n  \\])`, 'g');

dataContent = dataContent.replace(personArrayRegex, (match, start, items, end) => {
  // Check if there are existing items
  const trimmedItems = items.trim();
  if (trimmedItems) {
    return `${start}${items},\n${itemString}${end}`;
  } else {
    return `${start}\n${itemString}${end}`;
  }
});

// Write the updated content back to the file
fs.writeFileSync(dataFilePath, dataContent, 'utf8');

console.log(`Successfully added "${title}" to ${person}'s wishlist`);
