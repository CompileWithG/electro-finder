export default defineNuxtConfig({
  plugins: [
    '~/plugins/piniaPersistedState.js',
  ],
  modules: ['@nuxtjs/tailwindcss', '@primevue/nuxt-module', '@pinia/nuxt'],

  // Defaults options
  tailwindcss: {
    cssPath: ['~/assets/css/tailwind.css', { injectPosition: "first" }],
    config: {},
    viewer: true,
    exposeConfig: false,
  },

  compatibilityDate: '2025-02-14',
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap"
        }
      ]
    }
  }
})