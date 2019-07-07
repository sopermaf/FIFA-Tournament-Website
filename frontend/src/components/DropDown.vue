<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <v-btn  v-on="on" flat>
        League Standings
      </v-btn>
    </template>
    <v-list>
       
        <v-list-tile>
            <v-btn  @click="chooseTable('LeagueTable')" flat>
                <v-list-tile-title>League Table</v-list-tile-title>
            </v-btn>
        </v-list-tile>
        <v-list-tile>
            <v-btn  @click="chooseTable('GoldenBoot')" flat>
                <v-list-tile-title>Golden Boot</v-list-tile-title>
            </v-btn>
        </v-list-tile>
        <v-list-tile>
            <v-btn  @click="chooseTable('GoldenGlove')" flat>
                <v-list-tile-title>Golden Glove</v-list-tile-title>
            </v-btn>
        </v-list-tile>
        <v-list-tile>
            <v-btn   flat>
                <v-list-tile-title>Tournament Tree</v-list-tile-title>
            </v-btn>
        </v-list-tile>
        
    </v-list>
  </v-menu>
</template>

<script>
  export default {
    data: () => ({
    }),
    methods: {
        chooseTable(table) {
            this.$emit('choice-update', table);
        }
    }
  }
</script>