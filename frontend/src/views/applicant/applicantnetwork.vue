<template>
  <div class="dashboard">
    <!-- Боковая панель (Sidebar) — общая для всех разделов -->
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
        <a
          href="applicantprofile.vue"
          @click="currentTab = 'profile'"
          :class="{ active: currentTab === 'profile' }"
          class="nav-item"
        >
          <span>👤</span> ПРОФИЛЬ
        </a>
        <a
          href="applicant.vue"
          @click="currentTab = 'applications'"
          :class="{ active: currentTab === 'applications' }"
          class="nav-item"
        >
          <span>📄</span> МОИ ЗАЯВКИ
        </a>
        <a
          href="#"
          @click="currentTab = 'networking'"
          :class="{ active: currentTab === 'networking' }"
          class="nav-item"
        >
          <span>🌐</span> НЕТВОРКИНГ
        </a>
        <a href="#" class="nav-item"><span>🔖</span> ИЗБРАННОЕ</a>
        <a href="#" class="nav-item"><span>⚙️</span> НАСТРОЙКИ</a>
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
          <span :class="{ active: currentTab === 'networking' }" @click="currentTab = 'networking'"
            >Обзор</span
          >
          <span
            :class="{ active: currentTab === 'applications' }"
            @click="currentTab = 'applications'"
            >Мои заявки</span
          >
        </div>
        <div class="top-actions">
          <span class="icon">🔔</span>
          <span class="icon">⚡</span>
          <div class="user-circle">AK</div>
        </div>
      </header>

      <div class="content-wrapper">
        <!-- Вкладка: НЕТВОРКИНГ -->
        <div v-if="currentTab === 'networking'" class="tab-networking">
          <section class="hero-section">
            <span class="label-mint">ВЫСОКОСКОРОСТНЫЕ СВЯЗИ</span>
            <h1>Расширьте свою профессиональную <span class="mint-text">орбиту в IT.</span></h1>
            <p>Рекомендации для вас на основе профиля МГТУ им. Баумана и навыков.</p>
          </section>

          <div class="experts-grid">
            <div v-for="expert in experts" :key="expert.name" class="expert-card card">
              <div class="expert-avatar" :style="{ backgroundImage: `url(${expert.img})` }">
                <div v-if="expert.online" class="online-status"></div>
              </div>
              <h3>{{ expert.name }}</h3>
              <p class="role">{{ expert.role }}</p>
              <div class="tech-tags">
                <span v-for="tag in expert.tags" :key="tag">{{ tag }}</span>
              </div>
              <button :class="['btn-rec', { primary: expert.primary }]">РЕКОМЕНДОВАТЬ</button>
            </div>
          </div>

          <div class="bottom-grid">
            <!-- Ожидающие запросы -->
            <div class="card pending-card">
              <div class="card-header">
                <h3>Ожидающие запросы</h3>
                <span class="count-badge">3 НОВЫХ</span>
              </div>
              <div v-for="req in requests" :key="req.name" class="request-item">
                <div class="avatar-xs"></div>
                <div class="req-info">
                  <strong>{{ req.name }}</strong>
                  <span>{{ req.title }}</span>
                </div>
                <div class="req-btns">
                  <button class="btn-decline">ОТКЛОНИТЬ</button>
                  <button class="btn-accept">ПРИНЯТЬ</button>
                </div>
              </div>
            </div>

            <!-- Turbo Boost -->
            <div class="card turbo-card">
              <div class="boost-icon">🚀</div>
              <h3>Turbo Boost</h3>
              <p>Повысьте видимость вашего профиля для топ-рекрутеров на 24 часа.</p>
              <div class="price">249 <small>ТОКЕНОВ / ИСПОЛЬЗОВАНИЕ</small></div>
            </div>
          </div>
        </div>

        <!-- Вкладка: МОИ ЗАЯВКИ (Таблица) -->
        <div v-if="currentTab === 'applications'" class="tab-applications">
          <section class="hero-section">
            <span class="label-mint">КАРЬЕРНЫЙ ПРОГРЕСС</span>
            <h1>Мои заявки</h1>
            <p>
              Управляйте своим профессиональным путем. Отслеживание активных заявок в различных
              секторах.
            </p>
          </section>

          <div class="table-card card">
            <table class="app-table">
              <thead>
                <tr>
                  <th>КОМПАНИЯ</th>
                  <th>ДОЛЖНОСТЬ</th>
                  <th>ДАТА</th>
                  <th>СТАТУС</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="app in applications" :key="app.id">
                  <td class="company-name">🏢 {{ app.company }}</td>
                  <td>{{ app.position }}</td>
                  <td>{{ app.date }}</td>
                  <td>
                    <span :class="['status', getStatusClass(app.status)]">{{
                      getStatusText(app.status)
                    }}</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
defineOptions({
  name: 'ApplicantNetworkView',
})
import { ref } from 'vue'

const currentTab = ref('networking')

const experts = ref([
  {
    name: 'Дмитрий Соколов',
    role: 'SENIOR JAVA DEV • СБЕРТЕХ',
    tags: ['JAVA', 'SPRING', 'МИКРОСЕРВИСЫ'],
    online: true,
    primary: true,
    img: '',
  },
  {
    name: 'Елена Васильева',
    role: 'DATA ANALYST • ЯНДЕКС',
    tags: ['SQL', 'PYTHON', 'TABLEAU'],
    online: false,
    primary: false,
    img: '',
  },
  {
    name: 'Игорь Петров',
    role: 'BACKEND LEAD • АВИТО',
    tags: ['GO', 'K8S', 'REDIS'],
    online: false,
    primary: false,
    img: '',
  },
])

const requests = ref([
  { name: 'Иван Петров', title: 'JUNIOR FRONTEND • ВШЭ' },
  { name: 'София Волкова', title: 'ML RESEARCHER • СКОЛТЕХ' },
])

const applications = ref([
  {
    id: 1,
    company: 'Quantum Systems',
    position: 'Frontend Developer',
    date: '24 ОКТ 2023',
    status: 'pending',
  },
  {
    id: 2,
    company: 'Aether Cloud',
    position: 'SRE Engineer',
    date: '18 ОКТ 2023',
    status: 'accepted',
  },
  {
    id: 3,
    company: 'Nova Labs',
    position: 'UI/UX Engineer',
    date: '20 ОКТ 2023',
    status: 'reviewed',
  },
  {
    id: 4,
    company: 'Orbital Tech',
    position: 'Backend Developer',
    date: '15 ОКТ 2023',
    status: 'rejected',
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
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
  background: var(--color-bg);
  color: white;
  font-family: 'Montserrat', 'Inter', sans-serif;
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
  font-weight: 900;
  font-size: 22px;
  margin-bottom: 30px;
  letter-spacing: 2px;
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
  cursor: pointer;
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

.top-nav-links span {
  color: var(--text-muted);
  font-size: 14px;
  cursor: pointer;
  transition: color 0.2s;
  padding-bottom: 4px;
}

.top-nav-links span:hover {
  color: white;
}

.top-nav-links span.active {
  color: var(--color-mint);
  border-bottom: 2px solid var(--color-mint);
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
  margin-bottom: 40px;
}

.label-mint {
  color: var(--color-mint);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hero-section h1 {
  font-size: 32px;
  margin: 8px 0;
}

.hero-section p {
  color: var(--text-muted);
  font-size: 15px;
}

.mint-text {
  color: var(--color-mint);
}

/* Networking Grid */
.experts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}

.expert-card {
  padding: 24px;
  text-align: center;
  transition:
    transform 0.2s,
    border-color 0.2s;
}

.expert-card:hover {
  transform: translateY(-4px);
  border-color: var(--color-mint);
}

.expert-avatar {
  width: 60px;
  height: 60px;
  background: var(--color-border);
  border-radius: 12px;
  margin: 0 auto 15px;
  position: relative;
}

.online-status {
  position: absolute;
  bottom: -4px;
  right: -4px;
  width: 12px;
  height: 12px;
  background: var(--color-mint);
  border-radius: 50%;
  border: 2px solid var(--color-bg-card);
}

.role {
  font-size: 12px;
  color: var(--text-muted);
  margin: 8px 0;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
  margin: 12px 0;
}

.tech-tags span {
  background: var(--color-bg);
  padding: 4px 8px;
  font-size: 10px;
  border-radius: 4px;
  color: var(--text-muted);
  border: 1px solid var(--color-border);
}

.btn-rec {
  width: 100%;
  margin-top: 20px;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid var(--color-mint);
  background: transparent;
  color: var(--color-mint);
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-rec:hover {
  transform: translateY(-2px);
}

.btn-rec.primary {
  background: var(--color-mint);
  color: var(--color-bg);
}

.btn-rec.primary:hover {
  background: var(--color-mint-dark);
}

/* Bottom Grid */
.bottom-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-top: 30px;
}

.card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 20px;
  transition: border-color 0.2s;
}

.card:hover {
  border-color: var(--color-mint);
}

.pending-card .card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.count-badge {
  background: var(--color-mint-dim);
  color: var(--color-mint);
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 10px;
  font-weight: 700;
}

.request-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--color-border);
}

.request-item:last-child {
  border-bottom: none;
}

.avatar-xs {
  width: 32px;
  height: 32px;
  background: var(--color-border);
  border-radius: 50%;
  flex-shrink: 0;
}

.req-info {
  flex: 1;
}

.req-info strong {
  display: block;
  font-size: 13px;
  margin-bottom: 2px;
}

.req-info span {
  font-size: 10px;
  color: var(--text-muted);
}

.req-btns {
  display: flex;
  gap: 8px;
}

.btn-decline,
.btn-accept {
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-decline {
  background: rgba(231, 76, 60, 0.1);
  color: #e74c3c;
}

.btn-decline:hover {
  background: rgba(231, 76, 60, 0.2);
}

.btn-accept {
  background: var(--color-mint-dim);
  color: var(--color-mint);
}

.btn-accept:hover {
  background: var(--color-mint);
  color: var(--color-bg);
}

.turbo-card {
  text-align: center;
}

.boost-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.turbo-card h3 {
  margin-bottom: 12px;
}

.turbo-card p {
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 20px;
}

.price {
  font-size: 24px;
  font-weight: 700;
  color: var(--color-mint);
}

.price small {
  font-size: 10px;
  color: var(--text-muted);
}

/* Таблица */
.table-card {
  margin-top: 20px;
  overflow-x: auto;
}

.app-table {
  width: 100%;
  border-collapse: collapse;
}

.app-table th {
  text-align: left;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 700;
  padding: 16px;
  border-bottom: 1px solid var(--color-border);
  letter-spacing: 0.5px;
}

.app-table td {
  padding: 16px;
  border-bottom: 1px solid var(--color-border);
  font-size: 14px;
}

.app-table tr:hover {
  background: rgba(255, 255, 255, 0.02);
}

.company-name {
  font-weight: 600;
}

.status {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
  display: inline-block;
}

.status.accepted {
  color: #2ecc71;
  background: rgba(46, 204, 113, 0.1);
}

.status.pending {
  color: #f1c40f;
  background: rgba(241, 196, 15, 0.1);
}

.status.reviewed {
  color: #3498db;
  background: rgba(52, 152, 219, 0.1);
}

.status.rejected {
  color: #e74c3c;
  background: rgba(231, 76, 60, 0.1);
}

/* Responsive */
@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
  }

  .sidebar {
    display: none;
  }

  .experts-grid {
    grid-template-columns: 1fr;
  }

  .bottom-grid {
    grid-template-columns: 1fr;
  }

  .hero-section h1 {
    font-size: 24px;
  }

  .content-wrapper {
    padding: 20px;
  }

  .top-bar {
    padding: 16px 20px;
  }

  .app-table {
    font-size: 12px;
  }

  .app-table th,
  .app-table td {
    padding: 10px;
  }
}
</style>
