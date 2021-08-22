



function wakeTeam() {
  let team_a = document.getElementById('team_a');
  let team_b = document.getElementById('team_b');

  team_a.innerHTML = '';
  team_b.innerHTML = '';

  let member_list = document.getElementById('classic-member');
  let member = member_list.value.split(/\n/);

  let user_list = [];

  for (let i = 0, len = member.length; i < len; i++) {
    if (member[i] != '') {
      user_list.push(member[i]);
    }
  }

  for (let i = 0, len = user_list.length; i < len; i++) {
    user_list[i] = [user_list[i], Math.random()];
    }

  user_list.sort(function(a, b){return a[1] - b[1];});
  for (let i = 0, len = user_list.length; i < len; i++) {
    user_list[i] = user_list[i][0];
  }


  for (let i = 0, len = user_list.length; i < len; i ++) {
    if (i % 2 == 1) {
      team_a.insertAdjacentHTML("beforeend", "<li class='team-member'>" + user_list[i] + "</li>");
    } else {
      team_b.insertAdjacentHTML("beforeend", "<li class='team-member'>" + user_list[i] + "</li>");
    }
  }
  }




