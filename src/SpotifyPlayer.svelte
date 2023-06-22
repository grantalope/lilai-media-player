<script>
  import { onMount, onDestroy } from 'svelte';
  import { spotifyAccessToken } from './store';  // Import the spotifyAccessToken store
  
  let player;
  let deviceId;

  // Define onSpotifyWebPlaybackSDKReady as soon as this module is executed
  window.onSpotifyWebPlaybackSDKReady = () => {
    player = new Spotify.Player({
      name: 'Lilliputia Web Player',
      getOAuthToken: callback => { callback($spotifyAccessToken); }  // Use the value from the spotifyAccessToken store
    });

    player.addListener('ready', ({ device_id }) => {
      console.log('Ready with Device ID', device_id);
      deviceId = device_id;
    });

    player.connect();
  };

  // onMount and onDestroy can remain empty if you have no additional setup or cleanup code
  onMount(() => {});
  onDestroy(() => {});
  
  // You may need additional logic here for controlling the player (play, pause, next, previous)
</script>
