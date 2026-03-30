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
        <section class="hero-section hero-section--single">
          <div class="section-title">
            <span class="label">ВАКАНСИИ ДЛЯ IT</span>
            <h1>Поиск вакансий</h1>
            <p>
              Фильтруйте вакансии по формату, уровню и тегам в блоке ниже — таблица и карта обновляются
              автоматически.
            </p>
          </div>
        </section>

        <section class="filters-panel card">
          <div class="search-row">
            <input
              v-model.trim="searchQuery"
              class="search-input"
              type="text"
              placeholder="Поиск по компании, вакансии, городу или тегу"
            />
            <button
              type="button"
              class="favorites-toggle"
              :class="{ active: onlyFavorites }"
              @click="onlyFavorites = !onlyFavorites"
            >
              {{ onlyFavorites ? 'Только избранное: ВКЛ' : 'Только избранное' }}
            </button>
            <span class="results-count">Найдено: {{ filteredJobs.length }}</span>
          </div>

          <div class="filters-row">
            <div class="filter-group">
              <span class="filter-label">Формат</span>
              <button
                v-for="format in availableFormats"
                :key="format"
                type="button"
                class="chip"
                :class="{ active: selectedFormats.includes(format) }"
                @click="toggleArrayValue(selectedFormats, format)"
              >
                {{ format }}
              </button>
            </div>

            <div class="filter-group">
              <span class="filter-label">Уровень</span>
              <button
                v-for="level in availableLevels"
                :key="level"
                type="button"
                class="chip"
                :class="{ active: selectedLevels.includes(level) }"
                @click="toggleArrayValue(selectedLevels, level)"
              >
                {{ level }}
              </button>
            </div>
          </div>

          <div class="filter-group tags-group">
            <span class="filter-label">Теги</span>
            <button
              v-for="tag in availableTags"
              :key="tag"
              type="button"
              class="chip"
              :class="{ active: selectedTags.includes(tag) }"
              @click="toggleArrayValue(selectedTags, tag)"
            >
              {{ tag }}
            </button>
          </div>
        </section>

        <section class="map-section card">
          <div class="map-head">
            <h2>Карта вакансий</h2>
            <p>Кликните по точке на карте, чтобы открыть модульную карточку вакансии.</p>
          </div>

          <div class="map-canvas">
            <svg class="city-map" viewBox="0 0 1000 520" preserveAspectRatio="none" aria-hidden="true">
              <rect x="0" y="0" width="1000" height="520" class="map-bg" />
              <g class="roads-minor">
                <path d="M0 70 L1000 70" />
                <path d="M0 130 L1000 130" />
                <path d="M0 190 L1000 190" />
                <path d="M0 250 L1000 250" />
                <path d="M0 310 L1000 310" />
                <path d="M0 370 L1000 370" />
                <path d="M0 430 L1000 430" />
                <path d="M80 0 L80 520" />
                <path d="M180 0 L180 520" />
                <path d="M280 0 L280 520" />
                <path d="M380 0 L380 520" />
                <path d="M480 0 L480 520" />
                <path d="M580 0 L580 520" />
                <path d="M680 0 L680 520" />
                <path d="M780 0 L780 520" />
                <path d="M880 0 L880 520" />
              </g>

              <g class="roads-ring">
                <ellipse cx="500" cy="260" rx="120" ry="80" />
                <ellipse cx="500" cy="260" rx="190" ry="125" />
                <ellipse cx="500" cy="260" rx="270" ry="180" />
                <ellipse cx="500" cy="260" rx="360" ry="235" />
              </g>

              <g class="roads-radial">
                <line x1="500" y1="260" x2="500" y2="15" />
                <line x1="500" y1="260" x2="740" y2="90" />
                <line x1="500" y1="260" x2="950" y2="260" />
                <line x1="500" y1="260" x2="740" y2="430" />
                <line x1="500" y1="260" x2="500" y2="500" />
                <line x1="500" y1="260" x2="260" y2="430" />
                <line x1="500" y1="260" x2="50" y2="260" />
                <line x1="500" y1="260" x2="260" y2="90" />
              </g>
            </svg>

            <button
              v-for="point in mapJobs"
              :key="`map-${point.id}`"
              type="button"
              class="map-pin"
              :class="{ active: selectedMapJob?.id === point.id, favorite: isVacancyFavorite(point.id) }"
              :style="{ left: `${point.x}%`, top: `${point.y}%` }"
              @click="selectMapJob(point)"
            >
              <span>{{ point.id }}</span>
            </button>

            <div v-if="selectedMapJob" class="map-module-card">
              <div class="module-top">
                <div class="module-dot"></div>
                <span>{{ selectedMapJob.company }}</span>
              </div>
              <h3>{{ selectedMapJob.title }}</h3>
              <p>{{ selectedMapJob.location }} • {{ selectedMapJob.salary }}</p>
              <div class="module-tags">
                <span v-for="tag in selectedMapJob.tags.slice(0, 3)" :key="tag">{{ tag }}</span>
              </div>
              <div class="module-favorites">
                <button type="button" class="fav-btn" @click="toggleCompanyFavorite(selectedMapJob.company)">
                  {{ isCompanyFavorite(selectedMapJob.company) ? '★ Компания в избранном' : '☆ В избранное компанию' }}
                </button>
                <button type="button" class="fav-btn" @click="toggleVacancyFavorite(selectedMapJob.id)">
                  {{ isVacancyFavorite(selectedMapJob.id) ? '★ Вакансия в избранном' : '☆ В избранное вакансию' }}
                </button>
              </div>
              <button type="button" class="module-btn" @click="openJob(selectedMapJob.id)">
                Открыть вакансию
              </button>
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
              <tr
                v-for="job in filteredJobs"
                :key="job.id"
                class="job-row"
                role="button"
                tabindex="0"
                @click="openJob(job.id)"
                @keydown.enter="openJob(job.id)"
              >
                <td>
                  <div class="company-cell">
                    <div class="company-logo" :style="{ backgroundColor: job.logoBg }">
                      {{ job.logo }}
                    </div>
                    <span>{{ job.company }}</span>
                    <button
                      type="button"
                      class="inline-fav"
                      :class="{ active: isCompanyFavorite(job.company) }"
                      title="Добавить компанию в избранное"
                      @click.stop="toggleCompanyFavorite(job.company)"
                    >
                      {{ isCompanyFavorite(job.company) ? '★' : '☆' }}
                    </button>
                  </div>
                </td>
                <td>
                  <div class="job-title">
                    {{ job.title }}
                    <button
                      type="button"
                      class="inline-fav"
                      :class="{ active: isVacancyFavorite(job.id) }"
                      title="Добавить вакансию в избранное"
                      @click.stop="toggleVacancyFavorite(job.id)"
                    >
                      {{ isVacancyFavorite(job.id) ? '★' : '☆' }}
                    </button>
                  </div>
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
            <span>Показано {{ filteredJobs.length }} из {{ jobs.length }} вакансий</span>
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
import { computed, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { applicantJobs } from '@/data/applicantJobs'

const activeNav = 'jobs'
const router = useRouter()
const authStore = useAuthStore()
const searchQuery = ref('')
const selectedFormats = ref([])
const selectedLevels = ref([])
const selectedTags = ref([])
const onlyFavorites = ref(false)
const favoriteCompanies = ref([])
const favoriteVacancyIds = ref([])

const FAVORITE_COMPANIES_KEY = 'favorite_companies'
const FAVORITE_VACANCIES_KEY = 'favorite_vacancies'

try {
  const savedCompanies = JSON.parse(localStorage.getItem(FAVORITE_COMPANIES_KEY) || '[]')
  const savedVacancies = JSON.parse(localStorage.getItem(FAVORITE_VACANCIES_KEY) || '[]')
  if (Array.isArray(savedCompanies)) favoriteCompanies.value = savedCompanies
  if (Array.isArray(savedVacancies)) favoriteVacancyIds.value = savedVacancies
} catch (_e) {
  favoriteCompanies.value = []
  favoriteVacancyIds.value = []
}

const displayName = computed(() => authStore.user?.name || authStore.user?.username || authStore.user?.email || 'Соискатель')
const initials = computed(() => {
  const src = (displayName.value || '').trim()
  if (!src) return 'U'
  const parts = src.split(/\s+/).slice(0, 2)
  const letters = parts.map((p) => (p[0] || '').toUpperCase()).join('')
  return letters || 'U'
})

const jobs = applicantJobs
const availableFormats = computed(() => [...new Set(jobs.map((job) => job.format))])
const availableLevels = computed(() => [...new Set(jobs.map((job) => job.level))])
const availableTags = computed(() => [...new Set(jobs.flatMap((job) => job.tags))])
const filteredJobs = computed(() => {
  const q = searchQuery.value.toLowerCase()
  return jobs.filter((job) => {
    const searchable = `${job.company} ${job.title} ${job.location} ${job.tags.join(' ')}`.toLowerCase()
    const byText = !q || searchable.includes(q)
    const byFormat = !selectedFormats.value.length || selectedFormats.value.includes(job.format)
    const byLevel = !selectedLevels.value.length || selectedLevels.value.includes(job.level)
    const byTags =
      !selectedTags.value.length ||
      selectedTags.value.some((tag) => job.tags.includes(tag))
    const byFavorites =
      !onlyFavorites.value ||
      favoriteVacancyIds.value.includes(job.id) ||
      favoriteCompanies.value.includes(job.company)
    return byText && byFormat && byLevel && byTags && byFavorites
  })
})
const mapCoords = {
  1: { x: 44, y: 33 },
  2: { x: 31, y: 28 },
  3: { x: 58, y: 39 },
  4: { x: 68, y: 47 },
  5: { x: 24, y: 53 },
  6: { x: 52, y: 55 },
  7: { x: 74, y: 31 },
  8: { x: 40, y: 44 },
  9: { x: 17, y: 39 },
  10: { x: 62, y: 24 },
}
const mapJobs = computed(() =>
  filteredJobs.value.map((job) => ({
    ...job,
    x: mapCoords[job.id]?.x ?? 50,
    y: mapCoords[job.id]?.y ?? 50,
  })),
)
const selectedMapJob = ref(mapJobs.value[0] || null)

const selectMapJob = (job) => {
  selectedMapJob.value = job
}

watch(mapJobs, (next) => {
  if (!next.length) {
    selectedMapJob.value = null
    return
  }
  const selectedId = selectedMapJob.value?.id
  selectedMapJob.value = next.find((job) => job.id === selectedId) || next[0]
})

const toggleArrayValue = (targetRef, value) => {
  targetRef.value = targetRef.value.includes(value)
    ? targetRef.value.filter((item) => item !== value)
    : [...targetRef.value, value]
}

const isCompanyFavorite = (companyName) => favoriteCompanies.value.includes(companyName)
const isVacancyFavorite = (vacancyId) => favoriteVacancyIds.value.includes(vacancyId)

const saveFavorites = () => {
  localStorage.setItem(FAVORITE_COMPANIES_KEY, JSON.stringify(favoriteCompanies.value))
  localStorage.setItem(FAVORITE_VACANCIES_KEY, JSON.stringify(favoriteVacancyIds.value))
}

const toggleCompanyFavorite = (companyName) => {
  favoriteCompanies.value = isCompanyFavorite(companyName)
    ? favoriteCompanies.value.filter((name) => name !== companyName)
    : [...favoriteCompanies.value, companyName]
  saveFavorites()
}

const toggleVacancyFavorite = (vacancyId) => {
  favoriteVacancyIds.value = isVacancyFavorite(vacancyId)
    ? favoriteVacancyIds.value.filter((id) => id !== vacancyId)
    : [...favoriteVacancyIds.value, vacancyId]
  saveFavorites()
}

const openJob = (jobId) => {
  router.push({ name: 'applicant-job-details', params: { id: jobId } })
}

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

.hero-section--single {
  grid-template-columns: 1fr;
  align-items: start;
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

.filters-panel {
  padding: 16px;
  margin-bottom: 20px;
}

.search-row {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 12px;
}

.search-input {
  flex: 1;
  background: #0f172a;
  border: 1px solid var(--color-border);
  color: white;
  border-radius: 10px;
  padding: 12px 14px;
}

.favorites-toggle {
  border: 1px solid var(--color-border);
  border-radius: 10px;
  background: transparent;
  color: #cbd5e1;
  padding: 10px 12px;
  font-size: 12px;
  cursor: pointer;
  white-space: nowrap;
}

.favorites-toggle.active {
  border-color: rgba(250, 204, 21, 0.7);
  color: #facc15;
  background: rgba(250, 204, 21, 0.1);
}

.results-count {
  color: #9ca3af;
  font-size: 13px;
}

.filters-row {
  display: flex;
  gap: 18px;
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.filter-label {
  color: #9ca3af;
  font-size: 12px;
  margin-right: 6px;
}

.tags-group {
  margin-top: 10px;
}

.chip {
  border: 1px solid var(--color-border);
  background: transparent;
  color: #cbd5e1;
  border-radius: 999px;
  padding: 6px 10px;
  font-size: 12px;
  cursor: pointer;
}

.chip.active {
  border-color: var(--color-mint);
  color: var(--color-mint);
  background: var(--color-mint-dim);
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

.map-section {
  margin-bottom: 20px;
  padding: 18px;
}

.map-head {
  margin-bottom: 12px;
}

.map-head h2 {
  margin: 0 0 4px;
  font-size: 20px;
}

.map-head p {
  margin: 0;
  color: var(--text-muted);
  font-size: 13px;
}

.map-canvas {
  position: relative;
  min-height: 360px;
  border-radius: 14px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  overflow: hidden;
  background: #0b0f15;
}

.city-map {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0.95;
}

.map-bg {
  fill: #090d13;
}

.roads-minor path {
  stroke: rgba(148, 163, 184, 0.08);
  stroke-width: 1.1;
}

.roads-ring ellipse {
  fill: none;
  stroke: rgba(148, 163, 184, 0.45);
  stroke-width: 2.2;
}

.roads-radial line {
  stroke: rgba(148, 163, 184, 0.34);
  stroke-width: 1.8;
  stroke-linecap: round;
}

.map-pin {
  position: absolute;
  transform: translate(-50%, -50%);
  width: 22px;
  height: 22px;
  border-radius: 999px;
  border: none;
  background: rgba(16, 185, 129, 0.95);
  color: #041012;
  font-size: 10px;
  font-weight: 800;
  cursor: pointer;
  box-shadow:
    0 0 0 3px rgba(16, 185, 129, 0.18),
    0 0 20px rgba(16, 185, 129, 0.45);
  transition: transform 0.2s ease;
}

.map-pin:hover,
.map-pin.active {
  transform: translate(-50%, -50%) scale(1.15);
}

.map-pin.favorite {
  background: #facc15;
  color: #1f2937;
  box-shadow:
    0 0 0 3px rgba(250, 204, 21, 0.18),
    0 0 18px rgba(250, 204, 21, 0.5);
}

.map-module-card {
  position: absolute;
  right: 18px;
  bottom: 18px;
  width: 280px;
  border-radius: 14px;
  border: 1px solid rgba(16, 185, 129, 0.5);
  background: rgba(11, 18, 32, 0.92);
  backdrop-filter: blur(6px);
  padding: 14px;
  box-shadow: 0 12px 30px rgba(2, 6, 23, 0.55);
}

.module-top {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #a7f3d0;
  font-size: 12px;
  margin-bottom: 6px;
}

.module-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.8);
}

.map-module-card h3 {
  margin: 0 0 6px;
  font-size: 15px;
}

.map-module-card p {
  margin: 0 0 10px;
  color: #cbd5e1;
  font-size: 12px;
}

.module-tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.module-tags span {
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 999px;
  padding: 4px 8px;
  font-size: 11px;
  color: #cbd5e1;
}

.module-btn {
  width: 100%;
  margin-top: 10px;
  border: none;
  border-radius: 10px;
  padding: 10px;
  background: #10b981;
  color: #052617;
  font-weight: 800;
  cursor: pointer;
}

.module-favorites {
  display: grid;
  gap: 6px;
  margin-top: 8px;
}

.fav-btn {
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 8px;
  background: transparent;
  color: #cbd5e1;
  padding: 8px;
  font-size: 12px;
  cursor: pointer;
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

.job-row {
  cursor: pointer;
}

.job-row:focus-visible {
  outline: 2px solid var(--color-mint);
  outline-offset: -2px;
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
  display: flex;
  align-items: center;
  gap: 8px;
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

.inline-fav {
  border: 1px solid rgba(148, 163, 184, 0.4);
  border-radius: 6px;
  background: transparent;
  color: #cbd5e1;
  width: 24px;
  height: 24px;
  cursor: pointer;
  font-size: 14px;
  line-height: 1;
}

.inline-fav.active {
  color: #facc15;
  border-color: rgba(250, 204, 21, 0.6);
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

