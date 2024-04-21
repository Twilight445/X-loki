// Import the Express.js module
const express = require('express');

// Create an Express application
const app = express();

// Define a route handler for the root URL
app.get('/', (req, res) => {
  // Send a response to the client
  res.send('Hello, world!');
});

// Specify the port to listen on
const port = 3000;

// Start the server and listen for incoming connections
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
