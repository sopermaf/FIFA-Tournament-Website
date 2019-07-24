<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 ma-2>
          <h1>Welcome {{ user }} </h1>
          <h3> Select Your Teams for Each Game </h3>
        </v-flex>  
        <v-flex md2 >
                <select v-model="opponent_chosen" class="player1" @click="response =''">
                    <option disabled value="">Opponent</option>
                    <option v-for="p in players" :key="p.id"> {{ p.name }} </option>
                </select>
        </v-flex>
        <v-flex md2 >
                <select v-model="team_chosen" class="player1" @click="response =''">
                    <option disabled value="">TEAM</option>
                    <option v-for="i in 20" :key="i"> {{ i }} </option>
                </select>
        </v-flex>

        <!-- Preview of Selection -->
        <v-flex md5 mt-5>
            <v-card md3>
              <h2>  <span> {{ opponent_chosen }}</span> </h2>
              <h2> <span> {{ team_chosen }}</span> </h2>
            </v-card>
        </v-flex>

        <v-flex md5 mt-2>
            <v-btn  @click="addResult()">
                <span class=""> Submit Result </span>
            </v-btn>

            <p mt-4 :style="{ color: response_color }"> {{ response }} </p>
        </v-flex>

      </v-layout>
    </v-container>
</template>

<script>
import axios from "axios";

  export default {
    props: {
        players: {
            type: Array
        },
        user:  {
            type: String
        }
    }, 
    data: () => ({
        opponent_chosen: "",
        team_chosen: "",
        response: "",
        response_color: "",
        search: "",
    }),
    methods: {
        addResult() {
            /*if(this.match_players[0] == "Player 1" || this.match_players[1] == 'Player 2'){
                this.response = "Please select two players for this game";
                this.response_color = "red"
                return
            } else if (this.match_players[0] == this.match_players[1]) {
                this.response = "Both players cannot be the same";
                this.response_color = "red"
                return;
            }
            
            //form the search and make request
            this.search = '/fifa/input/' + this.match_players[0] + '/' + this.goals[0] + '/'
            this.search += this.match_players[1] + '/' + this.goals[1] + '/'

            axios.get(this.search).then(response => {
                //this.candidates = response.data['candidates']
                console.log(response)
            })

            // inform user
            this.response = "Result Recorded Successfully";
            this.response_color = "green";
            
            // reset inputs
            this.match_players[0] = "Player 1";
            this.match_players[1] = "Player 2";
            this.goals[0] = 0;
            this.goals[1] = 0;*/
        }
    }
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