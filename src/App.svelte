<script>
  import { Player, Ui, Video, DefaultControls } from '@vime/svelte';
  let showVideo = true;

  // The mediaId should be the actual identifier of the video or track being played.
  // Here I've used a placeholder value.
  let mediaId = 'abc123';

  async function logPlayback() {
    const response = await fetch('https://processplaybackdata.azurewebsites.net/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        userId: 'user123', // The ID of the user
        mediaId: mediaId // The ID of the media being played
      })
    });

    if (!response.ok) {
      console.error('Failed to log playback:', response.statusText);
    }
  }

  // Call this function when the media starts playing
  logPlayback();
</script>

<button on:click={() => showVideo = !showVideo}>
  Toggle Player
</button>

{#if showVideo}
  <main>
    <h1>Welcome to Your Media Player</h1>
    
    <Player>
      <Video poster="https://media.vimejs.com/poster.png">
        <source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
      </Video>
      <Ui>
        <DefaultControls />
      </Ui>
    </Player>
  </main>
{:else}
  <iframe src="https://open.spotify.com/embed/track/1P8tISEFOeOmEsuFPTx5dZ" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
{/if}

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 2em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
