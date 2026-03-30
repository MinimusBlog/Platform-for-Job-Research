<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

// Данные формы
const form = reactive({
  phone: '',
  website: '',
  description: '',
  city: 'Москва',
})

const handleNext = () => {
  // Здесь можно добавить API запрос для сохранения контактов
  // axios.post('/api/company/details', form)

  // Переходим к следующему шагу (создание первой вакансии)
  router.push({ name: 'OnboardVacancies' })
}

const steps = [
  { id: 1, name: 'КОНТАКТЫ', active: true },
  { id: 2, name: 'ВАКАНСИЯ', active: false },
]
</script>

<template>
  <div class="min-h-screen bg-[var(--color-bg)] text-white font-['Montserrat'] flex flex-col">
    <header
      class="h-20 px-12 flex items-center justify-between border-b border-white/5 bg-[var(--color-bg)]/50 backdrop-blur-md sticky top-0 z-50"
    >
      <div class="text-[var(--color-mint)] font-bold text-xl tracking-tighter uppercase">
        Трамплин
      </div>

      <nav class="flex gap-10">
        <div
          v-for="step in steps"
          :key="step.id"
          :class="[
            'font-bold tracking-[0.2em] text-[10px] uppercase',
            step.active ? 'text-[var(--color-mint)]' : 'text-gray-600',
          ]"
        >
          {{ step.id }}. {{ step.name }}
        </div>
      </nav>

      <div class="text-[10px] font-bold text-gray-500 uppercase tracking-widest">
        Настройка профиля HR
      </div>
    </header>

    <main class="flex-1 max-w-5xl mx-auto w-full py-16 px-6">
      <div
        class="relative bg-gradient-to-br from-[#161B22] to-[#0D1117] border border-white/5 rounded-[40px] p-12 overflow-hidden shadow-2xl"
      >
        <div class="flex flex-col md:flex-row gap-16 relative z-10">
          <div class="md:w-1/3">
            <div
              class="inline-block px-3 py-1 border border-[var(--color-mint)]/30 rounded-full mb-6"
            >
              <span class="text-[var(--color-mint)] text-[9px] font-bold tracking-widest uppercase"
                >Шаг 01</span
              >
            </div>
            <h1 class="text-4xl font-bold mb-6 tracking-tight italic font-serif">
              Контакты <br />компании
            </h1>
            <p class="text-gray-400 text-sm leading-relaxed">
              Заполните основные данные, чтобы соискатели могли узнать больше о вашей корпоративной
              культуре и способах связи.
            </p>
          </div>

          <div class="flex-1 space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-[10px] font-bold text-gray-500 uppercase tracking-widest"
                  >Телефон для связи</label
                >
                <input
                  v-model="form.phone"
                  type="text"
                  placeholder="+7 (999) 000-00-00"
                  class="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 focus:border-[var(--color-mint)] outline-none transition-all text-sm"
                />
              </div>
              <div class="space-y-2">
                <label class="text-[10px] font-bold text-gray-500 uppercase tracking-widest"
                  >Сайт или соцсети</label
                >
                <input
                  v-model="form.website"
                  type="text"
                  placeholder="https://company.ru"
                  class="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 focus:border-[var(--color-mint)] outline-none transition-all text-sm"
                />
              </div>
            </div>

            <div class="space-y-2">
              <label class="text-[10px] font-bold text-gray-500 uppercase tracking-widest"
                >О компании (кратко)</label
              >
              <textarea
                v-model="form.description"
                rows="4"
                placeholder="Расскажите о миссии компании..."
                class="w-full bg-white/5 border border-white/10 rounded-xl px-5 py-3 focus:border-[var(--color-mint)] outline-none transition-all text-sm resize-none"
              ></textarea>
            </div>

            <div class="flex justify-end pt-4">
              <button
                @click="handleNext"
                class="btn-primary flex items-center gap-3 px-10 py-4 text-xs group uppercase tracking-widest"
              >
                Далее: Создать вакансию <span>→</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer
      class="mt-auto border-t border-white/5 py-8 px-12 flex justify-between items-center opacity-30"
    >
      <div class="text-[10px] font-bold text-gray-500 tracking-widest uppercase italic">
        © 2024 ТРАМПЛИН.
      </div>
      <div class="text-[10px] text-gray-600 font-medium uppercase tracking-[0.3em]">
        High-Velocity Sophistication.
      </div>
    </footer>
  </div>
</template>

<style scoped>
.btn-primary {
  background-color: var(--color-mint);
  color: var(--color-bg);
  font-weight: 800;
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 30px -10px rgba(0, 229, 160, 0.5);
}
input:focus,
textarea:focus {
  background: rgba(0, 229, 160, 0.02);
}
</style>
