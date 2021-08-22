"use strict";
{
  const team_a = document.getElementById('ul-team-a');
  const team_b = document.getElementById('ul-team-b');
  const member_list = document.getElementsByClassName('member-list');

  function memberClick() {
    if (member_list in team_a) {
      team_b.append(member_list);
    } else {
      team_a.append(member_list);
    }
  }


// function wakeTeam() {
//   let list_a_element = document.getElementById('list-c-a');
//   let list_b_element = document.getElementById('list-c-b');

//   let member = document.getElementById('classic-member');
//   let member = member.split(/\n/);

//   console.log(member);
//   alert('hihi');
// }

// let try_js = document.getElementById('try-js');

// try_js.click(wakeTeam());

function art() {
  alert('konbanha');
}



}
