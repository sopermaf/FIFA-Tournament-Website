<template>
  <v-app>
    <v-toolbar app>
      <v-btn flat href="/fifa/" >
        <span class="mr-2"> Home </span>
      </v-btn>
      
      <v-btn flat href="/fifa/" >
        <span class="mr-2" href=""> League Standings </span>
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
      <!--<v-container grid-list-md text-xs-center>
        <v-layout row wrap justify-center>
          <v-flex md9 ma-2>
            <v-btn flat @click="choice = 'Fixtures'">
              <h1>Fixtures</h1>
            </v-btn>
            <v-btn flat @click="choice = 'Results'">
              <h1>Results</h1>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-container>-->

      <v-tabs fixed-tabs color="cyan" dark slider-color="yellow">
        <v-tab ripple>
          <h2> Fixtures </h2>
        </v-tab>
        <v-tab ripple>
          <h2> Results </h2>
        </v-tab>
        <v-tab-item>
          <v-card flat>
            <FixturesList />
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <ResultsList />
          </v-card>
        </v-tab-item>  
      </v-tabs>

      <!--<template v-if="choice == 'Fixtures'">
        <FixturesList />
      </template>
      <template v-else-if="choice == 'Results'">
        <ResultsList />
      </template>-->
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
import FixturesList from './components/FixturesList';
import ResultsList from './components/ResultsList';
import DropDown from './components/DropDown';

export default {
  name: 'Fixtures',
  components: {
    DropDown,
    FixturesList,
    ResultsList,
  },
  data () {
    return {
      players: [],
      choice: "Fixtures",
    }
  },
  methods: {
  },
  mounted() {
    /*this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];*/
  }
}
</script>
