<template>
    <div class="cart-container">
      <NavBar />
      <h2 class="cart-title">Your Cart</h2>
      <div v-if="cart.length === 0" class="empty-cart">
        Your cart is empty.
      </div>
      <div v-else class="cart-items-container">
        <div v-for="(item, index) in cart" :key="index" class="cart-item">
          <div class="cart-item-content">
            <img :src="item.image" alt="" class="cart-image">
            <div class="cart-details">
              <h3 class="cart-item-title">{{ item.name }}</h3>
              <p class="cart-price">Price: <span class="discount-price">{{ item.discount_price }}</span></p>
              <div class="quantity-controls">
                <p class="cart-quantity">Quantity:</p>
                <div class="quantity-actions">
                  <button @click="decreaseQuantity(index)" class="quantity-button">-</button>
                  <span class="quantity-value">{{ item.quantity }}</span>
                  <button @click="increaseQuantity(index)" class="quantity-button">+</button>
                </div>
              </div>
              <button @click="removeFromCart(index)" class="remove-button">Remove Item</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import NavBar from '~/components/NavBar.vue';
  
  export default {
    data() {
      return {
        cart: []
      };
    },
    mounted() {
      this.loadCart();
    },
    methods: {
      loadCart() {
        const storedCart = localStorage.getItem('cart');
        if (storedCart) {
          this.cart = JSON.parse(storedCart);
        }
      },
      saveCart() {
        localStorage.setItem('cart', JSON.stringify(this.cart));
      },
      removeFromCart(index) {
        this.cart.splice(index, 1);
        this.saveCart();
      },
      increaseQuantity(index) {
        this.cart[index].quantity += 1;
        this.saveCart();
      },
      decreaseQuantity(index) {
        if (this.cart[index].quantity > 1) {
          this.cart[index].quantity -= 1;
        } else {
          this.removeFromCart(index);
        }
        this.saveCart();
      }
    }
  }
  </script>
  
  <style scoped>
  .cart-container {
    min-height: 100vh;
    background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding: 40px 20px;
    color: white;
  }
  
  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  
  .cart-title {
    text-align: center;
    font-size: 2.5rem;
    margin-top:20px;
    margin-bottom: 30px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  }
  
  .empty-cart {
    text-align: center;
    font-size: 1.4rem;
    margin-top: 50px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .cart-items-container {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .cart-item {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 20px;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .cart-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    background: rgba(255, 255, 255, 0.15);
  }
  
  .cart-item-content {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  
  .cart-image {
    width: 120px;
    height: 120px;
    object-fit: contain;
    background: rgba(0, 0, 0, 0.2);
    padding: 10px;
    border-radius: 10px;
  }
  
  .cart-details {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .cart-item-title {
    font-size: 1.4rem;
    margin: 0;
    color: #ffffff;
  }
  
  .cart-price {
    font-size: 1.1rem;
    margin: 0;
  }
  
  .discount-price {
    color: #38bdf8;
    font-weight: bold;
    font-size: 1.2rem;
  }
  
  .quantity-controls {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-top: 5px;
  }
  
  .cart-quantity {
    font-size: 1.1rem;
    margin: 0;
  }
  
  .quantity-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .quantity-value {
    font-size: 1.2rem;
    min-width: 25px;
    text-align: center;
  }
  
  .quantity-button {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.15);
    color: white;
    border: none;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .quantity-button:hover {
    background-color: rgba(255, 255, 255, 0.25);
    transform: scale(1.1);
  }
  
  .remove-button {
    background-color: #e63946;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s;
    margin-top: 10px;
    align-self: flex-start;
    font-weight: bold;
  }
  
  .remove-button:hover {
    background-color: #c72f3e;
    transform: scale(1.05);
  }
  
  /* Responsive adjustments */
  @media (max-width: 600px) {
    .cart-item-content {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .cart-image {
      width: 100%;
      height: 200px;
      margin-bottom: 15px;
    }
    
    .quantity-controls {
      flex-direction: column;
      align-items: flex-start;
      gap: 5px;
    }
    
    .remove-button {
      width: 100%;
      text-align: center;
    }
  }
  </style>