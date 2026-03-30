<template>
  <div class="dashboard">
    <aside class="sidebar">
      <div class="logo">ТРАМПЛИН</div>

      <div class="user-mini-card">
        <div class="avatar-container">
          <div class="avatar-sm"></div>
          <div class="online-dot"></div>
        </div>
        <div class="user-info">
          <span class="user-name">{{ displayName }}</span>
          <span class="user-status">IT СОИСКАТЕЛЬ • ПОДБОР ВАКАНСИЙ</span>
        </div>
        <button class="btn-update">ОБНОВИТЬ РЕЗЮМЕ</button>
      </div>

      <nav class="side-nav">
        <router-link :to="{ name: 'applicant-jobs' }" class="nav-item" :class="{ active: activeNav === 'jobs' }">
          <span>🔎</span> ПОИСК ВАКАНСИЙ
        </router-link>

        <router-link :to="{ name: 'applicant' }" class="nav-item" :class="{ active: activeNav === 'applications' }">
          <span>📄</span> МОИ ЗАЯВКИ
        </router-link>

        <router-link
          :to="{ name: 'applicant-profile' }"
          class="nav-item"
          :class="{ active: activeNav === 'profile' }"
        >
          <span>👤</span> ПРОФИЛЬ
        </router-link>

        <router-link
          :to="{ name: 'applicant-network' }"
          class="nav-item"
          :class="{ active: activeNav === 'networking' }"
        >
          <span>🌐</span> НЕТВОРКИНГ
        </router-link>
      </nav>

      <div class="side-footer">
        <a href="#" class="nav-item"><span>🎧</span> ПОДДЕРЖКА</a>
        <button class="nav-item logout" type="button" @click="handleLogout"><span>🚪</span> ВЫЙТИ</button>
      </div>
    </aside>

    <main class="main-content">
      <header class="top-bar">
        <div class="top-nav-links">
          <span class="active">Поиск вакансий</span>
          <span>Мои заявки</span>
          <span>Нетворкинг</span>
        </div>
        <div class="top-actions">
          <span class="icon">🔔</span>
          <span class="icon">⚡</span>
          <div class="user-circle">{{ initials }}</div>
        </div>
      </header>

      <div class="content-wrapper">
        <section class="hero-section">
          <div class="section-title">
            <span class="label">ВАКАНСИИ ДЛЯ IT</span>
            <h1>Поиск вакансий</h1>
            <p>10 подобранных вакансий, чтобы вы могли начать откликаться сразу после регистрации.</p>
          </div>
          <div class="filters card">
            <div class="filters-title">Фильтры</div>
            <div class="filters-row">
              <div class="pill active">Junior</div>
              <div class="pill">Internship</div>
              <div class="pill">Remote</div>
              <div class="pill">Москва</div>
            </div>
          </div>
        </section>

        <div class="table-container card">
          <table class="apps-table">
            <thead>
              <tr>
                <th>КОМПАНИЯ</th>
                <th>ДОЛЖНОСТЬ</th>
                <th>ФОРМАТ</th>
                <th>УРОВЕНЬ</th>
                <th>СТЕК</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="job in jobs" :key="job.id">
                <td>
                  <div class="company-cell">
                    <div class="company-logo" :style="{ backgroundColor: job.logoBg }">
                      {{ job.logo }}
                    </div>
                    {{ job.company }}
                  </div>
                </td>
                <td>
                  <div class="job-title">{{ job.title }}</div>
                  <div class="job-meta">{{ job.location }} • {{ job.salary }}</div>
                </td>
                <td>
                  <span class="badge" :class="job.format === 'Remote' ? 'badge-remote' : 'badge-hybrid'">
                    {{ job.format }}
                  </span>
                </td>
                <td>
                  <span class="badge badge-level">{{ job.level }}</span>
                </td>
                <td>
                  <div class="stack-cell">
                    <span v-for="tag in job.tags" :key="tag" class="tag">{{ tag }}</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>

          <div class="pagination">
            <span>Показано 10 из 10 вакансий</span>
            <div class="page-controls">
              <button disabled>&lt;</button>
              <button class="active" disabled>&gt;</button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const activeNav = 'jobs'
const router = useRouter()
const authStore = useAuthStore()

const displayName = computed(() => authStore.user?.name || authStore.user?.username || authStore.user?.email || 'Соискатель')
const initials = computed(() => {
  const src = (displayName.value || '').trim()
  if (!src) return 'U'
  const parts = src.split(/\s+/).slice(0, 2)
  const letters = parts.map((p) => (p[0] || '').toUpperCase()).join('')
  return letters || 'U'
})

const jobs = ref([
  {
    id: 1,
    company: 'Quantum Systems',
    title: 'Junior Frontend Developer',
    location: 'Москва',
    salary: 'от 120 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['Vue', 'TypeScript', 'CSS'],
    logo: '田',
    logoBg: '#2d333b',
  },
  {
    id: 2,
    company: 'Nova Labs',
    title: 'Intern UI/UX Engineer',
    location: 'Санкт-Петербург',
    salary: 'от 80 000 ₽',
    format: 'Remote',
    level: 'Intern',
    tags: ['Figma', 'Design Systems', 'UX'],
    logo: '▦',
    logoBg: '#2d333b',
  },
  {
    id: 3,
    company: 'Aether Cloud',
    title: 'Junior Backend Developer',
    location: 'Казань',
    salary: 'от 140 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['Python', 'FastAPI', 'PostgreSQL'],
    logo: '☁',
    logoBg: '#1e3a2f',
  },
  {
    id: 4,
    company: 'Orbital Tech',
    title: 'SRE / DevOps Engineer',
    location: 'Москва',
    salary: 'от 170 000 ₽',
    format: 'Hybrid',
    level: 'Junior+',
    tags: ['Linux', 'Docker', 'CI/CD'],
    logo: '🚀',
    logoBg: '#3d2b2b',
  },
  {
    id: 5,
    company: 'DeepMind AI',
    title: 'ML Engineer (Junior)',
    location: 'Remote',
    salary: 'от 180 000 ₽',
    format: 'Remote',
    level: 'Junior',
    tags: ['PyTorch', 'NLP', 'MLOps'],
    logo: '🧠',
    logoBg: '#2d333b',
  },
  {
    id: 6,
    company: 'Kinetic Payments',
    title: 'QA Engineer (Manual/Auto)',
    location: 'Екатеринбург',
    salary: 'от 110 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['Postman', 'Playwright', 'SQL'],
    logo: '⚙',
    logoBg: '#2d333b',
  },
  {
    id: 7,
    company: 'Vector Data',
    title: 'Data Analyst (IT)',
    location: 'Новосибирск',
    salary: 'от 130 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['SQL', 'BI', 'Python'],
    logo: '∑',
    logoBg: '#2d333b',
  },
  {
    id: 8,
    company: 'Signal Mobile',
    title: 'Junior Android Developer',
    location: 'Москва',
    salary: 'от 150 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['Kotlin', 'Android', 'REST'],
    logo: '📱',
    logoBg: '#2d333b',
  },
  {
    id: 9,
    company: 'Arctic Web',
    title: 'Junior Fullstack Developer',
    location: 'Remote',
    salary: 'от 160 000 ₽',
    format: 'Remote',
    level: 'Junior',
    tags: ['Node.js', 'Vue', 'PostgreSQL'],
    logo: '❄',
    logoBg: '#2d333b',
  },
  {
    id: 10,
    company: 'SecureStack',
    title: 'Junior Security Engineer',
    location: 'Москва',
    salary: 'от 175 000 ₽',
    format: 'Hybrid',
    level: 'Junior',
    tags: ['OWASP', 'AppSec', 'Burp'],
    logo: '🛡',
    logoBg: '#2d333b',
  },
])

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}
</script>

<style scoped>
.dashboard {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100vh;
  background: var(--color-bg);
  color: white;
  font-family: 'Montserrat', sans-serif;
}

.sidebar {
  background: var(--color-bg-card);
  border-right: 1px solid var(--color-border);
  padding: 24px;
  display: flex;
  flex-direction: column;
}

.logo {
  color: var(--color-mint);
  font-weight: 800;
  font-size: 20px;
  letter-spacing: 1px;
  margin-bottom: 40px;
}

.user-mini-card {
  background: rgba(255, 255, 255, 0.03);
  padding: 16px;
  border-radius: 12px;
  margin-bottom: 30px;
}

.avatar-container {
  position: relative;
  width: 40px;
  margin-bottom: 12px;
}

.avatar-sm {
  width: 40px;
  height: 40px;
  background: var(--color-border);
  border-radius: 50%;
}

.online-dot {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 10px;
  height: 10px;
  background: var(--color-mint);
  border-radius: 50%;
  border: 2px solid var(--color-bg-card);
}

.user-info {
  margin: 12px 0;
}

.user-name {
  display: block;
  font-weight: 600;
  font-size: 14px;
}

.user-status {
  font-size: 10px;
  color: var(--text-muted);
}

.btn-update {
  width: 100%;
  background: var(--color-mint);
  border: none;
  padding: 10px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 11px;
  cursor: pointer;
  transition: all 0.2s;
  color: var(--color-bg);
}

.btn-update:hover {
  background: var(--color-mint-dark);
  transform: translateY(-1px);
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  border-radius: 8px;
  transition: all 0.2s;
  background: transparent;
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: left;
}

.nav-item:hover {
  color: white;
  background: var(--color-bg);
}

.nav-item.active {
  color: var(--color-mint);
  background: var(--color-mint-dim);
}

.side-footer {
  margin-top: auto;
  padding-top: 20px;
  border-top: 1px solid var(--color-border);
}

.logout {
  color: #9ca3af;
}

.main-content {
  padding: 0;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 40px;
  border-bottom: 1px solid var(--color-border);
  background: var(--color-bg-card);
}

.top-nav-links {
  display: flex;
  gap: 24px;
  color: var(--text-muted);
  font-size: 14px;
}

.top-nav-links .active {
  color: var(--color-mint);
  border-bottom: 2px solid var(--color-mint);
  padding-bottom: 4px;
}

.top-actions {
  display: flex;
  gap: 20px;
  align-items: center;
}

.icon {
  font-size: 20px;
  cursor: pointer;
  transition: color 0.2s;
}

.icon:hover {
  color: var(--color-mint);
}

.user-circle {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--color-mint);
  color: var(--color-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s;
}

.user-circle:hover {
  transform: scale(1.05);
}

.content-wrapper {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-section {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 20px;
  align-items: end;
  margin-bottom: 24px;
}

.label {
  color: var(--color-mint);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1px;
}

.hero-section h1 {
  font-size: 32px;
  margin: 8px 0;
}

.hero-section p {
  color: var(--text-muted);
  font-size: 15px;
}

.card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
}

.filters {
  padding: 16px;
}

.filters-title {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #9ca3af;
  margin-bottom: 12px;
}

.filters-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.pill {
  border: 1px solid var(--color-border);
  border-radius: 999px;
  padding: 8px 12px;
  font-size: 12px;
  color: #9ca3af;
  background: transparent;
}

.pill.active {
  border-color: var(--color-mint);
  color: var(--color-mint);
  background: var(--color-mint-dim);
}

.table-container {
  overflow: hidden;
}

.apps-table {
  width: 100%;
  border-collapse: collapse;
}

.apps-table th {
  text-align: left;
  padding: 20px;
  font-size: 11px;
  color: var(--text-muted);
  border-bottom: 1px solid var(--color-border);
  font-weight: 700;
  letter-spacing: 0.5px;
}

.apps-table td {
  padding: 18px 20px;
  border-bottom: 1px solid var(--color-border);
  font-size: 14px;
  vertical-align: top;
}

.apps-table tr:hover {
  background: rgba(255, 255, 255, 0.02);
}

.company-cell {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
}

.company-logo {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

.job-title {
  font-weight: 700;
}

.job-meta {
  color: var(--text-muted);
  font-size: 12px;
  margin-top: 4px;
}

.stack-cell {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid var(--color-border);
  color: #cbd5e1;
  background: rgba(255, 255, 255, 0.03);
}

.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.2px;
  border: 1px solid var(--color-border);
  color: #e5e7eb;
}

.badge-remote {
  border-color: rgba(79, 209, 197, 0.35);
  color: var(--color-mint);
  background: var(--color-mint-dim);
}

.badge-hybrid {
  border-color: rgba(148, 163, 184, 0.25);
  color: #cbd5e1;
  background: rgba(148, 163, 184, 0.08);
}

.badge-level {
  border-color: rgba(129, 140, 248, 0.35);
  color: #a5b4fc;
  background: rgba(99, 102, 241, 0.12);
}

.pagination {
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--text-muted);
  font-size: 12px;
  border-top: 1px solid var(--color-border);
}

.page-controls {
  display: flex;
  gap: 8px;
}

.page-controls button {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  opacity: 0.7;
}

.page-controls button:disabled {
  cursor: not-allowed;
}

.page-controls button.active {
  background: var(--color-mint-dim);
  border-color: var(--color-mint);
  color: var(--color-mint);
  opacity: 1;
}

@media (max-width: 1024px) {
  .hero-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .sidebar {
    display: none;
  }

  .apps-table th,
  .apps-table td {
    padding: 12px;
  }
}
</style>

