<template>
  <div class="min-h-screen bg-[#050505] text-white">
    <TheNavbar />
    <div class="flex items-center justify-center px-4 py-10">
      <div class="bg-white/5 border border-white/10 rounded-2xl p-8 w-full max-w-md">
        <h2 class="text-2xl font-bold text-center mb-6">Вход в систему</h2>

        <form @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm text-gray-400 mb-2">Email</label>
            <input
              v-model="email"
              type="email"
              class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:border-mint outline-none"
              placeholder="admin@example.com"
              required
            />
          </div>

          <div>
            <label class="block text-sm text-gray-400 mb-2">Пароль</label>
            <input
              v-model="password"
              type="password"
              class="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:border-mint outline-none"
              placeholder="••••••••"
              required
            />
          </div>

          <button
            type="submit"
            class="w-full bg-mint text-bg font-bold py-3 rounded-lg hover:bg-mint/80 transition-colors"
            :disabled="loading"
          >
            {{ loading ? 'Вход...' : 'Войти' }}
          </button>
        </form>

        <div class="mt-6 text-center text-sm text-gray-400">
          <p class="mb-4">Тестовые учетные данные:</p>
          <div class="grid grid-cols-1 gap-3 text-xs">
            <div class="bg-white/5 p-3 rounded-lg">
              <p class="font-bold text-mint mb-1">Администратор</p>
              <p>Email: admin@trampoline.ru</p>
              <p>Пароль: admin123</p>
            </div>
            <div class="bg-white/5 p-3 rounded-lg">
              <p class="font-bold text-mint mb-1">Соискатель</p>
              <p>Email: applicant@trampoline.ru</p>
              <p>Пароль: applicant123</p>
            </div>
            <div class="bg-white/5 p-3 rounded-lg">
              <p class="font-bold text-mint mb-1">Работодатель</p>
              <p>Email: employer@trampoline.ru</p>
              <p>Пароль: employer123</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import TheNavbar from '@/components/layout/TheNavbar.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true

  try {
    // Имитация API вызова (замените на реальный API)
    const testUsers = {
      'admin@trampoline.ru': {
        id: 1,
        email: 'admin@trampoline.ru',
        role: 'admin',
        name: 'Администратор',
      },
      'applicant@trampoline.ru': {
        id: 2,
        email: 'applicant@trampoline.ru',
        role: 'applicant',
        name: 'Соискатель',
      },
      'employer@trampoline.ru': {
        id: 3,
        email: 'employer@trampoline.ru',
        role: 'employer',
        name: 'Работодатель',
      },
    }

    const userData = testUsers[email.value]

    if (userData && password.value === `${userData.role}123`) {
      authStore.login(userData)

      // Перенаправление в зависимости от роли
      if (userData.role === 'admin') {
        router.push('/admin/main')
      } else if (userData.role === 'applicant') {
        router.push('/applicant')
      } else if (userData.role === 'employer') {
        router.push('/company/dashboard') // Предполагаем, что будет страница компании
      }
    } else {
      alert('Неверные учетные данные')
    }
  } catch (error) {
    console.error('Ошибка входа:', error)
    alert('Ошибка входа в систему')
  } finally {
    loading.value = false
  }
}
</script>
