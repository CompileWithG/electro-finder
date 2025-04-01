<script>
import NavBar from '../components/NavBar'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '~/stores/auth'

export default {
    setup() {
        const router = useRouter()
        const authStore = useAuthStore()
        const form = ref({
            email: '',
            password: ''
        })
        const isSubmitting = ref(false)
        const showSuccess = ref(false)
        const errorMessage = ref('')

        const validateForm = () => {
            if (!form.value.email || !form.value.password) {
                errorMessage.value = 'Please fill in all fields'
                return false
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
            if (!emailRegex.test(form.value.email)) {
                errorMessage.value = 'Please enter a valid email address'
                return false
            }

            return true
        }

        const handleSubmit = async () => {
    errorMessage.value = ''

    if (!validateForm()) return

    isSubmitting.value = true

    // Retrieve the stored user details from localStorage
    const storedUser = JSON.parse(localStorage.getItem('user'))

    // Check if the stored user details match the form values
    if (!storedUser || storedUser.email !== form.value.email || storedUser.password !== form.value.password) {
        errorMessage.value = 'Invalid email or password'
        isSubmitting.value = false
        return
    }

    // Simulate API call (optional)
    setTimeout(() => {
        isSubmitting.value = false
        showSuccess.value = true

        // Update auth state
        authStore.login()

        // Redirect after success animation
        setTimeout(() => {
            router.push('/')
        }, 1500)
    }, 2000)
}


        // Animation functions
        const animateInput = (input) => {
            input.parentElement.classList.add('active')
        }

        const removeAnimation = (input) => {
            if (!input.value) {
                input.parentElement.classList.remove('active')
            }
        }

        return {
            form,
            isSubmitting,
            showSuccess,
            errorMessage,
            handleSubmit,
            animateInput,
            removeAnimation
        }
    }
}
</script>
<template>

    <div class="login-container">
        <div class="form-wrapper">
            <form @submit.prevent="handleSubmit" class="login-form">
                <div class="form-header">
                    <h1 class="form-title">Welcome to ElectroFinder</h1>
                    <p class="form-subtitle">Sign in to continue your shopping experience</p>
                </div>

                <div class="input-group">
                    <input type="email" v-model="form.email" required @focus="animateInput($event.target)"
                        @blur="removeAnimation($event.target)">
                    <label>Email Address</label>
                    <span class="focus-border"></span>
                    <span class="input-icon">✉️</span>
                </div>

                <div class="input-group">
                    <input type="password" v-model="form.password" required @focus="animateInput($event.target)"
                        @blur="removeAnimation($event.target)">
                    <label>Password</label>
                    <span class="focus-border"></span>
                    <span class="input-icon">🔒</span>
                </div>

                <div class="form-options">
                    <label class="remember-me">
                        <input type="checkbox" v-model="form.remember">
                        <span class="checkmark"></span>
                        Remember me
                    </label>
                    <router-link to="/forgot-password" class="forgot-password">
                        Forgot Password?
                    </router-link>
                </div>

                <button type="submit" class="submit-btn" :disabled="isSubmitting">
                    <span v-if="!isSubmitting">Sign In</span>
                    <div v-else class="spinner"></div>
                    <div v-if="showSuccess" class="success-check">✔</div>
                </button>

                <div class="social-login">
                    <p class="divider">Or continue with</p>
                    <div class="social-buttons">
                        <button type="button" class="social-btn google">
                            <img src="../assets/google1.png" alt="Google">
                            Google
                        </button>
                        <button type="button" class="social-btn facebook">
                            <img src="../assets/google (2).png" alt="Facebook">
                            Facebook
                        </button>
                    </div>
                </div>

                <p class="signup-link">
                    Don't have an account?
                    <router-link to="/signup">Create account</router-link>
                </p>

                <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
            </form>
        </div>
    </div>
</template>
<style scoped>
.login-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.form-wrapper {
    perspective: 1000px;
    width: 100%;
    max-width: 600px;
    padding: 2rem;
}

.login-form {
    background: rgba(255, 255, 255, 0.98);
    padding: 3rem 4rem;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    transform: rotateY(0deg);
    transition: all 0.6s cubic-bezier(0.18, 0.89, 0.32, 1.28);
    animation: formEntrance 0.8s ease-out;
}

.form-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.form-title {
    font-size: 2.5rem;
    color: #2d3748;
    margin-bottom: 0.5rem;
}

.form-subtitle {
    color: #718096;
    font-size: 1.1rem;
}

.input-group {
    position: relative;
    margin-bottom: 2rem;
}

.input-group.active label {
    transform: translateY(-24px) scale(0.8);
    color: #667eea;
}

.input-group label {
    position: absolute;
    left: 50px;
    top: 50%;
    transform: translateY(-50%);
    color: #a0aec0;
    pointer-events: none;
    transition: all 0.3s ease;
}

.input-icon {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.2rem;
}

input {
    width: 100%;
    padding: 1rem 1.5rem;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    font-size: 1.1rem;
    padding-left: 3rem;
    transition: all 0.3s ease;
}

input:focus {
    border-color: #667eea;
    outline: none;
    box-shadow: 0 0 8px rgba(102, 126, 234, 0.2);
}

.focus-border {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: #667eea;
    transition: all 0.3s ease;
}

.input-group input:focus ~ .focus-border {
    width: 100%;
}

.form-options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 1.5rem 0;
}

.remember-me {
    display: flex;
    align-items: center;
    color: #4a5568;
    cursor: pointer;
}

.remember-me input {
    display: none;
}

.checkmark {
    display: inline-block;
    width: 18px;
    height: 18px;
    border: 2px solid #cbd5e0;
    border-radius: 4px;
    margin-right: 0.5rem;
    position: relative;
    transition: all 0.2s ease;
}

.remember-me input:checked ~ .checkmark {
    background: #667eea;
    border-color: #667eea;
}

.forgot-password {
    color: #667eea;
    text-decoration: none;
    font-size: 0.95rem;
    transition: opacity 0.2s ease;
    border-bottom: 2px solid transparent;
    padding-bottom: 2px;
}

.forgot-password:hover {
    opacity: 0.8;
    border-bottom-color: #667eea;
}

.submit-btn {
    width: 100%;
    padding: 1.2rem;
    font-size: 1.2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    font-weight: bold;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    border: 2px solid transparent;
}

.submit-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

.submit-btn:active {
    transform: translateY(1px);
    box-shadow: 0 2px 10px rgba(102, 126, 234, 0.4);
}

.submit-btn:disabled {
    background: linear-gradient(135deg, #a0aec0 0%, #cbd5e0 100%);
    cursor: not-allowed;
    transform: none;
    box-shadow: 0 4px 10px rgba(160, 174, 192, 0.3);
}

.social-login {
    margin: 2rem 0;
}

.divider {
    text-align: center;
    color: #718096;
    position: relative;
    margin: 1.5rem 0;
}

.divider::before,
.divider::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 45%;
    height: 1px;
    background: #e2e8f0;
}

.divider::before {
    left: 0;
}

.divider::after {
    right: 0;
}

.social-buttons {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

.social-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    background: white;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.social-btn img {
    width: 20px;
    margin-right: 0.5rem;
}

.social-btn:hover {
    border-color: #667eea;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

.signup-link {
    text-align: center;
    color: #4a5568;
    margin-top: 1.5rem;
}

.signup-link a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
    border-bottom: 2px solid transparent;
    padding-bottom: 2px;
    transition: border-color 0.2s ease;
}

.signup-link a:hover {
    border-bottom-color: #667eea;
}

.error-message {
    background-color: #fed7d7;
    color: #c53030;
    padding: 1rem;
    border-radius: 8px;
    font-size: 1rem;
    margin-top: 1.5rem;
    border-left: 4px solid #e53e3e;
    text-align: center;
    animation: shake 0.5s ease-in-out;
}

@keyframes formEntrance {
    from {
        opacity: 0;
        transform: translateY(-50px) rotateY(90deg) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) rotateY(0deg) scale(1);
    }
}

@media (max-width: 768px) {
    .form-wrapper {
        padding: 1rem;
    }
    .login-form {
        padding: 2rem;
    }
    .form-title {
        font-size: 2rem;
    }
    .submit-btn {
        padding: 1rem;
        font-size: 1.1rem;
    }
}
</style>