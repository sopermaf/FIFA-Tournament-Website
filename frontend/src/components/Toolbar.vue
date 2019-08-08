<template>
    <v-toolbar>
      <v-btn flat href='/fifa/'>
        <span class="mr-2"> Home </span>
      </v-btn>
      
      <v-btn flat href='/fifa/league/'>
        <span class="mr-2"> League Standings </span>
      </v-btn>

      <v-btn flat href='/fifa/players/'>
        <span class="mr-2"> Players </span>
      </v-btn>

      <v-btn flat href="/fifa/fixtures/">
        <span class="mr-2"> Fixtures & Results </span>
      </v-btn>

      <v-btn flat href="/fifa/history/">
        <span class="mr-2"> History </span>
      </v-btn>

      <v-btn flat >
        <span class="mr-2"> Shop </span>
      </v-btn>

      <!--<v-btn flat :href='url_user'>
        <span class="mr-2"> Team Selection </span>
      </v-btn>
      <v-btn flat href='/fifa/data/'>
        <span class="mr-2"> Result Input </span>
      </v-btn>-->

      <v-spacer></v-spacer>
      
      <v-toolbar-title class="headline text-uppercase">
        <span>FIFA</span>
        <span class="font-weight-light">Tournament</span>
      </v-toolbar-title>
    </v-toolbar>
</template>

<script>
export default {
  data () {
    return {
      username: 'Cameron McBain',
      url_user: '/fifa/playerInput/Cameron McBain/'
    }
  },
}
</script>