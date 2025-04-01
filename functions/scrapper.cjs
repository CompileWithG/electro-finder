const puppeteer = require("puppeteer");

async function scrapeAmazon(productName) {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
    
    await page.goto(`https://www.amazon.in/s?k=${productName}`, {
      waitUntil: "networkidle2",
      timeout: 30000
    });

    const amazonData = await page.evaluate(() => {
      const results = [];
      const items = document.querySelectorAll('div[data-component-type="s-search-result"]');

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

      function extractSpecifications(title) {
        const specs = {};
        const ramMatch = title.match(/(\d+GB)/i);
        const storageMatch = title.match(/(\d+GB (SSD|HDD))/i);
        const processorMatch = title.match(/(Intel|AMD) (Core|Ryzen) (\d+)(\w?)/i);
        const graphicsMatch = title.match(/(NVIDIA|AMD|Intel) (GeForce|Radeon|UHD|Graphics)/i);

        if (ramMatch) specs.RAM = ramMatch[0];
        if (storageMatch) specs.Storage = storageMatch[0];
        if (processorMatch) {
          specs.Processor = `${processorMatch[1]} ${processorMatch[2]} ${processorMatch[3]}${processorMatch[4] ? " " + processorMatch[4] : ""}`;
          specs.ProcessorGeneration = processorMatch[3];
        }
        if (graphicsMatch) specs.GraphicsCard = graphicsMatch[0];

        return specs;
      }

      return results;
    });

    await page.close();
    return amazonData;
  } catch (error) {
    console.error('Scraping error:', error);
    throw error;
  } finally {
    await browser.close().catch(err => console.error('Browser close error:', err));
  }
}

module.exports = { scrapeAmazon };