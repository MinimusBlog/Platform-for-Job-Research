<template>
  <div class="page">
    <main class="content">
      <div class="header-row">
        <button class="back-btn" type="button" @click="goBack">← К поиску вакансий</button>
      </div>

      <section v-if="job" class="card">
        <div class="title-row">
          <div class="company-logo" :style="{ backgroundColor: job.logoBg }">{{ job.logo }}</div>
          <div>
            <p class="company">{{ job.company }}</p>
            <h1>{{ job.title }}</h1>
          </div>
        </div>

        <div class="meta-grid">
          <div class="meta-item"><span>Локация</span><strong>{{ job.location }}</strong></div>
          <div class="meta-item"><span>Формат</span><strong>{{ job.format }}</strong></div>
          <div class="meta-item"><span>Уровень</span><strong>{{ job.level }}</strong></div>
          <div class="meta-item"><span>Зарплата</span><strong>{{ job.salary }}</strong></div>
        </div>

        <div class="section">
          <h3>Описание вакансии</h3>
          <p>{{ job.description }}</p>
        </div>

        <div class="section">
          <h3>Ключевые требования</h3>
          <ul>
            <li v-for="item in job.requirements" :key="item">{{ item }}</li>
          </ul>
        </div>

        <div class="section">
          <h3>Стек</h3>
          <div class="tags">
            <span v-for="tag in job.tags" :key="tag" class="tag">{{ tag }}</span>
          </div>
        </div>

        <button class="apply-btn" type="button">Откликнуться</button>
      </section>

      <section v-else class="card">
        <h2>Вакансия не найдена</h2>
        <p>Возможно, она была удалена или ссылка содержит неверный идентификатор.</p>
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { applicantJobs } from '@/data/applicantJobs'

const route = useRoute()
const router = useRouter()

const jobId = computed(() => Number(route.params.id))
const job = computed(() => applicantJobs.find((item) => item.id === jobId.value))

const goBack = () => {
  router.push({ name: 'applicant-jobs' })
}
</script>

<style scoped>
.page {
  min-height: 100vh;
  background: var(--color-bg);
  color: white;
  font-family: 'Montserrat', sans-serif;
  padding: 32px 20px;
}

.content {
  max-width: 900px;
  margin: 0 auto;
}

.header-row {
  margin-bottom: 16px;
}

.back-btn {
  border: 1px solid var(--color-border);
  background: transparent;
  color: #cbd5e1;
  border-radius: 10px;
  padding: 10px 14px;
  cursor: pointer;
}

.card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 16px;
  padding: 24px;
}

.title-row {
  display: flex;
  gap: 14px;
  align-items: center;
  margin-bottom: 20px;
}

.company-logo {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}

.company {
  color: var(--color-mint);
  font-weight: 700;
  margin: 0;
}

h1 {
  margin: 4px 0 0;
}

.meta-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
  margin-bottom: 20px;
}

.meta-item {
  border: 1px solid var(--color-border);
  border-radius: 10px;
  padding: 12px;
}

.meta-item span {
  display: block;
  color: #9ca3af;
  font-size: 12px;
  margin-bottom: 6px;
}

.section {
  margin-bottom: 20px;
}

.section h3 {
  margin-bottom: 10px;
}

.section p,
.section li {
  color: #cbd5e1;
  line-height: 1.6;
}

ul {
  margin: 0;
  padding-left: 18px;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  font-size: 12px;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid var(--color-border);
  color: #cbd5e1;
}

.apply-btn {
  width: 100%;
  border: none;
  border-radius: 10px;
  padding: 14px;
  background: var(--color-mint);
  color: #0d1117;
  font-weight: 800;
  cursor: pointer;
}

@media (max-width: 768px) {
  .meta-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>

