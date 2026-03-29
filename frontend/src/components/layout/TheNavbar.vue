<template>
  <nav class="navbar">
    <RouterLink to="/" class="logo">ТРАМПЛИН</RouterLink>

    <button class="burger" @click="menuOpen = !menuOpen">
      <span></span><span></span><span></span>
    </button>

    <div class="nav-links" :class="{ open: menuOpen }">
      <a href="#" class="nav-link">Стажировки</a>
      <a href="#" class="nav-link">Мероприятия</a>
      <a href="#" class="nav-link">Компании</a>
      <a href="#" class="nav-link">База знаний</a>
    </div>

    <!-- Навигация для авторизованных пользователей -->
    <div v-if="authStore.isAuthenticated" class="user-nav">
      <span class="user-name">{{ authStore.user.name }}</span>
      <RouterLink v-if="authStore.isAdmin" to="/admin/main" class="nav-link admin-link"
        >Админка</RouterLink
      >
      <RouterLink v-else-if="authStore.isApplicant" to="/applicant" class="nav-link"
        >Профиль</RouterLink
      >
      <RouterLink v-else-if="authStore.isEmployer" to="/company/dashboard" class="nav-link"
        >Компания</RouterLink
      >
      <button @click="handleLogout" class="btn-logout">Выйти</button>
    </div>

    <!-- Навигация для неавторизованных пользователей -->
    <RouterLink v-else to="/register" class="btn-login">Войти</RouterLink>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const menuOpen = ref(false)

const handleLogout = () => {
  authStore.logout()
  router.push('/')
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 60px;
  border-bottom: 1px solid var(--color-border);
  gap: 32px;
  font-family: 'Montserrat', sans-serif;
}

.logo {
  font-size: 24px;
  font-weight: 800;
  color: var(--color-mint);
  letter-spacing: 2px;
  cursor: pointer;
  text-decoration: none;

  &:hover {
    opacity: 0.8;
  }
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 18px;
  flex: 1;
  justify-content: center;
}

.nav-link {
  white-space: nowrap;
  color: #9ca3af;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  position: relative;
  padding-bottom: 4px;
  transition: color 0.2s;

  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--color-mint);
    border-radius: 2px;
    transition: width 0.25s ease;
  }

  &:hover {
    color: white;
    &::after {
      width: 100%;
    }
  }
}

.btn-login {
  border: 1px solid var(--color-border);
  background: transparent;
  color: white;
  font-weight: 700;
  padding: 10px 28px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 14px;
  font-family: 'Montserrat', sans-serif;
  text-decoration: none;
  display: inline-block;
  transition:
    border-color 0.2s,
    color 0.2s,
    background 0.2s;

  &:hover {
    border-color: var(--color-mint);
    color: var(--color-mint);
    background: var(--color-mint-dim);
  }
}

.burger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;

  span {
    display: block;
    width: 24px;
    height: 2px;
    background: white;
    border-radius: 2px;
  }
}

@media (max-width: 768px) {
  .navbar {
    display: grid;
    grid-template-columns: 1fr auto;
    grid-template-areas: 'logo burger' 'links links';
    padding: 16px 24px;
    gap: 0;
  }

  .logo {
    grid-area: logo;
  }
  .burger {
    grid-area: burger;
    display: flex;
  }
  .btn-login {
    display: none;
  }

  .nav-links {
    grid-area: links;
    display: none;
    flex-direction: column;
    gap: 16px;
    padding: 16px 0;
    border-top: 1px solid var(--color-border);
    margin-top: 16px;

    &.open {
      display: flex;
    }
  }
}

.user-nav {
  display: flex;
  align-items: center;
  gap: 16px;
}

.user-name {
  color: white;
  font-weight: 500;
}

.admin-link {
  color: var(--color-mint) !important;
  font-weight: 600;
}

.btn-logout {
  padding: 6px 12px;
  background: transparent;
  border: 1px solid var(--color-border);
  color: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;

  &:hover {
    background: var(--color-border);
    border-color: var(--color-mint);
  }
}
</style>
