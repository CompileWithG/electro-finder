<template>
  <div>
    <input 
      type="text" 
      v-model="searchQuery" 
      placeholder="Search products..."
      class="search-bar"
      @keyup.enter="performSearch"
    >
    <button @click="performSearch" class="search-button">Search</button>

    <div v-if="loading" class="loading">Loading products...</div>

    <div v-else-if="hasSearched && filteredProducts.length === 0" class="no-results">
      No products found for "{{ searchQuery }}". Try a different search term.
    </div>

    <div v-else-if="hasSearched" class="product-grid">
      <div 
        v-for="product in filteredProducts" 
        :key="product.link || index" 
        class="product-card"
      >
        <img :src="product.image" :alt="product.name" class="product-image">
        <div class="product-details">
          <h3>{{ product.name }}</h3>
          <div class="price-section">
            <span class="discount-price">{{ product.discount_price }}</span>
            <span class="actual-price">{{ product.actual_price }}</span>
          </div>
          <div class="ratings">
            <span class="rating-stars">{{ product.ratings }} ★</span>
            <span class="rating-count">({{ product.no_of_ratings }} ratings)</span>
          </div>
          <a :href="product.link" target="_blank" class="buy-button">Buy Now</a>
          <button @click="addToCart(product)" class="cart-button">Add to Cart</button>
        </div>
      </div>
    </div>

    <div v-else class="initial-state">
      Enter a product name, category, or subcategory to search for products.
    </div>
  </div>
</template>

<script>
import Papa from 'papaparse'

export default {
  data() {
    return {
      searchQuery: '',
      products: [],
      loading: true,
      hasSearched: false
    }
  },
  computed: {
    filteredProducts() {
      const query = this.searchQuery.toLowerCase().trim()
      if (!query) return []
      
      return this.products.filter(product => {
        // Safe property access with null checks
        const name = product.name ? product.name.toLowerCase() : '';
        const mainCategory = product.main_category ? product.main_category.toLowerCase() : '';
        const subCategory = product.sub_category ? product.sub_category.toLowerCase() : '';
        
        return name.includes(query) || 
               mainCategory.includes(query) || 
               subCategory.includes(query);
      });
    }
  },
  async mounted() {
    try {
      const response = await fetch('/products.csv') // Put your CSV in public folder
      const csvData = await response.text()
      
      Papa.parse(csvData, {
        header: true,
        complete: (results) => {
          // Filter out invalid entries
          this.products = results.data.filter(product => 
            product && typeof product === 'object' && product.name
          );
          
          console.log('Loaded products:', this.products.length);
          this.loading = false;
        },
        error: (error) => {
          console.error('Error parsing CSV:', error)
          this.loading = false
        }
      })
    } catch (error) {
      console.error('Error loading CSV:', error)
      this.loading = false
    }
  },
  methods: {
    performSearch() {
      if (this.searchQuery.trim()) {
        this.hasSearched = true;
        console.log('Searching for:', this.searchQuery);
        console.log('Found products:', this.filteredProducts.length);
      }
    },
    addToCart(product) {
      // Implement your cart logic here
      console.log('Added to cart:', product)
      alert(`Added ${product.name} to cart!`)
    }
  }
}
</script>

<style scoped>
.search-bar {
  width: calc(100% - 110px);
  padding: 15px;
  margin: 20px 0;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
}

.search-button {
  width: 100px;
  padding: 15px;
  margin: 20px 0;
  font-size: 16px;
  background-color: #007185;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image {
  width: 100%;
  height: 200px;
  object-fit: contain;
  padding: 10px;
  background: #f5f5f5;
}

.product-details {
  padding: 15px;
}

.price-section {
  margin: 10px 0;
}

.discount-price {
  color: #B12704;
  font-size: 1.2em;
  font-weight: bold;
  margin-right: 10px;
}

.actual-price {
  color: #565959;
  text-decoration: line-through;
}

.ratings {
  margin: 10px 0;
  color: #007185;
}

.buy-button, .cart-button {
  display: inline-block;
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  text-align: center;
  border-radius: 4px;
  cursor: pointer;
}

.buy-button {
  background-color: #FFA41C;
  color: black;
  border: 1px solid #FF8F00;
}

.cart-button {
  background-color: #007185;
  color: white;
  border: none;
}

.loading {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
}

.initial-state, .no-results {
  text-align: center;
  padding: 40px;
  font-size: 1.2em;
  color: #565959;
  background: #f9f9f9;
  border-radius: 8px;
  margin-top: 20px;
}
</style>