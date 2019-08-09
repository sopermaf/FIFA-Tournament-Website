<template>
  <v-app>
    <Toolbar />

    <v-content>
      <v-container grid-list-md >
        <v-layout row wrap justify-center>
          <!-- HEADER -->
          <v-flex md10 text-xs-center>
              <h1 text-s-center> Welcome! </h1>
              
              <img :src="iconUrl" >
              
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
                <option v-for="user in users" :key="user.id"> {{ user.name }} </option>
            </select>
          </v-flex>
          <v-flex md10 mt-5 mb-5 text-xs-center>
            <v-btn :href="'/fifa/playerInput/' + chosen + '/'">
                <span class=""> Login </span>
            </v-btn>
          </v-flex>

          <!-- POLL -->
          <v-flex md12 text-xs-center >
            <h2> Tournament Favourite Live Poll </h2>
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
  computed: {
    iconUrl () {
      return require('./assets/fifa_logo.png')
      // The path could be '../assets/img.png', etc., which depends on where your vue file is
    }
  }
}
</script>

<style>

.player1 {
    background-color: lightcoral;
     border: 2px solid black;
    border-radius: 5px;
    text-align: right;
    text-indent: 5px;
    padding-right: 5px;
}

img {
  width: 30%;
  height: 30%;
}

</style>
