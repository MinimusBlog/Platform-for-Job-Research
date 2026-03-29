<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const activeTab = ref('')

// Обновленный список навигации с корректными роутами
const navItems = [
  { name: 'ГЛАВНАЯ', icon: '🏠', routeName: 'admin-main' },
  { name: 'ПОЛЬЗОВАТЕЛИ', icon: '👥', routeName: 'admin-users' },
  { name: 'РАБОТОДАТЕЛИ', icon: '💼', routeName: 'admin-company' }, // Ссылка на adminCompany
  { name: 'КАРТОЧКИ', icon: '🗂️', routeName: 'admin-cards' }, // Ссылка на adminCard
]

// Следим за роутом, чтобы подсвечивать нужный пункт в сайдбаре
watch(
  () => route.name,
  (newName) => {
    const currentItem = navItems.find((item) => item.routeName === newName)
    if (currentItem) activeTab.value = currentItem.name
  },
  { immediate: true },
)

const stats = [
  { label: 'Юзеры', value: '12,8K', trend: '+12%', color: 'border-mint' },
  { label: 'Вакансии', value: '452', trend: '-2%', color: 'border-red-500' },
  { label: 'Тикеты', value: '18', trend: 'NEW', color: 'border-yellow-500' },
  { label: 'Отклики', value: '1,2K', trend: '+42%', color: 'border-mint' },
]
</script>

<template>
  <div class="flex h-screen w-full bg-[#0d1117] text-white font-sans overflow-hidden">
    <aside class="w-64 border-r border-[#30363d] bg-[#161b22] flex flex-col p-6 z-50 shrink-0">
      <div class="mb-10 flex items-center gap-3 px-2">
        <div class="w-2 h-7 bg-mint rounded-full shadow-[0_0_15px_rgba(0,229,160,0.5)]"></div>
        <span class="font-black text-xl tracking-tighter text-mint uppercase italic text-nowrap"
          >Трамплин</span
        >
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
          class="flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-bold transition-all border border-transparent group"
          :class="
            activeTab === item.name
              ? 'bg-mint/10 text-mint border-mint/20 shadow-lg'
              : 'text-gray-400 hover:bg-white/5 hover:text-white'
          "
        >
          <span class="text-lg group-hover:scale-110 transition-transform">{{ item.icon }}</span>
          {{ item.name }}
        </router-link>
      </nav>

      <div
        class="mt-auto p-4 bg-[#0d1117] border border-[#30363D] rounded-2xl flex items-center gap-3"
      >
        <div
          class="w-10 h-10 rounded-xl bg-gradient-to-br from-mint to-mint-dark flex items-center justify-center font-bold text-[#0d1117]"
        >
          AK
        </div>
        <div class="min-w-0">
          <p class="text-xs font-black truncate italic uppercase">Алексей К.</p>
          <p class="text-[9px] text-mint font-bold uppercase tracking-tighter animate-pulse">
            ● Admin Mode
          </p>
        </div>
      </div>
    </aside>

    <main class="flex-1 flex flex-col h-full overflow-y-auto bg-[#0d1117] relative">
      <header
        class="h-20 border-b border-[#30363d] bg-[#161b22]/50 backdrop-blur-xl sticky top-0 z-40 flex items-center justify-between px-10"
      >
        <div
          class="flex items-center gap-4 bg-[#0d1117] px-4 py-2.5 rounded-2xl border border-[#30363d] w-96 transition-focus focus-within:border-mint/50 group"
        >
          <span class="text-gray-500">🔍</span>
          <input
            type="text"
            placeholder="Поиск по системе..."
            class="bg-transparent border-none text-xs focus:outline-none w-full text-white placeholder:text-gray-600 font-bold"
          />
        </div>
        <div class="flex items-center gap-3">
          <div class="h-8 w-[1px] bg-[#30363d] mx-2"></div>
          <div
            class="text-[10px] bg-mint/10 text-mint px-3 py-1.5 rounded-xl border border-mint/20 font-black tracking-widest uppercase italic"
          >
            System Online
          </div>
        </div>
      </header>

      <div class="p-8 w-full max-w-[1400px] mx-auto space-y-8">
        <div class="mb-4">
          <h1 class="text-5xl font-black italic tracking-tighter uppercase leading-none">
            Консоль <span class="text-mint text-4xl">Обзора</span>
          </h1>
          <p
            class="text-[10px] text-gray-500 font-black uppercase mt-4 tracking-[0.3em] opacity-60"
          >
            Аналитика платформы в реальном времени
          </p>
        </div>

        <div class="grid grid-cols-12 gap-6">
          <div
            v-for="stat in stats"
            :key="stat.label"
            class="col-span-12 md:col-span-6 xl:col-span-3 bg-[#161b22] border border-[#30363d] p-7 rounded-[2.5rem] hover:border-mint/30 transition-all group relative overflow-hidden"
          >
            <div
              class="absolute -right-4 -top-4 w-16 h-16 bg-mint/5 blur-2xl group-hover:bg-mint/10 transition-all"
            ></div>
            <p
              class="text-[10px] text-gray-500 font-black uppercase tracking-widest mb-2 opacity-50"
            >
              {{ stat.label }}
            </p>
            <div class="flex items-end justify-between relative z-10">
              <h2 class="text-4xl font-black italic tracking-tighter">{{ stat.value }}</h2>
              <span
                class="text-[9px] font-black bg-white/5 px-2 py-1 rounded-lg text-mint border border-mint/10"
                >{{ stat.trend }}</span
              >
            </div>
          </div>

          <div
            class="col-span-12 xl:col-span-8 bg-[#161b22] border border-[#30363d] p-10 rounded-[3rem] min-h-[440px] relative overflow-hidden group"
          >
            <div class="absolute top-0 right-0 w-64 h-64 bg-mint/5 blur-[100px]"></div>
            <div class="flex justify-between items-start mb-12 relative z-10">
              <div>
                <h3 class="font-black italic text-xl uppercase tracking-tighter">
                  Динамика <span class="text-mint">Трафика</span>
                </h3>
                <p class="text-[9px] text-gray-500 font-bold uppercase tracking-widest mt-1">
                  Средняя активность за 24 часа
                </p>
              </div>
              <div class="flex gap-2">
                <div
                  class="w-8 h-8 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-xs"
                >
                  📊
                </div>
              </div>
            </div>

            <div class="flex items-end justify-between h-52 gap-2 relative z-10">
              <div
                v-for="i in 18"
                :key="i"
                class="flex-1 bg-gradient-to-t from-mint/5 to-mint/40 rounded-t-xl hover:to-mint transition-all cursor-pointer relative group/bar"
                :style="{ height: 15 + Math.random() * 85 + '%' }"
              >
                <div
                  class="absolute -top-8 left-1/2 -translate-x-1/2 bg-mint text-[#0d1117] text-[8px] font-black px-1.5 py-0.5 rounded opacity-0 group-hover/bar:opacity-100 transition-opacity"
                >
                  {{ Math.floor(Math.random() * 100) }}%
                </div>
              </div>
            </div>
          </div>

          <div
            class="col-span-12 xl:col-span-4 bg-[#161b22] border border-[#30363d] p-10 rounded-[3rem] flex flex-col relative overflow-hidden"
          >
            <div class="absolute -bottom-10 -right-10 w-32 h-32 bg-mint/5 blur-[50px]"></div>
            <h3 class="font-black italic text-xl uppercase mb-8 relative z-10">
              События <span class="text-mint">Live</span>
            </h3>
            <div class="space-y-6 flex-1 relative z-10">
              <div
                v-for="i in 3"
                :key="i"
                class="border-l-2 border-mint/20 pl-5 py-1 hover:border-mint transition-all cursor-default"
              >
                <p class="text-sm font-black italic uppercase tracking-tighter text-white">
                  Новый отклик
                </p>
                <p class="text-[10px] text-gray-500 font-bold uppercase tracking-tight mt-1">
                  Карточка: Senior Frontend
                </p>
                <span class="text-[9px] text-mint/40 font-black mt-2 block uppercase italic"
                  >2 мин. назад</span
                >
              </div>
            </div>
            <button
              class="mt-8 w-full py-5 bg-[#0d1117] border border-[#30363d] rounded-[1.5rem] text-[10px] font-black uppercase tracking-[0.3em] hover:bg-white/5 active:scale-95 transition-all text-gray-400 hover:text-white"
            >
              Открыть все логи
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Плавный скролл */
::-webkit-scrollbar {
  width: 4px;
}
::-webkit-scrollbar-thumb {
  background: #30363d;
  border-radius: 10px;
}
</style>
