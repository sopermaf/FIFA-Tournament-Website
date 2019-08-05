<template>
  <v-app>
    <v-toolbar app>
      <v-btn flat href="/fifa/" >
        <span class="mr-2"> Home </span>
      </v-btn>
      
      <v-btn flat href="/fifa/">
        <span class="mr-2"> League Standings </span>
      </v-btn>

      <v-btn flat >
        <span class="mr-2" href=""> Players </span>
      </v-btn>

      <v-btn flat href="/fifa/fixtures/">
        <span class="mr-2"> Fixtures & Results </span>
      </v-btn>

      <v-btn flat >
        <span class="mr-2"> History </span>
      </v-btn>

      <v-btn flat >
        <span class="mr-2"> Shop </span>
      </v-btn>

      <v-spacer></v-spacer>
      
      <v-toolbar-title class="headline text-uppercase">
        <span>FIFA</span>
        <span class="font-weight-light">Tournament</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-content>
        <span v-for="player in players" :key="player.id">
          <ProfileIndividual :player="player" class="mb-4 mt-4 elevation-4" elevation-1 ma-2/>
        </span>
    </v-content>

    <v-footer height="auto" color="primary lighten-1">
      <v-layout justify-center row wrap>
        <v-flex primary lighten-2 py-3 text-xs-center white--text md12>
          &copy;2019 — <strong>Fifa Tournament</strong>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-app>
</template>

<script>
import ProfileIndividual from './components/ProfileIndividual';

export default {
  name: 'Profile',
  components: {
    ProfileIndividual,
  },
  data () {
    return {
      players: [],
    }
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
  },
  methods: {
  },
}
</script>

<style>

.profile {
  border: 2px solid black;
  border-radius: 25px;
}

</style>
