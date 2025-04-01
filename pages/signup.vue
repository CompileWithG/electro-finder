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

                router.push('/');
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
                    <router-link to="/login" class="login-link">Log in</router-link>
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

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: spin 1s linear infinite;
    margin: 0 auto;
}

.success-check {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.5rem;
    color: white;
    background-color: #48bb78;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: scaleIn 0.5s ease-out;
}

.signup-link {
    text-align: center;
    margin-top: 1.5rem;
    color: #718096;
    font-size: 1rem;
}

.login-link {
    color: #667eea;
    font-weight: bold;
    text-decoration: none;
    transition: all 0.3s ease;
    border-bottom: 2px solid transparent;
    padding-bottom: 2px;
}

.login-link:hover {
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

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

@keyframes scaleIn {
    from {
        transform: translate(-50%, -50%) scale(0);
    }

    to {
        transform: translate(-50%, -50%) scale(1);
    }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
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
    
    .submit-btn {
        padding: 1rem;
        font-size: 1.1rem;
    }
}
</style>