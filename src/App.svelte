<script>
  import { onMount } from 'svelte';
  import { playersStore, spotifyAccessToken } from './store';  // import the new store
  import { fetchPlayers } from './services';
  import { getAccessToken } from './spotifyService';  // import the getAccessToken function
  import Player from './Player.svelte';
  import SpotifyPlayer from './SpotifyPlayer.svelte';  // import the Spotify player

  const clientId = process.env['spotify_client_id'];
  const clientSecret = process.env['spotify_client_secret'];

  onMount(async () => {
    const players = await fetchPlayers();
    playersStore.set(players);
    
    const accessToken = await getAccessToken(clientId, clientSecret);  // fetch the access token
    spotifyAccessToken.set(accessToken);  // store the access token
  });
</script>

<style> /* Your styles here */ </style>

<div class="container">
  {#each $playersStore as player (player.name)}
    <Player {player} />
  {/each}
  <SpotifyPlayer />  <!-- add the Spotify player -->
</div>
