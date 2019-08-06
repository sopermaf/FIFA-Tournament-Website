<template>
  <v-app>
    <Toolbar />

    <v-content>
        <TeamSelect :user="username" :userID="userID" :players="opponents" :teams="teams"/>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import TeamSelect from './components/TeamSelect';
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'PlayerTeam',
  components: {
    TeamSelect,
    Toolbar,
    Footer,
  },
  data () {
    return {
      username: '',
      teams: [],
      opponents: [],
      userID: '',
    }
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.teams = JSON.parse(this.data)['unusedTeams'];
    this.opponents = JSON.parse(this.data)['opponents'];
    this.username = JSON.parse(this.data)['username'];
    this.userID = JSON.parse(this.data)['userID'];
  },
  methods: {
  },
}
</script>

<style>

.player1 {
    background-color: lightcoral;
}

.player2 {
    background-color: lightgreen;
}

p {
    color: rgba(255, 0, 0, 0.767);
}

</style>
