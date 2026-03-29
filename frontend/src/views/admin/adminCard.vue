<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeTab = ref('')
const cardType = ref('Активные')
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

// Данные карточек (Вакансии/Проекты)
const cards = ref([
  {
    id: 102,
    title: 'Senior Frontend Developer',
    company: 'CyberSphere',
    category: 'Разработка',
    views: '1.2K',
    status: 'Active',
    date: '12.10',
  },
  {
    id: 105,
    title: 'UI/UX Designer (Fintech)',
    company: 'Трамплин ИТ',
    category: 'Дизайн',
    views: '840',
    status: 'Active',
    date: '11.10',
  },
  {
    id: 108,
    title: 'Data Scientist',
    company: 'DataFlow',
    category: 'Аналитика',
    views: '2.1K',
    status: 'Archived',
    date: '05.10',
  },
  {
    id: 110,
    title: 'Project Manager',
    company: 'Иннотех',
    category: 'Менеджмент',
    views: '450',
    status: 'Active',
    date: '01.10',
  },
])

const filteredCards = computed(() => {
  return cards.value.filter(
    (c) =>
      c.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      c.company.toLowerCase().includes(searchQuery.value.toLowerCase()),
  )
})
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
          Управление
        </p>
        <router-link
          v-for="item in navItems"
          :key="item.name"
          :to="{ name: item.routeName }"
          class="flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-bold transition-all border border-transparent"
          :class="
            activeTab === item.name || item.name === 'КАРТОЧКИ'
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
          <p class="text-[9px] text-mint font-bold uppercase mt-1 tracking-tighter">
            ● Контент-менеджер
          </p>
        </div>
      </div>
    </aside>

    <main class="flex-1 flex flex-col h-full overflow-y-auto bg-[#0d1117]">
      <header
        class="h-20 border-b border-[#30363d] bg-[#161b22]/50 backdrop-blur-xl sticky top-0 z-40 flex items-center justify-between px-10 shrink-0"
      >
        <div class="flex items-center gap-6">
          <h1 class="text-2xl font-black italic uppercase tracking-tighter text-nowrap">
            Управление <span class="text-mint text-xl">Карточками</span>
          </h1>
          <div class="flex bg-[#0d1117] p-1 rounded-xl border border-[#30363d]">
            <button
              @click="cardType = 'Активные'"
              :class="cardType === 'Активные' ? 'bg-mint text-[#0d1117]' : 'text-gray-500'"
              class="px-4 py-1.5 rounded-lg text-[10px] font-black uppercase transition-all"
            >
              Активные
            </button>
            <button
              @click="cardType = 'Архив'"
              :class="cardType === 'Архив' ? 'bg-mint text-[#0d1117]' : 'text-gray-500'"
              class="px-4 py-1.5 rounded-lg text-[10px] font-black uppercase transition-all"
            >
              Архив
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
            placeholder="Поиск вакансий..."
            class="bg-transparent border-none text-xs focus:outline-none w-full text-white font-bold"
          />
        </div>
      </header>

      <div class="p-8 w-full max-w-[1400px] mx-auto space-y-8">
        <div class="grid grid-cols-12 gap-6">
          <div
            class="col-span-12 lg:col-span-3 bg-[#161b22] border border-[#30363d] p-8 rounded-[2.5rem] flex flex-col justify-between group"
          >
            <div>
              <p class="text-[10px] text-gray-500 font-black uppercase tracking-widest mb-2">
                Всего карточек
              </p>
              <h3 class="text-5xl font-black italic tracking-tighter">2,481</h3>
            </div>
            <button
              class="mt-8 w-full py-4 bg-mint text-[#0d1117] rounded-2xl text-[10px] font-black uppercase tracking-widest hover:brightness-110 transition-all shadow-[0_10px_20px_rgba(0,229,160,0.1)]"
            >
              + Создать карту
            </button>
          </div>

          <div
            class="col-span-12 lg:col-span-9 bg-[#161b22] border border-[#30363d] rounded-[2.5rem] overflow-hidden"
          >
            <div
              class="grid grid-cols-5 px-8 py-5 text-[9px] font-black text-gray-500 uppercase tracking-widest border-b border-[#30363d] bg-white/[0.01]"
            >
              <div class="col-span-2">Название и компания</div>
              <div class="text-center">Категория</div>
              <div class="text-center">Просмотры</div>
              <div class="text-right">Статус</div>
            </div>

            <div class="divide-y divide-[#30363d]">
              <div
                v-for="card in filteredCards"
                :key="card.id"
                class="grid grid-cols-5 px-8 py-5 items-center hover:bg-white/[0.02] transition-all group"
              >
                <div class="col-span-2">
                  <p
                    class="text-sm font-black italic tracking-tight group-hover:text-mint transition-colors"
                  >
                    {{ card.title }}
                  </p>
                  <p class="text-[10px] text-gray-500 font-bold uppercase tracking-tighter">
                    {{ card.company }}
                  </p>
                </div>
                <div class="text-center">
                  <span
                    class="text-[9px] font-black px-2 py-1 rounded-lg border border-[#30363d] bg-[#0d1117] text-gray-400 uppercase"
                    >{{ card.category }}</span
                  >
                </div>
                <div class="text-center">
                  <p class="text-xs font-black italic">{{ card.views }}</p>
                  <p class="text-[8px] text-gray-600 font-bold uppercase tracking-tighter">
                    unique
                  </p>
                </div>
                <div class="flex justify-end items-center gap-3">
                  <div
                    :class="
                      card.status === 'Active' ? 'bg-mint shadow-[0_0_10px_#00e5a0]' : 'bg-gray-600'
                    "
                    class="w-1.5 h-1.5 rounded-full"
                  ></div>
                  <button class="text-gray-500 hover:text-white transition-colors">⚙️</button>
                </div>
              </div>
            </div>
          </div>

          <div
            class="col-span-12 md:col-span-6 lg:col-span-4 bg-[#161b22] border border-[#30363d] p-8 rounded-[2.5rem] relative overflow-hidden group"
          >
            <div
              class="absolute -bottom-10 -left-10 w-32 h-32 bg-mint blur-[80px] opacity-10 group-hover:opacity-20 transition-opacity"
            ></div>
            <p class="text-[10px] text-gray-500 font-black uppercase tracking-widest mb-4">
              Популярные теги
            </p>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="tag in ['Python', 'Vue.js', 'Remote', 'Middle', 'SQL', 'Fintech']"
                :key="tag"
                class="px-3 py-1.5 bg-[#0d1117] border border-[#30363d] rounded-xl text-[10px] font-black text-mint uppercase italic tracking-tighter"
                >#{{ tag }}</span
              >
            </div>
          </div>

          <div
            class="col-span-12 md:col-span-6 lg:col-span-8 bg-gradient-to-br from-[#161b22] to-[#1c2333] border border-mint/10 p-8 rounded-[2.5rem] flex items-center justify-between"
          >
            <div class="max-w-md">
              <h4 class="text-xl font-black italic uppercase tracking-tighter mb-2 text-mint">
                Авто-оптимизация
              </h4>
              <p class="text-xs text-gray-400 font-bold leading-relaxed uppercase tracking-tight">
                Система Трамплин.AI автоматически поднимает карточки с низким охватом, если они
                соответствуют профилям активных соискателей.
              </p>
            </div>
            <div class="text-right">
              <p class="text-4xl font-black italic text-white tracking-tighter">84%</p>
              <p class="text-[9px] text-gray-500 font-black uppercase tracking-widest mt-1">
                Efficiency rate
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
