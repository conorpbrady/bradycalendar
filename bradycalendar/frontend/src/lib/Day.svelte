<script lang="ts">
  export let day;
  export let events = [];

</script>

<td class='day'>
  <span class="day-marker">{day != 0 ? day : ''}</span>

  {#each events as event}
    <p>
    {event.anniversary}
    <br>
    {event.name} {event.secondName}
    <br>
    {event.year}
    <br>
    {event.death}
    </p>
  {/each}
</td>
