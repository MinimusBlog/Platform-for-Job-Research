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

// Админка
import AdminMain from '../views/admin/adminMain.vue'
import AdminUsers from '../views/admin/adminUsers.vue'
import AdminCompany from '../views/admin/adminCompany.vue'
import AdminCard from '../views/admin/AdminCard.vue'

// onboarding
import onboardContact from '../views/onboarding/onboardContact.vue'
import onboardVacansi from '../views/onboarding/onboardVacansi.vue'

//работодатель ЛК
import CompanyHans from '../views/company/companyHans.vue'
import CompanyVouke from '../views/company/companyVouke.vue'
import CompanyCreate from '../views/company/companyCreate.vue' 
import CompanyProfile from '../views/company/companyProfile.vue' 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Общие
    { path: '/', name: 'home', component: HomeView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: RegisterView },
    { path: '/register/step2', name: 'register-step2', component: RegisterStep2View },

    // Раздел СОИСКАТЕЛЯ
    {
      path: '/applicant',
      meta: { requiresAuth: true },
      children: [
        { path: '', name: 'applicant', component: ApplicantView },
        { path: 'profile', name: 'applicant-profile', component: ApplicantProfileView },
        { path: 'network', name: 'applicant-network', component: ApplicantNetworkView },
      ],
    },

    // Раздел РАБОТОДАТЕЛЯ
    {
      path: '/company',
      meta: { requiresAuth: true, requiresEmployer: true },
      children: [
        { 
          path: 'opportunities', // Это будет основной страницей
          name: 'company-opportunities', 
          component: CompanyHans 
        },
        { 
          path: 'responses', 
          name: 'company-responses', 
          component: CompanyVouke 
        },
        { path: 'create', name: 'company-create', component: CompanyCreate },
        { path: 'profile', name: 'company-profile', component: CompanyProfile },
        
        { path: '', redirect: { name: 'company-opportunities' } },
        { path: 'dashboard', redirect: { name: 'company-opportunities' } }
      ],
    },

    // Раздел АДМИНА
    { 
      path: '/admin/main', 
      name: 'admin-main', 
      component: AdminMain, 
      meta: { requiresAuth: true, requiresAdmin: true } 
    },
    { 
      path: '/admin/users', 
      name: 'admin-users', 
      component: AdminUsers, 
      meta: { requiresAuth: true, requiresAdmin: true } 
    },
    // НОВЫЕ МАРШРУТЫ ДЛЯ АДМИНКИ:
    { 
      path: '/admin/company', 
      name: 'admin-company', 
      component: AdminCompany, 
      meta: { requiresAuth: true, requiresAdmin: true } 
    },
    { 
      path: '/admin/cards', 
      name: 'admin-cards', 
      component: AdminCard, 
      meta: { requiresAuth: true, requiresAdmin: true } 
    },
    // routes oboarding
    {
      path: '/onboarding/contact',
      name: 'OnboardContact',
      component: onboardContact
    },
    {
      path: '/onboarding/vacancies',
      name: 'OnboardVacancies',
      component: onboardVacansi
    }
  ],
})

// Guard для защиты маршрутов
router.beforeEach((to) => {
  const authStore = useAuthStore()
  authStore.checkAuth()

  const isAuthenticated = authStore.isAuthenticated
  const userRole = authStore.user?.role

  // Требуется авторизация
  if (to.meta.requiresAuth && !isAuthenticated) {
    return { name: 'login' }
  }

  // Требуется роль админа
  if (to.meta.requiresAdmin && userRole !== 'admin') {
    return { name: 'home' }
  }

  // Требуется роль работодателя
  if (to.meta.requiresEmployer && userRole !== 'employer') {
    return { name: 'home' }
  }
})

export default router