<script setup>
import { ref } from 'vue'

const emit = defineEmits(['close', 'confirm'])

const form = ref({
  name: '',
  email: '',
  permissions: [],
})

const roles = [
  {
    id: 'moderation',
    title: 'Модерация',
    desc: 'Контент и жалобы',
  },
  {
    id: 'users',
    title: 'Пользователи',
    desc: 'Управление профилями',
  },
  {
    id: 'analytics',
    title: 'Аналитика',
    desc: 'Отчеты и метрики',
  },
]

const handleConfirm = () => {
  emit('confirm', { ...form.value })
}
</script>

<template>
  <Teleport to="body">
    <div
      class="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-[#0d1117]/80 backdrop-blur-xl"
    >
      <div
        class="bg-[#161b22] border border-[#30363d] w-full max-w-[480px] rounded-[3rem] shadow-[0_32px_64px_-16px_rgba(0,0,0,0.6)] overflow-hidden relative group"
      >
        <div
          class="absolute -top-24 -right-24 w-48 h-48 bg-mint blur-[100px] opacity-10 group-hover:opacity-20 transition-opacity"
        ></div>

        <div class="p-10 pb-6">
          <div class="flex justify-between items-start">
            <div>
              <h2
                class="text-3xl font-black italic uppercase tracking-tighter text-white leading-none"
              >
                Новый <span class="text-mint">Куратор</span>
              </h2>
              <p
                class="text-[10px] font-black uppercase tracking-[0.3em] text-gray-500 mt-3 opacity-60 text-nowrap"
              >
                Регистрация в системе управления
              </p>
            </div>
            <button
              @click="$emit('close')"
              class="w-10 h-10 flex items-center justify-center rounded-2xl bg-white/5 border border-white/10 text-gray-400 hover:text-white hover:bg-white/10 transition-all cursor-pointer text-xl"
            >
              &times;
            </button>
          </div>
        </div>

        <div class="px-10 pb-6 space-y-6">
          <div class="grid grid-cols-1 gap-5">
            <div class="space-y-2">
              <label class="text-[9px] font-black uppercase tracking-[0.3em] text-gray-500 ml-2"
                >Имя Фамилия</label
              >
              <input
                v-model="form.name"
                type="text"
                placeholder="Иван Иванов"
                class="w-full bg-[#0d1117] border border-[#30363d] rounded-2xl px-5 py-4 text-sm focus:border-mint/50 outline-none transition-all placeholder:text-gray-700 font-bold"
              />
            </div>

            <div class="space-y-2">
              <label class="text-[9px] font-black uppercase tracking-[0.3em] text-gray-500 ml-2"
                >Рабочая почта</label
              >
              <input
                v-model="form.email"
                type="email"
                placeholder="staff@tramplin.it"
                class="w-full bg-[#0d1117] border border-[#30363d] rounded-2xl px-5 py-4 text-sm focus:border-mint/50 outline-none transition-all placeholder:text-gray-700 font-bold"
              />
            </div>
          </div>

          <div class="space-y-3">
            <label class="text-[9px] font-black uppercase tracking-[0.3em] text-gray-500 ml-2"
              >Привилегии</label
            >

            <div class="grid grid-cols-1 gap-2">
              <label
                v-for="role in roles"
                :key="role.id"
                class="flex items-center gap-4 p-4 rounded-[1.5rem] cursor-pointer transition-all border group"
                :class="
                  form.permissions.includes(role.id)
                    ? 'bg-mint/5 border-mint/20 shadow-[inset_0_0_20px_rgba(0,229,160,0.05)]'
                    : 'bg-[#0d1117] border-[#30363d] hover:border-gray-600'
                "
              >
                <div class="relative flex items-center">
                  <input
                    type="checkbox"
                    :value="role.id"
                    v-model="form.permissions"
                    class="peer h-5 w-5 cursor-pointer appearance-none rounded-lg border border-[#30363d] bg-transparent checked:bg-mint checked:border-mint transition-all"
                  />
                  <svg
                    class="absolute h-3 w-3 pointer-events-none hidden peer-checked:block text-[#0d1117] left-1 top-1"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="4"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div class="min-w-0">
                  <div
                    class="text-[11px] font-black uppercase tracking-widest transition-colors"
                    :class="form.permissions.includes(role.id) ? 'text-mint' : 'text-gray-300'"
                  >
                    {{ role.title }}
                  </div>
                  <div
                    class="text-[9px] text-gray-500 font-bold uppercase tracking-tighter truncate"
                  >
                    {{ role.desc }}
                  </div>
                </div>
              </label>
            </div>
          </div>
        </div>

        <div class="p-10 pt-4 flex items-center gap-6">
          <button
            @click="$emit('close')"
            class="text-[10px] font-black uppercase tracking-[0.2em] text-gray-600 hover:text-white transition-colors cursor-pointer"
          >
            Отмена
          </button>

          <button
            @click="handleConfirm"
            class="flex-1 py-5 bg-mint text-[#0d1117] rounded-3xl text-[11px] font-black uppercase tracking-[0.3em] hover:brightness-110 active:scale-[0.98] transition-all shadow-[0_10px_20px_rgba(0,229,160,0.15)]"
          >
            Сохранить
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</template>
