<template>
  <div
    class="dashboard min-h-screen bg-[#050505] text-white flex flex-col font-sans selection:bg-mint selection:text-bg"
  >
    <!-- Фоновое свечение -->
    <div
      class="fixed inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(0,229,160,0.02),_transparent_50%)] pointer-events-none"
    ></div>

    <!-- Шапка из скриншота -->
    <header
      class="relative z-10 flex items-center justify-between px-10 py-5 border-b border-white/5 bg-black/40 backdrop-blur-xl"
    >
      <div class="flex items-center gap-12">
        <div class="logo text-lg font-black tracking-[-0.05em] text-mint uppercase">ТРАМПЛИН</div>
        <nav class="flex gap-8 text-[10px] font-bold uppercase tracking-[0.25em] text-gray-500">
          <a href="#" class="hover:text-white transition-colors">Компания</a>
          <a href="#" class="hover:text-white transition-colors">Возможности</a>
          <a href="#" class="text-mint border-b border-mint pb-1">Отклики</a>
          <a href="#" class="hover:text-white transition-colors">Аналитика</a>
        </nav>
      </div>
      <div class="flex items-center gap-6 text-gray-500">
        <button class="hover:text-mint transition-colors text-lg">🔔</button>
        <button class="text-mint text-lg">🛡️</button>
        <button class="hover:text-mint transition-colors text-lg">⚙️</button>
        <div
          class="w-9 h-9 rounded-xl bg-bg-card border border-border flex items-center justify-center text-[10px] font-black text-white/80"
        >
          HR
        </div>
      </div>
    </header>

    <main class="relative z-10 max-w-7xl mx-auto w-full p-12 flex-1">
      <!-- Заголовок и Action Buttons -->
      <div class="flex justify-between items-end mb-12">
        <div class="space-y-3">
          <p class="text-[9px] uppercase tracking-[0.5em] text-gray-500 font-black">
            MANAGEMENT HUB
          </p>
          <h1 class="text-6xl font-serif italic tracking-tight text-white leading-none">Отклики</h1>
        </div>
        <div class="flex gap-3">
          <button
            class="btn-outline flex items-center gap-2 py-2.5 px-6 text-[11px] uppercase tracking-widest border-white/10 hover:bg-white/5"
          >
            <span class="text-lg">📥</span> Экспорт
          </button>
          <button
            class="btn-primary py-2.5 px-8 text-[11px] uppercase tracking-widest shadow-[0_0_25px_rgba(0,229,160,0.15)]"
          >
            Опубликовать вакансию
          </button>
        </div>
      </div>

      <!-- Фильтры (Glass Style) -->
      <div class="grid grid-cols-12 gap-4 mb-10">
        <div v-for="filter in ['Вакансия', 'Статус', 'Период']" :key="filter" class="col-span-2">
          <label
            class="text-[9px] uppercase text-gray-500 block mb-2.5 tracking-[0.2em] font-black"
            >{{ filter }}</label
          >
          <div class="relative group">
            <select
              v-if="filter !== 'Период'"
              class="w-full bg-white/[0.03] border border-white/5 rounded-xl p-3.5 text-xs font-bold appearance-none focus:border-mint/50 outline-none transition-all cursor-pointer"
            >
              <option>{{ filter === 'Вакансия' ? 'Все вакансии' : 'Любой статус' }}</option>
            </select>
            <div
              v-else
              class="w-full bg-white/[0.03] border border-white/5 rounded-xl p-3.5 text-xs font-bold flex items-center gap-3 cursor-pointer hover:border-mint/30 transition-all"
            >
              <span class="text-mint">📅</span> Последние 30 дней
            </div>
            <span
              v-if="filter !== 'Период'"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-[10px] text-gray-500 pointer-events-none group-hover:text-mint transition-colors"
              >▼</span
            >
          </div>
        </div>
        <div class="col-span-6 flex flex-col justify-end">
          <div class="relative group">
            <span
              class="absolute left-5 top-1/2 -translate-y-1/2 text-gray-500 group-focus-within:text-mint transition-colors"
              >🔍</span
            >
            <input
              type="text"
              placeholder="Поиск кандидата по имени или роли..."
              class="w-full bg-white/[0.03] border border-white/5 rounded-xl py-3.5 pl-14 pr-4 text-xs font-bold focus:border-mint/50 outline-none transition-all placeholder:text-gray-600"
            />
          </div>
        </div>
      </div>

      <!-- Контейнер таблицы -->
      <div
        class="bg-white/[0.01] border border-white/5 rounded-[2rem] overflow-hidden backdrop-blur-sm"
      >
        <table class="w-full text-left border-collapse">
          <thead class="bg-white/[0.02] border-b border-white/5">
            <tr>
              <th class="p-6 text-[10px] uppercase tracking-[0.2em] text-gray-500 font-black">
                Кандидат
              </th>
              <th class="p-6 text-[10px] uppercase tracking-[0.2em] text-gray-500 font-black">
                Дата отклика
              </th>
              <th class="p-6 text-[10px] uppercase tracking-[0.2em] text-gray-500 font-black">
                Статус
              </th>
              <th
                class="p-6 text-right text-[10px] uppercase tracking-[0.2em] text-gray-500 font-black"
              >
                Действия
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5">
            <tr
              v-for="app in applications"
              :key="app.id"
              class="hover:bg-white/[0.02] transition-all duration-300 group"
            >
              <td class="p-6">
                <div class="flex items-center gap-5">
                  <div
                    class="w-12 h-12 rounded-2xl bg-gradient-to-br from-gray-800 to-gray-900 border border-white/10 p-[1px] group-hover:border-mint/30 transition-all"
                  >
                    <img
                      :src="app.avatar"
                      alt=""
                      class="w-full h-full object-cover rounded-2xl grayscale group-hover:grayscale-0 transition-all duration-500"
                    />
                  </div>
                  <div>
                    <div class="text-sm font-bold group-hover:text-mint transition-colors">
                      {{ app.name }}
                    </div>
                    <div
                      class="text-[10px] text-gray-500 uppercase tracking-widest mt-0.5 font-bold"
                    >
                      {{ app.role }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="p-6">
                <span
                  class="text-xs font-mono text-gray-400 group-hover:text-gray-200 transition-colors"
                  >{{ app.date }}</span
                >
              </td>
              <td class="p-6">
                <div class="relative inline-block dropdown">
                  <button
                    :class="statusClasses[app.status]"
                    class="flex items-center gap-3 px-4 py-2 rounded-full text-[9px] font-black uppercase tracking-[0.15em] border transition-all hover:scale-105"
                  >
                    <span
                      class="w-1.5 h-1.5 rounded-full bg-current shadow-[0_0_8px_currentColor]"
                    ></span>
                    {{ app.statusLabel }}
                    <span class="ml-1 opacity-40">▼</span>
                  </button>
                </div>
              </td>
              <td class="p-6 text-right">
                <button
                  class="inline-flex items-center justify-center w-10 h-10 rounded-xl border border-white/5 bg-white/5 text-gray-500 hover:text-mint hover:border-mint/30 hover:scale-110 transition-all active:scale-95"
                >
                  <svg
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2.5"
                  >
                    <path
                      d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Пагинация в стиле "Linear" -->
        <div class="p-8 flex justify-between items-center bg-white/[0.01]">
          <span class="text-[10px] text-gray-600 font-black uppercase tracking-[0.2em]"
            >Показано 4 из 128 откликов</span
          >
          <div class="flex gap-2">
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl border border-white/5 text-gray-500 hover:border-mint hover:text-mint transition-all"
            >
              ‹
            </button>
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl bg-mint text-bg font-black text-xs shadow-[0_0_20px_rgba(0,229,160,0.2)]"
            >
              1
            </button>
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl border border-white/5 text-gray-400 text-xs font-bold hover:text-white hover:bg-white/5 transition-all"
            >
              2
            </button>
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl border border-white/5 text-gray-400 text-xs font-bold hover:text-white hover:bg-white/5 transition-all"
            >
              3
            </button>
            <button
              class="w-10 h-10 flex items-center justify-center rounded-xl border border-white/5 text-gray-500 hover:border-mint hover:text-mint transition-all"
            >
              ›
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- Твой премиальный футер -->
    <footer
      class="p-10 border-t border-white/5 flex justify-between items-center opacity-40 hover:opacity-100 transition-all duration-700"
    >
      <div class="space-y-2">
        <div class="text-[11px] font-black tracking-[0.4em] text-mint uppercase">ТРАМПЛИН</div>
        <div class="text-[9px] font-bold text-gray-500 tracking-[0.1em] uppercase italic">
          © 2024 High-Velocity Sophistication.
        </div>
      </div>
      <div class="flex gap-10 text-[9px] font-black uppercase tracking-[0.3em] text-gray-500">
        <a href="#" class="hover:text-mint transition-colors">Privacy</a>
        <a href="#" class="hover:text-mint transition-colors">Terms</a>
        <a href="#" class="hover:text-mint transition-colors">Support</a>
        <a href="#" class="hover:text-mint transition-colors">API</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
const applications = [
  {
    id: 1,
    name: 'Alex Kovalev',
    role: 'Frontend Developer',
    date: 'Oct 24, 2023',
    status: 'pending',
    statusLabel: 'На рассмотрении',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 2,
    name: 'Maria Petrova',
    role: 'UX/UI Designer',
    date: 'Oct 22, 2023',
    status: 'pending',
    statusLabel: 'На рассмотрении',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 3,
    name: 'Dmitry Sokolov',
    role: 'Backend Engineer',
    date: 'Oct 20, 2023',
    status: 'rejected',
    statusLabel: 'Отклонён',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 4,
    name: 'Elena Vlasova',
    role: 'QA Engineer',
    date: 'Oct 19, 2023',
    status: 'reserve',
    statusLabel: 'В резерве',
    avatar: 'https://i.pravatar.cc',
  },
]

const statusClasses = {
  pending: 'bg-yellow-500/5 text-yellow-500 border-yellow-500/10',
  accepted: 'bg-mint/5 text-mint border-mint/10',
  rejected: 'bg-red-500/5 text-red-500 border-red-500/10',
  reserve: 'bg-purple-500/5 text-purple-500 border-purple-500/10',
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com');

.font-serif {
  font-family: 'Playfair Display', serif;
}

/* Эффект свечения при наведении на строку */
tr:hover td:first-child {
  box-shadow: inset 4px 0 0 -2px var(--color-mint);
}

/* Стилизация скроллбара внутри таблицы */
.overflow-hidden::-webkit-scrollbar {
  width: 4px;
}
</style>
