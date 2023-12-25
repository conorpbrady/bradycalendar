<script lang="ts">
  export let day;
  export let events = [];
  let anniversaryStyle; 
</script>

<td class={day == 0 ? 'noday' : 'day'}>
  {#if day != 0}
  <span class="day-marker">{day != 0 ? day : ''}</span>
  {/if}
  {#each events as event}
    <p class="{event.anniversary? 'anniversary': 'birthday'} {event.death? 'deceased': ''}">
    {event.name}
    <br>
    {event.year}
    {#if event.death != ''}
    ({(new Date(event.death)).toLocaleDateString()})
    {/if}
    </p>
  {/each}
</td>
