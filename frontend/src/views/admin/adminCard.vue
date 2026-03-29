<script setup>
import { ref, computed } from 'vue'

// 1. Состояние навигации
const activeTab = ref('ПОЛЬЗОВАТЕЛИ')
const userType = ref('Соискатели') // Переключатель вверху таблицы

// 2. Данные (имитация из скриншота)
const users = ref([
  {
    id: 88219,
    name: 'Артем Марков',
    email: 'a.markov@it-jump.ru',
    role: 'FRONTEND DEV',
    status: 'Active',
    lastSeen: 'Сегодня, 14:20',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 88215,
    name: 'Елена Кузнецова',
    email: 'kuznetsova.e@gmail.com',
    role: 'UI/UX LEAD',
    status: 'Active',
    lastSeen: 'Вчера, 09:15',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 87301,
    name: 'Иван Петров',
    email: 'i.petrov@spam.ru',
    role: 'JUNIOR QA',
    status: 'Banned',
    lastSeen: '12 Окт. 2023',
    avatar: 'https://i.pravatar.cc',
  },
  {
    id: 88201,
    name: 'Дарья Васильева',
    email: 'darya_v@edu.it',
    role: 'PYTHON JUNIOR',
    status: 'Active',
    lastSeen: '3 часа назад',
    avatar: 'https://i.pravatar.cc',
  },
])

const searchQuery = ref('')

// 3. Поиск (фильтрация)
const filteredUsers = computed(() => {
  return users.value.filter(
    (u) =>
      u.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      u.id.toString().includes(searchQuery.value),
  )
})

// Меню
const menuLinks = [
  { name: 'ГЛАВНАЯ', icon: '■', link: 'adminmain.vue' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', link: 'admidusers.vue' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', link: 'admincompani.vue' },
  { name: 'КАРТОЧКИ', icon: '🗂', link: '#' },
  { name: 'ТЕГИ', icon: '🏷' },
  { name: 'КУРАТОРЫ', icon: '🎧', link: '#' },
]
</script>

<template>
  <div class="flex min-h-screen bg-[#0D1117] text-white font-['Montserrat']">
    <!-- SIDEBAR -->
    <aside class="w-64 border-r border-[#30363D] flex flex-col p-6 shrink-0">
      <div class="mb-10">
        <p class="text-[10px] text-gray-500 font-bold tracking-[0.2em] uppercase">Admin Core</p>
        <h2 class="text-xl font-bold text-blue-500 tracking-tighter italic">CONSOLE</h2>
        <p class="text-[8px] text-gray-600 tracking-[0.4em] uppercase">System Control</p>
      </div>

      <nav class="flex flex-col gap-1">
        <a
          v-for="item in menuLinks"
          :key="item.name"
          href="#"
          @click.prevent="activeTab = item.name"
          :class="[
            'font-bold tracking-widest transition-all',
            activeTab === item.name
              ? 'bg-[#1C2333] text-blue-400 border-l-2 border-blue-500'
              : 'text-gray-500 hover:text-gray-300',
          ]"
        >
          <span class="text-sm opacity-70">{{ item.icon }}</span> {{ item.name }}
        </a>
      </nav>

      <div class="mt-auto pt-6 space-y-6">
        <button
          class="w-full py-3 bg-[#4F46E5] hover:bg-[#4338CA] text-[10px] font-bold rounded-lg transition-colors uppercase tracking-widest shadow-[0_0_15px_rgba(79,70,229,0.3)]"
        >
          Generate Report
        </button>
        <div
          class="text-gray-500 text-[10px] font-bold flex flex-col gap-4 px-2 uppercase tracking-tighter"
        >
          <a href="#" class="hover:text-white flex items-center gap-2">⚙ Settings</a>
          <a href="#" class="hover:text-white flex items-center gap-2">🚪 Logout</a>
        </div>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="flex-1 p-12 overflow-y-auto">
      <!-- Header Area -->
      <div class="flex justify-between items-start mb-12">
        <div>
          <h1 class="text-4xl font-serif mb-2">Пользователи</h1>
          <p class="text-gray-500 text-sm max-w-md leading-relaxed">
            Управление участниками платформы Трамплин: соискатели и представители компаний.
          </p>
        </div>

        <!-- Toggle Switch -->
        <div class="bg-[#161B22] p-1 rounded-xl border border-[#30363D] flex">
          <button
            @click="userType = 'Соискатели'"
            :class="
              userType === 'Соискатели'
                ? 'bg-[#00E5A0] text-black font-bold transition-all'
                : 'text-gray-500 font-bold transition-all'
            "
          >
            Соискатели
          </button>
          <button
            @click="userType = 'Работодатели'"
            :class="
              userType === 'Работодатели'
                ? 'bg-[#00E5A0] text-black font-bold transition-all'
                : 'text-gray-500 font-bold transition-all'
            "
          >
            Работодатели
          </button>
        </div>
      </div>

      <!-- Filters Bar -->
      <div class="flex gap-4 mb-8">
        <div
          class="flex-1 bg-[#161B22] border border-[#30363D] rounded-xl px-5 flex items-center gap-3"
        >
          <span class="text-gray-500 text-sm">🔍</span>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск по имени, email или ID..."
            class="bg-transparent border-none text-xs w-full focus:ring-0 text-gray-300 py-3"
          />
        </div>
        <button
          class="bg-[#161B22] border border-[#30363D] px-6 rounded-xl text-[10px] font-bold tracking-widest flex items-center gap-3"
        >
          <span class="text-blue-500">≡</span> СТАТУС
        </button>
        <button
          class="bg-[#161B22] border border-[#30363D] px-6 rounded-xl text-[10px] font-bold tracking-widest flex items-center gap-3"
        >
          <span class="text-green-500">📅</span> АКТИВНОСТЬ
        </button>
      </div>

      <!-- Table -->
      <div class="mb-10">
        <!-- Labels -->
        <div
          class="grid grid-cols-6 px-8 mb-4 text-[9px] font-black text-gray-600 uppercase tracking-[0.2em]"
        >
          <div class="col-span-1">Пользователь</div>
          <div class="col-span-1">Email</div>
          <div class="col-span-1 text-center">Роль</div>
          <div class="col-span-1 text-center">Статус</div>
          <div class="col-span-1">Последний вход</div>
          <div class="col-span-1 text-right">Действия</div>
        </div>

        <!-- Rows -->
        <div class="space-y-2">
          <div
            v-for="user in filteredUsers"
            :key="user.id"
            class="grid grid-cols-6 items-center bg-[#161B22] border border-[#30363D] hover:bg-[#1C2333] p-5 rounded-2xl transition-all cursor-default group"
          >
            <div class="flex items-center gap-4">
              <img
                :src="user.avatar"
                class="w-11 h-11 rounded-xl bg-gray-800 border border-white/5 shadow-lg"
              />
              <div>
                <div class="text-sm font-bold group-hover:text-blue-400 transition-colors">
                  {{ user.name }}
                </div>
                <div class="text-[9px] text-gray-500 font-mono">ID: {{ user.id }}</div>
              </div>
            </div>

            <div class="text-xs text-gray-400 font-medium">{{ user.email }}</div>

            <div class="text-center">
              <span
                class="text-[8px] font-black bg-[#0D1117] px-2.5 py-1 rounded-md text-gray-500 border border-[#30363D] uppercase tracking-tighter"
              >
                {{ user.role }}
              </span>
            </div>

            <div class="flex items-center justify-center gap-2 text-[10px] font-bold">
              <span
                :class="[
                  'w-1.5 h-1.5 rounded-full',
                  user.status === 'Active'
                    ? 'bg-[#00E5A0] shadow-[0_0_8px_#00E5A0]'
                    : 'bg-red-500 shadow-[0_0_8px_red]',
                ]"
              ></span>
              {{ user.status }}
            </div>

            <div class="text-[10px] text-gray-500 font-medium">{{ user.lastSeen }}</div>

            <div
              class="text-right pr-4 text-gray-600 hover:text-white cursor-pointer transition-colors text-xl"
            >
              ⋮
            </div>
          </div>
        </div>

        <!-- Pagination -->
        <div class="flex justify-between items-center mt-6 px-2">
          <p class="text-[10px] text-gray-600 font-bold uppercase tracking-widest">
            Показано {{ filteredUsers.length }} из 1,240 пользователей
          </p>
          <div class="flex gap-2">
            <button
              class="w-8 h-8 rounded-lg bg-[#161B22] border border-[#30363D] text-xs flex items-center justify-center text-gray-500"
            >
              ‹
            </button>
            <button
              class="w-8 h-8 rounded-lg bg-blue-600 text-xs flex items-center justify-center font-bold"
            >
              1
            </button>
            <button
              class="w-8 h-8 rounded-lg bg-[#161B22] border border-[#30363D] text-xs flex items-center justify-center text-gray-500"
            >
              2
            </button>
            <button
              class="w-8 h-8 rounded-lg bg-[#161B22] border border-[#30363D] text-xs flex items-center justify-center text-gray-500"
            >
              3
            </button>
            <button
              class="w-8 h-8 rounded-lg bg-[#161B22] border border-[#30363D] text-xs flex items-center justify-center text-gray-500"
            >
              ›
            </button>
          </div>
        </div>
      </div>

      <!-- Footer Stats -->
      <div class="grid grid-cols-3 gap-6">
        <div
          class="bg-[#161B22] border border-[#30363D] p-8 rounded-3xl relative overflow-hidden group"
        >
          <div
            class="absolute top-4 right-6 text-gray-800 group-hover:text-blue-500/20 transition-colors text-4xl italic font-serif opacity-10"
          >
            Trend
          </div>
          <p class="text-[9px] text-[#00E5A0] font-black uppercase tracking-[0.2em] mb-3">
            Прирост (30д)
          </p>
          <div class="text-4xl font-bold tracking-tighter">+12.4%</div>
        </div>

        <div class="bg-[#161B22] border border-[#30363D] p-8 rounded-3xl relative overflow-hidden">
          <div
            class="absolute top-6 right-8 w-10 h-10 border-2 border-white/5 rounded-full flex items-center justify-center opacity-20 italic"
          >
            ✓
          </div>
          <p class="text-[9px] text-gray-500 font-black uppercase tracking-[0.2em] mb-3">
            Верифицировано
          </p>
          <div class="text-4xl font-bold tracking-tighter">942</div>
          <p class="text-[9px] text-gray-600 mt-2 font-bold uppercase tracking-tight">
            76% всех соискателей
          </p>
        </div>

        <div
          class="bg-[#161B22] border border-[#30363D] p-8 rounded-3xl bg-gradient-to-br from-[#161B22] to-[#0D1117] relative"
        >
          <div class="absolute top-6 right-8 text-2xl opacity-10">🚀</div>
          <p class="text-[9px] text-gray-500 font-black uppercase tracking-[0.2em] mb-3">
            Нанято через трамплин
          </p>
          <div class="text-4xl font-bold tracking-tighter italic">158</div>
          <p class="text-[9px] text-gray-600 mt-2 font-bold uppercase tracking-tight italic">
            Рекордный показатель месяца
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<style>
/* Шрифты и кастомные скроллы */
::-webkit-scrollbar {
  width: 4px;
}
::-webkit-scrollbar-thumb {
  background: #30363d;
  border-radius: 10px;
}
input::placeholder {
  color: #4b5563;
}
</style>
