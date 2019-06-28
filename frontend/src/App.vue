<template>
  <v-app>
    <v-toolbar app>
      <v-btn flat @click="choice = 'LeagueTable'">
        <span class="mr-2"> League Table</span>
      </v-btn>
      <v-btn flat @click="choice = 'GoldenBoot'">
        <span class="mr-2"> Golden Boot</span>
      </v-btn>
      <v-btn flat @click="choice = 'GoldenGlove'">
        <span class="mr-2"> Golden Glove</span>
      </v-btn>

      <v-spacer></v-spacer>
      
      <v-toolbar-title class="headline text-uppercase">
        <span>FIFA</span>
        <span class="font-weight-light">Tournament</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-content>
      <template v-if=" choice == 'LeagueTable'">
        <LeagueTable :players="players"/>
      </template>
      <template v-else-if=" choice == 'GoldenBoot'">
        <GoldenBoot :players="players"/>
      </template>
      <template v-else-if=" choice == 'GoldenGlove'">
        <GoldenGlove :players="players"/>
      </template>
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
import LeagueTable from './components/LeagueTable.vue';
import GoldenBoot from './components/GoldenBoot.vue';
import GoldenGlove from './components/GoldenGlove.vue';

export default {
  name: 'App',
  components: {
    LeagueTable,
    GoldenBoot,
    GoldenGlove,
  },
  data () {
    return {
      choice: "LeagueTable",
      players: [],
    }
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
  }
}
</script>
