<template>
  <div class="container">
    <TheNavbar />

    <!-- Main -->
    <main class="main">
      <div class="card">
        <!-- Progress bar -->
        <div class="progress">
          <div class="progress-bar active"></div>
          <div class="progress-bar"></div>
        </div>

        <!-- Header -->
        <div class="card-header">
          <p class="step-label">ШАГ 1 ИЗ 2</p>
          <h1 class="card-title">Выберите вашу роль</h1>
          <p class="card-subtitle">Определите свой путь в экосистеме ТРАМПЛИН</p>
        </div>

        <!-- Role cards -->
        <div class="roles">
          <div
            class="role-card"
            :class="{ selected: selectedRole === 'applicant' }"
            @click="selectedRole = 'applicant'"
          >
            <div class="check-icon" v-if="selectedRole === 'applicant'">✓</div>
            <div class="role-icon">🎓</div>
            <div class="role-title">Я соискатель</div>
            <div class="role-desc">СТУДЕНТ ИЛИ ВЫПУСКНИК</div>
          </div>

          <div
            class="role-card"
            :class="{ selected: selectedRole === 'employer' }"
            @click="selectedRole = 'employer'"
          >
            <div class="check-icon" v-if="selectedRole === 'employer'">✓</div>
            <div class="role-icon">🏢</div>
            <div class="role-title">Я работодатель</div>
            <div class="role-desc">КОМПАНИЯ ИЛИ ИП</div>
          </div>
        </div>

        <!-- Button -->
        <button class="btn-continue" :disabled="!selectedRole" @click="nextStep">Продолжить</button>

        <!-- Login link -->
        <p class="login-link">
          Уже есть аккаунт?
          <a href="/login">Войти</a>
        </p>
      </div>
    </main>

    <!-- Footer -->
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import TheNavbar from '@/components/layout/TheNavbar.vue'

const router = useRouter()
const selectedRole = ref('applicant')

function nextStep() {
  if (!selectedRole.value) return
  router.push({ path: '/register/step2', query: { role: selectedRole.value } })
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  background: var(--color-bg);
  font-family: 'Montserrat', sans-serif;
}

/* ── Main ── */
.main {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

/* ── Card ── */
.card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 40px;
  width: 100%;
  max-width: 640px;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* ── Progress ── */
.progress {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.progress-bar {
  height: 3px;
  background: var(--color-border);
  border-radius: 2px;
  transition: background 0.3s;

  &.active {
    background: var(--color-mint);
  }
}

/* ── Header ── */
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

/* ── Roles ── */
.roles {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.role-card {
  background: var(--color-bg-elevated);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 28px 24px;
  cursor: pointer;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition:
    border-color 0.2s,
    transform 0.15s;

  &:hover {
    border-color: var(--color-border-light);
    transform: translateY(-2px);
  }

  &.selected {
    border-color: var(--color-mint);
    background: rgba(0, 229, 160, 0.05);
  }
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
  width: 48px;
  height: 48px;
  background: var(--color-bg-card);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}

.role-title {
  font-size: 16px;
  font-weight: 700;
  color: white;
}

.role-desc {
  font-size: 11px;
  font-weight: 600;
  color: #6b7280;
  letter-spacing: 1.5px;
}

/* ── Button ── */
.btn-continue {
  width: 100%;
  padding: 16px;
  background: var(--color-mint);
  color: #0d1117;
  font-weight: 700;
  font-size: 15px;
  font-family: 'Montserrat', sans-serif;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  transition:
    background 0.2s,
    transform 0.15s,
    box-shadow 0.2s;

  &:hover:not(:disabled) {
    background: var(--color-mint-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 229, 160, 0.3);
  }

  &:active:not(:disabled) {
    transform: translateY(0);
  }

  &:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
}

/* ── Login link ── */
.login-link {
  text-align: center;
  font-size: 14px;
  color: #6b7280;

  a {
    color: white;
    text-decoration: none;
    font-weight: 600;
    transition: color 0.2s;

    &:hover {
      color: var(--color-mint);
    }
  }
}

/* ── Footer ── */
.footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 32px;
  border-top: 1px solid var(--color-border);
}

.footer-copy {
  font-size: 11px;
  color: #4b5563;
  letter-spacing: 0.5px;
}

.footer-links {
  display: flex;
  gap: 24px;

  a {
    font-size: 11px;
    color: #4b5563;
    text-decoration: none;
    letter-spacing: 0.5px;
    transition: color 0.2s;

    &:hover {
      color: white;
    }
  }
}

/* ── Адаптив ── */
@media (max-width: 480px) {
  .card {
    padding: 28px 20px;
  }

  .roles {
    grid-template-columns: 1fr;
  }

  .footer {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
}
</style>
