const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const cors = require("cors"); // Import the cors package
const app = express();
const PORT = 5000;
app.use(cors()); // Enable CORS for all routes
app.use(express.json());

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
async function scrapeAmazon(product) {
  const url = `https://www.amazon.com/s?k=${product}`;
  const { data } = await axios.get(url);
  console.log("this is data;", data);
  const $ = cheerio.load(data);

  const products = [];
  $("#search .s-title").each((index, element) => {
    const title = $(element).text();
    const price = $(element)
      .closest(".s-result-item")
      .find(".a-price .a-offscreen")
      .first()
      .text();
    const link = $(element).closest(".s-title").find("a").attr("href");

    if (title && price) {
      products.push({ title, price, link: `https://www.amazon.com${link}` });
      console.log(title, price);
    }
  });
  return products;
}

async function scrapeFlipkart(product) {
  const url = `https://www.flipkart.com/search?q=${product}`;
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);

  const products = [];
  $("._4rR01T").each((index, element) => {
    const title = $(element).text();
    const price = $(element).closest("._1_WHN1").text();
    const link = $(element).closest("a").attr("href");

    if (title && price) {
      products.push({ title, price, link: `https://www.flipkart.com${link}` });
    }
  });
  return products;
}
function findCommonProducts(amazonProducts, flipkartProducts) {
  const commonProducts = [];

  amazonProducts.forEach((amazonProduct) => {
    flipkartProducts.forEach((flipkartProduct) => {
      if (
        amazonProduct.title.toLowerCase() ===
        flipkartProduct.title.toLowerCase()
      ) {
        commonProducts.push({
          title: amazonProduct.title,
          amazon: amazonProduct,
          flipkart: flipkartProduct,
        });
      }
    });
  });

  return commonProducts;
}
app.get("/compare", async (req, res) => {
  const { product } = req.query;
  try {
    console.log("this is the product:", product);
    const amazonProducts = await scrapeAmazon(product);
    const flipkartProducts = await scrapeFlipkart(product);

    const commonProducts = findCommonProducts(amazonProducts, flipkartProducts);

    res.json(commonProducts);
  } catch (error) {
    res.status(500).send("Error scraping data");
  }
});
