import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useRegisterStore = defineStore('register', () => {
  const currentStep = ref(1)
  const selectedRole = ref('')
  const formData = ref({
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    specialization: '',
    experience: '',
    skills: '',
    companyName: '',
    inn: '',
    domain: '',
    profileUrl: '',
    fullName: '',
    university: '',
    year: '',
    portfolio: ''
  })

  const isStep1Complete = computed(() => !!selectedRole.value)
  const isStep2Complete = computed(() => !!(formData.value.email && formData.value.password))

  // Упрощенная проверка для Шага 3
  const isStep3Complete = computed(() => {
    const { email, password, confirmPassword, username, companyName } = formData.value
    
    // Базовая проверка для всех: email и совпадающие пароли
    const baseValid = email && password && password === confirmPassword && password.length >= 6

    if (selectedRole.value === 'applicant') {
      return !!(baseValid && username) // Для соискателя нужен еще username
    } else if (selectedRole.value === 'employer') {
      return !!(baseValid && companyName) // Для работодателя - название компании
    } else if (selectedRole.value === 'admin') {
      return !!baseValid // Для админа достаточно базы
    }
    return false
  })

  function setRole(role) {
    selectedRole.value = role
  }

  function setStep(step) {
    currentStep.value = step
  }

  function updateFormData(data) {
    formData.value = { ...formData.value, ...data }
  }

  function resetRegistration() {
    currentStep.value = 1
    selectedRole.value = ''
    formData.value = {
      email: '', username: '', password: '', confirmPassword: '',
      specialization: '', experience: '', skills: '', companyName: '',
      inn: '', domain: '', profileUrl: '', fullName: '',
      university: '', year: '', portfolio: ''
    }
  }

  return {
    currentStep,
    selectedRole,
    formData,
    isStep1Complete,
    isStep2Complete,
    isStep3Complete,
    setRole,
    setStep,
    updateFormData,
    resetRegistration
  }
})