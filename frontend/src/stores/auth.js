import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// Настройка базового URL для axios
axios.defaults.baseURL = 'http://localhost:8000'

export const useAuthStore = defineStore('auth', () => {
  // СОСТОЯНИЕ
    const user = ref(null)
    const loading = ref(false)
    const error = ref(null)

  // ГЕТТЕРЫ
    const isAuthenticated = computed(() => !!user.value)
    const userRole = computed(() => user.value?.role)

  // Проверка прав
    const isAdmin = computed(() => user.value?.role === 'admin')
    const isApplicant = computed(() => user.value?.role === 'applicant')
    const isEmployer = computed(() => user.value?.role === 'employer')

/**
   * Логика Onboarding: 
   * Считаем пройденным, если роль не 'employer' или если флаг onboarded явно равен true
   */
    const isOnboarded = computed(() => {
        if (!user.value) return false
        if (user.value.role === 'employer') {
        return !!user.value.onboarded 
        }
        return true // Для соискателей и админов по умолчанию true
    })

/**
   * Установка заголовка авторизации для всех запросов axios
   */
    const setAuthHeader = (token) => {
        if (token) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
        } else {
        delete axios.defaults.headers.common['Authorization']
        }
    }

/**
   * Регистрация нового пользователя
   */
    async function register(registrationData) {
        loading.value = true
        error.value = null
        try {
        const response = await axios.post('/api/auth/register', registrationData)
        
        // Если бэкенд возвращает 201 или 200, сразу авторизуем
        if (response.status === 201 || response.status === 200) {
            if (response.data) {
            login(response.data)
            }
            return response.data
        }
        } catch (err) {
        error.value = err.response?.data?.detail || 'Ошибка при регистрации'
        console.error('Ошибка регистрации:', err)
        throw err 
        } finally {
        loading.value = false
        }
    }

/**
   * Вход в систему и сохранение данных
   */
    function login(userData) {
        user.value = userData
        localStorage.setItem('user', JSON.stringify(userData))
        
        if (userData.access_token) {
        setAuthHeader(userData.access_token)
        }
    }

/**
   * Завершение онбординга (вызывать на последнем шаге настройки профиля)
   */
    function completeOnboarding() {
        if (user.value && user.value.role === 'employer') {
        user.value.onboarded = true
        // Обновляем данные в localStorage, чтобы сохранить состояние
        localStorage.setItem('user', JSON.stringify(user.value))
        }
    }

    /**
   * Выход из системы
   */
    function logout() {
        user.value = null
        localStorage.removeItem('user')
        setAuthHeader(null)
    }

    /**
   * ПРОВЕРКА СОСТОЯНИЯ ПРИ ЗАГРУЗКЕ ПРИЛОЖЕНИЯ
   */
    function checkAuth() {
        const savedUser = localStorage.getItem('user')
        if (savedUser) {
        try {
            const parsedUser = JSON.parse(savedUser)
            user.value = parsedUser
            if (parsedUser.access_token) {
            setAuthHeader(parsedUser.access_token)
            }
        } catch (e) {
            console.error('Ошибка парсинга пользователя из localStorage:', e)
            logout()
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
        isOnboarded,
        login,
        register,
        logout,
        checkAuth,
        completeOnboarding
    }
    })