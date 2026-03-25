<template>
  <div class="dashboard">
    <!-- Боковая панель (Sidebar) -->
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
        <router-link to="/applicant/profile" class="nav-item"><span>👤</span> PROFILE</router-link>
        <a href="#" class="nav-item active"><span>📄</span> MY APPLICATIONS</a>
        <a href="#" class="nav-item"><span>🔖</span> FAVORITES</a>
        <router-link to="/applicant/network" class="nav-item"><span>🌐</span> NETWORKING</router-link>
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
          <a href="#">Explore</a>
          <a href="#" class="active">My Applications</a>
          <a href="#">Networking</a>
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
            <span class="label">CAREER PROGRESS</span>
            <h1>My Applications</h1>
            <p>Manage your professional journey. Tracking 12 active job applications across various sectors.</p>
          </div>
          <div class="view-toggle">
            <button class="toggle-btn active">▦ Table</button>
            <button class="toggle-btn">▤ Kanban</button>
          </div>
        </section>

        <!-- Таблица вакансий -->
        <div class="table-container">
          <table class="apps-table">
            <thead>
              <tr>
                <th>COMPANY</th>
                <th>POSITION</th>
                <th>DATE APPLIED</th>
                <th>STATUS</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="app in applications" :key="app.company">
                <td class="company-cell">
                  <div class="company-logo" :style="{ backgroundColor: app.logoBg }">{{ app.logo }}</div>
                  {{ app.company }}
                </td>
                <td>{{ app.position }}</td>
                <td class="date-cell">{{ app.date }}</td>
                <td>
                  <span class="status-badge" :class="app.status.toLowerCase()">
                    {{ app.status }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="pagination">
             <span>Showing 5 of 12 active applications</span>
             <div class="page-controls">
               <button>&lt;</button>
               <button class="active">&gt;</button>
             </div>
          </div>
        </div>

        <!-- Нижние карточки статистики -->
        <div class="stats-grid">
          <div class="stat-card success">
            <span class="stat-label">SUCCESS RATE</span>
            <div class="stat-value">42%</div>
            <div class="stat-meta">↗ +12% from last month</div>
          </div>
          <div class="stat-card active-int">
            <span class="stat-label">ACTIVE INTERVIEWS</span>
            <div class="stat-value">03</div>
            <div class="stat-meta">🕒 Next one: Tomorrow, 11:00 AM</div>
          </div>
          <div class="stat-card pending">
            <span class="stat-label">PENDING FEEDBACK</span>
            <div class="stat-value">08</div>
            <div class="stat-meta">📂 Avg response: 4.2 days</div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
const applications = [
  { company: 'Quantum Systems', position: 'Frontend Developer', date: 'OCT 24, 2023', status: 'PENDING', logo: '田', logoBg: '#2d333b' },
  { company: 'Nova Labs', position: 'UI/UX Engineer', date: 'OCT 20, 2023', status: 'REVIEWED', logo: '▦', logoBg: '#2d333b' },
  { company: 'Aether Cloud', position: 'SRE Engineer', date: 'OCT 18, 2023', status: 'ACCEPTED', logo: '☁', logoBg: '#1e3a2f' },
  { company: 'Orbital Tech', position: 'Backend Developer', date: 'OCT 15, 2023', status: 'REJECTED', logo: '🚀', logoBg: '#3d2b2b' },
  { company: 'DeepMind AI', position: 'ML Researcher', date: 'OCT 12, 2023', status: 'REVIEWED', logo: '🧠', logoBg: '#2d333b' },
];
</script>

<style scoped>
/* Основные цвета из скриншота */
:root {
  --bg-dark: #0b0e11;
  --bg-sidebar: #0d1117;
  --bg-card: #161b22;
  --mint: #00e5a0;
  --text-gray: #8b949e;
  --border: #21262d;
}

.dashboard {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100vh;
  background: #0b0e11;
  color: white;
  font-family: 'Segoe UI', Roboto, sans-serif;
}

/* Sidebar */
.sidebar {
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  padding: 24px;
  display: flex;
  flex-direction: column;
}

.logo {
  color: var(--mint);
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

.avatar-container { position: relative; width: 40px; }
.avatar-sm { width: 40px; height: 40px; background: #30363d; border-radius: 50%; }
.online-dot { 
  position: absolute; bottom: 0; right: 0; 
  width: 10px; height: 10px; background: var(--mint); 
  border-radius: 50%; border: 2px solid var(--bg-sidebar);
}

.user-info { margin: 12px 0; }
.user-name { display: block; font-weight: 600; font-size: 14px; }
.user-status { font-size: 10px; color: var(--text-gray); }

.btn-update {
  width: 100%;
  background: var(--mint);
  border: none;
  padding: 10px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 11px;
  cursor: pointer;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  color: var(--text-gray);
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  border-radius: 8px;
}

.nav-item.active {
  color: var(--mint);
  background: rgba(0, 229, 160, 0.05);
}

/* Main Content */
.main-content { padding: 0; }

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 40px;
  border-bottom: 1px solid var(--border);
}

.top-nav-links { display: flex; gap: 24px; }
.top-nav-links a { color: var(--text-gray); text-decoration: none; font-size: 14px; }
.top-nav-links a.active { color: var(--mint); border-bottom: 2px solid var(--mint); padding-bottom: 4px; }

.content-wrapper { padding: 40px; max-width: 1100px; margin: 0 auto; }

.hero-section {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 40px;
}

.label { color: var(--mint); font-size: 12px; font-weight: 700; letter-spacing: 1px; }
.hero-section h1 { font-size: 32px; margin: 8px 0; }
.hero-section p { color: var(--text-gray); font-size: 15px; }

.view-toggle { background: #161b22; padding: 4px; border-radius: 8px; }
.toggle-btn { 
  background: transparent; border: none; color: var(--text-gray); 
  padding: 6px 16px; border-radius: 6px; cursor: pointer;
}
.toggle-btn.active { background: #21262d; color: white; }

/* Table */
.table-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
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
  color: var(--text-gray);
  border-bottom: 1px solid var(--border);
}

.apps-table td { padding: 20px; border-bottom: 1px solid var(--border); font-size: 14px; }

.company-cell { display: flex; align-items: center; gap: 12px; font-weight: 600; }
.company-logo { 
  width: 32px; height: 32px; border-radius: 6px; 
  display: flex; align-items: center; justify-content: center;
}

.status-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 700;
}

.pending { color: #f1c40f; background: rgba(241, 196, 15, 0.1); }
.reviewed { color: #3498db; background: rgba(52, 152, 219, 0.1); }
.accepted { color: #2ecc71; background: rgba(46, 204, 113, 0.1); }
.rejected { color: #e74c3c; background: rgba(231, 76, 60, 0.1); }

.pagination {
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--text-gray);
  font-size: 12px;
}

.page-controls button {
  background: #0b0e11;
  border: 1px solid var(--border);
  color: white;
  width: 32px; height: 32px;
  border-radius: 6px;
  margin-left: 8px;
  cursor: pointer;
}
.page-controls button.active { background: #1e3a2f; border-color: var(--mint); }

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 40px;
}

.stat-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  position: relative;
}

.stat-card::before {
  content: ''; position: absolute; left: 0; top: 24px; bottom: 24px; width: 3px; border-radius: 0 4px 4px 0;
}
.success::before { background: var(--mint); }
.active-int::before { background: #3498db; }
.pending::before { background: #f1c40f; }

.stat-label { font-size: 10px; color: var(--text-gray); font-weight: 700; }
.stat-value { font-size: 32px; font-weight: 700; margin: 8px 0; }
.stat-meta { font-size: 12px; color: var(--text-gray); }
</style>
