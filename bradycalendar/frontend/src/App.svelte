<script>
  import Calendar from './lib/calendar.svelte';

  const month = 12;
  const year = 2023;

  const fetchData = (month) => {
    fetch(`api/events?month=${month}`).then((response) => response.json()).then((data) => {
      eventData = data })
  }

</script>

<main>
  <Calendar {month} {year} />
</main>
