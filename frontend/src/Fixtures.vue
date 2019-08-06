<template>
  <v-app>
    <Toolbar />

    <v-content>
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
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import FixturesList from './components/FixturesList';
import ResultsList from './components/ResultsList';
import DropDown from './components/DropDown';
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'Fixtures',
  components: {
    DropDown,
    FixturesList,
    ResultsList,
    Toolbar,
    Footer,
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
