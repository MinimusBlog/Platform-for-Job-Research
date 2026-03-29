<template>
  <div class="container">
    <TheNavbar />

    <section class="hero">
      <div class="hero-left">
        <span class="badge">LEVEL UP YOUR CAREER</span>
        <h1 class="hero-title">Запусти<br />карьеру в IT</h1>

        <div class="accent-line"></div>

        <p class="hero-subtitle">
          Лучшие стажировки и вакансии для начинающих специалистов от ведущих IT-компаний страны.
        </p>

        <div class="hero-buttons">
          <router-link to="/register" class="btn-primary">Войти</router-link>
          <router-link to="/register" class="btn-outline">Регистрация</router-link>
        </div>

        <div class="companies">
          <p class="companies-label">НАМ ДОВЕРЯЮТ ЛУЧШИЕ</p>
          <div class="companies-logos">
            <div class="company-logo">Яндекс</div>
            <div class="company-logo">VK</div>
            <div class="company-logo">Сбер</div>
            <div class="company-logo">Тинькофф</div>
          </div>
        </div>
      </div>

      <div class="hero-right">
        <div class="stat-card">
          <div class="stat-icon">🚀</div>
          <div>
            <div class="stat-number">1,240+</div>
            <div class="stat-label">Активных стажировок</div>
          </div>
        </div>

        <div class="feature-cards">
          <div class="feature-card">
            <div class="feature-icon">💼</div>
            <div>
              <div class="feature-title">Прямой путь в BigTech</div>
              <div class="feature-desc">Сотрудничаем напрямую с HR-департаментами</div>
            </div>
          </div>
          <div class="feature-card">
            <div class="feature-icon feature-icon--ai">AI</div>
            <div>
              <div class="feature-title">Умный подбор</div>
              <div class="feature-desc">Алгоритм подберёт вакансии по твоему стеку</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import TheNavbar from '@/components/layout/TheNavbar.vue'
</script>

<style scoped>
body {
  background: var(--color-bg);
}

.container {
  display: grid;
  grid-template-rows: auto 1fr;
  min-height: 100vh;
  max-width: 1440px;
  margin: 0 auto;
  font-family: 'Montserrat', sans-serif;
}

.feature-icon--ai {
  background: rgba(99, 102, 241, 0.15);
  color: #818cf8;
}

/* ── Hero: grid из двух колонок ── */
.hero {
  display: grid;
  grid-template-columns: 1fr 380px;
  align-items: center;
  gap: 60px;
  padding: 40px 60px;
}

.hero-left {
  display: flex;
  flex-direction: column;
  max-width: 520px;
}

.badge {
  font-size: 11px;
  border: 1px solid var(--color-border);
  border-radius: 25px;
  padding: 6px 16px;
  color: #6b7280;
  letter-spacing: 2px;
  display: inline-block;
  margin-bottom: 28px;
  align-self: flex-start;
}

.hero-title {
  font-size: 72px;
  font-weight: 900;
  line-height: 1.05;
  margin-bottom: 24px;
  color: white;
}

.accent-line {
  width: 60px;
  height: 3px;
  background: var(--color-mint);
  margin-bottom: 24px;
  border-radius: 2px;
}

.hero-subtitle {
  color: #9ca3af;
  font-size: 17px;
  line-height: 1.7;
  margin-bottom: 40px;
}

.hero-buttons {
  display: flex;
  gap: 16px;
}

.btn-primary {
  background: var(--color-mint);
  color: #0d1117;
  font-weight: 700;
  padding: 16px 36px;
  border-radius: 25px;
  border: none;
  cursor: pointer;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  transition:
    background 0.2s,
    transform 0.15s,
    box-shadow 0.2s;

  &:hover {
    background: var(--color-mint-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 229, 160, 0.3);
  }

  &:active {
    transform: translateY(0);
  }
}

.btn-outline {
  background: transparent;
  border: 1px solid var(--color-border);
  color: white;
  font-weight: 700;
  padding: 16px 36px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  transition:
    border-color 0.2s,
    color 0.2s,
    background 0.2s,
    transform 0.15s;

  &:hover {
    border-color: var(--color-mint);
    color: var(--color-mint);
    background: var(--color-mint-dim);
    transform: translateY(-2px);
  }

  &:active {
    transform: translateY(0);
  }
}

.companies {
  margin-top: 48px;
}

.companies-label {
  font-size: 10px;
  color: #4b5563;
  letter-spacing: 2px;
  margin-bottom: 16px;
}

.companies-logos {
  display: flex;
  gap: 16px;
}

.company-logo {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 8px 20px;
  font-size: 13px;
  font-weight: 600;
  color: #6b7280;
  transition:
    border-color 0.2s,
    color 0.2s;

  &:hover {
    border-color: var(--color-mint);
    color: white;
  }
}

/* ── Правая часть: grid карточек ── */
.hero-right {
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 16px;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 20px;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 28px 32px;
  transition:
    border-color 0.2s,
    transform 0.2s;

  &:hover {
    border-color: var(--color-mint);
    transform: translateY(-3px);
  }
}

.stat-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  background: var(--color-mint-dim);
  border-radius: 12px;
  font-size: 24px;
  flex-shrink: 0;
}

.stat-number {
  font-size: 34px;
  font-weight: 800;
  color: var(--color-mint);
}

.stat-label {
  font-size: 11px;
  color: #6b7280;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-top: 6px;
}

.feature-cards {
  display: grid;
  grid-template-rows: 1fr 1fr;
  gap: 12px;
}

.feature-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 14px;
  padding: 20px 24px;
  transition:
    border-color 0.2s,
    transform 0.2s;

  &:hover {
    border-color: var(--color-border-light);
    transform: translateY(-2px);
  }
}

.feature-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  background: var(--color-mint-dim);
  color: var(--color-mint);
  border-radius: 10px;
  font-size: 18px;
  font-weight: 800;
  flex-shrink: 0;
}

.feature-title {
  font-size: 14px;
  font-weight: 700;
  color: white;
  margin-bottom: 4px;
}

.feature-desc {
  font-size: 12px;
  color: #6b7280;
  line-height: 1.5;
}

/* ── Адаптив ── */
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    padding: 60px 40px;
  }

  .hero-right {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto;
  }

  .feature-cards {
    grid-template-rows: auto;
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 768px) {
  .navbar {
    display: grid;
    grid-template-columns: 1fr auto;
    grid-template-areas:
      'logo burger'
      'links links';
    padding: 16px 24px;
    gap: 0;
  }

  .logo {
    grid-area: logo;
  }
  .burger {
    grid-area: burger;
    display: flex;
  }
  .btn-login {
    display: inline-block;
    text-decoration: none;
  }

  .nav-links {
    grid-area: links;
    display: none;
    flex-direction: column;
    gap: 16px;
    padding: 16px 0;
    border-top: 1px solid var(--color-border);
    margin-top: 16px;

    &.open {
      display: flex;
    }
  }

  .hero {
    padding: 40px 24px;
  }

  .hero-title {
    font-size: 48px;
  }

  .hero-right {
    grid-template-columns: 1fr;
  }

  .feature-cards {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 38px;
  }

  .hero-buttons {
    flex-direction: column;
  }

  .btn-primary,
  .btn-outline {
    text-align: center;
  }
}
</style>
