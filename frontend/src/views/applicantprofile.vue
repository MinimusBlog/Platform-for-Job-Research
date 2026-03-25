<template>
  <div class="dashboard">
    <!-- Боковая панель -->
    <aside class="sidebar">
      <div class="logo">ТРАМПЛИН</div>
      
      <div class="user-mini-card">
        <div class="avatar-sm"></div>
        <div class="user-info">
          <span class="user-name">Alex Kovalev</span>
          <span class="user-status">IT GRADUATE • BAUMAN MSTU</span>
        </div>
        <button class="btn-update">UPDATE RESUME</button>
      </div>

      <nav class="side-nav">
        <a href="#" class="nav-item active"><span>👤</span> PROFILE</a>
        <router-link to="/applicant" class="nav-item"><span>📄</span> MY APPLICATIONS</router-link>
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
        <div class="search-box">
          <input type="text" placeholder="Поиск вакансий...">
        </div>
        <div class="top-actions">
          <span class="icon">🔔</span>
          <span class="icon">⚡</span>
          <div class="user-circle">AK</div>
        </div>
      </header>

      <div class="profile-grid">
        <!-- Шапка профиля -->
        <section class="profile-header card">
          <div class="profile-info-main">
            <div class="profile-avatar-large">
               <img src="https://via.placeholder.com" alt="Alex">
               <div class="online-status"></div>
            </div>
            <div class="profile-text">
              <div class="name-row">
                <h1>Alex Kovalev</h1>
                <span class="status-badge">ИЩУ СТАЖИРОВКУ</span>
              </div>
              <p>IT Graduate • Bauman MSTU • 2024</p>
            </div>
          </div>
          <div class="header-buttons">
            <div class="toggle-public">
               <span>ОТКРЫТЫЙ ПРОФИЛЬ</span>
               <div class="switch"></div>
            </div>
            <button class="btn-download">DOWNLOAD CV</button>
          </div>
        </section>

        <!-- Левая колонка (Стек и контакты) -->
        <div class="col-left">
          <section class="card">
            <h3>TECHNICAL STACK</h3>
            <div class="tech-tags">
              <span v-for="tech in ['React', 'TypeScript', 'Go', 'Docker', 'Node.js', 'PostgreSQL']" :key="tech" class="tag">
                {{ tech }}
              </span>
            </div>
          </section>

          <section class="card">
            <h3>CONTACT & SOCIALS</h3>
            <div class="social-links">
              <div class="social-item"><span>@</span> a.kovalev@bauman.ru</div>
              <div class="social-item"><span>🔗</span> linkedin.com/in/akovalev</div>
            </div>
          </section>
        </div>

        <!-- Правая колонка (Проекты) -->
        <div class="col-right">
          <section class="card">
            <div class="section-header">
              <h3>KEY PROJECTS & EXPERIENCE</h3>
              <span class="add-icon">+</span>
            </div>

            <div class="project-item">
              <div class="project-info">
                <h4>E-Commerce Microservices Engine</h4>
                <span class="project-meta">GRADUATION PROJECT • 2024</span>
                <p>Developed a highly scalable microservices architecture for real-time inventory tracking using Go and Kafka.</p>
                <div class="project-tags">
                  <span>Go</span> <span>Kafka</span> <span>Redis</span>
                </div>
              </div>
              <a href="#" class="github-link">View on GitHub ↗</a>
            </div>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
:root {
  --bg-dark: #0d1117;
  --bg-card: #161b22;
  --mint: #00e5a0;
  --border: #30363d;
  --text-muted: #8b949e;
}

.dashboard {
  display: grid;
  grid-template-columns: 260px 1fr;
  min-height: 100vh;
  background: #0d1117;
  color: white;
  font-family: 'Inter', sans-serif;
}

/* Sidebar */
.sidebar {
  background: #161b22;
  padding: 24px;
  border-right: 1px solid #30363d;
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 12px;
  color: #8b949e;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  border-radius: 8px;
  margin-bottom: 4px;
}

.nav-item.active {
  color: var(--mint);
  background: rgba(0, 229, 160, 0.05);
  border-left: 3px solid var(--mint);
}

/* Grid layout */
.profile-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 20px;
  padding: 24px;
}

.profile-header {
  grid-column: 1 / -1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 32px;
}

.card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 12px;
  padding: 20px;
}

/* Элементы */
.tag {
  background: #0d1117;
  border: 1px solid #30363d;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  margin: 4px;
  display: inline-block;
}

.btn-download {
  background: var(--mint);
  color: #000;
  border: none;
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
}

.project-item {
  background: #0d1117;
  border: 1px solid #30363d;
  padding: 20px;
  border-radius: 12px;
  margin-top: 16px;
}
</style>
