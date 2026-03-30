<template>
  <div class="admin-panel">
    <header class="header">
      <div class="header-left">
        <div class="logo">ТРАМПЛИН</div>
        <div class="company-badge">
          <span class="badge-icon">Q</span>
          <span class="badge-text">Quantum Systems</span>
          <i class="verified">🛡️</i>
        </div>
      </div>
      <nav class="nav-links">
        <router-link :to="{ name: 'company-profile' }" active-class="active">
          Компания
        </router-link>
        <router-link :to="{ name: 'company-opportunities' }" active-class="active">
          Возможности
        </router-link>
        <router-link :to="{ name: 'company-responses' }" active-class="active">
          Отклики
        </router-link>
        <a href="#" class="hover:text-white transition-all">Аналитика</a>
      </nav>
      <div class="header-right">
        <button class="icon-btn">🔔</button>
        <button class="icon-btn">⚙️</button>
        <div class="user-circle"></div>
      </div>
    </header>

    <main class="container">
      <!-- Баннер верификации -->
      <div class="banner-success">
        <div class="banner-info">
          <span class="check-icon">✓</span>
          <div>
            <h3>ВЕРИФИКАЦИЯ ПРОЙДЕНА</h3>
            <p>Ваш профиль подтвержден и доступен всем кандидатам.</p>
          </div>
        </div>
        <button class="details-link">ДЕТАЛИ</button>
      </div>

      <div class="layout-grid">
        <!-- Левая колонка: Форма -->
        <section class="content-card profile-form card">
          <div class="form-header">
            <div class="title-group">
              <h1>Профиль компании</h1>
              <p>Настройте визуальную идентичность вашего бренда</p>
            </div>
            <div class="avatar-upload">
              <div class="upload-box">
                <span class="icon">📷</span>
                <span>Загрузить</span>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="input-group">
              <label>НАЗВАНИЕ КОМПАНИИ</label>
              <input type="text" value="Quantum Systems" class="dark-input" />
            </div>
            <div class="input-group">
              <label>ИНДУСТРИЯ</label>
              <select class="dark-input">
                <option>Fintech Architecture</option>
                <option>Разработка ПО</option>
                <option>Искусственный интеллект</option>
              </select>
            </div>
          </div>

          <div class="input-group">
            <label>О КОМПАНИИ</label>
            <textarea class="dark-input" rows="4">
Quantum Systems — лидер в разработке высоконагруженных финтех-платформ. Мы создаем будущее распределенных вычислений для глобальных рынков капитала.</textarea
            >
          </div>

          <div class="row">
            <div class="input-group">
              <label>САЙТ</label>
              <div class="input-wrapper">
                <span class="prefix">🌐</span>
                <input type="text" value="https://quantum-systems.io" />
              </div>
            </div>
            <div class="input-group">
              <label>LINKEDIN</label>
              <div class="input-wrapper">
                <span class="prefix">🔗</span>
                <input type="text" value="linkedin.com/company/quantum-system" />
              </div>
            </div>
          </div>

          <button class="btn-submit">СОХРАНИТЬ ИЗМЕНЕНИЯ</button>
        </section>

        <!-- Правая колонка: Виджеты -->
        <aside class="sidebar-widgets">
          <!-- Превью карточки -->
          <div class="widget card">
            <span class="widget-title">ПРЕДПРОСМОТР КАРТОЧКИ</span>
            <div class="card-preview">
              <div class="card-top">
                <div class="q-logo">Q</div>
                <div>
                  <h4>Quantum Systems</h4>
                  <p>Fintech • 50-200 сотр.</p>
                </div>
              </div>
              <div class="card-skeleton">
                <div class="line"></div>
                <div class="line short"></div>
              </div>
              <div class="card-tags">
                <span class="tag">REMOTE</span>
                <span class="tag">HIRING</span>
              </div>
            </div>
          </div>

          <!-- Активность -->
          <div class="widget card">
            <span class="widget-title">НЕДАВНЯЯ АКТИВНОСТЬ</span>
            <ul class="activity-log">
              <li class="active">
                <p>Профиль обновлен</p>
                <small>2 часа назад • Администратор</small>
              </li>
              <li>
                <p>Новый отклик: Senior Dev</p>
                <small>5 часов назад • Трамплин AI</small>
              </li>
              <li>
                <p>Верификация подтверждена</p>
                <small>Вчера • Система</small>
              </li>
            </ul>
          </div>

          <!-- Совет -->
          <div class="tip-box">
            <span class="tip-icon">💡</span>
            <h5>Совет по брендингу</h5>
            <p>Компании с заполненным описанием получают на 45% больше качественных откликов.</p>
          </div>
        </aside>
      </div>
    </main>
  </div>
</template>

<style scoped>
.admin-panel {
  background-color: var(--color-bg);
  color: white;
  min-height: 100vh;
  font-family: 'Montserrat', 'Inter', sans-serif;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  padding: 15px 40px;
  border-bottom: 1px solid var(--color-border);
  align-items: center;
  background: var(--color-bg-card);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 24px;
}

.logo {
  font-weight: 900;
  font-size: 1.2rem;
  color: var(--color-mint);
  letter-spacing: -0.5px;
}

.company-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: var(--text-muted);
  background: var(--color-bg);
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid var(--color-border);
}

.badge-icon {
  width: 20px;
  height: 20px;
  background: var(--color-mint);
  color: var(--color-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
}

.verified {
  font-size: 12px;
  color: var(--color-mint);
}

.nav-links {
  display: flex;
  gap: 32px;
}

.nav-links a {
  text-decoration: none;
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 600;
  transition: color 0.2s;
  padding-bottom: 4px;
}

.nav-links a:hover {
  color: white;
}

.nav-links a.active {
  color: white;
  border-bottom: 2px solid var(--color-mint);
}

.header-right {
  display: flex;
  gap: 16px;
  align-items: center;
}

.icon-btn {
  background: transparent;
  border: none;
  font-size: 20px;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: all 0.2s;
  color: var(--text-muted);
}

.icon-btn:hover {
  background: var(--color-bg);
  color: var(--color-mint);
}

.user-circle {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--color-mint);
  cursor: pointer;
  transition: transform 0.2s;
}

.user-circle:hover {
  transform: scale(1.05);
}

/* Main Content */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.banner-success {
  background: var(--color-mint-dim);
  border: 1px solid var(--color-mint);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-radius: 12px;
  margin-bottom: 40px;
}

.banner-info {
  display: flex;
  gap: 16px;
  align-items: center;
}

.check-icon {
  width: 32px;
  height: 32px;
  background: var(--color-mint);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: var(--color-bg);
}

.banner-info h3 {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
}

.banner-info p {
  font-size: 13px;
  color: var(--text-muted);
}

.details-link {
  background: transparent;
  border: 1px solid var(--color-mint);
  color: var(--color-mint);
  padding: 8px 20px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.details-link:hover {
  background: var(--color-mint);
  color: var(--color-bg);
}

.layout-grid {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 40px;
}

/* Form Styles */
.profile-form {
  padding: 32px;
}

.form-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.title-group h1 {
  font-size: 24px;
  margin-bottom: 8px;
}

.title-group p {
  color: var(--text-muted);
  font-size: 14px;
}

.avatar-upload {
  margin-left: 20px;
}

.upload-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px;
  background: var(--color-bg);
  border: 1px dashed var(--color-border);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.upload-box:hover {
  border-color: var(--color-mint);
  background: var(--color-mint-dim);
}

.upload-box .icon {
  font-size: 24px;
}

.upload-box span:last-child {
  font-size: 12px;
  color: var(--text-muted);
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 25px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

label {
  font-size: 0.7rem;
  color: var(--text-muted);
  font-weight: 700;
  letter-spacing: 0.5px;
}

.dark-input,
.input-wrapper input,
.input-wrapper select {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  color: white;
  padding: 12px 14px;
  border-radius: 8px;
  width: 100%;
  font-size: 14px;
  transition: all 0.2s;
}

.dark-input:focus,
.input-wrapper input:focus {
  outline: none;
  border-color: var(--color-mint);
}

.input-wrapper {
  display: flex;
  align-items: center;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  overflow: hidden;
}

.input-wrapper .prefix {
  padding: 0 12px;
  color: var(--text-muted);
  font-size: 16px;
}

.input-wrapper input {
  border: none;
  padding: 12px 0;
}

.btn-submit {
  background: var(--color-mint);
  border: none;
  width: 100%;
  padding: 16px;
  border-radius: 10px;
  font-weight: 800;
  cursor: pointer;
  margin-top: 20px;
  color: var(--color-bg);
  transition: all 0.2s;
}

.btn-submit:hover {
  background: var(--color-mint-dark);
  transform: translateY(-2px);
}

/* Widgets */
.sidebar-widgets {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.widget {
  padding: 20px;
  transition: border-color 0.2s;
}

.widget:hover {
  border-color: var(--color-mint);
}

.widget-title {
  font-size: 0.6rem;
  color: var(--text-muted);
  display: block;
  margin-bottom: 15px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.card-preview {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  padding: 16px;
  border-radius: 10px;
}

.card-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 15px;
}

.q-logo {
  width: 40px;
  height: 40px;
  background: var(--color-mint);
  color: var(--color-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  font-weight: bold;
  font-size: 18px;
}

.card-top h4 {
  font-size: 14px;
  margin-bottom: 4px;
}

.card-top p {
  font-size: 11px;
  color: var(--text-muted);
}

.card-skeleton {
  margin: 12px 0;
}

.line {
  height: 8px;
  background: var(--color-border);
  border-radius: 4px;
  margin-bottom: 8px;
  width: 100%;
}

.line.short {
  width: 60%;
}

.card-tags {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.tag {
  font-size: 0.7rem;
  border: 1px solid var(--color-border);
  padding: 4px 8px;
  border-radius: 4px;
  color: var(--text-muted);
  background: var(--color-bg);
}

.activity-log {
  list-style: none;
  padding: 0;
}

.activity-log li {
  padding: 12px 0;
  border-bottom: 1px solid var(--color-border);
}

.activity-log li:last-child {
  border-bottom: none;
}

.activity-log p {
  font-size: 13px;
  margin-bottom: 4px;
}

.activity-log small {
  font-size: 10px;
  color: var(--text-muted);
}

.tip-box {
  background: var(--color-mint-dim);
  padding: 20px;
  border-radius: 12px;
  border: 1px solid var(--color-mint);
  text-align: center;
}

.tip-icon {
  font-size: 32px;
  display: block;
  margin-bottom: 12px;
}

.tip-box h5 {
  font-size: 14px;
  margin-bottom: 8px;
  color: var(--color-mint);
}

.tip-box p {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.4;
}

/* Responsive */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    gap: 16px;
    padding: 16px 20px;
  }

  .header-left {
    width: 100%;
    justify-content: space-between;
  }

  .nav-links {
    width: 100%;
    justify-content: space-around;
  }

  .layout-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .row {
    grid-template-columns: 1fr;
  }

  .banner-success {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }

  .banner-info {
    flex-direction: column;
  }

  .form-header {
    flex-direction: column;
    gap: 20px;
  }

  .avatar-upload {
    margin-left: 0;
    align-self: center;
  }

  .container {
    padding: 20px;
  }
}
</style>
