import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import RegisterStep2View from '../views/RegisterStep2View.vue'
import ApplicantView from '../views/applicant.vue'
import ApplicantNetworkView from '../views/applicantnetwork.vue'
import ApplicantProfileView from '../views/applicantprofile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/register/step2',
      name: 'register-step2',
      component: RegisterStep2View,
    },
    {
      path: '/applicant',
      name: 'applicant',
      component: ApplicantView,
    },
    {
      path: '/applicant/profile',
      name: 'applicant-profile',
      component: ApplicantProfileView,
    },
    {
      path: '/applicant/network',
      name: 'applicant-network',
      component: ApplicantNetworkView,
    },
  ],
})

export default router