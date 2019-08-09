<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md6 >
            <v-data-table :headers="headers" :items="fixtures" item-key="fixture.id" class="elevation-1" :pagination.sync="pagination">
              <template v-slot:items="props">
                <td> {{ props.item.time }}</td>
                <td>{{ props.item.fixture_sides[0].name}}</td>
                <td> {{ props.item.fixture_sides[1].name }}</td>
                <td> {{ props.item.tv }}</td>
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
          { text: 'Player 1', sortable: true, value: 'fixture_sides[0].name'},
          { text: 'Player 2', sortable: true, value: 'fixture_sides[1].name'},
          { text: 'TV', sortable: true, value: 'tv'},
        ],
      fixtures: [],
      pagination: {
        rowsPerPage: 15
      },
    };
  },
  mounted() {
    this.data = document.body.getAttribute('data');
    this.fixtures = JSON.parse(this.data)['fixtures'];
  }
};
</script>

<style>

</style>
