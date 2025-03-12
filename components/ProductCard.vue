<template>
    <!-- Template remains the same -->
    <div class="product-card">
        <h3>{{ product.title }}</h3>
        <div class="product-details">
            <div class="amazon-details">
                <h4>Amazon</h4>
                <p>Price: {{ product.amazon.price }}</p>
                <a :href="product.amazon.link" target="_blank">View on Amazon</a>
            </div>
            <div class="flipkart-details">
                <h4>Flipkart</h4>
                <p>Price: {{ product.flipkart.price }}</p>
                <a :href="product.flipkart.link" target="_blank">View on Flipkart</a>
            </div>
        </div>
    </div>
</template>

<script>
// Script remains the same
export default {
    props: {
        product: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.product-card {
    background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
        url('@/assets/product-bg.jpg');
    /* Add your image path here */
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
}

/* Rest of the styles remain the same */
.product-details {
    display: flex;
    justify-content: space-between;
}

.amazon-details,
.flipkart-details {
    width: 48%;
}

h3 {
    margin-bottom: 10px;
    position: relative;
    z-index: 1;
}

h4 {
    margin: 10px 0;
    position: relative;
    z-index: 1;
}

a {
    color: #60a5fa;
    text-decoration: none;
    position: relative;
    z-index: 1;
}

a:hover {
    color: #3b82f6;
    text-decoration: underline;
}
</style>