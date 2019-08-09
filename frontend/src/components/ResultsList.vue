<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md12 >
            <v-data-table :headers="headers" :items="results" item-key="fixture.id" class="elevation-1" :pagination.sync="pagination">
              <template v-slot:items="props">
                <td>{{ props.item.time}}</td>
                <td>{{ props.item.fixture_sides[0].team}}</td>
                <td>{{ props.item.fixture_sides[0].name}}</td>
                <td>{{ props.item.fixture_sides[0].goals}}</td>
                <td> {{ props.item.fixture_sides[1].goals }}</td>
                <td> {{ props.item.fixture_sides[1].name }}</td>
                <td> {{ props.item.fixture_sides[1].team }}</td>
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
          { text: 'Time', sortable: true, value: 'time'},
          { text: 'Team 1', sortable: true, value: 'fixture_sides[0].team'},
          { text: 'Player 1', sortable: true, value: 'fixture_sides[0].name'},
          { text: 'Goals 1', sortable: true, value: 'fixture_sides[0].goals'},
          { text: 'Goals 2', sortable: true, value: 'fixture_sides[1].team'},
          { text: 'Player 2', sortable: true, value: 'fixture_sides[1].name'},
          { text: 'Team 2', sortable: true, value: 'fixture_sides[1].goals'},
        ],
      results: [],
      pagination: {
        rowsPerPage: 15
      },
    };
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.results = JSON.parse(this.data)['results'];
  }
};
</script>

<style>

</style>
