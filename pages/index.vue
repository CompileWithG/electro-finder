<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Fjalla+One&family=Paytone+One&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet">
    <div class="app-container" @mousemove="handleMouseMove">
        <NavBar />
        <div class="gradient-overlay"></div>
        <div class="flex">
        </div>
        <h2>Filter Out the Best Products Using ElectroFinder AI</h2>
        <!-- Title Section with Floating Animation -->
        <h1 class=" title floating-title">ElectroFinder</h1>

        <!-- New Shop Now Button -->
        <a href="product" class="shop-button floating-button">
            SHOP NOW
        </a>

        <!-- Floating Image for Scroll Indication -->
        <img class="floating-image" src="../assets/down_arrow.png" alt="Floating Graphic" />

        <!-- Spacer to ensure first viewport only shows title and arrow -->
        <div class="spacer-large"></div>

        <!-- First Animated Text Box (Scroll from Left) -->
        <div v-animateonscroll="{ enterClass: 'animate-slideinleft', leaveClass: 'animate-slideoutleft' }"
            class="text-box">
            <p>Compare products effortlessly and make informed decisions based on specifications, prices, and user
                reviews.
            </p>
        </div>

        <!-- Reduced Spacer -->
        <div class="spacer-smaller"></div>

        <!-- Second Animated Text Box (Scroll from Right) -->
        <div v-animateonscroll="{ enterClass: 'animate-slideinright', leaveClass: 'animate-slideoutright' }"
            class="text-box">
            <p>Access product details from various brands, both Indian and international, all in one place.</p>
        </div>
    </div>
</template>

<script>
import Login from '../components/Login'
import NavBar from '../components/NavBar'
export default {
    data() {
        return {
            isFooterVisible: false,
            posX: 50,
            posY: 50
        };
    },
    mounted() {
        window.addEventListener("scroll", this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener("scroll", this.handleScroll);
    },
    methods: {
        handleScroll() {
            const bottom = document.documentElement.scrollHeight === document.documentElement.scrollTop + window.innerHeight;
            this.isFooterVisible = bottom;
        },
        handleMouseMove(event) {
            const rect = event.currentTarget.getBoundingClientRect();
            this.posX = ((event.clientX - rect.left) / rect.width) * 100;
            this.posY = ((event.clientY - rect.top) / rect.height) * 100;

            // Update CSS variables
            document.documentElement.style.setProperty('--x', `${this.posX}%`);
            document.documentElement.style.setProperty('--y', `${this.posY}%`);
        }
    },
};
</script>

<style scoped>
h2 {
    margin-top: 165px;
    color: aqua;
    font-family: "Paytone One", serif;
    font-weight: 400;
    font-style: normal;
    letter-spacing: 2px;
    font-size: xx-large;
}

.navbar-links li a {
    font-family: "Poppins", serif;
    font-weight: 400;
    font-style: normal;
}

/* Background Animation */
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

/* Floating Animation */
@keyframes floating {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-15px);
    }

    100% {
        transform: translateY(0);
    }
}

/* Darker Dynamic Gradient Background */
.app-container {
    min-height: 100vh;
    /* Ensure the container takes up at least the full viewport height */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    /* Distribute space between elements */
    background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding-top: 80px;
    font-family: 'Oswald', sans-serif;
    /* Apply Oswald font to the entire container */
}

/* Center Title in First Viewport */
.title {
    font-family: "Paytone One", serif;
    font-weight: 400;
    font-style: normal;
    /* Increased title font size */
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-align: center;
    justify-content: center;
    position: absolute;
    top: 50%;
    left: 50%;

    transform: translate(-50%, -50%);
}

/* Floating Image (Arrow) */
.floating-image {
    width: 60px;
    height: 60px;
    animation: floating 4s ease-in-out infinite;
    position: absolute;
    bottom: 30px;
    left: 51%;
}

.amazon {
    animation: floating 4s ease-in-out infinite;
    position: absolute;
    width: 350px;
    height: 200px;
    margin: 60px;
    left: 15%;
}

.flipkart {
    animation: floating 4s ease-in-out infinite;
    position: absolute;
    width: 300px;
    height: 250px;
    right: 0%;
}

.cashify {
    animation: floating 4s ease-in-out infinite;
    position: absolute;
    width: 350px;
    height: 200px;
    margin: 40px;
}

/* Spacer for first viewport */
.spacer-large {
    height: 100vh;
}

.spacer-smaller {
    height: 20vh;
}

/* Enlarged Text Box Styling */
.text-box {
    background-color: rgba(255, 255, 255, 0.08);
    color: #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 40px;
    /* Increased padding */
    width: 85%;
    max-width: 700px;
    font-size: 2rem;
    /* Increased font size */
    text-align: center;
    font-family: 'Oswald', sans-serif;
    /* Apply Oswald font */
    border-radius: 10px;
    transition: all 0.5s ease-in-out;
}

@keyframes floating {
    0% {
        transform: translate(-50%, 0);
    }

    50% {
        transform: translate(-50%, -15px);
    }

    100% {
        transform: translate(-50%, 0);
    }
}

/* Slide Animations */
@keyframes slideinleft {
    from {
        opacity: 0;
        transform: translateX(-100px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideinright {
    from {
        opacity: 0;
        transform: translateX(100px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideoutleft {
    from {
        opacity: 1;
        transform: translateX(0);
    }

    to {
        opacity: 0;
        transform: translateX(-100px);
    }
}

@keyframes slideoutright {
    from {
        opacity: 1;
        transform: translateX(0);
    }

    to {
        opacity: 0;
        transform: translateX(100px);
    }
}

@keyframes slideindown {
    from {
        opacity: 0;
        transform: translateY(-100px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideoutup {
    from {
        opacity: 1;
        transform: translateY(0);
    }

    to {
        opacity: 0;
        transform: translateY(-100px);
    }
}

@keyframes slideinup {
    from {
        opacity: 0;
        transform: translateY(100px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideoutdown {
    from {
        opacity: 1;
        transform: translateY(0);
    }

    to {
        opacity: 0;
        transform: translateY(100px);
    }
}

/* Define animation utility classes */
.animate-slideinleft {
    animation: slideinleft 2.5s ease forwards;
}

.animate-slideinright {
    animation: slideinright 2.5s ease forwards;
}

.animate-slideoutleft {
    animation: slideoutleft 2.5s ease forwards;
}

.animate-slideoutright {
    animation: slideoutright 2.5s ease forwards;
}

.animate-slideindown {
    animation: slideindown 2.5s ease forwards;
}

.animate-slideoutup {
    animation: slideoutup 2.5s ease forwards;
}

.animate-slideinup {
    animation: slideinup 2.5s ease forwards;
}

.animate-slideoutdown {
    animation: slideoutdown 2.5s ease forwards;
}

/* Navbar Styling */
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
    /* Increased font size */
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s ease;
}

.navbar-links a:hover {
    color: #f39c12;
}


.floating-title {
    animation: floating 4s ease-in-out infinite;
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
}

.nav-circle-image.right {
    right: 20px;
}

/* Rest of your existing styles remain exactly the same */
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


/* Bigger left circle image */
.nav-circle-image.left {
    left: 20px;
    width: 65px;
    /* Increased from 50px */
    height: 65px;
    /* Increased from 50px */
}

/* Adjusted title positioning */
.title {
    font-size: 5rem;
    font-weight: 700;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    /* Changed from 50% to 50% maintains center, see explanation below */
    transform: translate(-50%, -50%);
}

.shop-button {
    position: absolute;
    top: 60%;
    left: 45%;
    transform: translateX(-50%);
    padding: 15px 40px;
    font-size: 1.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #ffffff;
    background-color: #2563eb;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    z-index: 10;
    margin: 80px;
}

.shop-button:hover {
    background-color: #3b82f6;
    transform: translateX(-50%) scale(1.05);
}

.floating-button {
    animation: floating 3s ease-in-out infinite;
}

/* Keep all other existing styles the same below */
.navbar-links li a {
    font-family: "Poppins", serif;
    font-weight: 400;
    font-style: normal;
}
</style>
