<template>
  <v-app>
    <Toolbar />

    <v-content>
      <v-container grid-list-md >
        <v-layout row wrap justify-center>
          <!-- HEADER -->
          <v-flex md10 text-xs-center>
              <h1 text-s-center> Welcome! </h1>
              <!--
              <img src="https://i.ibb.co/rd4dg9m/3-D-Logo-White-Controller-PNG.png" >
              -->
          </v-flex>
          
          <!-- MAIN TEXT -->
          <v-flex md10 text-xs-left>
            <p>
            This year we celebrate the 5th year anniversary 
            of the FIFA Tournament. This prestigious competition 
            is rich with history and has laid witness to some of the 
            most incredible moments in competitive FIFA. This year will see 
            10 competitors from around the globe battle it out to become the 
            FIFA Tournament champion.
            </p>
            <p>
            Here you will find all of the latest content, news, 
            fixtures, and results to ensure that you are kept 
            up to date. 
            </p>
          </v-flex>

          <!-- LOGIN OPTION -->
          <v-flex md10 text-xs-center>
            <select v-model="chosen" class="player1">
                <option disabled value="">Select User</option>
                <option v-for="user in users" :key="user.id"> {{ user.name }} </option>-->
                <option> Ferd </option>
            </select>
          </v-flex>
          <v-flex md10 mt-5 mb-5 text-xs-center>
            <v-btn :href="'/fifa/playerInput/' + chosen + '/'">
                <span class=""> Login </span>
            </v-btn>
          </v-flex>

          <!-- POLL -->
          <v-flex md10 >
            <PollViewer />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import PollViewer from './components/PollViewer';
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'Profile',
  components: {
    PollViewer,
    Toolbar,
    Footer,
  },
  data () {
    return {
      players: [],
      users: [],
      chosen: 'Niall Burke',
    }
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
    this.users = JSON.parse(this.data)['users'];
  },
  methods: {
    createUrl() {
      return this.chosen;
    },
  },
}
</script>

<style>

.profile {
  border: 2px solid black;
  border-radius: 25px;
}

.player1 {
    background-color: lightcoral;
}

</style>
