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
      {#if event.anniversary != ''}
      <span style='font-weight: bold;text-decoration:underline'>{event.anniversary}</span>
    <br>
      {/if}
    {event.name}
    <br>
    {event.year}
    {#if event.death != ''}
    <br>
    {event.death}
    {/if}
    </p>
  {/each}
</td>
