<template>
  <v-navigation-drawer
    v-model="ui.drawer"
    :permanent="false"
    :temporary="mobile"
  >
    <v-list>
      <v-list-item
        prepend-avatar="https://randomuser.me/api/portraits/men/85.jpg"
        title="John Leider"
      />
    </v-list>

    <v-divider />

    <v-list nav>
      <v-list-item
        prepend-icon="mdi-home-city"
        title="example.com"
        value="home"
      />
      <v-list-item
        prepend-icon="mdi-domain"
        title="yourdomain.com"
        value="your domain"
      />
      <v-list-item
        prepend-icon="mdi-account-group-outline"
        title="mybusiness.com"
        value="users"
      />
    </v-list>
  </v-navigation-drawer>

</template>

<script setup>
  import { useUIStore } from '@/stores/ui'
  import { useDisplay } from 'vuetify'

  const ui = useUIStore()
  const { mobile } = useDisplay()
</script>
