<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeTab = ref('')
const userType = ref('Соискатели')
const searchQuery = ref('')

const navItems = [
  { name: 'ГЛАВНАЯ', icon: '🏠', routeName: 'admin-main' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', routeName: 'admin-users' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', routeName: 'admin-main' },
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

const users = ref([
  {
    id: 88219,
    name: 'Артем Марков',
    email: 'a.markov@it-jump.ru',
    role: 'FRONTEND DEV',
    status: 'Active',
    lastSeen: 'Сегодня, 14:20',
    avatar: 'https://i.pravatar.cc/100?u=1',
  },
  {
    id: 88215,
    name: 'Елена Кузнецова',
    email: 'kuznetsova.e@gmail.com',
    role: 'UI/UX LEAD',
    status: 'Active',
    lastSeen: 'Вчера, 09:15',
    avatar: 'https://i.pravatar.cc/100?u=2',
  },
  {
    id: 87301,
    name: 'Иван Петров',
    email: 'i.petrov@spam.ru',
    role: 'JUNIOR QA',
    status: 'Banned',
    lastSeen: '12 Окт, 2023',
    avatar: 'https://i.pravatar.cc/100?u=3',
  },
  {
    id: 88201,
    name: 'Дарья Васильева',
    email: 'darya_v@edu.it',
    role: 'PYTHON JUNIOR',
    status: 'Active',
    lastSeen: '3 часа назад',
    avatar: 'https://i.pravatar.cc/100?u=4',
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
          System
        </p>
        <router-link
          v-for="item in navItems"
          :key="item.name"
          :to="{ name: item.routeName }"
          class="flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-bold transition-all border border-transparent"
          :class="
            activeTab === item.name
              ? 'bg-mint/10 text-mint border-mint/20 shadow-lg'
              : 'text-gray-400 hover:bg-white/5 hover:text-white'
          "
        >
          <span class="text-lg">{{ item.icon }}</span>
          {{ item.name }}
        </router-link>
      </nav>

      <div
        class="mt-auto p-4 bg-[#0d1117] border border-[#30363d] rounded-2xl flex items-center gap-3"
      >
        <div
          class="w-10 h-10 rounded-xl bg-gradient-to-br from-mint to-mint-dark flex items-center justify-center font-bold text-[#0d1117]"
        >
          AK
        </div>
        <div class="min-w-0">
          <p class="text-xs font-black truncate italic uppercase leading-none">Алексей К.</p>
          <p class="text-[9px] text-mint font-bold uppercase mt-1">● Admin Mode</p>
        </div>
      </div>
    </aside>

    <main class="flex-1 flex flex-col h-full overflow-y-auto bg-[#0d1117]">
      <header
        class="h-20 border-b border-[#30363d] bg-[#161b22]/50 backdrop-blur-xl sticky top-0 z-40 flex items-center justify-between px-10 shrink-0"
      >
        <div class="flex items-center gap-6">
          <h1 class="text-2xl font-black italic uppercase tracking-tighter">Пользователи</h1>
          <div class="flex bg-[#0d1117] p-1 rounded-xl border border-[#30363d]">
            <button
              @click="userType = 'Соискатели'"
              :class="userType === 'Соискатели' ? 'bg-mint text-[#0d1117]' : 'text-gray-500'"
              class="px-4 py-1.5 rounded-lg text-[10px] font-black uppercase transition-all"
            >
              Соискатели
            </button>
            <button
              @click="userType = 'Работодатели'"
              :class="userType === 'Работодатели' ? 'bg-mint text-[#0d1117]' : 'text-gray-500'"
              class="px-4 py-1.5 rounded-lg text-[10px] font-black uppercase transition-all"
            >
              Работодатели
            </button>
          </div>
        </div>

        <div
          class="flex items-center gap-4 bg-[#0d1117] px-4 py-2 rounded-xl border border-[#30363d] w-80"
        >
          <span class="text-gray-500">🔍</span>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Поиск по ID или имени..."
            class="bg-transparent border-none text-xs focus:outline-none w-full text-white"
          />
        </div>
      </header>

      <div class="p-8 w-full max-w-[1400px] mx-auto space-y-8">
        <div class="bg-[#161b22] border border-[#30363d] rounded-[2.5rem] overflow-hidden">
          <div
            class="grid grid-cols-6 px-8 py-6 text-[10px] font-black text-gray-500 uppercase tracking-[0.2em] border-b border-[#30363d]"
          >
            <div class="col-span-2">Профиль</div>
            <div>Роль</div>
            <div>Статус</div>
            <div>Активность</div>
            <div class="text-right">Действие</div>
          </div>

          <div class="divide-y divide-[#30363d]">
            <div
              v-for="user in users"
              :key="user.id"
              class="grid grid-cols-6 px-8 py-5 items-center hover:bg-white/[0.02] transition-colors group"
            >
              <div class="col-span-2 flex items-center gap-4">
                <img
                  :src="user.avatar"
                  class="w-10 h-10 rounded-xl object-cover border border-[#30363d]"
                />
                <div class="min-w-0">
                  <p class="text-sm font-bold truncate group-hover:text-mint transition-colors">
                    {{ user.name }}
                  </p>
                  <p class="text-[10px] text-gray-500 font-medium truncate">{{ user.email }}</p>
                </div>
              </div>

              <div>
                <span
                  class="text-[9px] font-black bg-[#0d1117] px-2.5 py-1 rounded-lg border border-[#30363d] text-gray-400 uppercase tracking-tighter"
                >
                  {{ user.role }}
                </span>
              </div>

              <div class="flex items-center gap-2">
                <div
                  :class="user.status === 'Active' ? 'bg-mint' : 'bg-red-500'"
                  class="w-1.5 h-1.5 rounded-full shadow-[0_0_8px_currentColor]"
                ></div>
                <span class="text-[11px] font-bold uppercase tracking-widest text-gray-300">{{
                  user.status
                }}</span>
              </div>

              <div class="text-[11px] font-medium text-gray-500 italic">{{ user.lastSeen }}</div>

              <div class="text-right">
                <button class="text-gray-600 hover:text-white transition-colors text-lg">
                  •••
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-12 gap-6 pb-10">
          <div
            class="col-span-12 md:col-span-4 bg-[#161b22] border border-[#30363d] p-8 rounded-[2.5rem] relative overflow-hidden group"
          >
            <div
              class="absolute top-0 right-0 w-24 h-24 bg-mint blur-[60px] opacity-10 group-hover:opacity-20 transition-opacity"
            ></div>
            <p class="text-[10px] text-gray-500 font-black uppercase tracking-widest mb-2">
              Прирост базы
            </p>
            <div class="text-4xl font-black italic tracking-tighter">+12.4%</div>
          </div>

          <div
            class="col-span-12 md:col-span-4 bg-[#161b22] border border-[#30363d] p-8 rounded-[2.5rem]"
          >
            <p class="text-[10px] text-gray-500 font-black uppercase tracking-widest mb-2">
              Верификация
            </p>
            <div class="text-4xl font-black italic tracking-tighter">942</div>
            <p class="text-[9px] text-mint font-bold mt-2 uppercase tracking-widest">
              76% от всех юзеров
            </p>
          </div>

          <div
            class="col-span-12 md:col-span-4 bg-gradient-to-br from-[#161b22] to-[#1c2333] border border-mint/20 p-8 rounded-[2.5rem]"
          >
            <p class="text-[10px] text-mint font-black uppercase tracking-widest mb-2">
              Трудоустроено
            </p>
            <div class="text-4xl font-black italic tracking-tighter text-mint">158</div>
            <p class="text-[9px] text-gray-500 font-bold mt-2 uppercase tracking-widest italic">
              Рекорд месяца
            </p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
