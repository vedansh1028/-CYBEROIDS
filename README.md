# -CYBEROIDS
<!DOCTYPE html>
<html>
<head>
  <title>Hiring Platform</title>
</head>
<body>

  <h1>Apply for Job</h1>

  <form id="form">
    <label>Name:</label><br>
    <input type="text" id="name" required><br><br>

    <label>Skill (1-10):</label><br>
    <input type="number" id="skill" min="1" max="10" required><br><br>

    <label>Experience (years):</label><br>
    <input type="number" id="exp" required><br><br>

    <button type="submit">Submit</button>
  </form>

  <h2>Leaderboard</h2>
  <ul id="leaderboard"></ul>

<script>
  const form = document.getElementById("form");
  const leaderboard = document.getElementById("leaderboard");

  let candidates = [];

  form.addEventListener("submit", function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let skill = parseInt(document.getElementById("skill").value);
    let exp = parseInt(document.getElementById("exp").value);

    // scoring logic
    let score = (skill * 5) + (exp * 3);

    candidates.push({ name, score });

    // sort by score
    candidates.sort((a, b) => b.score - a.score);

    displayLeaderboard();
    form.reset();
  });

  function displayLeaderboard() {
    leaderboard.innerHTML = "";

    candidates.slice(0, 5).forEach(c => {
      let li = document.createElement("li");
      li.textContent = c.name + " - Score: " + c.score;
      leaderboard.appendChild(li);
    });
  }
</script>

</body>
</html>
