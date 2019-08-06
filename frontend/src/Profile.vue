<template>
  <v-app>
    <Toolbar />

    <v-content>
        <span v-for="player in players" :key="player.id">
          <ProfileIndividual :player="player" class="mb-4 mt-4 elevation-4" elevation-1 ma-2/>
        </span>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import ProfileIndividual from './components/ProfileIndividual';
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'Profile',
  components: {
    ProfileIndividual,
    Toolbar,
    Footer,
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
