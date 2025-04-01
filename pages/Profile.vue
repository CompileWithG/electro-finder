<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Paytone+One&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    
    <div class="profile-container">
        <div class="gradient-overlay"></div>
        <h1 class="profile-title">User Profile</h1>
        
        <div class="profile-card">
            <img class="profile-image floating-element" src="../assets/person3.jpg" alt="Profile Picture">
            <div class="profile-details">
                <label class="input-label">Username:</label>
                <input type="text" v-model="user.username" class="profile-input">

                <label class="input-label">Email:</label>
                <input type="email" v-model="user.email" disabled class="profile-input">

                <button @click="updateProfile" class="profile-button floating-button">
                    Update Profile
                </button>
            </div>
        </div>

        <h2 class="section-title">Order History</h2>
        <ul class="order-list">
            <li v-for="order in orders" :key="order.id" class="order-item">
                Order #{{ order.id }} - {{ order.date }} - {{ order.total }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const user = ref({ username: '', email: '' });
const orders = ref([]);

onMounted(() => {
    // Retrieve user data from localStorage
    const storedUser = JSON.parse(localStorage.getItem('user')) || {};

    // Assign values safely
    user.value.username = storedUser.username || 'Guest';
    user.value.email = storedUser.email || 'No email found';

    // Dummy order data (Replace this with actual fetched data)
    orders.value = [
        { id: 1, date: '2025-03-01', total: '$120' },
        { id: 2, date: '2025-02-20', total: '$90' }
    ];
});

const updateProfile = () => {
    // Save updated user data back to localStorage
    localStorage.setItem('user', JSON.stringify(user.value));
    alert('Profile updated successfully!');
};
</script>

<style scoped>
/* Base gradient animation */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes floating {
    0% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0); }
}

.profile-container {
    min-height: 100vh;
    padding: 120px 20px 50px;
    background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    position: relative;
    overflow: hidden;
}

.gradient-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at var(--x) var(--y), 
        rgba(255, 255, 255, 0.1) 0%, 
        rgba(0, 0, 0, 0.8) 70%);
    pointer-events: none;
}

.profile-title {
    font-family: 'Paytone One', sans-serif;
    color: #fff;
    text-align: center;
    font-size: 3rem;
    margin-bottom: 2rem;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.profile-card {
    max-width: 600px;
    margin: 0 auto 3rem;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    display: flex;
    gap: 2rem;
}

.profile-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #2563eb;
}

.profile-details {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.input-label {
    font-family: 'Poppins', sans-serif;
    color: #fff;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    display: block;
}

.profile-input {
    width: 100%;
    padding: 12px 20px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 8px;
    color: #fff;
    font-family: 'Poppins', sans-serif;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.profile-input:focus {
    outline: none;
    border-color: #2563eb;
    box-shadow: 0 0 10px rgba(37, 99, 235, 0.3);
}

.profile-button {
    align-self: flex-start;
    background: #2563eb;
    color: #fff;
    padding: 12px 35px;
    border: none;
    border-radius: 30px;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.profile-button:hover {
    background: #3b82f6;
    transform: translateY(-2px);
}

.section-title {
    font-family: 'Paytone One', sans-serif;
    color: #fff;
    text-align: center;
    font-size: 2rem;
    margin: 3rem 0 2rem;
    text-transform: uppercase;
}

.order-list {
    max-width: 600px;
    margin: 0 auto;
    padding: 0;
    list-style: none;
}

.order-item {
    padding: 1.5rem;
    margin-bottom: 1rem;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    color: #fff;
    font-family: 'Poppins', sans-serif;
    transition: transform 0.3s ease;
}

.order-item:hover {
    transform: translateX(10px);
}

.floating-element {
    animation: floating 4s ease-in-out infinite;
}

.floating-button {
    animation: floating 3s ease-in-out infinite;
}
</style>
