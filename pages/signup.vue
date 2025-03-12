<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '~/stores/auth'

export default {
    setup() {
        const router = useRouter()
        const authStore = useAuthStore()
        const form = ref({
            email: '',
            password: '',
            confirmPassword: ''
        })
        const isSubmitting = ref(false)
        const showSuccess = ref(false)
        const errorMessage = ref('')

        const validateForm = () => {
            if (!form.value.email || !form.value.password || !form.value.confirmPassword) {
                errorMessage.value = 'Please fill in all fields'
                return false
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
            if (!emailRegex.test(form.value.email)) {
                errorMessage.value = 'Please enter a valid email address'
                return false
            }

            if (form.value.password !== form.value.confirmPassword) {
                errorMessage.value = 'Passwords do not match'
                return false
            }

            return true
        }

        const handleSubmit = async () => {
            errorMessage.value = ''

            if (!validateForm()) return

            isSubmitting.value = true

            // Simulate API call
            setTimeout(() => {
                isSubmitting.value = false
                showSuccess.value = true

                // Update auth state
                authStore.signup()

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
                    <h1 class="form-title">Create Your Account</h1>
                    <p class="form-subtitle">Sign up to start your shopping journey</p>
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

                <div class="input-group">
                    <input type="password" v-model="form.confirmPassword" required @focus="animateInput($event.target)"
                        @blur="removeAnimation($event.target)">
                    <label>Confirm Password</label>
                    <span class="focus-border"></span>
                    <span class="input-icon">🔒</span>
                </div>

                <button type="submit" class="submit-btn" :disabled="isSubmitting">
                    <span v-if="!isSubmitting">Sign Up</span>
                    <div v-else class="spinner"></div>
                    <div v-if="showSuccess" class="success-check">✔</div>
                </button>

                <p class="signup-link">
                    Already have an account?
                    <router-link to="/login">Log in</router-link>
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

.input-icon {
    position: absolute;
    right: 15px;
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
}

input:focus {
    border-color: #667eea;
    outline: none;
    box-shadow: 0 0 8px rgba(102, 126, 234, 0.2);
}

.submit-btn {
    padding: 1.2rem;
    font-size: 1.2rem;
}

.error-message {
    font-size: 1.1rem;
    margin-top: 1.5rem;
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

/* Add media queries for responsiveness */
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
}
</style>