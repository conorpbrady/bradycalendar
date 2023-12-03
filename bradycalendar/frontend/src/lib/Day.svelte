<script lang="ts">
  export let day;
  export let events = [];

</script>

<td class={day == 0 ? 'noday' : 'day'}>
  {#if day != 0}
  <span class="day-marker">{day != 0 ? day : ''}</span>
  {/if}
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
