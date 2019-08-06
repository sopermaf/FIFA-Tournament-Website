<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 mb-5>
          {{ mock }}
        </v-flex>  

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 1 </h2> 
           <p> <strong> 1st: </strong> {{playersOrdered[0].name}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> Winner of Playoff 2 </p> 
           <p> ({{playersOrdered[6].name}} vs {{playersOrdered[9].name}}) </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 2 </h2> 
           <p> <strong> 3rd: </strong> {{playersOrdered[2].name}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> <strong> 6th: </strong> {{playersOrdered[5].name}} </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 3 </h2> 
           <p> <strong> 2nd: </strong> {{playersOrdered[1].name}} </p> 
           <p> <h3> vs </h3> </p>  
           <p> Winner of Playoff 1 </p> 
           <p> ({{playersOrdered[7].name}} vs {{playersOrdered[8].name}}) </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 4 </h2> 
           <p> <strong> 4th </strong> {{playersOrdered[3].name}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> <strong> 5th: </strong> {{playersOrdered[4].name}} </p> 
        </v-flex>

      </v-layout>
    </v-container>
</template>

<script>
  export default {
    props: {
        players: {
            type: Array
        },
    }, 
    data: () => ({
    }),
    computed: {
    playersOrdered: function() {
      function compare(a, b) {
        if (a.points > b.points)
          return -1;
        if (a.points < b.points)
          return 1;
        if (a.points == b.points){
          if (a.goal_difference > b.goal_difference)
            return -1;
          if (a.goal_difference < b.goal_diference)
            return 1;
          if (a.goals_difference == b.goal_difference){
            if (a.goal_scored > b.goal_scored)
            return -1;
            if (a.goal_scored < b.goal_scored)
              return 1;
          }
        }
        return 0;
      }
      return this.players.sort(compare);
    }
  }
  }
</script>

<style>

</style>