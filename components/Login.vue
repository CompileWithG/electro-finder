<template>
    <button class="login-button" :class="[status, { loading }]" @click="handleClick" :disabled="loading"
        aria-live="polite">
        <span class="button-text">
            <template v-if="!loading && !status">
                {{ text }}
            </template>
            <template v-if="loading">
                <span class="spinner"></span>
                Processing...
            </template>
            <template v-if="status === 'success'">
                <svg class="checkmark" viewBox="0 0 52 52">
                    <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" />
                    <path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8" />
                </svg>
                Success!
            </template>
            <template v-if="status === 'error'">
                <svg class="cross" viewBox="0 0 24 24">
                    <path
                        d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
                </svg>
                Try Again
            </template>
        </span>
    </button>
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            default: 'Login'
        },
        loading: {
            type: Boolean,
            default: false
        },
        status: {
            type: String,
            validator: value => ['', 'success', 'error'].includes(value),
            default: ''
        }
    },
    methods: {
        handleClick() {
            this.$emit('click');
        }
    }
}
</script>

<style scoped>
.login-button {
    position: relative;
    padding: 15px 30px;
    font-size: 1.1rem;
    font-weight: 600;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    background: #2563eb;
    color: white;
    transition: all 0.3s ease;
    overflow: hidden;
}

.login-button:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.1);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.login-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.4);
}

.login-button:hover:before {
    opacity: 1;
}

.login-button:active:not(:disabled) {
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(37, 99, 235, 0.3);
}

/* Loading State */
.login-button.loading {
    padding-left: 20px;
    padding-right: 20px;
    cursor: progress;
}

.spinner {
    display: inline-block;
    width: 18px;
    height: 18px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: white;
    animation: spin 0.8s ease-in-out infinite;
    margin-right: 8px;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

/* Success State */
.login-button.success {
    background: #10b981;
    padding-left: 20px;
    padding-right: 20px;
}

.checkmark {
    width: 20px;
    height: 20px;
    margin-right: 8px;
    vertical-align: middle;
}

.checkmark__circle {
    stroke-dasharray: 166;
    stroke-dashoffset: 166;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #fff;
    animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
}

.checkmark__check {
    transform-origin: 50% 50%;
    stroke-dasharray: 48;
    stroke-dashoffset: 48;
    animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.6s forwards;
}

@keyframes stroke {
    100% {
        stroke-dashoffset: 0;
    }
}

/* Error State */
.login-button.error {
    background: #ef4444;
    padding-left: 20px;
    padding-right: 20px;
}

.cross {
    width: 20px;
    height: 20px;
    margin-right: 8px;
    vertical-align: middle;
    fill: white;
    animation: scaleIn 0.3s ease-out;
}

@keyframes scaleIn {
    from {
        transform: scale(0);
    }

    to {
        transform: scale(1);
    }
}

/* Disabled State */
.login-button:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}
</style>