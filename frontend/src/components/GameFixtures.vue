<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md9 ma-2>
          <h1>Golden Glove</h1>
        </v-flex>  
        <v-flex md3 >
            <v-data-table :headers="headers" :items="playersGoldenGlove" item-key="player.id" class="elevation-1">
              <template v-slot:items="props">
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
  data() {
    return {
      headers: [
          { text: 'Team 1', sortable: false, value: 'name'},
          { text: 'Player 1', sortable: false, value: 'name'},
          { text: 'Player 1 Goals', sortable: false, value: 'name'},
          { text: 'Player 2 Goals', sortable: false, value: 'name'},
          { text: 'Player 2', sortable: false, value: 'name'},
          { text: 'Team 2', sortable: false, value: 'name'},
        ],
    };
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.players = JSON.parse(this.data)['fixtures'];
  }
};
</script>

<style>

</style>
