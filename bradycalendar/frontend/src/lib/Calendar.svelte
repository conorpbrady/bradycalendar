<script lang="ts">
  export const month = 0;
  export const year = 0;

  const getStartOfMonth = () => {
    return 5;
  }

  const generateDays = () => {
    let start = getStartOfMonth();
    let all_days = Array.from(Array(31).keys());
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

  const cal_days = generateDays();
</script>

<table>
  <thead>
    <tr>
      <th><a href={null}>&lt;</a></th>
    <th>December 2023</th>
    <th><a href={null}>&gt;</a></th>
    </tr>
  </thead>

  <tbody>
    {#each cal_days as row}
      <tr>
        {#each row as day}
        <td>{day}</td>
      {/each}
    </tr>
  {/each}
  </tbody>
</table>
