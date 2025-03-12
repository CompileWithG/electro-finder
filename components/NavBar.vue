<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">

    <nav class="navbar" v-animateonscroll="{ enterClass: 'animate-slideindown', leaveClass: 'animate-slideoutup' }">
        <!-- Conditional rendering for profile image/login button -->
        <template v-if="authStore && authStore.isLoggedIn">
            <img class="nav-circle-image left" src="../assets/person3.jpg" alt="Profile">
            <button class="logout-button" @click="logout">Logout</button>
        </template>
        <router-link v-else to="/Login" class="login-button">
            <span>Login</span>
        </router-link>

        <ul class="navbar-links">
            <li><a href="/">Home</a></li>
            <li><a href="Product">Products</a></li>
            <li><a href="About">About</a></li>
            <li><a href="contact">Contact</a></li>
            <li><a href="ai">AI Chat Bot</a></li>
        </ul>
        <a href="https://www.amazon.in" target="_blank">
            <img class="amazon" src="../assets/amazon.png" alt="Amazon">
        </a>
        <a href="https://www.cashify.in" target="_blank">
            <img class="cashify" src="../assets/cashify.png" alt="Cashify">
        </a>
        <a href="https://www.flipkart.in" target="_blank">
            <img class="flipkart" src="../assets/flipkart.png" alt="Flipkart">
        </a>
    </nav>
</template>

<script setup>
import { useAuthStore } from '~/stores/auth';
import { computed } from 'vue';

// Access the auth store
const authStore = useAuthStore();

// Use a computed property to ensure reactivity
const isLoggedIn = computed(() => authStore.isLoggedIn);

// Logout function
const logout = () => {
    authStore.logout();
};
</script>

<style>
.amazon {

    position: absolute;
    width: 90px;
    height: 30px;
    right: 3%;

}

.flipkart {
    position: absolute;
    width: 110px;
    height: 80px;
    right: 12%;
    top: 2%;
    margin-left: 20px;
}

.cashify {
    position: absolute;
    width: 70px;
    height: 25px;
    right: 20%;
    margin-bottom: 20px;
}

/* Existing navbar styles */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.7);
    padding: 20px 0;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
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
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
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

.login-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(120deg,
            transparent,
            rgba(255, 255, 255, 0.2),
            transparent);
    transition: all 0.6s ease;
}

.login-button:hover {
    transform: translateY(-50%) scale(1.05);
    box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
}

.login-button:hover::before {
    left: 100%;
}

/* Logout button styles */
.logout-button {
    position: absolute;
    left: 80px;
    /* Adjust this value to position the button next to the profile image */
    top: 50%;
    transform: translateY(-50%);
    padding: 8px 20px;
    background: #e74c3c;
    /* Red background for logout button */
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
    /* Darker red on hover */
}

/* Profile image styles */
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
}

.nav-circle-image.right {
    right: 20px;
}

/* Animations */
@keyframes buttonPulse {
    0% {
        transform: translateY(-50%) scale(1);
    }

    50% {
        transform: translateY(-50%) scale(1.05);
    }

    100% {
        transform: translateY(-50%) scale(1);
    }
}

.login-button:not(.router-link-active) {
    animation: buttonPulse 2s infinite;
}

/* Existing animations */
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