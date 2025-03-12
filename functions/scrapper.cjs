const puppeteer = require("puppeteer");

(async () => {
  // Launch a new browser instance
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // Navigate to the target URL
  await page.goto("https://www.amazon.in/s?k=laptop", {
    waitUntil: "networkidle2",
  });

  // Scrape the data from Amazon
  const amazonData = await page.evaluate(() => {
    const results = [];
    const items = document.querySelectorAll(
      'div[data-component-type="s-search-result"]'
    );

    items.forEach((item) => {
      const priceElement = item.querySelector(".a-price .a-offscreen");
      const titleElement = item.querySelector("h2.a-size-medium");

      const price = priceElement ? priceElement.innerText : "N/A";
      const title = titleElement ? titleElement.innerText : "N/A";

      // Extract specifications from the title
      const specifications = extractSpecifications(title);

      results.push({
        title,
        price,
        specifications,
      });
    });

    // Function to extract specifications from the title
    function extractSpecifications(title) {
      const specs = {};
      const ramMatch = title.match(/(\d+GB)/i);
      const storageMatch = title.match(/(\d+GB (SSD|HDD))/i);
      const processorMatch = title.match(
        /(Intel|AMD) (Core|Ryzen) (\d+)(\w?)/i
      );
      const graphicsMatch = title.match(
        /(NVIDIA|AMD|Intel) (GeForce|Radeon|UHD|Graphics)/i
      );

      if (ramMatch) {
        specs.RAM = ramMatch[0];
      }
      if (storageMatch) {
        specs.Storage = storageMatch[0];
      }
      if (processorMatch) {
        specs.Processor = `${processorMatch[1]} ${processorMatch[2]} ${
          processorMatch[3]
        }${processorMatch[4] ? " " + processorMatch[4] : ""}`;
        specs.ProcessorGeneration = processorMatch[3];
      }
      if (graphicsMatch) {
        specs.GraphicsCard = graphicsMatch[0];
      }

      return specs;
    }

    return results;
  });

  // Now scrape Flipkart for each Amazon product
  const flipkartData = await Promise.all(
    amazonData.map(async (item) => {
      const productName = item.title.split(",")[0]; // Extract the product name
      const flipkartProduct = await scrapeFlipkart(productName);
      return {
        amazon: item,
        flipkart: flipkartProduct,
      };
    })
  );

  console.log(flipkartData);

  // Close the browser
  await browser.close();
})();

// Function to scrape Flipkart based on the product name
async function scrapeFlipkart(productName) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  try {
    // Navigate to Flipkart search
    await page.goto(
      `https://www.flipkart.com/search?q=${encodeURIComponent(productName)}`,
      {
        waitUntil: "networkidle2",
        timeout: 60000, // Increase timeout to 60 seconds
      }
    );

    // Scrape the data from Flipkart
    const flipkartData = await page.evaluate(() => {
      const item = document.querySelector("div._1AtVbE"); // Select the first product
      if (!item) return null;

      const titleElement = item.querySelector("a.s1Q9rs");
      const priceElement = item.querySelector("div._30jeq3");

      const title = titleElement ? titleElement.innerText : "N/A";
      const price = priceElement ? priceElement.innerText : "N/A";

      return {
        title,
        price,
        specifications: {}, // You can add more specifications if needed
      };
    });

    return flipkartData;
  } catch (error) {
    console.error(`Error scraping Flipkart for "${productName}":`, error);
    return null; // Return null or an empty object if there's an error
  } finally {
    await browser.close();
  }
}
