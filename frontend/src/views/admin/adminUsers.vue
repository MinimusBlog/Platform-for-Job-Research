<script setup>
import { ref } from 'vue'

const activeTab = ref('ПОЛЬЗОВАТЕЛИ')
const userType = ref('Соискатели') // Переключатель вверху

// Данные пользователей (имитация базы данных)
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
    lastSeen: '12 Окт, 2023',
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

// Навигация (теперь с реальными названиями из твоего скрина)
const menuItems = [
  { name: 'ГЛАВНАЯ', icon: '🏠', link: 'adminmain.vue' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', link: '#' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', link: 'admincompani.vue' },
  { name: 'КАРТОЧКИ', icon: '🗂️', link: 'admincard.vue' },
  { name: 'ТЕГИ', icon: '🏷️', link: '#' },
  { name: 'КУРАТОРЫ', icon: '🎧', link: '#' },
]
</script>

<template>
  <div class="flex min-h-screen bg-[#0D1117] text-white font-['Montserrat']">
    <!-- SIDEBAR -->
    <aside class="w-64 border-r border-[#30363D] flex flex-col p-6 shrink-0">
      <div class="mb-10">
        <div class="text-[10px] text-gray-500 font-bold tracking-widest uppercase">Admin Core</div>
        <div class="text-xl font-bold text-blue-500 tracking-tighter">CONSOLE</div>
        <div class="text-[8px] text-gray-600 tracking-[0.3em] uppercase">System Control</div>
      </div>

      <nav class="flex flex-col gap-1">
        <a
          v-for="item in menuItems"
          :key="item.name"
          :href="item.link"
          @click="activeTab = item.name"
          :class="[
            'font-bold tracking-widest transition-all',
            activeTab === item.name
              ? 'bg-[#1C2333] text-blue-400 border-l-2 border-blue-500'
              : 'text-gray-500 hover:text-gray-300',
          ]"
        >
          <span>{{ item.icon }}</span> {{ item.name }}
        </a>
      </nav>

      <div class="mt-auto space-y-4">
        <button
          class="w-full py-3 bg-blue-600 hover:bg-blue-500 text-[10px] font-bold rounded-lg transition-colors uppercase tracking-widest"
        >
          Generate Report
        </button>
        <div class="text-gray-500 text-[10px] flex flex-col gap-3 px-4">
          <a href="#" class="hover:text-white">⚙️ SETTINGS</a>
          <a href="#" class="hover:text-white">🔓 LOGOUT</a>
        </div>
      </div>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="flex-1 p-10 overflow-y-auto">
      <!-- Header Section -->
      <div class="flex justify-between items-end mb-10">
        <div>
          <h1 class="text-4xl font-serif mb-2 text-gray-100">Пользователи</h1>
          <p class="text-gray-500 text-sm max-w-md">
            Управление участниками платформы Трамплин: соискатели и представители компаний.
          </p>
        </div>
        <!-- Свитчер как на скрине -->
        <div class="flex bg-[#161B22] p-1 rounded-xl border border-[#30363D]">
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
          class="flex-1 bg-[#161B22] border border-[#30363D] rounded-xl px-4 flex items-center gap-3"
        >
          <span class="text-gray-500">🔍</span>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск по имени, email или ID..."
            class="bg-transparent border-none text-sm w-full focus:ring-0 text-gray-300 py-3"
          />
        </div>
        <button
          class="bg-[#161B22] border border-[#30363D] px-5 rounded-xl text-xs font-bold flex items-center gap-2"
        >
          <span class="text-blue-500">≡</span> СТАТУС
        </button>
        <button
          class="bg-[#161B22] border border-[#30363D] px-5 rounded-xl text-xs font-bold flex items-center gap-2"
        >
          <span class="text-green-500">📅</span> АКТИВНОСТЬ
        </button>
      </div>

      <!-- Table Header -->
      <div
        class="grid grid-cols-6 px-6 mb-4 text-[10px] font-bold text-gray-600 uppercase tracking-widest"
      >
        <div class="col-span-1">Пользователь</div>
        <div class="col-span-1 pl-4">Email</div>
        <div class="col-span-1">Роль</div>
        <div class="col-span-1">Статус</div>
        <div class="col-span-1">Последний вход</div>
        <div class="col-span-1 text-right">Действия</div>
      </div>

      <!-- Table Rows -->
      <div class="space-y-3 mb-10">
        <div
          v-for="user in users"
          :key="user.id"
          class="grid grid-cols-6 items-center bg-[#161B22] border border-[#30363D] hover:border-gray-600 p-4 rounded-2xl transition-all group"
        >
          <div class="flex items-center gap-3">
            <img :src="user.avatar" class="w-10 h-10 rounded-lg bg-gray-800" />
            <div>
              <div class="text-sm font-bold">{{ user.name }}</div>
              <div class="text-[10px] text-gray-500 uppercase">ID: {{ user.id }}</div>
            </div>
          </div>

          <div class="text-xs text-gray-400 pl-4">{{ user.email }}</div>

          <div>
            <span
              class="text-[9px] font-bold bg-[#1C2333] px-2 py-1 rounded text-gray-400 border border-[#30363D]"
              >{{ user.role }}</span
            >
          </div>

          <div class="flex items-center gap-2 text-[11px]">
            <span
              :class="[
                'w-2 h-2 rounded-full',
                user.status === 'Active' ? 'bg-green-500 shadow-[0_0_8px_#10b981]' : 'bg-red-500',
              ]"
            ></span>
            {{ user.status }}
          </div>

          <div class="text-[11px] text-gray-500">{{ user.lastSeen }}</div>

          <div
            class="text-right text-gray-600 group-hover:text-white cursor-pointer transition-colors px-2"
          >
            ⋮
          </div>
        </div>
      </div>

      <!-- Bottom Stats Cards -->
      <div class="grid grid-cols-3 gap-6">
        <div class="bg-[#161B22] border border-[#30363D] p-6 rounded-2xl relative overflow-hidden">
          <p class="text-[10px] text-green-500 font-bold uppercase mb-2">Прирост (30д)</p>
          <div class="text-3xl font-bold">+12.4%</div>
          <div class="absolute bottom-4 right-6 text-2xl opacity-20">📈</div>
        </div>
        <div class="bg-[#161B22] border border-[#30363D] p-6 rounded-2xl">
          <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">Верифицировано</p>
          <div class="text-3xl font-bold">942</div>
          <p class="text-[10px] text-gray-600 mt-1">76% всех соискателей</p>
        </div>
        <div
          class="bg-[#161B22] border border-[#30363D] p-6 rounded-2xl bg-gradient-to-br from-[#161B22] to-[#1c2333]"
        >
          <p class="text-[10px] text-gray-500 font-bold uppercase mb-2">Нанято через трамплин</p>
          <div class="text-3xl font-bold italic">158</div>
          <p class="text-[10px] text-gray-600 mt-1">Рекордный показатель месяца</p>
        </div>
      </div>
    </main>
  </div>
</template>

<style>
/* Используем твои переменные, если они доступны в main.css */
input:focus {
  outline: none;
}
</style>
