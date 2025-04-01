<template>
    <div class="product-card">
      <img :src="productData[1]" :alt="productData[2]" class="product-image" />
      <div class="product-content">
        <h3 class="product-title">{{ productData[2] }}</h3>
        <p class="product-price">{{ productData[4] }}</p>
        
        <div class="product-features">
          <h4>Features:</h4>
          <ul>
            <li v-for="(feature, index) in productData[3]" :key="index">
              {{ feature }}
            </li>
          </ul>
        </div>
        
        <a :href="productData[0]" target="_blank" class="product-link">
          View on Website
        </a>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      productData: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .product-card {
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    overflow: hidden;
    transition: transform 0.2s;
  }
  
  .product-card:hover {
    transform: translateY(-5px);
  }
  
  .product-image {
    width: 100%;
    height: 250px;
    object-fit: contain;
    background: #f5f5f5;
    padding: 15px;
  }
  
  .product-content {
    padding: 15px;
  }
  
  .product-title {
    font-size: 1.1rem;
    margin-bottom: 10px;
    color: #333;
  }
  
  .product-price {
    font-size: 1.2rem;
    color: #42b983;
    font-weight: bold;
    margin-bottom: 15px;
  }
  
  .product-features {
    margin-bottom: 15px;
  }
  
  .product-features h4 {
    font-size: 1rem;
    color: #666;
    margin-bottom: 8px;
  }
  
  .product-features ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
  }
  
  .product-features li {
    font-size: 0.9rem;
    color: #444;
    padding: 4px 0;
    display: flex;
    align-items: center;
  }
  
  .product-features li::before {
    content: "•";
    color: #42b983;
    margin-right: 8px;
  }
  
  .product-link {
    display: block;
    text-align: center;
    background-color: #42b983;
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s;
  }
  
  .product-link:hover {
    background-color: #33a06f;
  }
  </style>