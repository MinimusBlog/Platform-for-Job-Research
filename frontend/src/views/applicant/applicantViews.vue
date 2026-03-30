<script>
export default {
  name: 'ApplicantViews',
}
</script>

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
          <span class="user-name">Alex Kovalev</span>
          <span class="user-status">IT ВЫПУСКНИК • МГТУ ИМ. БАУМАНА</span>
        </div>
        <button class="btn-update">ОБНОВИТЬ РЕЗЮМЕ</button>
      </div>

      <nav class="side-nav">
        <router-link
          :to="{ name: 'applicant-profile' }"
          class="nav-item"
          :class="{ active: activeNav === 'profile' }"
        >
          <span>👤</span> ПРОФИЛЬ
        </router-link>

        <router-link
          :to="{ name: 'applicant' }"
          class="nav-item"
          :class="{ active: activeNav === 'applications' }"
        >
          <span>📄</span> МОИ ЗАЯВКИ
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
        <a href="#" class="nav-item logout"><span>🚪</span> ВЫЙТИ</a>
      </div>
    </aside>

    <!-- Основной контент -->
    <main class="main-content">
      <header class="top-bar">
        <div class="top-nav-links">
          <a href="#">Обзор</a>
          <a href="#" class="active">Мои заявки</a>
          <a href="#">Нетворкинг</a>
        </div>
        <div class="top-actions">
          <span class="icon">🔔</span>
          <span class="icon">⚡</span>
          <div class="user-circle">AK</div>
        </div>
      </header>

      <div class="content-wrapper">
        <section class="hero-section">
          <div class="section-title">
            <span class="label">КАРЬЕРНЫЙ ПРОГРЕСС</span>
            <h1>Мои заявки</h1>
            <p>
              Управляйте своим профессиональным путем. Отслеживание 12 активных заявок в различных
              секторах.
            </p>
          </div>
          <div class="view-toggle">
            <button class="toggle-btn active">▦ Таблица</button>
            <button class="toggle-btn">▤ Канбан</button>
          </div>
        </section>

        <!-- Таблица вакансий -->
        <div class="table-container card">
          <table class="apps-table">
            <thead>
              <tr>
                <th>КОМПАНИЯ</th>
                <th>ДОЛЖНОСТЬ</th>
                <th>ДАТА ПОДАЧИ</th>
                <th>СТАТУС</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="app in applications" :key="app.company">
                <td class="company-cell">
                  <div class="company-logo" :style="{ backgroundColor: app.logoBg }">
                    {{ app.logo }}
                  </div>
                  {{ app.company }}
                </td>
                <td>{{ app.position }}</td>
                <td class="date-cell">{{ app.date }}</td>
                <td>
                  <span class="status-badge" :class="getStatusClass(app.status)">
                    {{ getStatusText(app.status) }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="pagination">
            <span>Показано 5 из 12 активных заявок</span>
            <div class="page-controls">
              <button>&lt;</button>
              <button class="active">&gt;</button>
            </div>
          </div>
        </div>

        <!-- Нижние карточки статистики -->
        <div class="stats-grid">
          <div class="stat-card success card">
            <span class="stat-label">ПОКАЗАТЕЛЬ УСПЕХА</span>
            <div class="stat-value">42%</div>
            <div class="stat-meta">↗ +12% по сравнению с прошлым месяцем</div>
          </div>
          <div class="stat-card active-int card">
            <span class="stat-label">АКТИВНЫЕ ИНТЕРВЬЮ</span>
            <div class="stat-value">03</div>
            <div class="stat-meta">🕒 Следующее: завтра, 11:00</div>
          </div>
          <div class="stat-card pending card">
            <span class="stat-label">ОЖИДАНИЕ ОБРАТНОЙ СВЯЗИ</span>
            <div class="stat-value">08</div>
            <div class="stat-meta">📂 Средний ответ: 4.2 дня</div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const applications = ref([
  {
    company: 'Quantum Systems',
    position: 'Frontend Developer',
    date: '24 ОКТ 2023',
    status: 'pending',
    logo: '田',
    logoBg: '#2d333b',
  },
  {
    company: 'Nova Labs',
    position: 'UI/UX Engineer',
    date: '20 ОКТ 2023',
    status: 'reviewed',
    logo: '▦',
    logoBg: '#2d333b',
  },
  {
    company: 'Aether Cloud',
    position: 'SRE Engineer',
    date: '18 ОКТ 2023',
    status: 'accepted',
    logo: '☁',
    logoBg: '#1e3a2f',
  },
  {
    company: 'Orbital Tech',
    position: 'Backend Developer',
    date: '15 ОКТ 2023',
    status: 'rejected',
    logo: '🚀',
    logoBg: '#3d2b2b',
  },
  {
    company: 'DeepMind AI',
    position: 'ML Researcher',
    date: '12 ОКТ 2023',
    status: 'reviewed',
    logo: '🧠',
    logoBg: '#2d333b',
  },
])

const getStatusClass = (status) => {
  const classes = {
    pending: 'pending',
    reviewed: 'reviewed',
    accepted: 'accepted',
    rejected: 'rejected',
  }
  return classes[status] || ''
}

const getStatusText = (status) => {
  const texts = {
    pending: 'НА РАССМОТРЕНИИ',
    reviewed: 'ПРОСМОТРЕНО',
    accepted: 'ПРИНЯТО',
    rejected: 'ОТКЛОНЕНО',
  }
  return texts[status] || status.toUpperCase()
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

/* Sidebar */
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

/* Main Content */
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
}

.top-nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}

.top-nav-links a:hover {
  color: white;
}

.top-nav-links a.active {
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
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 40px;
  flex-wrap: wrap;
  gap: 20px;
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

.view-toggle {
  background: var(--color-bg-card);
  padding: 4px;
  border-radius: 8px;
  display: flex;
  gap: 4px;
}

.toggle-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 6px 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.toggle-btn.active {
  background: var(--color-border);
  color: white;
}

.toggle-btn:hover:not(.active) {
  background: rgba(255, 255, 255, 0.05);
  color: white;
}

/* Table */
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
  padding: 20px;
  border-bottom: 1px solid var(--color-border);
  font-size: 14px;
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

.status-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  display: inline-block;
}

.pending {
  color: #f1c40f;
  background: rgba(241, 196, 15, 0.1);
}

.reviewed {
  color: #3498db;
  background: rgba(52, 152, 219, 0.1);
}

.accepted {
  color: #2ecc71;
  background: rgba(46, 204, 113, 0.1);
}

.rejected {
  color: #e74c3c;
  background: rgba(231, 76, 60, 0.1);
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
}

.page-controls button:hover {
  border-color: var(--color-mint);
  color: var(--color-mint);
}

.page-controls button.active {
  background: var(--color-mint-dim);
  border-color: var(--color-mint);
  color: var(--color-mint);
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 40px;
}

.stat-card {
  position: relative;
  transition:
    transform 0.2s,
    border-color 0.2s;
}

.stat-card:hover {
  transform: translateY(-2px);
  border-color: var(--color-mint);
}

.stat-card::before {
  content: '';
  position: absolute;
  left: 0;
  top: 24px;
  bottom: 24px;
  width: 3px;
  border-radius: 0 4px 4px 0;
}

.success::before {
  background: var(--color-mint);
}

.active-int::before {
  background: #3498db;
}

.pending::before {
  background: #f1c40f;
}

.stat-label {
  font-size: 10px;
  color: var(--text-muted);
  font-weight: 700;
  letter-spacing: 0.5px;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  margin: 8px 0;
}

.stat-meta {
  font-size: 12px;
  color: var(--text-muted);
}

/* Responsive */
@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .sidebar {
    display: none;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .hero-section {
    flex-direction: column;
    align-items: flex-start;
  }

  .apps-table {
    font-size: 12px;
  }

  .apps-table th,
  .apps-table td {
    padding: 12px;
  }
}
</style>
