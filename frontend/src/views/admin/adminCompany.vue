<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeTab = ref('')

const navItems = [
  { name: 'ГЛАВНАЯ', icon: '🏠', routeName: 'admin-main' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', routeName: 'admin-users' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', routeName: 'admin-main', badge: 18 },
  { name: 'КАРТОЧКИ', icon: '🗂️', routeName: 'admin-main' },
]

watch(
  () => route.name,
  (newName) => {
    const currentItem = navItems.find((item) => item.routeName === newName)
    if (currentItem) activeTab.value = currentItem.name
  },
  { immediate: true },
)

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
</script>

<template>
  <div class="flex h-screen w-full bg-[#0d1117] text-white font-sans overflow-hidden">
    <aside class="w-64 border-r border-[#30363d] bg-[#161b22] flex flex-col p-6 z-50 shrink-0">
      <div class="mb-10 flex items-center gap-3 px-2">
        <div class="w-2 h-7 bg-mint rounded-full shadow-[0_0_15px_rgba(0,229,160,0.5)]"></div>
        <span class="font-black text-xl tracking-tighter text-mint uppercase italic">Трамплин</span>
      </div>

      <nav class="flex-1 space-y-1">
        <p
          class="text-[10px] text-gray-500 font-bold mb-4 ml-2 tracking-widest uppercase opacity-40"
        >
          Система
        </p>
        <router-link
          v-for="item in navItems"
          :key="item.name"
          :to="{ name: item.routeName }"
          class="flex items-center justify-between px-4 py-3 rounded-2xl text-sm font-bold transition-all border border-transparent group"
          :class="
            activeTab === item.name || item.name === 'РАБОТОДАТЕЛИ'
              ? 'bg-mint/10 text-mint border-mint/20 shadow-lg'
              : 'text-gray-400 hover:bg-white/5 hover:text-white'
          "
        >
          <div class="flex items-center gap-3">
            <span class="text-lg">{{ item.icon }}</span>
            {{ item.name }}
          </div>
          <span
            v-if="item.badge"
            class="bg-mint text-[#0d1117] text-[9px] font-black px-1.5 py-0.5 rounded-md shadow-[0_0_10px_rgba(0,229,160,0.3)]"
          >
            {{ item.badge }}
          </span>
        </router-link>
      </nav>

      <div
        class="mt-auto p-4 bg-[#0d1117] border border-[#30363d] rounded-2xl flex items-center gap-3"
      >
        <div
          class="w-10 h-10 rounded-xl bg-gradient-to-br from-mint to-mint-dark flex items-center justify-center font-bold text-[#0d1117]"
        >
          АК
        </div>
        <div class="min-w-0">
          <p class="text-xs font-black truncate italic uppercase leading-none">Александр К.</p>
          <p class="text-[9px] text-gray-500 font-bold uppercase mt-1">Старший куратор</p>
        </div>
      </div>
    </aside>

    <main class="flex-1 flex flex-col h-full overflow-y-auto bg-[#0d1117]">
      <header
        class="h-20 border-b border-[#30363d] bg-[#161b22]/50 backdrop-blur-xl sticky top-0 z-40 flex items-center justify-between px-10 shrink-0"
      >
        <div
          class="flex items-center gap-4 bg-[#0d1117] px-4 py-2.5 rounded-2xl border border-[#30363d] w-96 transition-focus focus-within:border-mint/50 group"
        >
          <span class="text-gray-500">🔍</span>
          <input
            type="text"
            placeholder="Поиск компаний по ИНН или названию..."
            class="bg-transparent border-none text-xs focus:outline-none w-full text-white"
          />
        </div>
        <div class="flex items-center gap-6">
          <div
            class="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500"
          >
            <span class="w-2 h-2 rounded-full bg-mint"></span> Регион:
            <span class="text-white">Москва</span>
          </div>
          <button
            class="w-10 h-10 flex items-center justify-center rounded-xl bg-white/5 border border-white/10 text-gray-400 hover:text-white transition-all"
          >
            ⚙️
          </button>
        </div>
      </header>

      <div class="p-8 w-full max-w-[1400px] mx-auto space-y-8">
        <div class="flex justify-between items-end">
          <div>
            <h1 class="text-5xl font-black italic tracking-tighter uppercase leading-none">
              Модерация <span class="text-mint text-4xl">Бизнеса</span>
            </h1>
            <p
              class="text-gray-500 font-bold mt-4 tracking-wide uppercase text-[10px] opacity-60 italic"
            >
              Верификация корпоративных аккаунтов
            </p>
          </div>
          <div class="flex gap-4">
            <div
              class="bg-[#161b22] border border-[#30363d] p-5 rounded-[2rem] flex items-center gap-4 min-w-[180px]"
            >
              <div
                class="w-12 h-12 bg-mint/10 rounded-2xl flex items-center justify-center text-mint text-xl shadow-inner italic"
              >
                📥
              </div>
              <div>
                <p class="text-[9px] text-gray-500 font-black uppercase tracking-widest">Ожидают</p>
                <p class="text-2xl font-black italic">18</p>
              </div>
            </div>
            <div
              class="bg-[#161b22] border border-[#30363d] p-5 rounded-[2rem] flex items-center gap-4 min-w-[180px]"
            >
              <div
                class="w-12 h-12 bg-blue-500/10 rounded-2xl flex items-center justify-center text-blue-400 text-xl shadow-inner italic italic"
              >
                ✔
              </div>
              <div>
                <p class="text-[9px] text-gray-500 font-black uppercase tracking-widest">В базе</p>
                <p class="text-2xl font-black italic">1,240</p>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-[#161b22] border border-[#30363d] rounded-[2.5rem] overflow-hidden">
          <div
            class="grid grid-cols-12 px-8 py-6 text-[10px] font-black text-gray-500 uppercase tracking-[0.2em] border-b border-[#30363d] bg-white/[0.01]"
          >
            <div class="col-span-4">Компания</div>
            <div class="col-span-2 text-center">ИНН / Дата</div>
            <div class="col-span-2 text-center">Документы</div>
            <div class="col-span-4 text-right">Статус управления</div>
          </div>

          <div class="divide-y divide-[#30363d]">
            <div
              v-for="emp in employers"
              :key="emp.id"
              class="grid grid-cols-12 px-8 py-5 items-center hover:bg-white/[0.02] transition-colors group"
            >
              <div class="col-span-4 flex items-center gap-4">
                <div
                  class="w-12 h-12 bg-[#0d1117] rounded-2xl border border-[#30363d] flex items-center justify-center text-xl shadow-lg group-hover:border-mint/50 transition-all"
                >
                  🏢
                </div>
                <div class="min-w-0">
                  <p
                    class="text-sm font-black italic truncate group-hover:text-mint transition-all uppercase tracking-tight"
                  >
                    {{ emp.name }}
                  </p>
                  <p class="text-[10px] text-gray-500 font-bold truncate opacity-60">
                    {{ emp.type }}
                  </p>
                </div>
              </div>

              <div class="col-span-2 text-center">
                <p class="text-[11px] font-black italic">{{ emp.inn }}</p>
                <p class="text-[9px] text-gray-600 font-black uppercase mt-1">{{ emp.date }}</p>
              </div>

              <div class="col-span-2 flex justify-center gap-3">
                <span
                  v-if="emp.docs"
                  class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center text-xs hover:bg-mint/10 hover:text-mint cursor-pointer transition-all border border-transparent hover:border-mint/20"
                  >📄</span
                >
                <span v-else class="text-[9px] text-gray-700 font-black uppercase italic"
                  >Пусто</span
                >
              </div>

              <div class="col-span-4 flex justify-end gap-2">
                <button
                  class="px-4 py-2.5 bg-white/5 border border-[#30363d] rounded-xl text-[9px] font-black uppercase tracking-widest hover:bg-white/10 active:scale-95 transition-all"
                >
                  Инфо
                </button>
                <button
                  class="px-4 py-2.5 bg-red-500/10 border border-red-500/20 text-red-400 rounded-xl text-[9px] font-black uppercase tracking-widest hover:bg-red-500/20 active:scale-95 transition-all"
                >
                  Отказ
                </button>
                <button
                  class="px-4 py-2.5 bg-mint text-[#0d1117] rounded-xl text-[9px] font-black uppercase tracking-widest hover:brightness-110 active:scale-95 transition-all shadow-[0_5px_15px_rgba(0,229,160,0.2)]"
                >
                  Верифицировать
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-12 gap-6 pb-10">
          <div
            class="col-span-12 lg:col-span-8 bg-gradient-to-br from-[#161b22] to-[#1c2333] border border-blue-500/20 p-10 rounded-[3rem] relative overflow-hidden group"
          >
            <div
              class="absolute -top-24 -right-24 w-64 h-64 bg-blue-500 blur-[120px] opacity-10 group-hover:opacity-20 transition-opacity"
            ></div>
            <div class="flex items-center gap-4 mb-8">
              <div
                class="w-10 h-10 bg-blue-500/20 rounded-xl flex items-center justify-center text-blue-400 shadow-[0_0_15px_rgba(59,130,246,0.3)] italic"
              >
                ✨
              </div>
              <h3 class="text-xl font-black italic uppercase tracking-tighter">
                AI Рекомендации <span class="text-blue-400">Jump.AI</span>
              </h3>
            </div>
            <p class="text-sm text-gray-400 font-medium leading-relaxed mb-10 max-w-2xl">
              Система проанализировала государственные реестры:
              <span class="text-white italic font-bold">CyberSphere Solutions</span> имеет
              действующие госконтракты. Риск фрода:
              <span class="text-mint font-black tracking-widest">НИЗКИЙ (1.2%)</span>. Рекомендуется
              автоматическое подтверждение.
            </p>
            <div class="flex gap-12">
              <div>
                <p class="text-[9px] text-gray-500 font-black uppercase tracking-[0.3em] mb-2">
                  Точность предикта
                </p>
                <p class="text-3xl font-black italic tracking-tighter text-blue-400">98.4%</p>
              </div>
              <div class="h-12 w-[1px] bg-white/10 self-end mb-1"></div>
              <div>
                <p class="text-[9px] text-gray-500 font-black uppercase tracking-[0.3em] mb-2">
                  Флаги риска
                </p>
                <p class="text-3xl font-black italic tracking-tighter text-red-500">0</p>
              </div>
            </div>
          </div>

          <div
            class="col-span-12 lg:col-span-4 bg-[#161b22] border border-[#30363d] p-10 rounded-[3rem] flex flex-col items-center justify-center text-center group"
          >
            <div
              class="relative w-40 h-40 mb-8 transition-transform group-hover:scale-105 duration-500"
            >
              <svg class="w-full h-full transform -rotate-90">
                <circle
                  cx="80"
                  cy="80"
                  r="75"
                  stroke="#0d1117"
                  stroke-width="10"
                  fill="transparent"
                />
                <circle
                  cx="80"
                  cy="80"
                  r="75"
                  stroke="currentColor"
                  stroke-width="10"
                  fill="transparent"
                  stroke-dasharray="471"
                  stroke-dashoffset="120"
                  class="text-mint shadow-[0_0_20px_#00e5a0]"
                />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center">
                <span class="text-3xl font-black italic tracking-tighter leading-none">14м</span>
                <span class="text-[8px] text-gray-500 font-black uppercase tracking-[0.2em] mt-1"
                  >avg speed</span
                >
              </div>
            </div>
            <h4 class="text-xs font-black uppercase tracking-widest italic mb-1">
              Скорость обработки
            </h4>
            <p class="text-[9px] text-gray-600 font-bold uppercase tracking-tighter">
              Эффективность модераторов сегодня
            </p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
button,
.group {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
