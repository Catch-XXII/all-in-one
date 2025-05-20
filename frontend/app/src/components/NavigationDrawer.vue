<template>
  <v-navigation-drawer
    v-model="ui.drawer"
    :permanent="false"
    :temporary="mobile"
  >
    <v-list>
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg"
        :title="auth.user?.email"
      />
    </v-list>

    <v-divider />

    <v-list nav>
      <v-list-subheader>History </v-list-subheader>

      <v-list-item
        color="primary"
        prepend-icon="mdi-home-city"
        title="example.com"
        value="home"
      />
      <v-list-item
        color="primary"
        prepend-icon="mdi-domain"
        title="yourdomain.com"
        value="your domain"
      />
      <v-list-item
        color="primary"
        prepend-icon="mdi-account-group-outline"
        title="mybusiness.com"
        value="users"
      />
    </v-list>
    <template #append>
      <div class="pa-2">
        <v-btn block rounded @click="handleLogout">
          Logout
        </v-btn>
      </div>
    </template>
  </v-navigation-drawer>

</template>

<script setup>
  import { useUIStore } from '@/stores/ui'
  import { useDisplay } from 'vuetify'
  import { useAuthStore } from '@/stores/auth'
  import { useRouter } from 'vue-router'

  const ui = useUIStore()
  const { mobile } = useDisplay()
  const auth = useAuthStore()

  const router = useRouter()

  const handleLogout = () => {
    auth.logout()
    router.push('/')
  }
</script>
