<template>
  <v-container grid-list-md text-xs>
      <v-layout row wrap justify-center>
    
        <v-flex md3 ml-2>
            <h2> {{player.name}} </h2>
            <img :src="`https://randomuser.me/api/portraits/men/${player.id }.jpg`">
            <!--<img src="@/assets/Fabian_Mak.png" class="profile_pic">-->
        
            <p>
                <strong>Number of Apperances:</strong> 
                {{ player.tournament_appearances }} 
            </p>
            <p>
                <strong>Best Overall Finish:</strong> 
                {{ player.best_overall_finish }} 
            </p>
            <p>
                <strong>Best League Finish:</strong> 
                {{ player.best_league_finish }} 
            </p>
            <p>
                <strong>Tournament Favourite:</strong> 
                {{ player.tournament_favourite }} 
            </p>
            <p>
                 
                {{ player.description }} 
            </p>
        </v-flex> 
    
        <v-flex md3 ml-2 text-xs-center>
            <h2> Teams Remaining  </h2>
            <ProfileTeams :teams="player.teams_available" />
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import ProfileTeams from './ProfileTeams';

export default {
    components: {
        ProfileTeams,
    },
    props: {
        player: {
            type: Object
        },
    }, 
    data: () => ({
        playerUrl: '@/assets/rob.png'
    }),
    methods: {        
    },
    computed: {
        iconUrl () {
        return require('@/assets/rob.png')
        // The path could be '../assets/img.png', etc., which depends on where your vue file is
        }
    }
}
</script>

<style>

img {
    width: 170px;
    height: 170px;
}



</style>