<script setup>
import { ref } from 'vue'

// Состояние активной вкладки
const activeTab = ref('Мои вакансии')

// Меню для работодателя (Employer Hub)
// Сюда ты сможешь вставить ссылки на свои .vue файлы или роуты
const menuItems = [
  { name: 'МЕНТОРЫ', link: '#' },
  { name: 'ВАКАНСИИ', link: '#' },
  { name: 'КОНТАКТЫ', link: 'onboardcontact.vue' },
  { name: 'СООБЩЕСТВО', link: '#' },
]

const features = [
  {
    title: 'HIGH VELOCITY',
    desc: 'Быстрый отклик от студентов топовых вузов страны.',
    icon: '⚡',
  },
  {
    title: 'TALENT POOL',
    desc: 'Доступ к базе более чем 10,000 молодых специалистов.',
    icon: '💎',
  },
  {
    title: 'SMART MATCHING',
    desc: 'Алгоритмы подбора наиболее подходящих кандидатов.',
    icon: '🧠',
  },
]
</script>

<template>
  <div class="flex min-h-screen bg-[var(--color-bg)] text-white font-['Montserrat']">
    <!-- БОКОВОЕ МЕНЮ (SIDEBAR) -->
    <aside class="w-64 border-r border-[var(--color-border)] flex flex-col p-6 shrink-0">
      <div class="mb-10 text-[var(--color-mint)] font-bold text-xl tracking-widest uppercase">
        ТРАМПЛИН
      </div>

      <nav class="flex flex-col gap-2">
        <p class="text-[10px] text-gray-500 font-bold mb-4 ml-2 tracking-[0.2em] uppercase">
          Employer Hub
        </p>

        <a
          v-for="item in menuItems"
          :key="item.name"
          :href="item.link"
          @click.prevent="activeTab = item.name"
          :class="[
            item.name === activeTab
              ? 'text-[var(--color-mint)] border-[var(--color-mint)]'
              : 'text-gray-400 border-transparent hover:text-white hover:bg-white/5',
          ]"
        >
          <span class="opacity-50">{{ item.icon }}</span>
          {{ item.name }}
        </a>
      </nav>

      <!-- Профиль -->
      <div class="mt-auto p-4 card flex items-center gap-3">
        <div class="w-10 h-10 rounded-full border border-[var(--color-mint)] p-0.5">
          <img src="https://ui-avatars.com" class="rounded-full" />
        </div>
        <div class="overflow-hidden">
          <p class="text-xs font-bold truncate">Tech Recruit</p>
          <p class="text-[9px] text-[var(--color-mint)] uppercase font-bold">Pro Account</p>
        </div>
      </div>
    </aside>

    <!-- ОСНОВНОЙ КОНТЕНТ -->
    <main class="flex-1 flex flex-col">
      <!-- Верхняя панель (Header) -->
      <header
        class="h-16 border-b border-[var(--color-border)] flex items-center justify-end px-8 gap-6"
      >
        <div class="text-gray-400 hover:text-white cursor-pointer relative">
          🔔 <span class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"></span>
        </div>
        <button
          class="text-[10px] font-bold py-2 px-4 border border-[var(--color-border)] rounded-lg hover:border-[var(--color-mint)] transition-all"
        >
          ВЫЙТИ
        </button>
      </header>

      <!-- Центральный блок (Empty State) -->
      <div class="flex-1 flex flex-col items-center justify-center p-8 text-center">
        <!-- Карточка с 3D графикой (как на картинке) -->
        <div
          class="w-full max-w-2xl aspect-video card relative overflow-hidden mb-12 flex items-center justify-center group"
        >
          <div
            class="absolute inset-0 bg-gradient-to-t from-[var(--color-bg)] to-transparent opacity-60"
          ></div>

          <!-- Заглушка под 3D картинку -->
          <div
            class="relative z-10 w-48 h-48 bg-gradient-to-br from-gray-700 to-gray-900 rounded-3xl rotate-12 shadow-2xl flex items-center justify-center border border-white/10 group-hover:rotate-0 transition-transform duration-700"
          >
            <div
              class="w-12 h-12 bg-[var(--color-mint)] rounded-full blur-xl opacity-50 animate-pulse"
            ></div>
            <span class="text-4xl">📦</span>
          </div>

          <!-- Полоска снизу внутри карточки -->
          <div
            class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[var(--color-mint)] to-transparent"
          ></div>
        </div>

        <h2 class="text-4xl font-bold mb-4 tracking-tight">У вас еще нет вакансий</h2>
        <p class="text-gray-400 max-w-md mb-10 leading-relaxed">
          Опубликуйте свою первую вакансию или стажировку, чтобы привлечь лучших молодых
          специалистов.
        </p>

        <div class="flex gap-4">
          <button class="btn-primary flex items-center gap-2 shadow-[0_0_20px_rgba(0,229,160,0.2)]">
            <span class="text-xl">+</span> Создать вакансию
          </button>
          <button class="btn-outline">Узнать о стажировках</button>
        </div>
      </div>

      <!-- Сетка преимуществ снизу -->
      <div class="p-12 grid grid-cols-3 gap-12 border-t border-[var(--color-border)]">
        <div v-for="feat in features" :key="feat.title">
          <div class="text-[var(--color-mint)] mb-4 text-xl opacity-80">{{ feat.icon }}</div>
          <h4 class="text-[10px] font-black tracking-[0.2em] mb-2 uppercase">{{ feat.title }}</h4>
          <p class="text-gray-500 text-[11px] leading-relaxed">{{ feat.desc }}</p>
        </div>
      </div>

      <!-- FOOTER -->
      <footer
        class="p-8 border-t border-[var(--color-border)] flex justify-between items-center bg-black/20"
      >
        <div class="text-[10px] text-gray-600 font-bold uppercase tracking-widest">
          © 2026 ТРАМПЛИН. HIGH-VELOCITY SOPHISTICATION.
        </div>
        <div class="flex gap-6 text-[10px] text-gray-500 font-bold uppercase">
          <a href="#" class="hover:text-white">Vacancies</a>
          <a href="#" class="hover:text-white">Internships</a>
          <a href="#" class="hover:text-white">About</a>
        </div>
      </footer>
    </main>
  </div>
</template>

<style scoped>
/* Эти стили дополняют твой main.css для соответствия картинке */
.card {
  background-color: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 24px;
}

.btn-primary {
  background-color: var(--color-mint);
  color: var(--color-bg);
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  background-color: var(--color-mint-dark);
}

.btn-outline {
  background-color: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--color-border);
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  border-color: var(--color-mint);
  color: var(--color-mint);
}
</style>
