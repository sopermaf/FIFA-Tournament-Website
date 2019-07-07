<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md9 ma-2>
          <h1>Golden Glove</h1>
        </v-flex>  
        <v-flex md4 >
            <v-data-table :headers="headers" :items="playersGoldenGlove" item-key="player.id" class="elevation-1">
              <template v-slot:items="props">
                <td>{{ props.index + 1 }}</td>
                <td>{{ props.item.name }}</td>
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
          { text: 'Player', align: 'left', sortable: false },
          { text: 'Goals Conceded', value: 'goals_against', sortable: false},
        ],
    };
  },
  computed: {
    playersGoldenGlove: function() {
      function compare(a, b) {
        if (a.goals_against < b.goals_against)
          return -1;
        if (a.goals_against > b.goals_against)
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
