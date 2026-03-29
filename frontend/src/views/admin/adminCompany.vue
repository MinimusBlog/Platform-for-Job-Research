<script setup>
import { ref } from 'vue'

const activeTab = ref('Работодатели')

// Данные для таблицы (как на скрине)
const employers = ref([
  {
    id: 1,
    name: 'CyberSphere Solutions',
    type: 'IT Консалтинг • Москва',
    inn: '7701234567',
    date: '12 Окт 2023',
    docs: true,
    status: 'pending',
  },
  {
    id: 2,
    name: 'Квантовый Прыжок',
    type: 'Разработка ПО • Иннополис',
    inn: '1655987654',
    date: '08 Окт 2023',
    docs: true,
    status: 'pending',
  },
  {
    id: 3,
    name: 'ООО «Инновации»',
    type: 'Производство • Екатеринбург',
    inn: '6671098234',
    date: '05 Окт 2023',
    docs: true,
    status: 'pending',
  },
  {
    id: 4,
    name: 'DataFlow Systems',
    type: 'Big Data • Санкт-Петербург',
    inn: '7841002233',
    date: '01 Окт 2023',
    docs: false,
    status: 'pending',
  },
])

const menuItems = [
  { name: 'Главная', icon: 'grid', link: 'adminmain.vue' },
  { name: 'Пользователи', icon: 'users', link: 'admidusers.vue' },
  { name: 'Работодатели', icon: 'briefcase', link: '#', badge: 18 },
  { name: 'Карточки', icon: 'layout', link: 'admincard.vue' },
  { name: 'Теги', icon: 'tag', link: '#' },
  { name: 'Кураторы', icon: 'user-check', link: '#' },
]
</script>

<template>
  <div class="flex min-h-screen bg-[var(--color-bg)] text-white font-['Montserrat']">
    <!-- SIDEBAR -->
    <aside class="w-64 border-r border-[var(--color-border)] flex flex-col p-6 shrink-0">
      <div class="mb-10 flex items-center gap-2">
        <div class="w-8 h-8 bg-[var(--color-mint)] rounded-lg flex items-center justify-center">
          <span class="text-[var(--color-bg)] font-bold">Т</span>
        </div>
        <div class="leading-none">
          <div class="text-sm font-bold tracking-tight">Трамплин</div>
          <div class="text-[8px] text-gray-500 uppercase tracking-widest">Панель управления</div>
        </div>
      </div>

      <nav class="space-y-1">
        <a
          v-for="item in menuItems"
          :key="item.name"
          :href="item.link"
          @click.prevent="activeTab = item.name"
          :class="[
            item.link === activeTab
              ? 'text-[var(--color-mint)]'
              : 'text-gray-400 hover:bg-white/5 hover:text-white',
          ]"
        >
          <span class="flex items-center gap-3">
            <span class="opacity-50">#</span> {{ item.name }}
          </span>
          <span
            v-if="item.badge"
            class="bg-[var(--color-mint)] text-[var(--color-bg)] text-[10px] font-bold px-2 py-0.5 rounded-full"
          >
            {{ item.badge }}
          </span>
        </a>
      </nav>

      <!-- Профиль куратора снизу -->
      <div
        class="mt-auto p-3 card flex items-center gap-3 bg-[var(--color-bg-card)] border-[var(--color-border)]"
      >
        <img src="https://ui-avatars.com" class="w-10 h-10 rounded-lg" />
        <div class="overflow-hidden">
          <p class="text-xs font-bold truncate">Александр К.</p>
          <p class="text-[9px] text-gray-500 uppercase">Старший куратор</p>
        </div>
      </div>
    </aside>

    <!-- MAIN -->
    <main class="flex-1 flex flex-col overflow-hidden">
      <!-- Top Bar -->
      <header
        class="h-16 border-b border-[var(--color-border)] flex items-center justify-between px-8 bg-[var(--color-bg)]/80 backdrop-blur-md"
      >
        <div
          class="flex items-center gap-4 bg-[var(--color-bg-card)] px-4 py-2 rounded-lg border border-[var(--color-border)]"
        >
          <span class="text-gray-500 text-xs italic">🔍 Поиск компаний...</span>
        </div>
        <div class="flex items-center gap-4 text-gray-400">
          <span class="text-xs">Регион: <b>Москва и область</b></span>
          <span class="cursor-pointer hover:text-white">⚙️</span>
        </div>
      </header>

      <!-- Content Area -->
      <div class="p-10 overflow-y-auto custom-scrollbar">
        <!-- Title & Stats -->
        <div class="flex justify-between items-start mb-10">
          <div>
            <h1 class="text-3xl font-bold mb-2">Модерация работодателей</h1>
            <p class="text-gray-400 text-sm">
              Проверка и верификация новых компаний, подавших заявку.
            </p>
          </div>
          <div class="flex gap-4">
            <div class="card px-6 py-3 flex items-center gap-4">
              <div
                class="w-10 h-10 bg-blue-500/10 rounded flex items-center justify-center text-blue-500"
              >
                📥
              </div>
              <div>
                <p class="text-[9px] text-gray-500 uppercase font-bold">Ожидают</p>
                <p class="text-xl font-bold">18</p>
              </div>
            </div>
            <div class="card px-6 py-3 flex items-center gap-4">
              <div
                class="w-10 h-10 bg-[var(--color-mint-dim)] rounded flex items-center justify-center text-[var(--color-mint)]"
              >
                ✔
              </div>
              <div>
                <p class="text-[9px] text-gray-500 uppercase font-bold">Верифицировано</p>
                <p class="text-xl font-bold">1,240</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Таблица -->
        <div
          class="bg-[var(--color-bg-card)] border border-[var(--color-border)] rounded-2xl overflow-hidden mb-10"
        >
          <div
            class="grid grid-cols-12 px-6 py-4 border-b border-[var(--color-border)] text-[10px] font-bold text-gray-500 uppercase tracking-widest"
          >
            <div class="col-span-4">Компания</div>
            <div class="col-span-2">ИНН / Регистрация</div>
            <div class="col-span-2">Документы</div>
            <div class="col-span-4 text-right">Действия</div>
          </div>

          <div
            v-for="emp in employers"
            :key="emp.id"
            class="grid grid-cols-12 px-6 py-5 border-b border-[var(--color-border)] items-center hover:bg-white/[0.02] transition-colors"
          >
            <div class="col-span-4 flex items-center gap-4">
              <div
                class="w-10 h-10 bg-[var(--color-bg-elevated)] rounded-lg border border-[var(--color-border)] flex items-center justify-center text-lg"
              >
                🏢
              </div>
              <div>
                <p class="font-bold text-sm">{{ emp.name }}</p>
                <p class="text-[10px] text-gray-500">{{ emp.type }}</p>
              </div>
            </div>
            <div class="col-span-2">
              <p class="text-xs font-medium">{{ emp.inn }}</p>
              <p class="text-[10px] text-gray-500">{{ emp.date }}</p>
            </div>
            <div class="col-span-2 flex gap-2">
              <span v-if="emp.docs" class="text-gray-400">📄 📁</span>
              <span v-else class="text-[10px] text-gray-600 italic">Нет файлов</span>
            </div>
            <div class="col-span-4 flex justify-end gap-2">
              <button
                class="px-4 py-2 text-[9px] font-bold uppercase border border-[var(--color-border)] rounded-lg hover:border-[var(--color-mint)] transition-colors"
              >
                Запросить данные
              </button>
              <button
                class="px-4 py-2 text-[9px] font-bold uppercase text-red-400 hover:bg-red-400/10 rounded-lg"
              >
                Отклонить
              </button>
              <button
                class="px-4 py-2 text-[9px] font-bold uppercase bg-[var(--color-mint)] text-[var(--color-bg)] rounded-lg hover:brightness-110"
              >
                Верифицировать
              </button>
            </div>
          </div>
        </div>

        <!-- Блок ИИ Рекомендации -->
        <div class="grid grid-cols-3 gap-6">
          <div
            class="col-span-2 card p-8 bg-gradient-to-br from-[#1c2333] to-[var(--color-bg-card)] border-blue-500/30"
          >
            <div class="flex items-center gap-3 mb-6">
              <span class="text-blue-400 text-xl">✨</span>
              <h3 class="font-bold text-lg">Рекомендация ИИ по верификации</h3>
            </div>
            <p class="text-sm text-gray-400 leading-relaxed mb-8">
              Наша система проанализировала предоставленные ИНН.
              <span class="text-white font-medium">CyberSphere Solutions</span> и
              <span class="text-white font-medium">DataFlow Systems</span> имеют высокий рейтинг
              доверия и действующие государственные контракты. Рекомендуем ускоренную верификацию.
            </p>
            <div class="flex gap-10">
              <div>
                <p class="text-[10px] text-gray-500 font-bold uppercase mb-1">Точность модели</p>
                <p class="text-2xl font-bold">98.4%</p>
              </div>
              <div>
                <p class="text-[10px] text-gray-500 font-bold uppercase mb-1">Флаги риска</p>
                <p class="text-2xl font-bold text-red-500">0</p>
              </div>
            </div>
          </div>

          <div class="card p-8 flex flex-col items-center justify-center text-center">
            <div class="relative w-32 h-32 mb-6">
              <svg class="w-full h-full transform -rotate-90">
                <circle
                  cx="64"
                  cy="64"
                  r="60"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="transparent"
                  class="text-gray-800"
                />
                <circle
                  cx="64"
                  cy="64"
                  r="60"
                  stroke="currentColor"
                  stroke-width="8"
                  fill="transparent"
                  stroke-dasharray="376"
                  stroke-dashoffset="100"
                  class="text-[var(--color-mint)]"
                />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center">
                <span class="text-2xl font-bold italic">14м</span>
              </div>
            </div>
            <p class="text-xs font-bold mb-1">Скорость модерации</p>
            <p class="text-[10px] text-gray-500 uppercase">Среднее время сегодня</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: 10px;
}
.card {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 1.25rem;
}
</style>
