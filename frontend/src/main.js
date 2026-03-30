import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import { useAuthStore } from './stores/auth'

import './assets/main.css'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)

// 1. Сначала инициализируем данные пользователя
const authStore = useAuthStore()
authStore.checkAuth()

// 2. Только после того, как данные в Store загружены, подключаем роутер
app.use(router)

// 3. Монтируем приложение
app.mount('#app')