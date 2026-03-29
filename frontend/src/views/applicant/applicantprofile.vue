<template>
  <div class="flex min-h-screen bg-bg text-white font-sans">
    <aside class="w-64 border-r border-border bg-bg-card p-6 flex flex-col fixed h-full z-20">
      <div class="text-mint font-black text-2xl tracking-tighter mb-10">ТРАМПЛИН</div>

      <div class="bg-white/5 p-4 mb-8 rounded-2xl border border-border">
        <div class="flex items-center gap-3 mb-4">
          <div
            class="w-10 h-10 rounded-full bg-gradient-to-tr from-mint to-mint-dark flex-shrink-0"
          ></div>
          <div class="overflow-hidden">
            <p class="text-sm font-bold truncate">Alex Kovalev</p>
            <p class="text-[10px] text-muted tracking-wide uppercase truncate">МГТУ им. Баумана</p>
          </div>
        </div>
        <button
          class="w-full py-2 bg-mint-dim text-mint text-[10px] font-black rounded-lg hover:bg-mint hover:text-bg transition-all"
        >
          ОБНОВИТЬ РЕЗЮМЕ
        </button>
      </div>

      <nav class="space-y-1 flex-1">
        <router-link
          :to="{ name: 'applicant-profile' }"
          class="nav-item"
          :class="{ active: activeNav === 'profile' }"
        >
          <span>👤</span> ПРОФИЛЬ
        </router-link>
        <router-link :to="{ name: 'applicant' }" class="nav-item">
          <span>📄</span> МОИ ЗАЯВКИ
        </router-link>
        <router-link :to="{ name: 'applicant-network' }" class="nav-item">
          <span>🌐</span> НЕТВОРКИНГ
        </router-link>
        <a href="#" class="nav-item opacity-60"><span>⚙️</span> НАСТРОЙКИ</a>
      </nav>

      <div class="pt-6 border-t border-border mt-auto">
        <a href="#" class="nav-item hover:text-red-400 transition-colors"><span>🚪</span> ВЫЙТИ</a>
      </div>
    </aside>

    <main class="flex-1 ml-64 flex flex-col">
      <header
        class="flex justify-between items-center p-6 border-b border-border bg-bg-card sticky top-0 z-10"
      >
        <div class="relative">
          <input
            type="text"
            placeholder="Поиск вакансий..."
            class="bg-bg border border-border rounded-xl px-4 py-2 w-80 text-sm focus:outline-none focus:border-mint transition-all"
          />
        </div>
        <div class="flex items-center gap-4">
          <span class="cursor-pointer hover:text-mint transition-colors text-xl">🔔</span>
          <div
            class="w-10 h-10 rounded-full bg-mint text-bg font-bold flex items-center justify-center"
          >
            AK
          </div>
        </div>
      </header>

      <div class="p-8 max-w-6xl mx-auto w-full">
        <section
          class="bg-bg-card border border-border rounded-3xl p-8 mb-8 flex flex-col md:flex-row justify-between items-center gap-6 shadow-sm"
        >
          <div class="flex items-center gap-6">
            <div class="relative">
              <div
                class="w-24 h-24 rounded-3xl bg-gradient-to-br from-mint to-mint-dark flex items-center justify-center text-3xl font-black shadow-lg shadow-mint/10"
              >
                AK
              </div>
              <div
                class="absolute -bottom-1 -right-1 w-5 h-5 bg-green-500 rounded-full border-4 border-bg-card"
              ></div>
            </div>
            <div>
              <div class="flex items-center gap-3 mb-2">
                <h1 class="text-3xl font-black tracking-tight italic">Alex Kovalev</h1>
                <span
                  class="bg-mint-dim text-mint text-[10px] font-black px-3 py-1 rounded-lg uppercase tracking-wider"
                  >ИЩУ СТАЖИРОВКУ</span
                >
              </div>
              <p class="text-muted font-medium uppercase text-[11px] tracking-widest">
                IT Выпускник • МГТУ им. Баумана • 2024
              </p>
            </div>
          </div>
          <div class="flex items-center gap-6 bg-bg p-4 rounded-2xl border border-border">
            <div class="flex flex-col items-end">
              <span class="text-[9px] font-black text-muted uppercase">Публичный профиль</span>
              <div
                class="switch w-10 h-5 bg-bg-elevated rounded-full relative cursor-pointer mt-1 border border-border"
              >
                <div
                  class="switch-handle absolute top-0.5 left-0.5 w-3.5 h-3.5 bg-mint rounded-full transition-transform"
                ></div>
              </div>
            </div>
            <button
              class="bg-mint text-bg font-black px-6 py-3 rounded-xl hover:bg-mint-dark transition-all shadow-lg shadow-mint/20"
            >
              СКАЧАТЬ РЕЗЮМЕ
            </button>
          </div>
        </section>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div class="space-y-6">
            <section class="bg-bg-card border border-border rounded-3xl p-6">
              <h3 class="text-[10px] font-black text-muted mb-4 uppercase tracking-[0.2em]">
                Технологический стек
              </h3>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="tech in technicalStack"
                  :key="tech"
                  class="bg-bg border border-border text-[11px] font-bold px-3 py-2 rounded-xl"
                >
                  {{ tech }}
                </span>
              </div>
            </section>

            <section class="bg-bg-card border border-border rounded-3xl p-6">
              <h3 class="text-[10px] font-black text-muted mb-4 uppercase tracking-[0.2em]">
                Контакты
              </h3>
              <div class="space-y-4">
                <div class="flex items-center gap-3 text-sm font-medium">
                  <span class="text-mint">@</span> a.kovalev@bauman.ru
                </div>
                <div class="flex items-center gap-3 text-sm font-medium">
                  <span class="text-mint">🔗</span> linkedin.com/in/akovalev
                </div>
              </div>
            </section>
          </div>

          <div class="lg:col-span-2">
            <section class="bg-bg-card border border-border rounded-3xl p-8">
              <div class="flex justify-between items-center mb-8">
                <h3 class="text-[10px] font-black text-muted uppercase tracking-[0.2em]">
                  Проекты и опыт
                </h3>
                <button
                  class="w-8 h-8 rounded-full border border-border flex items-center justify-center hover:border-mint hover:text-mint transition-all"
                >
                  +
                </button>
              </div>

              <div
                v-for="project in projects"
                :key="project.id"
                class="bg-bg border border-border rounded-2xl p-6 mb-4 last:mb-0 group hover:border-mint/50 transition-all"
              >
                <div class="flex justify-between items-start mb-3">
                  <h4 class="text-lg font-bold group-hover:text-mint transition-colors italic">
                    {{ project.title }}
                  </h4>
                  <a
                    :href="project.link"
                    target="_blank"
                    class="text-mint text-[10px] font-black border-b border-mint/0 hover:border-mint transition-all"
                    >GITHUB ↗</a
                  >
                </div>
                <span
                  class="text-[9px] font-black text-mint/60 uppercase tracking-widest mb-3 block"
                  >{{ project.meta }}</span
                >
                <p class="text-sm text-muted mb-4 leading-relaxed">{{ project.description }}</p>
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="tech in project.tech"
                    :key="tech"
                    class="text-[10px] font-black text-mint bg-mint-dim px-2 py-1 rounded"
                  >
                    #{{ tech }}
                  </span>
                </div>
              </div>
            </section>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeNav = ref('profile')
const technicalStack = ref(['React', 'TypeScript', 'Go', 'Docker', 'Node.js', 'PostgreSQL'])
const projects = ref([
  {
    id: 1,
    title: 'Микросервисный движок для E-Commerce',
    meta: 'ВЫПУСКНАЯ РАБОТА • 2024',
    description:
      'Разработал архитектуру для отслеживания запасов в реальном времени с использованием Go и Kafka.',
    tech: ['Go', 'Kafka', 'Redis'],
    link: 'https://github.com',
  },
  {
    id: 2,
    title: 'Чат-приложение в реальном времени',
    meta: 'ЛИЧНЫЙ ПРОЕКТ • 2023',
    description:
      'Создал чат-приложение с использованием WebSockets и React с поддержкой групповых сообщений.',
    tech: ['React', 'Node.js', 'Socket.io'],
    link: 'https://github.com',
  },
])
</script>

<style scoped>
@reference "../../assets/main.css";

.nav-item {
  @apply flex items-center gap-4 px-4 py-3 text-[11px] font-bold tracking-widest text-muted rounded-xl transition-all cursor-pointer;
}
.nav-item:hover {
  @apply bg-bg-elevated text-white;
}
.nav-item.active {
  @apply bg-mint-dim text-mint border border-mint/20;
}
.switch-handle {
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
