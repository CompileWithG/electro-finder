<template>
    <div class="product-container">
        <NavBar />
        
        <div class="product-page">
            <div class="search-container">
                <input
                    type="text"
                    v-model="searchQuery"
                    placeholder="Search products..."
                    class="search-input"
                    @keyup.enter="searchProducts"
                />
                <button class="search-button" @click="searchProducts">
                    <img class="search" src="../assets/search.png">
                </button>
            </div>

            <div v-if="products.length" class="product-grid">
                <ProductCard
                    v-for="(product, index) in products"
                    :key="index"
                    :productData="product"
                />
            </div>
            
            <div v-else class="no-results">
                {{ searchQuery ? 'No products found' : 'Search for products' }}
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ProductCard from '~/components/ProductCard.vue';
import NavBar from '~/components/NavBar.vue';

export default {
    components: {
        ProductCard,
        NavBar
    },
    data() {
        return {
            searchQuery: '',
            products: []
        };
    },
    methods: {
        async searchProducts() {
            try {
                if (!this.searchQuery.trim()) {
                    this.products = [];
                    return;
                }
                this.searchQuery = this.searchQuery.replaceAll(" ", "%20");
                const response = await axios.get(
                    `http://localhost:5000/${encodeURIComponent(this.searchQuery)}`
                );
                
                if (response.data.status === 'success') {
                    this.products = response.data.products;
                } else {
                    this.products = [];
                }
            } catch (error) {
                console.error('Error fetching products:', error);
                this.products = [];
            }
        }
    }
};
</script>

<style scoped>
.search {
    height: 20px;
    width: 20px;
}

.product-container {
    min-height: 100vh;
    background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding-top: 100px;
}

.product-page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.search-container {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
    padding: 0 20px;
}

.search-input {
    width: 60%;
    max-width: 600px;
    padding: 15px 25px;
    font-size: 1.2rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 30px;
    color: #ffffff;
    font-family: 'Poppins', sans-serif;
    margin-right: 10px;
}

.search-input::placeholder {
    color: rgba(255, 255, 255, 0.7);
}

.search-button {
    padding: 15px 25px;
    background: #2563eb;
    border: none;
    border-radius: 30px;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-left: 10px;
}

.search-button:hover {
    background: #3b82f6;
    transform: scale(1.05);
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem 5%;
}

.no-results {
    text-align: center;
    padding: 40px;
    color: #ffffff;
    font-size: 18px;
}

@keyframes gradientShift {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* NavBar styles (assuming they're not already global) */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.7);
    padding: 20px 0;
    z-index: 1000;
}

.navbar-links {
    list-style-type: none;
    display: flex;
    justify-content: center;
    margin: 0;
}

.navbar-links li {
    margin: 0 20px;
}

.navbar-links a {
    text-decoration: none;
    color: #ffffff;
    font-size: 2rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s ease;
    font-family: "Poppins", serif;
}

.navbar-links a:hover {
    color: #f39c12;
}

.nav-circle-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}

.nav-circle-image.left {
    left: 20px;
    width: 65px;
    height: 65px;
}

.nav-circle-image.right {
    right: 20px;
}
</style>