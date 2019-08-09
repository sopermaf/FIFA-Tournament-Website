<template>
    <VueApexCharts width="600" type="bar" :options="options" :series="series" />
</template>

<script>
import VueApexCharts from 'vue-apexcharts';

export default {
    components: {
        VueApexCharts
    },
    data() {
        return {
            players: [],
            options: {
                xaxis: {
                        categories: [
                            'Jim',
                            'Johnny',
                            'Fabian',
                            'Kunal',
                            'Cameron',
                            'Niall',
                            'Oisín',
                            'Lyes',
                            'Peter',
                            'Daniel'
                        ]
                    }
            },
            series: [
                {
                name: 'Tournament Favourites',
                data: []
                },
            ]
        };
    },
    mounted() {
        this.data = document.body.getAttribute('data');
        this.players = JSON.parse(this.data)['poll'];
        console.log(this.players)
      
      this.series[0].data = this.players
      
      
      var vote_data = []
    },
}
</script>

<style>

.pie {
  background-image: conic-gradient(
    #d44 calc(3.6deg * var(--segment1)),
    #fc3 0 calc(3.6deg * var(--segment2)),
    #ac0 0
  );
}

</style>

