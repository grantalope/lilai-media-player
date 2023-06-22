<script>
  export let player;
</script>

<div class="player">
  <img src={player.avatar} alt={player.name} />
  <h2>{player.name}</h2>
  <p>{player.description}</p>
  <p><strong>Role:</strong> {player.role}</p>
</div>
