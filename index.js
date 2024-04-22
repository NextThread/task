const http = require('http');
const axios = require('axios');

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/detect') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString(); // Convert buffer to string
    });

    req.on('end', async () => {
      try {
        const { image_url } = JSON.parse(body);

        // Call your Flask service
        const apiUrl = 'http://localhost:5000/detect'; // Replace with your actual Flask service URL
        const response = await axios.post(apiUrl, { image_url });

        // Send response back to the client
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(response.data));
      } catch (error) {
        console.error('Error:', error);
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Internal Server Error' }));
      }
    });
  } else {
    // Handle invalid requests
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

const port = 3000; // You can change this to any available port
server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
