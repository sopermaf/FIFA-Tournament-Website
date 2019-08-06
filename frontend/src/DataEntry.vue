<template>
  <v-app>
    <Toolbar />

    <v-content>
      <ResultInput :players="players"/>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import ResultInput from './components/ResultInput';
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'DataEntry',
  components: {
    ResultInput,
    Toolbar,
    Footer,
  },
  data () {
    return {
      players: [],
    }
  },
  methods: {
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
  }
}
</script>
