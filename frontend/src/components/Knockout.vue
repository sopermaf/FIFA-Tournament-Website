<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 mb-5>
          {{ mock }}
        </v-flex>  

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 1 </h2> 
           <p> <strong> 1st: </strong> {{mock[0]}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> Winner of Playoff 2 </p> 
           <p> ({{mock[6]}} vs {{mock[9]}}) </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 2 </h2> 
           <p> <strong> 3rd: </strong> {{mock[2]}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> <strong> 6th: </strong> {{mock[5]}} </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 3 </h2> 
           <p> <strong> 2nd: </strong> {{mock[1]}} </p> 
           <p> <h3> vs </h3> </p>  
           <p> Winner of Playoff 1 </p> 
           <p> ({{mock[7]}} vs {{mock[8]}}) </p> 
        </v-flex>

        <v-flex xs2 md2 elevation-2 ma-2>
           <h2> Quarter Final 4 </h2> 
           <p> <strong> 4th </strong> {{mock[3]}} </p> 
           <p> <h3> vs </h3> </p> 
           <p> <strong> 5th: </strong> {{mock[4]}} </p> 
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
        mock: [
            'Fabian',
            'Oisin',
            'Johnny',
            'Whitto',
            'Burke',
            'Koon',
            'Rob',
            'McBain',
            'Ryan',
            'Jim',
        ]
    }),
    methods: {        
    }
  }
</script>

<style>

</style>