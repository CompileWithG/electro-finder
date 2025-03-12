<template>
    <div class="product-container">
        <!-- Navigation Bar (Same as App.vue) -->
        <NavBar />

        <!-- Search Bar -->
        <div class="search-container">
            <input type="text" v-model="searchQuery" placeholder="Search products..." class="search-input"
                @keyup.enter="fetchProducts">
            <button class="search-button" @click="fetchProducts">
                <i class="fas fa-search">
                    <img class="search" src="../assets/search.png">
                </i>
            </button>
            <button class="filter-button" @click="toggleFilterOptions">
                Filter
            </button>
        </div>

        <!-- Filter Options -->
        <div v-if="showFilterOptions" class="filter-options">
            <h3>Filter By:</h3>
            <div>
                <label>
                    Price:
                    <input type="number" v-model="priceFilter.min" placeholder="Min" />
                    <input type="number" v-model="priceFilter.max" placeholder="Max" />
                </label>
            </div>
            <div>
                <label>
                    RAM:
                    <input type="number" v-model="specsFilter.ram" placeholder="RAM (GB)" />
                </label>
            </div>
            <div>
                <label>
                    Screen Size:
                    <input type="number" v-model="specsFilter.screen" placeholder="Screen Size (inches)" />
                </label>
            </div>
            <button @click="applyFilters">Apply Filters</button>
        </div>

        <!-- Product Grid -->
        <div class="product-grid">
            <ProductCard v-for="product in filteredProducts" :key="product.amazon.link" :product="product" />
        </div>
    </div>
</template>

<script>
import ProductCard from '../components/ProductCard';
import NavBar from '../components/Navbar';
import axios from 'axios';

export default {
    components: {
        ProductCard,
        NavBar
    },
    data() {
        return {
            searchQuery: '',
            showFilterOptions: false,
            priceFilter: {
                min: null,
                max: null
            },
            specsFilter: {
                ram: null,
                screen: null
            },
            products: [
                {
                    title: "Apple iPhone 15 Pro",
                    image: "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1693009279096",
                    amazon: {
                        price: "₹124,999",
                        link: "https://amazon.com/s?k=iphone15pro"
                    },
                    flipkart: {
                        price: "₹123,999",
                        link: "https://flipkart.com/q=iphone15pro"
                    },
                    specs: {
                        ram: 6, // Example RAM
                        screen: 6.1 // Example screen size
                    }
                },
                {
                    title: "Samsung Galaxy S24 Ultra",
                    image: "https://images.samsung.com/in/smartphones/galaxy-s24-ultra/images/galaxy-s24-ultra-highlights-kv.jpg",
                    amazon: {
                        price: "₹134,999",
                        link: "https://amazon.com/s?k=galaxys24ultra"
                    },
                    flipkart: {
                        price: "₹133,500",
                        link: "https://flipkart.com/q=galaxys24ultra"
                    },
                    specs: {
                        ram: 12, // Example RAM
                        screen: 6.8 // Example screen size
                    }
                },
                {
                    title: "Sony WH-1000XM5 Wireless Headphones",
                    image: "https://www.sony.co.in/image/4e0d1b1e9d80b5a093e0f1b7e2a0d3a2?fmt=pjpeg&wid=165&bgcolor=FFFFFF&bgc=FFFFFF",
                    amazon: {
                        price: "₹24,990",
                        link: "https://amazon.com/s?k=sonyxm5"
                    },
                    flipkart: {
                        price: "₹23,999",
                        link: "https://flipkart.com/q=sonyxm5"
                    },
                    specs: {
                        ram: null, // Not applicable
                        screen: null // Not applicable
                    }
                },
                {
                    title: "MacBook Pro 16-inch M3 Max",
                    image: "https://via.placeholder.com/400x300.png?text=iPhone+15 Pro",
                    amazon: {
                        price: "₹3,49,990",
                        link: "https://amazon.com/s?k=macbookpro16"
                    },
                    flipkart: {
                        price: "₹3,47,999",
                        link: "https://flipkart.com/q=macbookpro16"
                    },
                    specs: {
                        ram: 16, // Example RAM
                        screen: 16 // Example screen size
                    }
                },
                {
                    title: "Apple Watch Series 9",
                    image: "https://www.apple.com/newsroom/images/product/watch/standard/Apple-Watch-S9-hero-230912_Full-Bleed-Image.jpg.large.jpg",
                    amazon: {
                        price: "₹41,900",
                        link: "https://amazon.com/s?k=applewatch9"
                    },
                    flipkart: {
                        price: "₹40,999",
                        link: "https://flipkart.com/q=applewatch9"
                    },
                    specs: {
                        ram: null, // Not applicable
                        screen: 1.9 // Example screen size
                    }
                }
            ]
        }
    },
    computed: {
        filteredProducts() {
            return this.products.filter(product => {
                const matchesSearch = product.title.toLowerCase().includes(this.searchQuery.toLowerCase());
                const matchesPrice = this.priceFilter.min === null || parseInt(product.amazon.price.replace(/[^\d]/g, '')) >= this.priceFilter.min;
                const matchesMaxPrice = this.priceFilter.max === null || parseInt(product.amazon.price.replace(/[^\d]/g, '')) <= this.priceFilter.max;
                const matchesRam = this.specsFilter.ram === null || (product.specs.ram && product.specs.ram >= this.specsFilter.ram);
                const matchesScreen = this.specsFilter.screen === null || (product.specs.screen && product.specs.screen >= this.specsFilter.screen);

                return matchesSearch && matchesPrice && matchesMaxPrice && matchesRam && matchesScreen;
            });
        }
    },
    methods: {
        async fetchProducts() {
            if (!this.searchQuery) {
                console.log("error");
                return;
            }
            try {
                const response = await axios.get(`http://localhost:5000/compare?product=${this.searchQuery}`);
                this.products = response.data; // Set the fetched products
            } catch (error) {
                console.error("Error fetching products:", error);
            }
        },
        toggleFilterOptions() {
            this.showFilterOptions = !this.showFilterOptions;
        },
        applyFilters() {
            this.showFilterOptions = false; // Hide filter options after applying
        }
    }
}
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

.search-button,
.filter-button {
    padding: 15px 25px;
    background: #2563eb;
    border: none;
    border-radius: 30px;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-left: 10px;
}

.search-button:hover,
.filter-button:hover {
    background: #3b82f6;
    transform: scale(1.05);
}

.filter-options {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    margin: 1rem 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.filter-options h3 {
    color: #ffffff;
}

.filter-options label {
    color: #ffffff;
}

.filter-options input {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    background: rgba(255, 255, 255, 0.2);
    color: #ffffff;
}

.filter-options input::placeholder {
    color: rgba(255, 255, 255, 0.7);
}

.filter-options button {
    padding: 10px 20px;
    background: #2563eb;
    border: none;
    border-radius: 5px;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
}

.filter-options button:hover {
    background: #3b82f6;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem 5%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Reuse animations from App.vue */
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

/* Include existing navbar styles from App.vue */
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