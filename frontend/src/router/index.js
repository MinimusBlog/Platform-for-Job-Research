import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Общие страницы
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import RegisterStep2View from '../views/RegisterStep2View.vue'

// Соискатель
import ApplicantView from '../views/applicant/applicant.vue'
import ApplicantNetworkView from '../views/applicant/applicantnetwork.vue'
import ApplicantProfileView from '../views/applicant/applicantprofile.vue'
import ApplicantJobsView from '../views/applicant/applicantJobs.vue'
import ApplicantJobDetailsView from '../views/applicant/applicantJobDetails.vue'

// Админка
import AdminMain from '../views/admin/adminMain.vue'
import AdminUsers from '../views/admin/adminUsers.vue'
import AdminCompany from '../views/admin/adminCompany.vue'
import AdminCard from '../views/admin/AdminCard.vue'

// Работодатель ЛК
import CompanyHans from '../views/company/companyHans.vue'
import CompanyVouke from '../views/company/companyVouke.vue'
import CompanyCreate from '../views/company/companyCreate.vue' 
import CompanyProfile from '../views/company/companyProfile.vue' 

// Onboarding
import onboardContact from '../views/onboarding/onboardContact.vue'
import onboardVacansi from '../views/onboarding/onboardVacansi.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // --- ОБЩИЕ МАРШРУТЫ ---
    { path: '/', name: 'home', component: HomeView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: RegisterView },
    { path: '/register/step2', name: 'register-step2', component: RegisterStep2View },

    // --- ONBOARDING (Для новых работодателей) ---
    {
      path: '/onboarding',
      meta: { requiresAuth: true, requiresEmployer: true },
      children: [
        { path: 'contact', name: 'OnboardContact', component: onboardContact },
        { path: 'vacancies', name: 'OnboardVacancies', component: onboardVacansi },
        { path: '', redirect: { name: 'OnboardContact' } }
      ]
    },

    // --- РАЗДЕЛ СОИСКАТЕЛЯ ---
    {
      path: '/applicant',
      meta: { requiresAuth: true, role: 'applicant' },
      children: [
        { path: '', name: 'applicant', component: ApplicantView },
        { path: 'jobs', name: 'applicant-jobs', component: ApplicantJobsView },
        { path: 'jobs/:id', name: 'applicant-job-details', component: ApplicantJobDetailsView },
        { path: 'profile', name: 'applicant-profile', component: ApplicantProfileView },
        { path: 'network', name: 'applicant-network', component: ApplicantNetworkView },
      ],
    },

    // --- РАЗДЕЛ РАБОТОДАТЕЛЯ ---
    {
      path: '/company',
      meta: { requiresAuth: true, requiresEmployer: true, checkOnboarding: true },
      children: [
        { path: 'opportunities', name: 'company-opportunities', component: CompanyHans },
        { path: 'responses', name: 'company-responses', component: CompanyVouke },
        { path: 'create', name: 'company-create', component: CompanyCreate },
        { path: 'profile', name: 'company-profile', component: CompanyProfile },
        { path: '', redirect: { name: 'company-opportunities' } }
      ],
    },

    // --- РАЗДЕЛ АДМИНА ---
    { 
      path: '/admin',
      meta: { requiresAuth: true, requiresAdmin: true },
      children: [
        { path: 'main', name: 'admin-main', component: AdminMain },
        { path: 'users', name: 'admin-users', component: AdminUsers },
        { path: 'company', name: 'admin-company', component: AdminCompany },
        { path: 'cards', name: 'admin-cards', component: AdminCard },
      ]
    }
  ],
})

// --- ГЛОБАЛЬНЫЙ GUARD ---
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  // Синхронная проверка состояния (из localStorage/cookie внутри стора)
  authStore.checkAuth()

  const isAuthenticated = authStore.isAuthenticated
  const user = authStore.user
  const userRole = user?.role

  // 1. Проверка авторизации
  if (to.meta.requiresAuth && !isAuthenticated) {
    return next({ name: 'login' })
  }

  // 2. Логика Onboarding для Работодателя
  // Если залогинен как работодатель, но не прошел онбординг (onboarded === false)
  if (isAuthenticated && userRole === 'employer' && user?.onboarded === false) {
    // Разрешаем находиться ТОЛЬКО на страницах онбординга
    if (!to.path.startsWith('/onboarding')) {
      return next({ name: 'OnboardContact' })
    }
  }

  // 3. Защита от повторного онбординга
  // Если онбординг уже пройден, не пускаем обратно на эти страницы
  if (isAuthenticated && user?.onboarded === true && to.path.startsWith('/onboarding')) {
    return next({ name: 'company-opportunities' })
  }

  // 4. Защита ролей (Admin)
  if (to.meta.requiresAdmin && userRole !== 'admin') {
    return next({ name: 'home' })
  }

  // 5. Защита ролей (Employer)
  if (to.meta.requiresEmployer && userRole !== 'employer') {
    return next({ name: 'home' })
  }

  next()
})

export default router