<script setup>
const navLinks = [
  { name: 'МЕНТОРЫ', link: '#' },
  { name: 'ВАКАНСИИ', link: 'onboardvacansi.vue' },
  { name: 'КОНТАКТЫ', link: '#', active: true },
  { name: 'СООБЩЕСТВО', link: '#' },
]

const features = [
  {
    title: 'Сообщество',
    desc: 'Вступайте в тематические группы по языкам программирования и фреймворкам.',
    icon: '👥',
  },
  {
    title: 'Менторство',
    desc: 'Найдите опытного наставника, который поможет составить индивидуальный план развития.',
    icon: '🎓',
  },
  {
    title: 'Митапы',
    desc: 'Посещайте наши регулярные онлайн и офлайн встречи для расширения круга общения.',
    icon: '📅',
  },
]
</script>

<template>
  <div class="min-h-screen bg-[var(--color-bg)] text-white font-['Montserrat'] flex flex-col">
    <!-- HEADER -->
    <header
      class="h-20 px-12 flex items-center justify-between border-b border-white/5 bg-[var(--color-bg)]/50 backdrop-blur-md sticky top-0 z-50"
    >
      <div class="text-[var(--color-mint)] font-bold text-xl tracking-tighter uppercase">
        Трамплин
      </div>

      <nav class="flex gap-10">
        <a
          v-for="link in navLinks"
          :key="link.name"
          :href="link.link"
          :class="[
            'font-bold tracking-[0.2em] transition-colors hover:text-[var(--color-mint)]',
            link.active ? 'text-[var(--color-mint)]' : 'text-gray-400',
          ]"
        >
          {{ link.name }}
        </a>
      </nav>

      <div class="flex items-center gap-6">
        <span class="text-gray-400 cursor-pointer hover:text-white">🔔</span>
        <div class="w-8 h-8 rounded-full border border-[var(--color-mint)] p-0.5">
          <img src="https://ui-avatars.com" class="w-full h-full rounded-full" />
        </div>
      </div>
    </header>

    <!-- HERO SECTION (Main Card) -->
    <main class="flex-1 max-w-6xl mx-auto w-full py-16 px-6">
      <div
        class="relative bg-gradient-to-br from-[#161B22] to-[#0D1117] border border-white/5 rounded-[40px] p-16 overflow-hidden shadow-2xl mb-12"
      >
        <!-- Декоративное свечение -->
        <div
          class="absolute -top-24 -right-24 w-96 h-96 bg-[var(--color-mint)] opacity-[0.03] blur-[100px] rounded-full"
        ></div>

        <div class="flex flex-col md:flex-row items-center gap-16 relative z-10">
          <!-- Иллюстрация-заглушка (как на скрине) -->
          <div
            class="w-72 h-56 bg-[#D2B48C]/20 rounded-3xl border border-white/5 flex items-center justify-center relative overflow-hidden shrink-0"
          >
            <div class="absolute inset-0 opacity-20 flex flex-col justify-center gap-2 px-8">
              <div
                v-for="i in 8"
                :key="i"
                class="h-1 bg-white rounded-full"
                :style="{ width: 100 - i * 8 + '%' }"
              ></div>
            </div>
          </div>

          <!-- Контент -->
          <div class="flex-1 text-center md:text-left">
            <div
              class="inline-block px-3 py-1 border border-[var(--color-mint)]/30 rounded-full mb-6"
            >
              <span
                class="text-[var(--color-mint)] text-[9px] font-bold tracking-widest uppercase flex items-center gap-2"
              >
                <span class="w-1 h-1 bg-[var(--color-mint)] rounded-full animate-pulse"></span>
                Status: Offline
              </span>
            </div>

            <h1 class="text-5xl font-bold mb-6 tracking-tight">
              Нет активных <span class="text-[var(--color-mint)] italic font-serif">контактов</span>
            </h1>

            <p class="text-gray-400 text-lg leading-relaxed mb-10 max-w-xl">
              Нетворкинг — ключ к успеху в IT. Найдите единомышленников и менторов в нашем
              сообществе, чтобы ускорить свой профессиональный рост.
            </p>

            <div class="flex flex-wrap gap-4 justify-center md:justify-start">
              <button class="btn-primary flex items-center gap-2 px-8 py-4 text-sm group">
                <span>👤+</span> Найти контакты
              </button>
              <button
                class="btn-outline flex items-center gap-2 px-8 py-4 text-sm border-white/10 hover:border-[var(--color-mint)]"
              >
                <span>✨</span> Рекомендации
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- FEATURES GRID -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="feat in features"
          :key="feat.title"
          class="card p-10 bg-[#161B22]/50 hover:bg-[#161B22] border-white/5 transition-all cursor-pointer group"
        >
          <div
            class="text-2xl mb-6 opacity-80 group-hover:scale-110 transition-transform duration-300"
          >
            {{ feat.icon }}
          </div>
          <h3 class="text-xl font-bold mb-4">{{ feat.title }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">{{ feat.desc }}</p>
        </div>
      </div>
    </main>

    <!-- FOOTER -->
    <footer
      class="mt-auto border-t border-white/5 py-12 px-12 flex flex-col md:flex-row justify-between items-center gap-8"
    >
      <div class="text-gray-500 font-bold text-sm tracking-tighter uppercase">Трамплин.</div>

      <div class="flex gap-8 text-[10px] font-bold text-gray-500 tracking-widest uppercase">
        <a href="#" class="hover:text-white">Vacancies</a>
        <a href="#" class="hover:text-white">Internships</a>
        <a href="#" class="hover:text-white">Mentors</a>
        <a href="#" class="hover:text-white">About Us</a>
      </div>

      <div class="text-[10px] text-gray-600 font-medium">
        © 2024 ТРАМПЛИН. HIGH-VELOCITY SOPHISTICATION.
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* Дополнительные стили для эффектов */
.btn-primary {
  background-color: var(--color-mint);
  color: var(--color-bg);
  font-weight: 700;
  border-radius: 14px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -5px rgba(0, 229, 160, 0.4);
}
.btn-outline {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 14px;
  font-weight: 700;
  transition: all 0.3s ease;
}
.card {
  border-radius: 32px;
}
</style>
