<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 mb-5>
          <h1>Welcome {{ user }} </h1>
          <h3> Select Your Teams for Each Game </h3>
        </v-flex>  
        <v-flex md3 >
                <select v-model="opponent_chosen" class="player1" @click="response_status =''">
                    <option disabled value="">Opponent</option>
                    <option v-for="p in players" :key="p.id"> {{ p.name }} </option>
                </select>
        </v-flex>
        <v-flex md3 >
                <select v-model="team_chosen" class="player2" @click="response_status =''">
                    <option disabled value="">Team</option>
                    <option v-for="team in teams" :key="team.id"> {{ team.name }} </option>
                </select>
        </v-flex>

        <!-- Preview of Selection -->
        <v-flex md5 ma-5>
            <v-card md3>
              <h2>  <span class=""> {{ opponent_chosen }}</span> </h2>
              <h2> <span class=""> {{ team_chosen }}</span> </h2>
            </v-card>
        </v-flex>

        <v-flex md12 mt-5>
            <v-btn  @click="selectTeam()">
                <span class=""> Submit Team </span>
            </v-btn>

            <p mt-4 mb-4 :style="{ color: response_color }"> {{ response_status }} </p>
        </v-flex>

        <v-flex md12 mt-5 mb-3>
          <h3> Cast Your Vote For Tournament Favourite </h3>
        </v-flex>  
        <v-flex md3 >
                <select v-model="vote" class="player1" @click="response_vote =''">
                    <option disabled value="">Select Favourite</option>
                    <option v-for="v_option in voting" :key="v_option.id"> {{ v_option.name }} </option>
                    <option> Robert McDaid </option>
                    <option> Ferd </option>
                </select>
        </v-flex>
        <v-flex md12 mt-5>
            <v-btn  @click="castVote()">
                <span class=""> Vote </span>
            </v-btn>

            <p mt-4 mb-4 :style="{ color: response_color }"> {{ response_vote }} </p>
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
        },
        userID:  {
            type: String
        },
        teams: {
            type: Array
        },
        voting: {
            type: Array
        },
    }, 
    data: () => ({
        opponent_chosen: "",
        team_chosen: "",
        response_status: "",
        response_color: "",
        response_vote: "",
        search: "No search made",
        vote: "",
    }),
    methods: {
        findID(search_list, find_name) {
            for(var i = 0; i < search_list.length; i++) {
                if(search_list[i].name == find_name)
                    return search_list[i].id
            } 

            return -1;
        },
        selectTeam() {
            // add check for fields being filled
            if(this.opponent_chosen == "" || this.team_chosen == ""){
                this.response_status = "Please select both an Opponent and a Team";
                this.response_color = "red";
                return
            }
            
            // get id codes
            this.opp_id = this.findID(this.players, this.opponent_chosen)
            this.team_id = this.findID(this.teams, this.team_chosen)

            //form the search and make request
            this.search = '/fifa/selectTeam/' + this.userID + '/'
            this.search += this.opp_id + '/' + this.team_id + '/'

            axios.get(this.search).then(response => {
                this.teams = response.data['teams'];
                this.players = response.data['opponents'];
                console.log(response)
            })

            // inform user
            this.response_status = "Team Selected Successfully";
            this.response_color = "green";
            
            // reset inputs from JSON
            this.opponent_chosen = "";
            this.team_chosen = "";
        },
        castVote() {
            // add check for fields being filled
            if(this.vote == ""){
                this.response_vote = "Please select a Player";
                this.response_color = "red";
                return
            }
            
            // get id codes
            this.opp_id = this.findID(this.players, this.opponent_chosen)
            this.team_id = this.findID(this.teams, this.team_chosen)

            //form the search and make request
            this.search = '/fifa/vote/' + this.userID + '/'
            this.search += this.vote + '/'

            axios.get(this.search).then(response => {
                console.log(response)
            })

            // inform user
            this.response_vote = "Vote Recorded Successfully";
            this.response_color = "green";
            
            // reset inputs from JSON
            this.vote = "";
        },
        
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