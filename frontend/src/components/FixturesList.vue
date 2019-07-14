<template>
  <v-container grid-list-md text-xs-center>
      <v-layout row wrap justify-center>
        <v-flex md9 ma-2>
          <h1>Fixtures</h1>
        </v-flex>  
        <v-flex md3 >
            <v-data-table :headers="headers" :items="fixtures" item-key="fixture.id" class="elevation-1">
              <template v-slot:items="props">
                <td>{{ props.item.fixture_sides[0].name}}</td>
                <td> {{ props.item.fixture_sides[1].name }}</td>
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
          { text: 'Player 1', sortable: false, value: 'name'},
          { text: 'Player 2', sortable: false, value: 'name'},
        ],
      fixtures: []
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
