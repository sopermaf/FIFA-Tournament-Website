<template>
  <v-app>
    <v-toolbar app>
      <v-btn flat >
        <span class="mr-2"> Home </span>
      </v-btn>
      
      <v-btn flat >
        <span class="mr-2"> League Standings </span>
      </v-btn>

      <v-btn flat href='/fifa/players/'>
        <span class="mr-2"> Players </span>
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
      <v-tabs fixed-tabs color="cyan" dark slider-color="yellow">
        <v-tab ripple>
          <h2> League Table </h2>
        </v-tab>
        <v-tab ripple>
          <h2> Golden Boot </h2>
        </v-tab>
        <v-tab ripple>
          <h2> Golden Glove </h2>
        </v-tab>
        <v-tab ripple>
          <h2> Knockout Matchups </h2>
        </v-tab>

        <v-tab-item>
          <v-card flat>
            <LeagueTable />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
          <GoldenBoot />
          </v-card>
        </v-tab-item>  
        <v-tab-item>
          <v-card flat>
          <GoldenGlove />
          </v-card>
        </v-tab-item>  
        <v-tab-item>
          <v-card flat>
          <Knockout />
          </v-card>
        </v-tab-item>  
      </v-tabs>
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
import Knockout from './components/Knockout.vue';

export default {
  name: 'App',
  components: {
    LeagueTable,
    GoldenBoot,
    GoldenGlove,
    Knockout,
  },
  data () {
    return {
      choice: "LeagueTable",
      players: [],
      pagination: {
        rowsPerPage: 30
      },
    }
  },
  methods: {
    messageReceived(table) {
        this.choice = table;
    }
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
  }
}
</script>
