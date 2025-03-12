// plugins/piniaPersistedState.js
import { defineNuxtPlugin } from "#app";
import { createPinia } from "pinia";
import { createPersistedState } from "pinia-plugin-persistedstate";

export default defineNuxtPlugin((nuxtApp) => {
  const pinia = createPinia();

  // Only use the persisted state plugin in the client-side
  if (process.client) {
    pinia.use(createPersistedState());
  }

  nuxtApp.vueApp.use(pinia);
});
