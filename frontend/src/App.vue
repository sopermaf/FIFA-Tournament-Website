<template>
  <v-app>
    <Toolbar />

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
          <Knockout :players="players"/>
          </v-card>
        </v-tab-item>  
      </v-tabs>
    </v-content>

    <Footer />
    
  </v-app>
</template>

<script>
import LeagueTable from './components/LeagueTable.vue';
import GoldenBoot from './components/GoldenBoot.vue';
import GoldenGlove from './components/GoldenGlove.vue';
import Knockout from './components/Knockout.vue';
import Toolbar from './components/Toolbar.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    LeagueTable,
    GoldenBoot,
    GoldenGlove,
    Knockout,
    Toolbar,
    Footer,
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
