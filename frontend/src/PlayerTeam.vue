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
      <!-- LOG IN Section -->
      <!--<template v-if="!loggedIn">
        <v-container grid-list-md text-xs-center>
          <v-layout row wrap justify-center>
            <v-flex md12 ma-2 >
              <select v-model="user" class="player1">
                  <option disabled value="">Username</option>
                  <option v-for="u in users_available" :key="u.index"> {{ u }} </option>
              </select>
            </v-flex>

            <v-flex md5 ma-5 >
              <input v-model="user" placeholder="edit me">
              <p>Message is: {{ user }}</p>
            </v-flex>
            
            <v-flex md5 ma-5 >
              <v-btn  @click="loggedIn = true">
                  <span class=""> Submit Result </span>
              </v-btn>
            </v-flex>          
          </v-layout>
        </v-container>
      </template>-->      

     
        <TeamSelect :user="username" :userID="userID" :players="opponents" :teams="teams"/>

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
import TeamSelect from './components/TeamSelect';

export default {
  name: 'PlayerTeam',
  components: {
    TeamSelect
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
