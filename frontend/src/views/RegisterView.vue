<template>
  <div class="container">
    <TheNavbar />

    <main class="main">
      <div class="card">
        <div class="progress">
          <div class="progress-bar" :class="{ active: registerStore.currentStep >= 1 }"></div>
          <div class="progress-bar" :class="{ active: registerStore.currentStep >= 2 }"></div>
          <div class="progress-bar" :class="{ active: registerStore.currentStep >= 3 }"></div>
        </div>

        <div class="card-header">
          <p class="step-label">ШАГ {{ registerStore.currentStep }} ИЗ 3</p>
          <h1 class="card-title">
            {{
              registerStore.currentStep === 1
                ? 'Выберите вашу роль'
                : registerStore.currentStep === 2
                  ? 'Вход в систему'
                  : 'Регистрация'
            }}
          </h1>
          <p class="card-subtitle">
            {{
              registerStore.currentStep === 1
                ? 'Определите свой путь в экосистеме ТРАМПЛИН'
                : registerStore.currentStep === 2
                  ? 'Введите данные для входа'
                  : 'Заполните информацию для регистрации'
            }}
          </p>
        </div>

        <div v-if="registerStore.currentStep === 1" class="step-wrapper">
          <div class="roles">
            <div
              v-for="role in rolesConfig"
              :key="role.id"
              class="role-card"
              :class="{ selected: registerStore.selectedRole === role.id }"
              @click="registerStore.setRole(role.id)"
            >
              <div v-if="registerStore.selectedRole === role.id" class="check-icon">✓</div>
              <div class="role-icon">{{ role.icon }}</div>
              <div class="role-title">{{ role.title }}</div>
              <div class="role-desc">{{ role.desc }}</div>
            </div>
          </div>

          <div v-if="registerStore.selectedRole" class="login-prompt">
            <p class="login-text">Уже есть аккаунт?</p>
            <a href="#" class="login-link-btn" @click.prevent="registerStore.setStep(2)">Войти</a>
          </div>

          <div class="step-actions">
            <button
              class="btn-continue"
              :disabled="!registerStore.selectedRole"
              @click="registerStore.setStep(3)"
            >
              Продолжить
            </button>
          </div>
        </div>

        <div v-else-if="registerStore.currentStep === 2" class="login-form">
          <form class="form-container" @submit.prevent="handleLogin">
            <div class="form-group">
              <label class="form-label">Email</label>
              <input
                v-model="loginEmail"
                type="email"
                class="form-input"
                :placeholder="getEmailPlaceholder()"
                required
              />
            </div>
            <div class="form-group">
              <label class="form-label">Пароль</label>
              <input
                v-model="loginPassword"
                type="password"
                class="form-input"
                placeholder="••••••••"
                required
              />
            </div>
            <div class="form-actions">
              <button type="submit" class="btn-login-main" :disabled="loading">
                {{ loading ? 'Вход...' : 'Войти' }}
              </button>
              <button type="button" class="btn-back" @click="registerStore.setStep(1)">
                ← Назад к выбору роли
              </button>
            </div>
          </form>
        </div>

        <div v-else-if="registerStore.currentStep === 3" class="register-form">
          <div class="form-section">
            <h3 class="section-title">Основная информация</h3>
            <div class="form-grid">
              <div class="form-group">
                <label class="form-label">Email</label>
                <input
                  v-model="formEmail"
                  type="email"
                  class="form-input"
                  placeholder="name@example.com"
                  required
                />
              </div>

              <div class="form-group">
                <label class="form-label">Имя пользователя</label>
                <input
                  v-model="formUsername"
                  type="text"
                  class="form-input"
                  placeholder="Ivan_Dev"
                  required
                />
              </div>

              <div v-if="registerStore.selectedRole === 'employer'" class="form-group">
                <label class="form-label">Название компании</label>
                <input
                  v-model="formCompanyName"
                  type="text"
                  class="form-input"
                  placeholder="TechCorp Inc."
                  required
                />
              </div>

              <div class="form-group">
                <label class="form-label">Пароль</label>
                <input
                  v-model="formPassword"
                  type="password"
                  class="form-input"
                  placeholder="••••••••"
                  required
                />
              </div>
              <div class="form-group">
                <label class="form-label">Подтверждение</label>
                <input
                  v-model="formConfirmPassword"
                  type="password"
                  class="form-input"
                  placeholder="••••••••"
                  required
                />
              </div>
            </div>
          </div>

          <div class="form-actions">
            <button
              type="button"
              class="btn-register-main"
              :disabled="loading"
              @click="handleRegister"
            >
              {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
            </button>
            <button type="button" class="btn-back" @click="registerStore.setStep(1)">
              ← Назад
            </button>
          </div>
        </div>
      </div>
    </main>

    <footer class="footer">
      <p class="footer-copy">© 2026 ТРАМПЛИН KINETIC. ALL RIGHTS RESERVED.</p>
    </footer>
  </div>
</template>

<script setup>
import TheNavbar from '@/components/layout/TheNavbar.vue'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { useRegisterStore } from '../stores/register'
import axios from 'axios'

const router = useRouter()
const authStore = useAuthStore()
const registerStore = useRegisterStore()

const loading = ref(false)
const loginEmail = ref('')
const loginPassword = ref('')

const rolesConfig = [
  { id: 'admin', icon: '👑', title: 'Администратор', desc: 'УПРАВЛЕНИЕ СИСТЕМОЙ' },
  { id: 'applicant', icon: '🎓', title: 'Я соискатель', desc: 'СТУДЕНТ ИЛИ ВЫПУСКНИК' },
  { id: 'employer', icon: '🏢', title: 'Я работодатель', desc: 'КОМПАНИЯ ИЛИ ИП' },
]

onMounted(() => {
  registerStore.resetRegistration()
})

// Computed properties for v-model mapping to store
const formEmail = computed({
  get: () => registerStore.formData.email,
  set: (v) => registerStore.updateFormData({ email: v }),
})
const formPassword = computed({
  get: () => registerStore.formData.password,
  set: (v) => registerStore.updateFormData({ password: v }),
})
const formConfirmPassword = computed({
  get: () => registerStore.formData.confirmPassword,
  set: (v) => registerStore.updateFormData({ confirmPassword: v }),
})
const formUsername = computed({
  get: () => registerStore.formData.username,
  set: (v) => registerStore.updateFormData({ username: v }),
})
const formCompanyName = computed({
  get: () => registerStore.formData.companyName,
  set: (v) => registerStore.updateFormData({ companyName: v }),
})

const getEmailPlaceholder = () => {
  const map = {
    admin: 'admin@trampoline.ru',
    applicant: 'applicant@trampoline.ru',
    employer: 'employer@trampoline.ru',
  }
  return map[registerStore.selectedRole] || 'your@email.com'
}

const handleRegister = async () => {
  if (formPassword.value !== formConfirmPassword.value) {
    alert('Пароли не совпадают!')
    return
  }

  loading.value = true
  try {
    // Подготовка данных с учетом возможных требований FastAPI (Pydantic)
    const payload = {
      email: formEmail.value,
      password: formPassword.value,
      role: registerStore.selectedRole,
      username: formUsername.value || formEmail.value.split('@')[0],
      full_name: formUsername.value || 'User', // Часто обязательное поле
    }

    console.log('Отправка на бэкенд:', payload)

    const response = await axios.post('http://localhost:8000/api/auth/register', payload)
    const data = response?.data || {}

    // Если бэкенд вернул токен/пользователя — используем его, иначе создаём минимальную сессию локально
    const userData = {
      ...data,
      email: data.email || payload.email,
      role: data.role || payload.role,
      username: data.username || payload.username,
      name: data.name || data.username || payload.username,
    }

    authStore.login(userData)

    if (registerStore.selectedRole === 'applicant') {
      router.push({ name: 'applicant-jobs' })
      return
    }

    if (registerStore.selectedRole === 'employer') {
      router.push({ name: 'company-dashboard' })
      return
    }

    if (registerStore.selectedRole === 'admin') {
      router.push({ name: 'admin-main' })
      return
    }

    router.push('/')
  } catch (error) {
    console.error('Ошибка:', error.response?.data)
    const detail = error.response?.data?.detail

    // Если бэкенд вернул массив ошибок валидации
    if (Array.isArray(detail)) {
      const errorMsg = detail.map((err) => `${err.loc[1] || 'поле'}: ${err.msg}`).join('\n')
      alert(`Ошибка валидации:\n${errorMsg}`)
    } else {
      alert(detail || 'Ошибка сервера. Проверьте логи Docker.')
    }
  } finally {
    loading.value = false
  }
}

const handleLogin = async () => {
  loading.value = true
  try {
    // Здесь будет запрос на получение токена
    const userData = {
      email: loginEmail.value,
      role: registerStore.selectedRole,
      username: loginEmail.value?.split('@')?.[0] || 'user',
      name: loginEmail.value?.split('@')?.[0] || 'user',
    }
    authStore.login(userData)

    if (registerStore.selectedRole === 'applicant') {
      router.push({ name: 'applicant-jobs' })
      return
    }
    if (registerStore.selectedRole === 'employer') {
      router.push({ name: 'company-dashboard' })
      return
    }
    if (registerStore.selectedRole === 'admin') {
      router.push({ name: 'admin-main' })
      return
    }
    router.push('/')
  } catch (error) {
    alert('Ошибка входа. Проверьте данные.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* Стили без изменений для сохранения дизайна */
.container {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  background: var(--color-bg);
  font-family: 'Montserrat', sans-serif;
}
.main {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}
.card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 32px;
  width: 100%;
  max-width: 480px;
  display: flex;
  flex-direction: column;
  gap: 32px;
}
.progress {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 8px;
}
.progress-bar {
  height: 3px;
  background: var(--color-border);
  border-radius: 2px;
  transition: background 0.3s;
}
.progress-bar.active {
  background: var(--color-mint);
}
.card-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
}
.step-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--color-mint);
  letter-spacing: 2px;
}
.card-title {
  font-size: 28px;
  font-weight: 800;
  color: white;
}
.card-subtitle {
  font-size: 14px;
  color: #6b7280;
}
.step-wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.roles {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}
.role-card {
  background: var(--color-bg-elevated);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 16px 12px;
  cursor: pointer;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-height: 140px;
  transition: all 0.2s;
}
.role-card.selected {
  border-color: var(--color-mint);
  background: rgba(0, 229, 160, 0.05);
}
.check-icon {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--color-mint);
  color: #0d1117;
  font-size: 13px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
}
.role-icon {
  font-size: 24px;
}
.role-title {
  font-size: 14px;
  font-weight: 700;
  color: white;
}
.role-desc {
  font-size: 10px;
  font-weight: 600;
  color: #6b7280;
  letter-spacing: 1.2px;
}
.login-prompt {
  text-align: center;
  margin-top: 10px;
}
.login-link-btn {
  font-size: 14px;
  font-weight: 700;
  color: var(--color-mint);
  text-decoration: none;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}
.form-label {
  font-size: 14px;
  font-weight: 600;
  color: white;
}
.form-input {
  width: 100%;
  padding: 14px 16px;
  background: var(--color-bg-elevated);
  border: 1px solid var(--color-border);
  border-radius: 10px;
  color: white;
}
.btn-continue,
.btn-login-main,
.btn-register-main {
  width: 100%;
  padding: 16px;
  background: var(--color-mint);
  color: #0d1117;
  font-weight: 700;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-continue:hover,
.btn-login-main:hover,
.btn-register-main:hover {
  background: var(--color-mint-dark);
  transform: translateY(-2px);
}
.btn-continue:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
.btn-back {
  width: 100%;
  padding: 14px;
  background: transparent;
  border: 1px solid var(--color-border);
  color: white;
  font-weight: 600;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 10px;
}
.footer {
  padding: 20px;
  text-align: center;
  border-top: 1px solid var(--color-border);
  color: #4b5563;
  font-size: 11px;
}
@media (max-width: 480px) {
  .roles {
    grid-template-columns: 1fr;
  }
}
</style>
