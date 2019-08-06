<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md5 >
            <v-data-table :headers="headers" :items="playersGoldenBoot" item-key="player.id" class="elevation-1" :pagination.sync="pagination">
              <template v-slot:items="props">
                <td>{{ props.index + 1 }}</td>
                <td>{{ props.item.name }}</td>
                <td class="text-xs-right">{{ props.item.goals_scored }}</td>
              </template>
            </v-data-table>         
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
export default {
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['players'];
  },
  data() {
    return {
      players: [],
      headers: [
          { text: 'Position', align: 'left', sortable: false},
          { text: 'Player', align: 'left', sortable: false },
          { text: 'Goals Scored', value: 'points', sortable: false},
        ],
      pagination: {
        rowsPerPage: 15
      },
    };
  },
  computed: {
    playersGoldenBoot: function() {
      function compare(a, b) {
        if (a.goals_scored > b.goals_scored)
          return -1;
        if (a.goals_scored < b.goals_scored)
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
