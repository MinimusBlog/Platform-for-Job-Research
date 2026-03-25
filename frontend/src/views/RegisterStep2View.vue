<template>
  <div class="container">
    <TheNavbar />

    <main class="main">
      <div class="page-header">
        <span class="page-label">РЕГИСТРАЦИЯ</span>
        <span class="page-step">Шаг 2 из 2</span>
      </div>

      <!-- Progress bar -->
      <div class="progress">
        <div class="progress-bar done"></div>
        <div class="progress-bar active"></div>
      </div>

      <div class="card">
        <div class="card-header">
          <h1 class="card-title">Завершение профиля</h1>
          <p class="card-subtitle">
            {{
              role === 'employer'
                ? 'Пожалуйста, заполните данные для создания аккаунта работодателя.'
                : 'Пожалуйста, заполните данные для создания аккаунта соискателя.'
            }}
          </p>
        </div>

        <form class="form" @submit.prevent="handleSubmit">
          <!-- Общие поля -->
          <div class="form-grid">
            <div class="field">
              <label class="field-label">EMAIL</label>
              <input
                v-model="form.email"
                class="field-input"
                type="email"
                :placeholder="role === 'employer' ? 'name@company.com' : 'name@example.com'"
              />
            </div>
            <div class="field">
              <label class="field-label">ИМЯ ПОЛЬЗОВАТЕЛЯ</label>
              <input
                v-model="form.username"
                class="field-input"
                type="text"
                :placeholder="role === 'employer' ? 'Alex_HR' : 'Ivan_Dev'"
              />
            </div>
            <div class="field">
              <label class="field-label">ПАРОЛЬ</label>
              <input
                v-model="form.password"
                class="field-input"
                type="password"
                placeholder="••••••••"
              />
            </div>
            <div class="field">
              <label class="field-label">ПОВТОРИТЕ ПАРОЛЬ</label>
              <input
                v-model="form.confirmPassword"
                class="field-input"
                type="password"
                placeholder="••••••••"
              />
            </div>
          </div>

          <!-- Данные работодателя -->
          <template v-if="role === 'employer'">
            <div class="divider">
              <span>ДАННЫЕ КОМПАНИИ</span>
            </div>
            <div class="form-grid">
              <div class="field">
                <label class="field-label">НАЗВАНИЕ КОМПАНИИ</label>
                <input
                  v-model="form.companyName"
                  class="field-input"
                  type="text"
                  placeholder="Tech Kinetic Inc."
                />
              </div>
              <div class="field">
                <label class="field-label">ИНН / TAX ID</label>
                <input
                  v-model="form.inn"
                  class="field-input"
                  type="text"
                  placeholder="7700123456"
                />
              </div>
              <div class="field">
                <label class="field-label">КОРПОРАТИВНЫЙ ДОМЕН</label>
                <div class="input-prefix">
                  <span class="prefix">@</span>
                  <input
                    v-model="form.domain"
                    class="field-input prefix-input"
                    type="text"
                    placeholder="company.ru"
                  />
                </div>
              </div>
              <div class="field">
                <label class="field-label">LINKEDIN / HH.RU PROFILE</label>
                <input
                  v-model="form.profileUrl"
                  class="field-input"
                  type="url"
                  placeholder="https://hh.ru..."
                />
              </div>
            </div>
          </template>

          <!-- Данные соискателя -->
          <template v-if="role === 'applicant'">
            <div class="divider">
              <span>ДАННЫЕ СОИСКАТЕЛЯ</span>
            </div>
            <div class="form-grid">
              <div class="field">
                <label class="field-label">ФИО</label>
                <input
                  v-model="form.fullName"
                  class="field-input"
                  type="text"
                  placeholder="Иванов Иван Иванович"
                />
              </div>
              <div class="field">
                <label class="field-label">ВУЗ</label>
                <input
                  v-model="form.university"
                  class="field-input"
                  type="text"
                  placeholder="МГУ им. Ломоносова"
                />
              </div>
              <div class="field">
                <label class="field-label">КУРС / ГОД ВЫПУСКА</label>
                <input
                  v-model="form.year"
                  class="field-input"
                  type="text"
                  placeholder="3 курс / 2026"
                />
              </div>
              <div class="field">
                <label class="field-label">GITHUB / ПОРТФОЛИО</label>
                <input
                  v-model="form.portfolio"
                  class="field-input"
                  type="url"
                  placeholder="https://github.com"
                />
              </div>
            </div>
          </template>

          <button type="submit" class="btn-submit">ЗАРЕГИСТРИРОВАТЬСЯ</button>

          <button type="button" class="btn-back" @click="goBack">← Назад к выбору роли</button>

          <p class="login-link">Уже есть аккаунт? <RouterLink to="/login">Войти</RouterLink></p>
        </form>
      </div>
    </main>

    <footer class="footer">
      <p class="footer-copy">© 2024 ТРАМПЛИН KINETIC. ALL RIGHTS RESERVED.</p>
      <div class="footer-links">
        <a href="#">PRIVACY POLICY</a>
        <a href="#">TERMS OF SERVICE</a>
        <a href="#">SUPPORT</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import TheNavbar from '@/components/layout/TheNavbar.vue'

const router = useRouter()
const route = useRoute()

const role = route.query.role || 'applicant'

const form = reactive({
  email: '',
  username: '',
  password: '',
  confirmPassword: '',
  companyName: '',
  inn: '',
  domain: '',
  profileUrl: '',
  fullName: '',
  university: '',
  year: '',
  portfolio: '',
})

const goBack = () => router.push('/register')

const handleSubmit = () => {
  console.log('form submitted', { role, ...form })
}
</script>

<style scoped>
/* ── Layout ── */
.container {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  font-family: 'Montserrat', sans-serif;
  background-color: var(--color-bg, #f9fafb);
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 24px;
}

/* ── Header & Progress ── */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 616px;
  margin-bottom: 12px;
}

.page-label {
  font-size: 11px;
  font-weight: 600;
  color: #6b7280;
  letter-spacing: 2px;
}

.page-step {
  font-size: 14px;
  font-weight: 700;
  font-style: italic;
  color: var(--color-mint, #4fd1c5);
}

.progress {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  width: 100%;
  max-width: 616px;
  margin-bottom: 32px;
}

.progress-bar {
  height: 3px;
  background: var(--color-border, #e5e7eb);
  border-radius: 2px;
}

.progress-bar.done {
  background: var(--color-mint, #4fd1c5);
  opacity: 0.5;
}

.progress-bar.active {
  background: var(--color-mint, #4fd1c5);
}

/* ── Card ── */
.card {
  background: var(--color-bg-card, #ffffff);
  border: 1px solid var(--color-border, #e5e7eb);
  border-radius: 16px;
  padding: 40px;
  width: 100%;
  max-width: 616px;
}

.card-header {
  margin-bottom: 28px;
  text-align: center;
}

.card-title {
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 8px;
}

.card-subtitle {
  color: #6b7280;
  font-size: 14px;
}

/* ── Form & Grid ── */
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 24px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field-label {
  font-size: 10px;
  font-weight: 700;
  color: #374151;
}

.field-input {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--color-border, #e5e7eb);
  border-radius: 8px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s;
}

.field-input:focus {
  border-color: var(--color-mint, #4fd1c5);
}

/* ── Input Prefix (@) ── */
.input-prefix {
  display: flex;
  align-items: stretch;
}

.prefix {
  display: flex;
  align-items: center;
  padding: 0 12px;
  background: #f3f4f6;
  border: 1px solid var(--color-border, #e5e7eb);
  border-right: none;
  border-radius: 8px 0 0 8px;
  color: #6b7280;
  font-weight: 600;
  font-size: 14px;
}

.prefix-input {
  border-radius: 0 8px 8px 0 !important;
}

/* ── Divider ── */
.divider {
  display: flex;
  align-items: center;
  margin: 32px 0 24px;
  font-size: 10px;
  font-weight: 700;
  color: #9ca3af;
  letter-spacing: 1px;
}

.divider::before,
.divider::after {
  content: '';
  flex: 1;
  border-bottom: 1px solid var(--color-border, #e5e7eb);
}

.divider span {
  padding: 0 12px;
}

/* ── Buttons ── */
.btn-submit {
  width: 100%;
  padding: 16px;
  background: #000;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  margin-top: 12px;
  transition: opacity 0.2s;
}

.btn-submit:hover {
  opacity: 0.8;
}

.btn-back {
  width: 100%;
  background: none;
  border: none;
  color: #6b7280;
  margin-top: 16px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
}

.login-link {
  text-align: center;
  margin-top: 24px;
  font-size: 14px;
  color: #6b7280;
}

.login-link a {
  color: var(--color-mint, #4fd1c5);
  text-decoration: none;
  font-weight: 600;
}

/* ── Footer ── */
.footer {
  padding: 32px 24px;
  text-align: center;
}

.footer-copy {
  font-size: 10px;
  color: #9ca3af;
  margin-bottom: 12px;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.footer-links a {
  font-size: 10px;
  color: #6b7280;
  text-decoration: none;
  font-weight: 600;
}
</style>
