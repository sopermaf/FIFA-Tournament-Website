<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 ma-2>
          <h1>Results Input:</h1>
        </v-flex>  
        <v-flex md2 >
                <select v-model="match_players[0]" class="player1" @click="response =''">
                    <option disabled value="p1">Player 1</option>
                    <option v-for="p in players" :key="p.id"> {{ p.name }} </option>
                </select>
        </v-flex>
        <v-flex md2 >
                <select v-model="goals[0]" class="player1" @click="response =''">
                    <option disabled value="">Goals Player 1</option>
                    <option v-for="i in 20" :key="i"> {{ i }} </option>
                </select>
        </v-flex>
        <v-flex md2 >
                <select v-model="match_players[1]" class="player2" @click="response =''">
                    <option disabled value="p2">Player 2</option>
                    <option v-for="p in players" :key="p.id"> {{ p.name }} </option>
                </select>
        </v-flex>
        <v-flex md2 >
                <select v-model="goals[1]" class="player2" @click="response =''">
                    <option disabled value="">Goals Player 2</option>
                    <option v-for="i in 50" :key="i"> {{ i }} </option>
                </select>
        </v-flex>

        <!-- Preview of Selection -->
        <v-flex md5 mt-5>
            <v-card md3>
              <h2>  <span> {{ match_players[0] }}</span> </h2>
              <h2> <span> {{ goals[0] }}</span> </h2>
            </v-card>
        </v-flex>
        <v-flex md5 mt-5>
            <v-card md3>
              <h2> <span> {{ match_players[1] }}</span> </h2>
              <h2>  <span> {{ goals[1] }}</span> </h2>
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
  export default {
    props: {
        players: {
            type: Array
        }
    }, 
    data: () => ({
        match_players: ["Player 1", "Player 2"],
        goals: [0,0],
        response: "",
        response_color: ""
    }),
    methods: {
        addResult() {
            if(this.match_players[0] == "Player 1" || this.match_players[1] == 'Player 2'){
                this.response = "Please select two players for this game";
                this.response_color = "red"
                return
            } else if (this.match_players[0] == this.match_players[1]) {
                this.response = "Both players cannot be the same";
                this.response_color = "red"
                return;
            }

            // inform user
            this.response = "Result Recorded Successfully";
            this.response_color = "green";
            
            // reset inputs
            this.match_players[0] = "Player 1";
            this.match_players[1] = "Player 2";
            this.goals[0] = 0;
            this.goals[1] = 0;
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