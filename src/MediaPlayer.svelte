<script>
import { Player, Ui, Video } from '@vime/svelte';
</script>

<Player>
  <Video poster="https://media.vimejs.com/poster.png">
    <source data-src="https://media.vimejs.com/720p.mp4" type="video/mp4" />
    <track
      default
      kind="subtitles"
      src="https://media.vimejs.com/en.vtt"
      srclang="en"
      label="English"
    />
  </Video>
  <Ui>
    <!-- UI components go here. -->
  </Ui>
</Player>
