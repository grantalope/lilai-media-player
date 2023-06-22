<script>
  import { onMount } from 'svelte';
  let players = [];

  onMount(async () => {
    const response = await fetch('characters.json');
    players = await response.json();
  });
</script>

<style>
  .container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .player {
    width: 300px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
  }

  .player img {
    width: 100%;
    height: auto;
  }
</style>

<div class="container">
  {#each players as player}
    <div class="player">
      <img src={player.avatar} alt={player.name} />
      <h2>{player.name}</h2>
      <p>{player.description}</p>
      <p><strong>Role:</strong> {player.role}</p>
    </div>
  {/each}
</div>

<iframe style="border-radius:10px" src="https://open.spotify.com/embed/playlist/28hLyn3dYE70ZOKye24IhI?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
