<script setup>
import { ref } from 'vue'

const emit = defineEmits(['close', 'confirm'])

const form = ref({
  name: '',
  email: '',
  permissions: []
})

const roles = [
  { 
    id: 'moderation', 
    title: 'Модерация', 
    desc: 'Управление контентом и жалобами' 
  },
  { 
    id: 'users', 
    title: 'Пользователи', 
    desc: 'Блокировка и редактирование профилей' 
  },
  { 
    id: 'analytics', 
    title: 'Аналитика', 
    desc: 'Просмотр отчетов и метрик системы' 
  }
]

const handleConfirm = () => {
  emit('confirm', { ...form.value })
}
</script>

<template>
  <!-- Телепорт выносит модалку в корень body для правильного наслоения -->
  <Teleport to="body">
    <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-md">
      
      <!-- Контейнер модалки с твоим классом .card -->
      <div class="card w-full max-w-[520px] shadow-2xl shadow-black/80">
        
        <!-- Шапка -->
        <div class="p-8 pb-4 flex justify-between items-start">
          <div>
            <h2 class="text-2xl font-black uppercase tracking-tight text-white leading-none">Новый куратор</h2>
            <p class="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-500 mt-2">Добавление в систему</p>
          </div>
          <button @click="$emit('close')" class="text-gray-500 hover:text-white transition-colors cursor-pointer text-2xl">&times;</button>
        </div>

        <!-- Форма -->
        <div class="p-8 pt-4 space-y-6">
          
          <!-- Инпут: Имя -->
          <div class="flex flex-col gap-2">
            <label class="text-[10px] font-bold uppercase tracking-[0.25em] text-gray-500 ml-1">Полное имя</label>
            <input 
              v-model="form.name"
              type="text" 
              placeholder="Иван Иванов" 
              class="w-full bg-[#1C2333]/40 border border-border rounded-lg p-4 text-sm focus:border-mint/50 focus:ring-1 focus:ring-mint/20 outline-none transition-all placeholder:text-gray-600"
            >
          </div>

          <!-- Инпут: Email -->
          <div class="flex flex-col gap-2">
            <label class="text-[10px] font-bold uppercase tracking-[0.25em] text-gray-500 ml-1">Email адрес</label>
            <input 
              v-model="form.email"
              type="email" 
              placeholder="example@tramplin.it" 
              class="w-full bg-[#1C2333]/40 border border-border rounded-lg p-4 text-sm focus:border-mint/50 focus:ring-1 focus:ring-mint/20 outline-none transition-all placeholder:text-gray-600"
            >
          </div>

          <!-- Доступы -->
          <div class="space-y-3">
            <label class="text-[10px] font-bold uppercase tracking-[0.25em] text-gray-500 ml-1">Уровни доступа</label>
            
            <label 
              v-for="role in roles" 
              :key="role.id"
              class="flex items-center gap-4 p-4 bg-[#1C2333]/20 border border-border/50 rounded-xl cursor-pointer hover:bg-[#1C2333]/40 transition-all group"
            >
              <div class="relative flex items-center">
                <input 
                  type="checkbox" 
                  :value="role.id"
                  v-model="form.permissions"
                  class="peer h-5 w-5 cursor-pointer appearance-none rounded border border-border bg-transparent checked:bg-mint checked:border-mint transition-all"
                >
                <svg class="absolute h-3.5 w-3.5 pointer-events-none hidden peer-checked:block text-bg left-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="4">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <div>
                <div class="text-sm font-bold group-hover:text-white transition-colors">{{ role.title }}</div>
                <div class="text-[10px] text-gray-500 uppercase tracking-tight">{{ role.desc }}</div>
              </div>
            </label>
          </div>
        </div>

        <!-- Футер -->
        <div class="p-8 pt-4 flex items-center gap-8">
          <button 
            @click="$emit('close')"
            class="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-500 hover:text-white transition-colors cursor-pointer"
          >
            Отмена
          </button>
            <a href="adminmain.vue">
          <button 
            @click="handleConfirm"
            class="btn-primary flex-1 py-4 text-[11px] uppercase tracking-[0.3em]"
          >
            Подтвердить
          </button>
          </a>
        </div>

      </div>
    </div>
  </Teleport>
</template>

<style scoped>
/* Дополнительная кастомизация чекбоксов, если стандартных Tailwind не хватит */
input[type="checkbox"] {
  border-radius: 4px;
}
</style>
