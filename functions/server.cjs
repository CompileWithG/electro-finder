const express = require('express');
const { scrapeAmazon } = require('./scrapper.cjs');
const cors = require('cors');

const app = express();

// Configure CORS properly
app.use(cors({
  origin: 'http://localhost:3000', // Your Vue app's port
  methods: ['GET'],
  optionsSuccessStatus: 200
}));

// Fix the route definition order
app.get('/scrape', async (req, res) => {
  try {
    if (!req.query.product) {
      return res.status(400).json({ error: "Missing product parameter" });
    }
    
    const data = await scrapeAmazon(req.query.product);
    res.json(data);
  } catch (error) {
    console.error('Server error:', error);
    res.status(500).json({ 
      error: error.message,
      stack: process.env.NODE_ENV === 'development' ? error.stack : undefined // Fixed syntax
    });
  }
});

app.listen(3001, () => {
  console.log('Server running on port 3001');
  console.log('Test endpoint: http://localhost:3001/scrape?product=laptop');
});