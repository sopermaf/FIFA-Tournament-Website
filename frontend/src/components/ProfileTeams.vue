<template>
  <v-data-table :headers="headers" :items="teams" item-key="team.id" class="elevation-1">
    <template v-slot:items="props">
      <!--<td :style="{ backgroundColor: colorRank(props.index) }">
        {{ props.index + 1 }}
      </td>-->
      <td class="text-xs-left">{{ props.item.name }}</td>
      <td class="text-xs-left">{{ props.item.star_rating }}</td>
    </template>
  </v-data-table>   
</template>

<script>
export default {
  props: {
    teams: {
      type: Array
    },
  },
  data() {
    return {
      headers: [
          { text: 'Name', align: 'left', sortable: false},
          { text: 'Star Rating', align: 'left', sortable: false},
        ],
      pagination: {
        rowsPerPage: 30
      }, 
    };
  },
  methods: {
    colorRank(index) {
      if(index < 6)
        return "green";
      else return 'red';
    }
  },
};
</script>

<style>

</style>
