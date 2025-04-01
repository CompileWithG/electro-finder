<template>
    <nav class="navbar" v-animateonscroll="{ enterClass: 'animate-slideindown', leaveClass: 'animate-slideoutup' }">
        <template v-if="authStore && authStore.isLoggedIn">
            <router-link to="/profile">
                <img class="nav-circle-image left" src="../assets/person3.jpg" alt="Profile">
            </router-link>
            <button class="logout-button" @click="logout">Logout</button>
        </template>
        <router-link v-else to="/Login" class="login-button">
            <span>Login</span>
        </router-link>

        <ul class="navbar-links">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/product">Products</router-link></li>
            <li><router-link to="/about">About</router-link></li>
            <li><router-link to="/ai">AI Chat Bot</router-link></li>
        </ul>

        <router-link to="/cart" class="cart-button">
            <svg xmlns="http://www.w3.org/2000/svg" class="cart-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
        </router-link>
    </nav>
</template>

<script setup>
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();
const logout = () => authStore.logout();
</script>

<style>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.7);
    padding: 20px 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 30px;
}

.navbar-links {
    list-style-type: none;
    display: flex;
    margin: 0;
    padding: 0;
}

.navbar-links li {
    margin: 0 20px;
}

.navbar-links a {
    text-decoration: none;
    color: #ffffff;
    font-size: 1.2rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s ease;
    font-family: "Poppins", sans-serif;
    font-weight: 500;
}

.navbar-links a:hover {
    color: #f39c12;
}

/* Login button styles */
.login-button {
    padding: 12px 30px;
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    font-family: "Poppins", sans-serif;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.login-button span {
    position: relative;
    z-index: 1;
}

.login-button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
}

/* Cart button styles */
.cart-button {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
    color: white;
    border: none;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    margin-left: auto;
}

.cart-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(243, 156, 18, 0.3);
}

.cart-icon {
    width: 24px;
    height: 24px;
}

/* Logout button */
.logout-button {
    padding: 8px 20px;
    background: #e74c3c;
    color: white;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    font-family: "Poppins", sans-serif;
    font-weight: 600;
    transition: background 0.3s ease;
}

.logout-button:hover {
    background: #c0392b;
}

/* Profile image styles */
.nav-circle-image {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 20px;
}

/* Animations */
.animate-slideindown {
    animation: slideindown 0.5s ease forwards;
}

.animate-slideoutup {
    animation: slideoutup 0.5s ease forwards;
}

@keyframes slideindown {
    from {
        transform: translateY(-100%);
    }

    to {
        transform: translateY(0);
    }
}

@keyframes slideoutup {
    from {
        transform: translateY(0);
    }

    to {
        transform: translateY(-100%);
    }
}
</style>
