<template>
  <div class="dashboard min-h-screen bg-bg text-white font-sans selection:bg-mint selection:text-bg pb-20">
    <!-- Шапка (консистентно с предыдущими страницами) -->
    <header class="relative z-10 flex items-center justify-between px-10 py-5 border-b border-border bg-bg-card/50 backdrop-blur-md">
      <div class="flex items-center gap-12">
        <div class="logo text-lg font-black tracking-tighter text-mint uppercase">ТРАМПЛИН</div>
        <nav class="flex gap-8 text-[10px] font-bold uppercase tracking-[0.25em] text-gray-400">
          <a href="#" class="hover:text-white">Компания</a>
          <a href="#" class="text-mint border-b border-mint pb-1">Возможности</a>
          <a href="#" class="hover:text-white">Отклики</a>
          <a href="#" class="hover:text-white">Аналитика</a>
        </nav>
      </div>
      <div class="flex items-center gap-6 text-gray-400">
        <button class="hover:text-mint">🔔</button>
        <button class="hover:text-mint">⚙️</button>
        <div class="w-8 h-8 rounded-lg bg-bg-elevated border border-border flex items-center justify-center text-[10px] font-bold text-white">HR</div>
      </div>
    </header>

    <main class="max-w-5xl mx-auto pt-16 px-6">
      <!-- Заголовок и Степы -->
      <div class="flex justify-between items-end mb-12">
        <h1 class="text-4xl font-serif italic tracking-tight">Создать новую возможность</h1>
        <div class="text-[10px] font-black uppercase tracking-[0.3em] text-gray-500">Шаг 1 из 3</div>
      </div>

      <!-- Линия прогресса -->
      <div class="grid grid-cols-3 gap-4 mb-16">
        <div class="space-y-3">
          <div class="h-[2px] w-full bg-mint shadow-[0_0_10px_rgba(0,229,160,0.5)]"></div>
          <span class="text-[9px] font-black uppercase tracking-widest text-mint">Детали</span>
        </div>
        <div class="space-y-3 opacity-30">
          <div class="h-[2px] w-full bg-gray-600"></div>
          <span class="text-[9px] font-black uppercase tracking-widest text-gray-400">Требования</span>
        </div>
        <div class="space-y-3 opacity-30">
          <div class="h-[2px] w-full bg-gray-600"></div>
          <span class="text-[9px] font-black uppercase tracking-widest text-gray-400">Проверка</span>
        </div>
      </div>

      <!-- Секция: Тип публикации -->
      <section class="mb-12">
        <label class="text-[10px] font-black uppercase tracking-[0.2em] text-gray-500 mb-6 block">— Тип публикации</label>
        <div class="grid grid-cols-4 gap-4">
          <div v-for="type in pubTypes" :key="type.id" 
               @click="selectedType = type.id"
               :class="selectedType === type.id ? 'border-mint bg-mint/5 shadow-[0_0_20px_rgba(0,229,160,0.05)]' : 'border-border bg-bg-card/30 hover:border-gray-600'"
               class="p-6 rounded-xl border cursor-pointer transition-all group">
            <div class="text-2xl mb-4 group-hover:scale-110 transition-transform" :class="selectedType === type.id ? 'opacity-100' : 'opacity-40'">
              {{ type.icon }}
            </div>
            <div class="text-sm font-bold mb-1">{{ type.label }}</div>
            <div class="text-[10px] text-gray-500 leading-relaxed">{{ type.desc }}</div>
          </div>
        </div>
      </section>

      <!-- Основная форма -->
      <div class="grid grid-cols-12 gap-10">
        <!-- Левая колонка -->
        <div class="col-span-7 space-y-10">
          <div>
            <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Название позиции</label>
            <input type="text" placeholder="например, Junior Frontend Developer (React)" 
                   class="w-full bg-transparent border-b border-border py-3 text-lg focus:outline-none focus:border-mint transition-colors placeholder:text-gray-700">
          </div>

          <div>
            <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Описание</label>
            <div class="border border-border rounded-xl bg-bg-card/20 overflow-hidden focus-within:border-mint/50 transition-colors">
              <div class="flex gap-4 p-3 border-b border-border bg-white/[0.02]">
                <button class="text-xs font-bold hover:text-mint">B</button>
                <button class="text-xs italic hover:text-mint">I</button>
                <button class="text-xs hover:text-mint">list</button>
                <button class="text-xs hover:text-mint">link</button>
              </div>
              <textarea placeholder="Расскажите о задачах, команде и стеке технологий..." 
                        class="w-full bg-transparent p-5 h-48 focus:outline-none resize-none text-sm leading-relaxed"></textarea>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-6">
            <div>
              <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Навыки</label>
              <div class="flex flex-wrap gap-2 p-3 border border-border rounded-xl bg-bg-card/20 min-h-[46px]">
                <span class="bg-mint/10 text-mint text-[10px] px-2 py-1 rounded border border-mint/20 flex items-center gap-2">
                  React <button class="hover:text-white">×</button>
                </span>
                <span class="bg-mint/10 text-mint text-[10px] px-2 py-1 rounded border border-mint/20 flex items-center gap-2">
                  TypeScript <button class="hover:text-white">×</button>
                </span>
                <input type="text" placeholder="Добавить..." class="bg-transparent text-[10px] outline-none w-20">
              </div>
            </div>
            <div>
              <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Формат</label>
              <select class="w-full bg-bg-card/20 border border-border rounded-xl p-3 text-xs font-bold focus:border-mint outline-none appearance-none cursor-pointer">
                <option>Office (В офисе)</option>
                <option>Remote (Удаленно)</option>
                <option>Hybrid (Гибрид)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Правая колонка -->
        <div class="col-span-5 space-y-10">
          <div>
            <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Локация</label>
            <div class="relative mb-4">
              <span class="absolute left-4 top-1/2 -translate-y-1/2 text-mint">📍</span>
              <input type="text" placeholder="Москва, БЦ 'Академик'" 
                     class="w-full bg-bg-card/40 border border-border rounded-xl py-3 pl-12 pr-4 text-xs font-bold focus:border-mint outline-none transition-all">
            </div>
            <!-- Плейсхолдер карты -->
            <div class="w-full h-32 rounded-xl bg-bg-elevated border border-border flex flex-col items-center justify-center relative overflow-hidden group">
              <div class="absolute inset-0 bg-gradient-to-br from-mint/5 to-transparent"></div>
              <div class="text-[10px] font-bold text-gray-500 group-hover:text-mint transition-colors">● ПРЕДПРОСМОТР КАРТЫ</div>
            </div>
          </div>

          <div>
            <div class="flex justify-between mb-3">
              <label class="text-[9px] font-black uppercase tracking-widest text-gray-500">Зарплатная вилка</label>
              <span class="text-xs font-bold text-mint">120K — 180K ₽</span>
            </div>
            <div class="relative h-6 flex items-center">
              <div class="h-[2px] w-full bg-border rounded-full"></div>
              <div class="absolute left-1/4 right-1/4 h-[2px] bg-mint shadow-[0_0_10px_rgba(0,229,160,0.3)]"></div>
              <div class="absolute left-1/4 w-3 h-3 bg-mint rounded-full -translate-x-1/2 shadow-lg"></div>
              <div class="absolute right-1/4 w-3 h-3 bg-mint rounded-full translate-x-1/2 shadow-lg"></div>
            </div>
            <div class="flex justify-between mt-2 text-[8px] font-black uppercase text-gray-600 tracking-tighter">
              <span>40K</span>
              <span>500K+</span>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-6">
            <div>
              <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Дата публикации</label>
              <input type="date" class="w-full bg-bg-card/20 border border-border rounded-xl p-3 text-xs font-bold focus:border-mint outline-none invert-[0.8] brightness-150">
            </div>
            <div>
              <label class="text-[9px] font-black uppercase tracking-widest text-gray-500 mb-3 block">Срок действия</label>
              <input type="date" class="w-full bg-bg-card/20 border border-border rounded-xl p-3 text-xs font-bold focus:border-mint outline-none invert-[0.8] brightness-150">
            </div>
          </div>
        </div>
      </div>

      <!-- Кнопки действий -->
      <div class="mt-20 flex justify-end gap-4 border-t border-border pt-10">
        <button class="btn-outline px-10 py-3 text-[11px] uppercase tracking-[0.2em]">Предпросмотр</button>
        <button class="btn-primary px-12 py-3 text-[11px] uppercase tracking-[0.2em] shadow-[0_0_30px_rgba(0,229,160,0.2)]">Продолжить</button>
      </div>
    </main>

    <!-- Футер из дизайна -->
    <footer class="mt-20 px-10 py-10 border-t border-white/5 flex justify-between items-center opacity-40">
      <div class="space-y-2">
        <div class="text-[11px] font-black tracking-[0.4em] text-mint uppercase">ТРАМПЛИН</div>
        <div class="text-[9px] font-bold text-gray-500 tracking-widest uppercase">© 2024 HIGH-VELOCITY SOPHISTICATION.</div>
      </div>
      <div class="flex gap-8 text-[9px] font-black uppercase tracking-widest text-gray-500">
        <a href="#" class="hover:text-white">Конфиденциальность</a>
        <a href="#" class="hover:text-white">Условия</a>
        <a href="#" class="hover:text-white">Поддержка</a>
        <a href="#" class="hover:text-white">API</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const selectedType = ref(1);

const pubTypes = [
  { id: 1, label: 'Стажировка', icon: '💼', desc: 'Для студентов и начинающих' },
  { id: 2, label: 'Работа', icon: '👔', desc: 'Постоянная занятость' },
  { id: 3, label: 'Событие', icon: '📅', desc: 'Хакатоны, лекции, митапы' },
  { id: 4, label: 'Менторство', icon: '🤝', desc: 'Обмен опытом и развитие' }
];
</script>

<style scoped>
@import url('https://fonts.googleapis.com');

.font-serif {
  font-family: 'Playfair Display', serif;
}

/* Стилизация календаря (инпутов типа date) для темной темы */
input[type="date"]::-webkit-calendar-picker-indicator {
  cursor: pointer;
  filter: invert(1);
  opacity: 0.5;
}

input[type="date"]::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}

section {
  animation: slideUp 0.6s ease-out forwards;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
