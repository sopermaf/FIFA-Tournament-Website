<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md9 ma-2>
          <h1>League Table</h1>
        </v-flex>  
        <v-flex md10 >
            <v-data-table :headers="headers" :items="playersOrdered" item-key="player.id" class="elevation-1">
              <template v-slot:items="props">
                <td :style="{ backgroundColor: colorRank(props.index) }">
                  {{ props.index + 1 }}
                </td>
                <td>{{ props.item.name }}</td>
                <td class="text-xs-right">{{ props.item.points }}</td>
                <td class="text-xs-right">{{ props.item.wins }}</td>
                <td class="text-xs-right">{{ props.item.draws }}</td>
                <td class="text-xs-right">{{ props.item.losses }}</td>
                <td class="text-xs-right">{{ props.item.goals_scored - props.item.goals_against }}</td>
                <td class="text-xs-right">{{ props.item.goals_scored }}</td>
                <td class="text-xs-right">{{ props.item.goals_against }}</td>
              </template>
            </v-data-table>         
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
  data() {
    return {
      headers: [
          { text: 'Position', align: 'left', sortable: false},
          { text: 'Names', align: 'left', sortable: false, value: 'name'},
          { text: 'Points', value: 'points', sortable: false},
          { text: 'Wins', value: 'wins', sortable: false},
          { text: 'Draws', value: 'draws', sortable: false},
          { text: 'Losses', value: 'losses', sortable: false},
          { text: 'Goal Difference', sortable: false},
          { text: 'Goals Scored', value: 'goals_scored', sortable: false},
          { text: 'Goals Against', value: 'goals_against', sortable: false},
        ],
    };
  },
  methods: {
    colorRank(index) {
      if(index < 4)
        return "green"
      else return "red"
    }
  },
  computed: {
    playersOrdered: function() {
      function compare(a, b) {
        if (a.points > b.points)
          return -1;
        if (a.points < b.points)
          return 1;
        return 0;
      }
      return this.players.sort(compare);
    }
  }
};
</script>

<style>

</style>
