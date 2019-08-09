<template>
  <v-app>
    <Toolbar />

    <v-content>
      <v-container grid-list-md >
        <v-layout row wrap justify-center>
          <!-- HEADER -->
          <v-flex md12 text-xs-left mb-3>
              <h1 text-xs-left> History </h1>

            <p>
            The first FIFA Tournament took place on the 27th 
            of September 2015, with 9 competitors taking part. 
            Since that time the FIFA Tournament has become an annual 
            competition, which has attracted the best competitors from 
            around the globe. Since 2015 there have been 4 FIFA 
            Tournaments and 4 different champions.
            </p>
            
          </v-flex>
  

          <!-- Yearly Text -->
            <!-- Description -->
            <span v-for="award in awards" :key="award.Year">
              <v-flex md12 text-xs-left elevation-4 ma-2 class="year_desc">
                  <h2>{{award.Year}}</h2>
                  <p>{{descriptions[award.Year]}}</p>
                  <br>
                  <ul>
                    <li><strong>Champion:</strong> {{award.Champion}} </li>
                    <li><strong>Runner Up:</strong> {{award.Runner_Up}} </li>
                    <li><strong>Golden Boot:</strong> {{award.Golden_Boot}} </li>
                    <li><strong>Golden Glove:</strong> {{award.Golden_Glove}} </li>
                    <li><strong>Last Place:</strong> {{award.Last_Place}} </li>
                  </ul>
              </v-flex>
            </span>

        </v-layout>
      </v-container>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'History',
  components: {
    Toolbar,
    Footer,
  },
  data () {
    return {
      descriptions: {
        2015: '9 competitors took part in the inaugural FIFA Tournament. Fabian, Rob, Kunal, Lyes, Daniel, Burke, Oisín, Jim, and Johnny gathered on the early hours of Sunday morning to compete, not knowing that they would be making history as they kicked off the very first FIFA Tournament. The 2015 format saw 2 groups of 4 and 5, with the top 4 from each group through to the Quarter Finals. Teams were selected on the basis of randomization.',
        2016: '2016 saw the introduction of the league stage, replacing the outdated group stage. For the first time, competitors were able to play against each and every other player in the Tournament. 6 competitors took to the controllers, with the knockout stage comprised simply of two-legged Semi Finals and a Final. And the introduction of the last place playoff sparked a rivalry between Lyes and Daniel that would continue for many years.',
        2017:'For the first time in the FIFA Tournament, team selection was no longer randomised. This year, every player competed using the same teams from a preselected list, comprised of teams ranging from 5 star to .5 star ratings. This increased the tactical element of the FIFA Tournament ten-fold. Further changes saw the requirements for earning a bonus point reduced from scoring 5 goals in a game, to scoring 4 in a game. 8 competitors took part in a double round robin league format with the top 4 advancing to the Semi Final.',
        2018:'The 2018 FIFA Tournament was a special World Cup edition. By far the most complete tournament at the time, there were numerous changes to the format and other aspects of the tournament. Players were drawn different international teams from the same various star ratings. 7 players competed in a league format, with the top 3 advancing straight to the Semi Finals, while the bottom 4 battled it out in a backdoor qualifier to claim the final Semi Final spot. The FIFA Tournament finally had silverware to highlight the glorious nature of the competition. The FIFA Tournament Cup, Golden Boot Award, and Golden Glove Award were all introduced. ',
      },
      awards: [
        {
          Year: 2015,
          Champion: 'Kunal Kapoor',
          Runner_Up: 'Robert McDaid',
          Golden_Boot: 'Robert McDaid',
          Golden_Glove: 'Robert McDaid',
          Last_Place: 'Lyes Djennadi',
        },
        {
          Year: 2016,
          Champion: 'Fabian Mak',
          Runner_Up: 'Robert McDaid',
          Golden_Boot: 'Fabian Mak',
          Golden_Glove: 'Fabian Mak',
          Last_Place: 'Lyes Djennadi',
        },
        {
          Year: 2017,
          Champion: 'Johnny McNulty',
          Runner_Up: 'Kunal Kapoor',
          Golden_Boot: 'Kunal Kapoor',
          Golden_Glove: 'Kunal Kapoor',
          Last_Place: 'Daniel Whitaker',
        },
        {
          Year: 2018,
          Champion: "Peter O'Donnel",
          Runner_Up: 'Robert McDaid',
          Golden_Boot: 'Fabian Mak',
          Golden_Glove: 'Fabian Mak',
          Last_Place: 'Daniel Whitaker',
        },
      ]
    }
  }
}
</script>

<style>

.year_desc:hover {
  transform: scale(1.1);
}

</style>
