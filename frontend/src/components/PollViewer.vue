<template>
    <pure-vue-chart
    :points="points"
    :show-y-axis="true"
    :show-x-axis="true"
    :width="900"
    :height="400"
    :show-values="true"
    :use-month-labels="false"
/>   
</template>

<script>
import PureVueChart from 'pure-vue-chart';

export default {
    components: {
        PureVueChart,
    },
    data: () => ({
        points: [
            {label:'', value:1},
            {label:'', value:2},
            {label:'', value:3},
            {label:'', value:4},
            {label:'', value:5},
            {label:'', value:6},
            {label:'', value:7},
            {label:'', value:8},
            {label:'', value:9},
            {label:'', value:10},
        ],
        barChartData: [],
        players: []
    }),
    methods: {
        returnObject(passed){
            var format = {
                label: passed.label,
                value: parseInt(passed.value)
            }
            return format;
        },
        makeObject() {
            for(var i=0; i < this.players.length; i++){
                this.points[i] = this.players[i]
            }
        }
    },
    mounted() {
        this.data = document.body.getAttribute('data');
        this.players = JSON.parse(this.data)['points'];

        for(var i=0; i < this.players.length; i++){
                this.points[i] = this.players[i]
        }
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

