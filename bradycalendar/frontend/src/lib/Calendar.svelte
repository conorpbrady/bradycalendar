<script lang="ts">
  import Day from './Day.svelte';


  let month = new Date().getMonth() + 1;
  let year = new Date().getFullYear();

  const MONTHS = [, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const getStartOfMonth = (month, year) => {
    let d = new Date(year, month - 1, 1);
    return d.getDay();
  }

  const getDaysInMonth = (month, year) => {
    let d = new Date(year, month, 0)
    return d.getDate();
  }

  const increment = () => {
    console.log('hi');
    if(month == 12) {
      year = year + 1;
      month = 1;
      } else {
      month = month + 1; 
      }
      }
      
  const decrement = () => {
    if(month == 1) {
      year = year - 1;
      month = 12;
      } else {
      month = month - 1}
      }
      
  const generateDays = (month, year) => {
    let start = getStartOfMonth(month, year);
    let all_days = Array.from(Array(getDaysInMonth(month, year))).map((e, i) => i+1);
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
      dayEvent.anniversary = 'Anniversary'
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

  $: cal_days = generateDays(month, year);
  $: eventsPromise = getAllEvents(month);
</script>
<div class="heading-container">
  <div class="nav">
      <a href={null} on:click={decrement}>&lt;</a>
  </div>
  <div class="month-heading">
    <h3>{MONTHS[month]} {year}</h3>
  </div>
  <div class="nav">
    <a href={null} on:click={increment}>&gt;</a>
  </div>
</div>

<table>
  <thead>
    <tr style="border: 1px solid black;margin-bottom:.3em;">
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
