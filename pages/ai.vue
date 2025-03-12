<template>
    <NavBar />
    <div class="ai-container">
        <div class="form-wrapper">
            <h1 class="form-title">ElectroFinder HelpBot</h1>
            <textarea v-model="userInput"
                placeholder="List all the Samsung phones available in Amazon right now in the range of 0 to 50,000 rupees"
                class="input-area" rows="8"></textarea>
            <button @click="handleSubmit" class="submit-btn" :disabled="isLoading">
                <span v-if="!isLoading">Send</span>
                <div v-else class="spinner"></div>
            </button>
            <div v-if="response" class="response-area">
                <h2 class="response-title">Response:</h2>
                <p class="response-text">{{ response }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import NavBar from '../components/NavBar';
import OpenAI from 'openai';

const openai = new OpenAI({
    baseURL: 'https://api.deepseek.com/v1',
    apiKey: 'sk-7a63086967a041c4b23942e11a51c560', dangerouslyAllowBrowser: true // Replace with your actual API key
});

export default {
    setup() {
        const userInput = ref('');
        const response = ref('');
        const isLoading = ref(false);

        const handleSubmit = async () => {
            if (!userInput.value) return;

            isLoading.value = true;
            response.value = '';

            try {
                const completion = await openai.chat.completions.create({
                    messages: [{ role: "user", content: userInput.value }],
                    model: "deepseek-chat",
                });

                response.value = completion.choices[0].message.content;
            } catch (error) {
                console.error("Error fetching response from OpenAI:", error);
                response.value = "An error occurred while fetching the response.";
            } finally {
                isLoading.value = false;
                userInput.value = '';
            }
        };

        return {
            userInput,
            response,
            isLoading,
            handleSubmit
        };
    }
}
</script>

<style scoped>
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

.ai-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(45deg, #000000, #1a042b, #0f1a40, #02010a);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding: 2rem;
}

.form-wrapper {
    width: 100%;
    max-width: 800px;
    background: rgba(255, 255, 255, 0.98);
    padding: 3rem;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.form-title {
    text-align: center;
    font-size: 2.5rem;
    color: #2d3748;
    margin-bottom: 1.5rem;
}

.input-area {
    width: 100%;
    padding: 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    font-size: 1.1rem;
    margin-bottom: 1rem;
    resize: none;
}

.input-area:focus {
    border-color: #667eea;
    outline: none;
    box-shadow: 0 0 8px rgba(102, 126, 234, 0.2);
}

.submit-btn {
    width: 100%;
    padding: 1rem;
    font-size: 1.2rem;
    background-color: #667eea;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.submit-btn:disabled {
    background-color: #a0aec0;
    cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
    background-color: #5a67d8;
}

.response-area {
    margin-top: 2rem;
}

.response-title {
    font-size: 1.5rem;
    color: #2d3748;
}

.response-text {
    font-size: 1.1rem;
    color: #4a5568;
}

.spinner {
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top: 4px solid white;
    border-radius: 50%;
    width: 24px;
    height: 24px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>