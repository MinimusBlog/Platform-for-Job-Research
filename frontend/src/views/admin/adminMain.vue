<script setup>
import { ref } from 'vue'

// Состояние активной вкладки
const activeTab = ref('Компания')

// Массив пунктов меню для удобного управления ссылками
const navItems = [
  { name: 'ГЛАВНАЯ', icon: '🏠', link: '#' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', link: 'admidusers.vue' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', link: 'admincompani.vue' },
  { name: 'КАРТОЧКИ', icon: '🗂️', link: 'admincard.vue' },
  { name: 'ТЕГИ', icon: '🏷️', link: '#' },
  { name: 'КУРАТОРЫ', icon: '🎧', link: '#' },
]
</script>

<template>
  <div class="flex min-h-screen bg-[var(--color-bg)] text-white">
    <!-- БОКОВОЕ МЕНЮ (Sidebar) -->
    <aside class="w-64 border-r border-[var(--color-border)] flex flex-col p-6">
      <div class="mb-10 flex items-center gap-2">
        <div class="w-2 h-6 bg-[var(--color-mint)] rounded-full"></div>
        <span class="font-bold text-xl tracking-tight text-[var(--color-mint)] uppercase"
          >Трамплин</span
        >
      </div>

      <!-- Твое меню с навигацией -->
      <nav class="flex flex-col gap-2">
        <p class="text-[10px] text-gray-500 font-bold mb-2 ml-2 tracking-widest uppercase">
          Панель управления
        </p>

        <a
          v-for="item in navItems"
          :key="item.name"
          :href="item.link"
          @click="activeTab = item.name"
          :class="
            activeTab === item.name
              ? 'text-[var(--color-mint)] border-[var(--color-mint)]'
              : 'text-gray-400 border-transparent hover:text-white hover:bg-white/5'
          "
        >
          {{ item.name }}
        </a>
      </nav>

      <!-- Нижняя часть с профилем -->
      <div class="mt-auto p-4 card flex items-center gap-3">
        <div
          class="w-10 h-10 rounded-lg bg-[var(--color-bg-elevated)] border border-[var(--color-border)] flex items-center justify-center overflow-hidden"
        >
          <img src="https://ui-avatars.com" alt="AV" />
        </div>
        <div class="overflow-hidden">
          <p class="text-xs font-bold truncate">Алексей К.</p>
          <p class="text-[10px] text-gray-500 uppercase">Главный куратор</p>
        </div>
      </div>
    </aside>

    <!-- ОСНОВНОЙ КОНТЕНТ -->
    <main class="flex-1 flex flex-col">
      <!-- Верхняя панель -->
      <header
        class="h-16 border-b border-[var(--color-border)] flex items-center justify-between px-8"
      >
        <div class="text-gray-500 text-sm italic">Поиск по системе...</div>
        <div class="flex items-center gap-6">
          <div class="flex gap-4 text-gray-400">
            <span class="cursor-pointer hover:text-[var(--color-mint)]">🔔</span>
            <span class="cursor-pointer hover:text-[var(--color-mint)]">⚙️</span>
          </div>
          <div
            class="text-[10px] bg-[var(--color-mint-dim)] text-[var(--color-mint)] px-2 py-1 rounded border border-[var(--color-mint)]/20 font-bold"
          >
            ADMIN СИСТЕМА АКТИВНА
          </div>
        </div>
      </header>

      <!-- Тело страницы -->
      <div class="p-8">
        <div class="mb-10">
          <h1 class="text-3xl font-bold">Обзор платформы</h1>
          <p class="text-gray-400 text-sm mt-1">
            Добро пожаловать обратно, Алексей. Вот текущее состояние системы.
          </p>
        </div>

        <!-- Сетка статистики -->
        <div class="grid grid-cols-4 gap-4 mb-8">
          <div class="card p-5">
            <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">Всего пользователей</p>
            <h2 class="text-2xl font-bold italic">12,840</h2>
          </div>
          <div class="card p-5 relative overflow-hidden">
            <div class="absolute top-0 left-0 w-1 h-full bg-red-500/50"></div>
            <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">
              Активные вакансии <span class="text-red-500 ml-1">-2%</span>
            </p>
            <h2 class="text-2xl font-bold">452</h2>
          </div>
          <div class="card p-5 bg-[var(--color-bg-elevated)] border-[var(--color-mint)]/30">
            <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">
              На проверке
              <span class="bg-red-500 text-white text-[8px] px-1.5 py-0.5 rounded ml-2"
                >СРОЧНО</span
              >
            </p>
            <h2 class="text-2xl font-bold text-[var(--color-mint)]">18</h2>
          </div>
          <div class="card p-5">
            <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">
              Новые отклики <span class="text-[var(--color-mint)] ml-1">+42%</span>
            </p>
            <h2 class="text-2xl font-bold italic">1,204</h2>
          </div>
        </div>

        <!-- Графики и Активность -->
        <div class="grid grid-cols-3 gap-6">
          <div class="col-span-2 card p-6 min-h-[300px] relative">
            <div class="flex justify-between items-center mb-6">
              <h3 class="font-bold">Тренды регистраций</h3>
              <div class="flex gap-2">
                <button
                  class="text-[10px] px-3 py-1 bg-[var(--color-bg-elevated)] border border-[var(--color-border)] rounded hover:border-[var(--color-mint)] transition-colors"
                >
                  Неделя
                </button>
                <button
                  class="text-[10px] px-3 py-1 bg-[var(--color-bg-elevated)] border border-[var(--color-border)] rounded hover:border-[var(--color-mint)] transition-colors"
                >
                  Месяц
                </button>
              </div>
            </div>
            <!-- Заглушка под график -->
            <div class="absolute bottom-10 left-10 right-10 flex items-end justify-between h-32">
              <div
                v-for="i in 7"
                :key="i"
                class="w-8 bg-[var(--color-mint)]/20 rounded-t"
                :style="{ height: Math.random() * 100 + '%' }"
              ></div>
            </div>
          </div>

          <div class="card p-6">
            <h3 class="font-bold mb-6 flex items-center justify-between">
              Последняя активность
              <span class="text-gray-500 text-xs font-normal cursor-pointer hover:text-white"
                >🔄</span
              >
            </h3>
            <div class="space-y-6">
              <div class="flex gap-3 items-start border-l-2 border-[var(--color-mint)] pl-4">
                <div>
                  <p class="text-[11px] text-gray-300">
                    Работодатель <span class="text-[var(--color-mint)]">TechnoStream</span> загрузил
                    документы
                  </p>
                  <span class="text-[9px] text-gray-500">2 МИН. НАЗАД</span>
                </div>
              </div>
              <div class="flex gap-3 items-start border-l-2 border-red-500 pl-4">
                <div>
                  <p class="text-[11px] text-gray-300">
                    Вакансия <span class="text-white">Junior Dev</span> отмечена флагом
                  </p>
                  <span class="text-[9px] text-gray-500">15 МИН. НАЗАД</span>
                </div>
              </div>
            </div>
            <button
              class="w-full mt-8 py-2 text-[10px] font-bold uppercase tracking-widest bg-[var(--color-bg-elevated)] border border-[var(--color-border)] rounded hover:bg-[var(--color-border)] transition-colors"
            >
              Показать всё
            </button>
          </div>
        </div>
      </div>

      <!-- Плавающая кнопка -->
      <button
        class="fixed bottom-8 right-8 w-14 h-14 bg-[var(--color-mint)] text-[var(--color-bg)] rounded-xl text-3xl font-light shadow-[0_0_20px_rgba(0,229,160,0.3)] hover:scale-110 transition-transform active:scale-95"
      >
        +
      </button>
    </main>
  </div>
</template>

<style scoped>
/* Дополнительные стили для имитации UI с картинки */
.card {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 12px;
}
</style>
