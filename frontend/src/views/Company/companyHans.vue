<template>
  <div
    class="dashboard min-h-screen bg-bg text-white font-sans selection:bg-mint selection:text-bg"
  >
    <!-- Тонкий фоновый градиент для глубины, не меняя основной фон -->
    <div
      class="fixed inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(0,229,160,0.03),_transparent_40%)] pointer-events-none"
    ></div>

    <header
      class="relative z-10 flex items-center justify-between px-10 py-6 border-b border-border bg-bg-card/50 backdrop-blur-md"
    >
      <div class="flex items-center gap-16">
        <div class="logo text-xl font-bold tracking-tighter text-mint uppercase">ТРАМПЛИН</div>
        <nav class="flex gap-10 text-[10px] font-bold uppercase tracking-[0.2em] text-gray-400">
          <router-link :to="{ name: 'company-profile' }" class="hover:text-white transition-all"
            >Компания</router-link
          >
          <router-link
            :to="{ name: 'company-opportunities' }"
            class="text-mint border-b border-mint pb-1"
            >Возможности</router-link
          >
          <router-link :to="{ name: 'company-responses' }" class="hover:text-white transition-all"
            >Отклики</router-link
          >
          <a href="#" class="hover:text-white transition-all">Аналитика</a>
        </nav>
      </div>
      <div class="flex items-center gap-6">
        <div class="flex items-center bg-white/5 border border-border rounded-full px-4 py-1.5">
          <span class="text-[10px] font-bold text-mint mr-2">●</span>
          <span class="text-[10px] font-bold uppercase tracking-wider">Работодатель</span>
        </div>
        <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-mint to-mint-dark p-[1px]">
          <div
            class="w-full h-full rounded-full bg-bg flex items-center justify-center text-xs font-bold"
          >
            HR
          </div>
        </div>
      </div>
    </header>

    <main class="relative z-10 max-w-[1400px] mx-auto p-12">
      <!-- Заголовок в стиле твоего скрина -->
      <div class="flex justify-between items-end mb-16">
        <div class="space-y-2">
          <div class="flex items-center gap-3">
            <span class="h-[1px] w-8 bg-mint"></span>
            <p class="text-[10px] uppercase tracking-[0.5em] text-gray-500 font-bold">
              MANAGEMENT HUB
            </p>
          </div>
          <h1 class="text-6xl font-serif italic tracking-tight text-white">Возможности</h1>
        </div>
        <a href="companicreate.vue" class="block">
          <button
            class="btn-primary group relative px-8 py-4 rounded-full overflow-hidden transition-all hover:scale-105 active:scale-95 shadow-[0_0_30px_rgba(0,229,160,0.1)]"
          >
            <span class="relative z-10 flex items-center gap-2 uppercase text-xs tracking-widest">
              Создать позицию <span class="text-xl leading-none">+</span>
            </span>
          </button>
        </a>
      </div>

      <!-- Сетка карточек -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Карточка вакансии -->
        <div
          v-for="job in jobs"
          :key="job.id"
          class="card group border-border/40 p-8 transition-all duration-500 hover:border-mint/30 hover:shadow-[0_0_40px_rgba(0,0,0,0.3)] cursor-pointer relative overflow-hidden"
        >
          <!-- Легкий блик при наведении -->
          <div
            class="absolute inset-0 bg-gradient-to-br from-mint/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"
          ></div>

          <div class="relative z-10">
            <div class="flex justify-between items-start mb-10">
              <div
                class="px-4 py-1.5 rounded-md bg-mint-dim border border-mint/10 text-[9px] font-black uppercase tracking-[0.2em] text-mint"
              >
                {{ job.category }}
              </div>
              <div class="text-gray-600 group-hover:text-white transition-colors">
                <span class="text-xl">↗</span>
              </div>
            </div>

            <h2
              class="text-2xl font-bold mb-2 leading-tight group-hover:text-mint transition-colors duration-300"
            >
              {{ job.title }}
            </h2>
            <p class="text-gray-500 text-sm mb-10 font-medium tracking-wide">
              Москва, Гибрид • Full-time
            </p>

            <!-- Статистика с полосками прогресса -->
            <div class="space-y-6 mb-10">
              <div
                v-for="(val, label) in { Отклики: job.responses, Просмотры: job.views }"
                :key="label"
              >
                <div
                  class="flex justify-between text-[10px] uppercase tracking-widest font-bold mb-2"
                >
                  <span class="text-gray-500">{{ label }}</span>
                  <span class="text-gray-300">{{ val }}</span>
                </div>
                <div class="h-[1px] w-full bg-border rounded-full overflow-hidden">
                  <div
                    class="h-full bg-mint transition-all duration-1000 ease-out"
                    :style="{ width: label === 'Отклики' ? '45%' : '75%', opacity: '0.6' }"
                  ></div>
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between pt-6 border-t border-border/50">
              <div class="flex -space-x-3">
                <div
                  v-for="i in 3"
                  :key="i"
                  class="w-9 h-9 rounded-full border-2 border-bg-card bg-bg-elevated"
                ></div>
                <div
                  class="w-9 h-9 rounded-full border-2 border-bg-card bg-mint text-bg flex items-center justify-center text-[10px] font-black"
                >
                  +{{ job.newResponses }}
                </div>
              </div>
              <div class="text-right">
                <p class="text-[9px] uppercase tracking-tighter text-gray-500 font-bold">
                  До дедлайна
                </p>
                <p class="text-xs font-bold text-mint">{{ job.daysLeft }} дней</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Кнопка добавления -->
        <div
          class="border-2 border-dashed border-border/40 rounded-[1.5rem] flex flex-col items-center justify-center p-12 group hover:border-mint/30 hover:bg-white/[0.02] transition-all cursor-pointer"
        >
          <div
            class="w-16 h-16 rounded-full border border-border flex items-center justify-center mb-6 group-hover:scale-110 group-hover:border-mint/50 transition-all duration-500"
          >
            <span class="text-3xl font-light text-gray-500 group-hover:text-mint">+</span>
          </div>
          <p class="text-[10px] uppercase text-center tracking-[0.3em] text-gray-500 font-black">
            Опубликовать<br />новую позицию
          </p>
        </div>
      </div>
    </main>

    <!-- Футер как на скрине -->
    <footer
      class="mt-auto px-12 py-10 border-t border-border flex justify-between items-center opacity-60"
    >
      <div class="space-y-2">
        <div class="text-[11px] font-bold tracking-[0.3em] uppercase text-mint">ТРАМПЛИН</div>
        <div class="text-[9px] font-bold text-gray-600 tracking-widest uppercase italic">
          © 2024 High-Velocity Sophistication.
        </div>
      </div>
      <div class="flex gap-10 text-[9px] font-black uppercase tracking-widest text-gray-500">
        <a href="#" class="hover:text-white transition-colors">Конфиденциальность</a>
        <a href="#" class="hover:text-white transition-colors">Условия</a>
        <a href="#" class="hover:text-white transition-colors">Поддержка</a>
        <a href="#" class="hover:text-white transition-colors">API</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
const jobs = [
  {
    id: 1,
    title: 'Senior Backend Developer (Go)',
    category: 'INTERNSHIP',
    views: '1.2k',
    responses: 42,
    daysLeft: 12,
    newResponses: 39,
  },
  {
    id: 2,
    title: 'UI/UX Designer (Product Team)',
    category: 'JUNIOR',
    views: '856',
    responses: 18,
    daysLeft: 5,
    newResponses: 15,
  },
  {
    id: 3,
    title: 'Data Scientist (ML / AI)',
    category: 'MIDDLE',
    views: '3.1k',
    responses: 94,
    daysLeft: 21,
    newResponses: 12,
  },
]
</script>

<style scoped>
/* Локальное дополнение к main.css для уникальных стилей */
.font-serif {
  font-family: 'Playfair Display', Georgia, serif;
}

/* Эффект плавного появления для контента */
main {
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
