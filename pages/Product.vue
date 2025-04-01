<template>
  <div class="product-container">
    <NavBar/>
    <div class="search-container">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search products..."
        class="search-input"
        @keyup.enter="performSearch"
      >
      <button @click="performSearch" class="search-button">
        <span class="search-icon">🔍</span>
      </button>
    </div>

    <div v-if="loading" class="loading-text">Loading products...</div>

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
          <h3 class="product-title">{{ product.name }}</h3>
          <div class="price-section">
            <span class="discount-price">{{ product.discount_price }}</span>
            <span class="actual-price">{{ product.actual_price }}</span>
          </div>
          <div class="ratings">
            <span class="rating-stars">{{ product.ratings }} ★</span>
            <span class="rating-count">({{ product.no_of_ratings }} ratings)</span>
          </div>
          <div class="button-container">
            <a :href="product.link" target="_blank" class="buy-button">Buy Now</a>
            <button @click="addToCart(product)" class="cart-button">Add to Cart</button>
          </div>
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
import NavBar from '~/components/NavBar.vue'

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
.product-container {
  min-height: 100vh;
  background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
  padding: 40px 20px;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.search-container {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
  padding: 0 20px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.search-input {
  width: 80%;
  padding: 15px 25px;
  font-size: 1.2rem;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 30px 0 0 30px;
  color: #ffffff;
  outline: none;
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.7);
}

.search-button {
  padding: 15px 25px;
  background: #2563eb;
  border: none;
  border-radius: 0 30px 30px 0;
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.2rem;
}

.search-button:hover {
  background: #3b82f6;
}

.search-icon {
  display: inline-block;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem 5%;
  max-width: 1200px;
  margin: 0 auto;
}

.product-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.product-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.product-image {
  width: 100%;
  height: 220px;
  object-fit: contain;
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
}

.product-details {
  padding: 20px;
  color: #ffffff;
}

.product-title {
  font-size: 1.2rem;
  margin-bottom: 10px;
  color: #ffffff;
  height: 2.8em;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.price-section {
  margin: 15px 0;
}

.discount-price {
  color: #38bdf8;
  font-size: 1.4em;
  font-weight: bold;
  margin-right: 10px;
}

.actual-price {
  color: rgba(255, 255, 255, 0.6);
  text-decoration: line-through;
}

.ratings {
  margin: 10px 0;
  color: #f59e0b;
}

.button-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 15px;
}

.buy-button, .cart-button {
  padding: 12px;
  text-align: center;
  border-radius: 30px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s;
  text-decoration: none;
  font-size: 1rem;
}

.buy-button {
  background-color: #2563eb;
  color: white;
  border: none;
}

.buy-button:hover {
  background-color: #1d4ed8;
  transform: scale(1.05);
}

.cart-button {
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.cart-button:hover {
  background-color: rgba(255, 255, 255, 0.2);
  transform: scale(1.05);
}

.loading-text {
  text-align: center;
  font-size: 1.5rem;
  color: #ffffff;
  margin: 4rem 0;
}

.initial-state, .no-results {
  text-align: center;
  padding: 40px;
  font-size: 1.2rem;
  color: #ffffff;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  margin: 4rem auto;
  max-width: 700px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.no-results {
  color: #f87171;
}
</style>