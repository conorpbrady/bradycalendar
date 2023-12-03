<script lang="ts">
  import Day from './Day.svelte';

  const getStartOfMonth = () => {
    return 4;
  }

  const generateDays = () => {
    let start = getStartOfMonth();
    let all_days = Array.from(Array(32).keys());
    let cal_days = Array()
    while (all_days.length > 0) {
      let week = []
      if(cal_days.length == 0) {
        week = week.concat(Array.from({length: start}, (v, i) => 0))
      }
      while(week.length < 7) {
        if(all_days.length == 0) {
          week.push(0);
        }
        else {
        week.push(all_days.shift())
        }
      }
        cal_days.push(week);

    }
    return cal_days;
  }

  async function getAllEvents(month)  {

    const response = await fetch(`http://localhost:8000/api/events?month=${month}`)
    const data = await response.json()
 
    let eventsByDay = {}
    for (event of data) { 

    const dateObj = new Date(`${event.event_date} 12:00`);
    const year = dateObj.getFullYear();
    const day = dateObj.getDate();
    let dayEvent = {};
    dayEvent.anniversary = '';
    dayEvent.death = '';
    dayEvent.secondName = '';
    if (event.is_anniversary) { 
      dayEvent.anniversary = '<b><u>Anniversary</b></u>'
      dayEvent.secondName = ` and ${event.second_name}`;
    } 
    
    if (event.death_date) {
      dayEvent.death = event.death_date;
} 
    dayEvent.name = event.name
    dayEvent.year = year

    if (day in eventsByDay) { 
      eventsByDay[day].push(dayEvent);
    } else {
      eventsByDay[day] = [dayEvent];
}
  }
  return eventsByDay
  }

  const cal_days = generateDays();
  const eventsPromise = getAllEvents(4);
</script>

<table>
  <thead>
    <tr>
      <th></th>
      <th><a href={null}>&lt;</a></th>
    <th colspan="3">December 2023</th>
    <th><a href={null}>&gt;</a></th>
    <th></th>
    </tr>
    <tr>
      <th>Sun</th>
      <th>Mon</th>
      <th>Tue</th>
      <th>Wed</th>
      <th>Thu</th>
      <th>Fri</th>
      <th>Sat</th>
    </tr>
  </thead>

  <tbody>
    {#await eventsPromise }
    {:then events}
    {#each cal_days as row}
      <tr>
        {#each row as day}
          <Day events={events[day]} day={day} />
        {/each}
    </tr>
  {/each}
    {/await}
  </tbody>
</table>
