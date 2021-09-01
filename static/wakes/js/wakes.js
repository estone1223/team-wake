
function wakeTeam() {
  let team_a = document.getElementById('team_a');
  let team_b = document.getElementById('team_b');

  // 各チームを空にする
  team_a.textContent = '';
  team_b.textContent = '';

  // メンバーリストの取得

  const selected_member = document.getElementsByName('selected-member');

  // // 配分用のリストの作成
  let user_list = [];

  for (let i = 0, len = selected_member.length; i < len; i++) {
    if (selected_member[i].checked) {
      user_list.push(selected_member[i].value);
    }
  }

  // 配分用リストの要素に重みをつけ、ソート
  for (let i = 0, len = user_list.length; i < len; i++) {
    user_list[i] = [user_list[i], Math.random()];
    }

  user_list.sort(function(a, b){return a[1] - b[1];});

  // ソート済みの要素から重みを取り除く処理
  for (let i = 0, len = user_list.length; i < len; i++) {
    user_list[i] = user_list[i][0];
  }

  //チーム分け処理 　
  for (let i = 0, len = user_list.length; i < len; i ++) {
    if (i % 2 == 1) {
      team_b.insertAdjacentHTML("beforeend", "<li class='team-member'>" + user_list[i] + "</li>");
    } else {
      team_a.insertAdjacentHTML("beforeend", "<li class='team-member'>" + user_list[i] + "</li>");
    }
  }
  }

