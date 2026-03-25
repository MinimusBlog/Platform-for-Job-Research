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
          <span class="user-status">IT GRADUATE • BAUMAN MSTU</span>
        </div>
        <button class="btn-update">UPDATE RESUME</button>
      </div>

      <nav class="side-nav">
        <router-link to="/applicant/profile" class="nav-item">
          <span>👤</span> PROFILE
        </router-link>
        <router-link to="/applicant" class="nav-item">
          <span>📄</span> MY APPLICATIONS
        </router-link>
        <a href="#" class="nav-item active"> <span>🌐</span> NETWORKING </a>
        <a href="#" class="nav-item"><span>🔖</span> FAVORITES</a>
        <a href="#" class="nav-item"><span>⚙️</span> SETTINGS</a>
      </nav>

      <div class="side-footer">
        <a href="#" class="nav-item"><span>🎧</span> SUPPORT</a>
        <a href="#" class="nav-item logout"><span>🚪</span> LOGOUT</a>
      </div>
    </aside>

    <!-- Основной контент -->
    <main class="main-content">
      <header class="top-bar">
        <div class="top-nav-links">
          <span :class="{ active: currentTab === 'networking' }">Explore</span>
          <span :class="{ active: currentTab === 'applications' }">My Applications</span>
        </div>
        <div class="top-actions">
          <span class="icon">🔔</span>
          <span class="icon">⚡</span>
          <div class="user-circle">AK</div>
        </div>
      </header>

      <div class="content-wrapper">
        <!-- Вкладка: NETWORKING (Как на вашем скриншоте) -->
        <div v-if="currentTab === 'networking'" class="tab-networking">
          <section class="hero-section">
            <span class="label-mint">HIGH-VELOCITY CONNECTIONS</span>
            <h1>Expand your professional <span class="mint-text">orbit in IT.</span></h1>
            <p>Recommended for you based on your Bauman MSTU profile and skillset.</p>
          </section>

          <div class="experts-grid">
            <div v-for="expert in experts" :key="expert.name" class="expert-card">
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
            <!-- Pending Requests -->
            <div class="card pending-card">
              <div class="card-header">
                <h3>Pending Requests</h3>
                <span class="count-badge">3 NEW</span>
              </div>
              <div v-for="req in requests" :key="req.name" class="request-item">
                <div class="avatar-xs"></div>
                <div class="req-info">
                  <strong>{{ req.name }}</strong>
                  <span>{{ req.title }}</span>
                </div>
                <div class="req-btns">
                  <button class="btn-decline">DECLINE</button>
                  <button class="btn-accept">ACCEPT</button>
                </div>
              </div>
            </div>

            <!-- Turbo Boost -->
            <div class="card turbo-card">
              <div class="boost-icon">🚀</div>
              <h3>Turbo Boost</h3>
              <p>Boost your profile visibility to top-tier recruiters for 24 hours.</p>
              <div class="price">249 <small>TOKENS / USE</small></div>
            </div>
          </div>
        </div>

        <!-- Вкладка: APPLICATIONS (Таблица) -->
        <div v-if="currentTab === 'applications'" class="tab-applications">
          <h1>My Applications</h1>
          <div class="table-card card">
            <table class="app-table">
              <thead>
                <tr>
                  <th>COMPANY</th>
                  <th>POSITION</th>
                  <th>DATE</th>
                  <th>STATUS</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="app in applications" :key="app.id">
                  <td class="company-name">🏢 {{ app.company }}</td>
                  <td>{{ app.position }}</td>
                  <td>{{ app.date }}</td>
                  <td>
                    <span :class="['status', app.status.toLowerCase()]">{{ app.status }}</span>
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
import { ref } from 'vue'

const currentTab = ref('networking')

const experts = [
  {
    name: 'Dmitry Sokolov',
    role: 'SENIOR JAVA DEV • SBERTECH',
    tags: ['JAVA', 'SPRING', 'MICROSERVICES'],
    online: true,
    primary: true,
  },
  {
    name: 'Elena Vasileva',
    role: 'DATA ANALYST • YANDEX',
    tags: ['SQL', 'PYTHON', 'TABLEAU'],
    online: false,
    primary: false,
  },
  {
    name: 'Igor Petrov',
    role: 'BACKEND LEAD • AVITO',
    tags: ['GO', 'K8S', 'REDIS'],
    online: false,
    primary: false,
  },
]

const requests = [
  { name: 'Ivan Petrov', title: 'JUNIOR FRONTEND • HSE' },
  { name: 'Sofia Volkova', title: 'ML RESEARCHER • SKOLTECH' },
]

const applications = [
  {
    id: 1,
    company: 'Quantum Systems',
    position: 'Frontend Dev',
    date: 'OCT 24',
    status: 'PENDING',
  },
  { id: 2, company: 'Aether Cloud', position: 'SRE Engineer', date: 'OCT 18', status: 'ACCEPTED' },
]
</script>

<style scoped>
:root {
  --bg-main: #0b0e11;
  --bg-sidebar: #0d1117;
  --bg-card: #161b22;
  --mint: #00e5a0;
  --text-gray: #8b949e;
  --border: #30363d;
}

.dashboard {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
  background: #0b0e11;
  color: white;
  font-family: 'Inter', sans-serif;
}

/* Sidebar */
.sidebar {
  background: #0d1117;
  border-right: 1px solid #30363d;
  padding: 24px;
}

.logo {
  color: var(--mint);
  font-weight: 900;
  font-size: 22px;
  margin-bottom: 30px;
  letter-spacing: 2px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  color: #8b949e;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  border-radius: 8px;
  transition: 0.3s;
}

.nav-item.active {
  color: var(--mint);
  background: rgba(0, 229, 160, 0.05);
}

/* Main Content */
.top-bar {
  display: flex;
  justify-content: space-between;
  padding: 20px 40px;
  border-bottom: 1px solid #30363d;
}

.top-nav-links span {
  margin-right: 20px;
  color: #8b949e;
  font-size: 14px;
  cursor: pointer;
}
.top-nav-links span.active {
  color: var(--mint);
  border-bottom: 2px solid var(--mint);
  padding-bottom: 5px;
}

.content-wrapper {
  padding: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Networking Grid */
.experts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}

.expert-card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 16px;
  padding: 24px;
  text-align: center;
}

.expert-avatar {
  width: 60px;
  height: 60px;
  background: #30363d;
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
  background: var(--mint);
  border-radius: 50%;
  border: 2px solid #161b22;
}

.tech-tags span {
  background: #0d1117;
  padding: 4px 8px;
  font-size: 10px;
  border-radius: 4px;
  margin: 2px;
  display: inline-block;
  color: #8b949e;
}

.btn-rec {
  width: 100%;
  margin-top: 20px;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid var(--mint);
  background: transparent;
  color: var(--mint);
  font-weight: 700;
  cursor: pointer;
}

.btn-rec.primary {
  background: var(--mint);
  color: black;
}

/* Bottom Grid */
.bottom-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  margin-top: 30px;
}

.card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 16px;
  padding: 20px;
}

.turbo-card {
  text-align: center;
  background: linear-gradient(145deg, #161b22 0%, #0d1117 100%);
}

.mint-text {
  color: var(--mint);
}
.label-mint {
  color: var(--mint);
  font-size: 10px;
  font-weight: 800;
}

/* Таблица */
.app-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
.app-table th {
  text-align: left;
  color: #8b949e;
  font-size: 12px;
  padding: 12px;
}
.app-table td {
  padding: 12px;
  border-top: 1px solid #30363d;
  font-size: 14px;
}

.status.accepted {
  color: #2ecc71;
}
.status.pending {
  color: #f1c40f;
}
</style>
