import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// Настройка базового URL для axios
axios.defaults.baseURL = 'http://localhost:8000'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!user.value)
  const userRole = computed(() => user.value?.role)

  // Вспомогательные геттеры ролей
  const isAdmin = computed(() => user.value?.role === 'admin')
  const isApplicant = computed(() => user.value?.role === 'applicant')
  const isEmployer = computed(() => user.value?.role === 'employer')

  async function register(registrationData) {
    loading.value = true
    error.value = null
    try {
      const response = await axios.post('/api/auth/register', registrationData)
      
      // Бэкенд возвращает 201 Created — обрабатываем как успех
      if (response.status === 201 || response.status === 200) {
        if (response.data && (response.data.access_token || response.data.email)) {
          login(response.data)
        }
        return response.data
      }
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка при регистрации'
      console.error('Ошибка регистрации:', err)
      throw err // Пробрасываем ошибку дальше в компонент для модалки
    } finally {
      loading.value = false
    }
  }

  function login(userData) {
    user.value = userData
    localStorage.setItem('user', JSON.stringify(userData))
    
    // Если бэкенд возвращает токен, устанавливаем его в заголовки axios
    if (userData.access_token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${userData.access_token}`
    }
  }

  function logout() {
    user.value = null
    localStorage.removeItem('user')
    delete axios.defaults.headers.common['Authorization']
  }

  /**
   * ПРОВЕРКА СОСТОЯНИЯ ПРИ ЗАГРУЗКЕ
   */
  function checkAuth() {
    const savedUser = localStorage.getItem('user')
    if (savedUser) {
      try {
        const parsedUser = JSON.parse(savedUser)
        user.value = parsedUser
        if (parsedUser.access_token) {
          axios.defaults.headers.common['Authorization'] = `Bearer ${parsedUser.access_token}`
        }
      } catch (e) {
        localStorage.removeItem('user')
      }
    }
  }

  return {
    user,
    loading,
    error,
    isAuthenticated,
    userRole,
    isAdmin,
    isApplicant,
    isEmployer,
    login,
    register,
    logout,
    checkAuth
  }
})